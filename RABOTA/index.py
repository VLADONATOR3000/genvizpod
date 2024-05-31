# Импортирем нужные библиотеки
from PIL import Image, ImageDraw, ImageFont

def add_text_to_image(image_path, text, output_path, font_path=None, text_x=None, text_y=None):
    # Открываем изображение
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)

    # Устанавливаем шрифт
    if font_path:
        font = ImageFont.truetype(font_path, size=50)
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
image_path = "slide (3).JPG"
text = "цфвцфвцфвфцвфцвфцвфцвв"
output_path = "RABOTA/img.jpg"
font_path = "arial.ttf"  # путь к файлу шрифта, если используется другой шрифт
text_x = 60  # координата X текста
text_y = 170  # координата Y текста

add_text_to_image(image_path, text, output_path, font_path, text_x, text_y)
