import requests
import json
import time
import base64
import random
from PIL import Image, ImageDraw, ImageFont
from flask import Flask, render_template, request
import asyncio


def process_data(data1, data2):
    text = data1

    if data1 == "":
        text = "---"
    if data2 == "":
        data2 = "404"

    response = requests.get("https://fusionbrain.ai")

    class Text2ImageAPI:
        def __init__(self, url, api_key, secret_key):
            self.URL = url
            self.AUTH_HEADERS = {
                'X-Key': f'Key {api_key}',
                'X-Secret': f'Secret {secret_key}',
            }

        def get_model(self):
            response = requests.get(self.URL + 'key/api/v1/models', headers=self.AUTH_HEADERS)
            data = response.json()
            return data[0]['id']

        async def generate(self, prompt, model, images=1, width=400, height=400):
            params = {
                "type": "GENERATE",
                "numImages": images,
                "width": width,
                "height": height,
                "style": "DETAL",
                "generateParams": {
                    "query": f"{prompt}"
                }
            }
            data = {
                'model_id': (None, model),
                'params': (None, json.dumps(params), 'application/json')
            }
            response = requests.post(self.URL + 'key/api/v1/text2image/run', headers=self.AUTH_HEADERS, files=data)
            data = response.json()
            return data['uuid']

        async def check_generation(self, request_id, attempts=10, delay=10):
            while attempts > 0:
                response = requests.get(self.URL + 'key/api/v1/text2image/status/' + request_id,
                                        headers=self.AUTH_HEADERS)
                data = response.json()
                if data['status'] == 'DONE':
                    return data['images']
                elif data['status'] == 'FAILED':
                    raise ValueError("Image generation failed.")
                attempts -= 1
                await asyncio.sleep(delay)
            raise TimeoutError("Timeout exceeded while waiting for response from the server")

    async def main():
        api = Text2ImageAPI('https://api-key.fusionbrain.ai/', '7BCA944A173FFE11E0ADB4D67E833F4F',
                            '2E34B8E7A9A2C952AE2FA140EF47DC5F')
        model_id = api.get_model()
        uuid = await api.generate(data2, model_id)
        images = await api.check_generation(uuid)
        image_base64 = images[0]
        image_data = base64.b64decode(image_base64)
        with open("image.jpg", "wb") as file:
            file.write(image_data)

    asyncio.run(main())

    # Открываем изображение 1
    image = Image.open("slide (1).jpg")
    draw = ImageDraw.Draw(image)
    x1, y1 = 50, 100  # Начальная точка
    x2, y2 = 700, 350  # Конечная точка
    draw.rectangle([x1, y1, x2, y2], fill="rgb(234, 243, 250)")
    image.save("img(1_1).jpg")

    # Открываем изображение 2
    image = Image.open("slide (2).jpg")
    draw = ImageDraw.Draw(image)
    x1, y1 = 00, 000  # Начальная точка
    x2, y2 = 700, 350  # Конечная точка
    draw.rectangle([x1, y1, x2, y2], fill="rgb(254, 247, 231)")
    image.save("img(2_1).jpg")

    # Файл 3 не нуждается
    # image = Image.open("slide (3).jpg")
    # draw = ImageDraw.Draw(image)
    # x1, y1 = 50, 100  # Начальная точка
    # x2, y2 = 700, 350  # Конечная точка
    # draw.rectangle([x1, y1, x2, y2], fill="rgb(234, 243, 250)")
    # image.save("img(3_1).jpg")

    # Открываем изображение 4
    image = Image.open("slide (4).jpg")
    draw = ImageDraw.Draw(image)
    x1, y1 = 50, 100  # Начальная точка
    x2, y2 = 700, 350  # Конечная точка
    draw.rectangle([x1, y1, x2, y2], fill="white")
    image.save("img(4_1).jpg")

    def add_text_to_image(image_path, text, output_path, font_path=None, text_x=None, text_y=None):
        # Открываем изображение
        image = Image.open(image_path)
        draw = ImageDraw.Draw(image)

        # Устанавливаем шрифт
        if font_path:
            font = ImageFont.truetype(font_path, size=40)
        else:
            font = ImageFont.load_default()

        # Получаем размеры изображения
        image_width, image_height = image.size

        # Если не заданы координаты текста, центрируем его по умолчанию
        if text_x is None:
            text_width, _ = draw.textsize(text, font=font)
            text_x = (image_width - text_width) / 2
        if text_y is None:
            _, text_height = draw.textsize(text, font=font)
            text_y = (image_height - text_height) / 2

        # Добавляем текст на изображение
        draw.text((text_x, text_y), text, fill=(0, 0, 0), font=font)

        # Сохраняем результат
        image.save(output_path)

    # Пример использования
    font_path = "arial.ttf"  # путь к файлу шрифта, если используется другой шрифт
    text_x = 60
    text_y = 150

    def drop_part_with_space(text):
        words = text.split()
        new_text = ""
        char_count = 0
        for i, word in enumerate(words):
            if (char_count + len(word) > 15) or ((i + 1) % 3 == 0 and i != len(words) - 1):
                new_text += word + '\n'
                char_count = 0
            else:
                new_text += word + ' '
                char_count += len(word) + 1
        return new_text.strip()

    dropped_text = drop_part_with_space(text)
    text = dropped_text

    output_path = "img(1).jpg"
    image_path = "img(1_1).JPG"
    add_text_to_image(image_path, text, output_path, font_path, text_x, text_y)  # Запуск для первого фото.

    output_path = "img(2).jpg"
    image_path = "img(2_1).JPG"
    add_text_to_image(image_path, text, output_path, font_path, text_x, text_y)  # Запуск для второго фото.

    output_path = "img(3).jpg"
    image_path = "img(3_1).JPG"
    add_text_to_image(image_path, text, output_path, font_path, text_x, text_y)  # Запуск для третьего фото.

    output_path = "img(4).jpg"
    image_path = "img(4_1).JPG"
    add_text_to_image(image_path, text, output_path, font_path, text_x, text_y)  # Запуск для четвертого фото.

    image = Image.open('image.jpg')
    draw = ImageDraw.Draw(image)

    # Получаем текущие размеры изображения
    current_width, current_height = image.size

    # Генерируем случайные размеры для уменьшения изображения
    resized_width = random.randint(1, current_width)
    resized_height = random.randint(1, current_height)

    # Определяем координаты, куда хотим вставить случайное изображение
    position = (720, 70)  # Пример координат

    # Загружаем изображение, в которое хотим вставить случайное изображение
    background_image = Image.open("img(1).jpg")

    # Вставляем случайное изображение в фоновое изображение
    background_image.paste(image, position)

    # Сохраняем результат
    background_image.save("static/img/img(1).jpg")

    background_image = Image.open("img(2).jpg")
    background_image.paste(image, position)
    background_image.save("static/img/img(2).jpg")

    background_image = Image.open("img(3).jpg")
    background_image.paste(image, position)
    background_image.save("static/img/img(3).jpg")

    background_image = Image.open("img(4).jpg")
    background_image.paste(image, position)
    background_image.save("static/img/img(4).jpg")

    return data1, data2
