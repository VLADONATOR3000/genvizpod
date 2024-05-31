# Импортирем нужные библиотеки
import os
import random
from PIL import Image, ImageDraw, ImageFont

# Открываем изображение 1
image = Image.open("slide (1).jpg")
draw = ImageDraw.Draw(image)
x1, y1 = 50, 100  # Начальная точка
x2, y2 = 700, 350  # Конечная точка
draw.rectangle([x1, y1, x2, y2], fill="rgb(234, 243, 250)")
image.save("RABOTA/img(1_1).jpg")

# Открываем изображение 2
image = Image.open("slide (2).jpg")
draw = ImageDraw.Draw(image)
x1, y1 = 00, 000  # Начальная точка
x2, y2 = 700, 350  # Конечная точка
draw.rectangle([x1, y1, x2, y2], fill="rgb(254, 247, 231)")
image.save("RABOTA/img(2_1).jpg")

# Файл 3 не нуждается
# image = Image.open("slide (3).jpg")
# draw = ImageDraw.Draw(image)
# x1, y1 = 50, 100  # Начальная точка
# x2, y2 = 700, 350  # Конечная точка
# draw.rectangle([x1, y1, x2, y2], fill="rgb(234, 243, 250)")
# image.save("RABOTA/img(3_1).jpg")

# Открываем изображение 4
image = Image.open("slide (4).jpg")
draw = ImageDraw.Draw(image)
x1, y1 = 50, 100  # Начальная точка
x2, y2 = 700, 350  # Конечная точка
draw.rectangle([x1, y1, x2, y2], fill="white")
image.save("RABOTA/img(4_1).jpg")





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
    if len(text) > 30:
        first_space = text.find(' ')
        if first_space != -1:
            second_space = text.find(' ', first_space + 1)
            if second_space != -1 and second_space <= 30:
                dropped_text = text[:second_space] + '\n' + text[second_space + 1:]
            else:
                dropped_text = text[:first_space] + '\n' + text[first_space + 1:]
        else:
            dropped_text = text
    else:
        dropped_text = text
    return dropped_text

text = "Пресс-конференция по итогам заседания Совета директоров по денежно-кредитной политике"
dropped_text = drop_part_with_space(text)
text = dropped_text 


output_path = "RABOTA/img(1).jpg"
image_path = "RABOTA/img(1_1).JPG"
add_text_to_image(image_path, text, output_path, font_path, text_x, text_y) # Запуск для первого фото.

output_path = "RABOTA/img(2).jpg"
image_path = "RABOTA/img(2_1).JPG"
add_text_to_image(image_path, text, output_path, font_path, text_x, text_y) # Запуск для второго фото.

output_path = "RABOTA/img(3).jpg"
image_path = "RABOTA/img(3_1).JPG" 
add_text_to_image(image_path, text, output_path, font_path, text_x, text_y) # Запуск для третьего фото.

output_path = "RABOTA/img(4).jpg"
image_path = "RABOTA/img(4_1).JPG"
add_text_to_image(image_path, text, output_path, font_path, text_x, text_y) # Запуск для четвертого фото.




# Функция для выбора случайного изображения из папок
def get_random_image_path(root_dir):
    # Список путей к изображениям
    image_paths = []

    # Обход всех файлов и подпапок в корневой папке
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            # Проверка расширения файла
            if file.endswith(('.jpg', '.jpeg', '.png', '.gif')):
                image_paths.append(os.path.join(root, file))

    # Возвращаем случайный путь к изображению
    return random.choice(image_paths)

# Путь к папке с изображениями
images_folder = "RABOTA/illustrations"

# Получаем случайный путь к изображению
random_image_path = get_random_image_path(images_folder)

# Открываем случайное изображение
random_image = Image.open(random_image_path)

# Задаем желаемые параметры размера
desired_width = 80  # Желаемая ширина
desired_height = 80  # Желаемая высота

# Получаем текущие размеры изображения
current_width, current_height = random_image.size

# Задаем желаемые параметры размера
desired_width = 60  # Желаемая ширина
desired_height = 60  # Желаемая высота

# Генерируем случайные размеры для уменьшения изображения
resized_width = random.randint(1, current_width)
resized_height = random.randint(1, current_height)

# Уменьшаем размеры до максимально допустимых значений
resized_width = min(resized_width, desired_width)
resized_height = min(resized_height, desired_height)

# Определяем координаты, куда хотим вставить случайное изображение
position = (700, 80)  # Пример координат

# Загружаем изображение, в которое хотим вставить случайное изображение
background_image = Image.open("RABOTA/img(1).jpg")

# Вставляем случайное изображение в фоновое изображение
background_image.paste(random_image, position)

# Сохраняем результат
background_image.save("RABOTA/img(1).jpg")


background_image = Image.open("RABOTA/img(2).jpg")
background_image.paste(random_image, position)
background_image.save("RABOTA/img(2).jpg")

background_image = Image.open("RABOTA/img(3).jpg")
background_image.paste(random_image, position)
background_image.save("RABOTA/img(3).jpg")

background_image = Image.open("RABOTA/img(4).jpg")
background_image.paste(random_image, position)
background_image.save("RABOTA/img(4).jpg")


