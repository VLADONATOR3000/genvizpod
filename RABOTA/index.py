# Импортирем нужные библиотеки
from PIL import Image, ImageDraw, ImageFont

# Открываем изображение 1
image = Image.open("slide (1).jpg")
draw = ImageDraw.Draw(image)
x1, y1 = 50, 100  # Начальная точка
x2, y2 = 700, 350  # Конечная точка
draw.rectangle([x1, y1, x2, y2], fill="rgb(234, 243, 250)")
image.save("RABOTA/img(1_1).jpg")





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
font_path = "arial.ttf"  # путь к файлу шрифта, если используется другой шрифт
text = "Текст"

output_path = "RABOTA/img(1).jpg"
image_path = "slide (1).JPG"
text_x = 60 
text_y = 120 
add_text_to_image(image_path, text, output_path, font_path, text_x, text_y) # Запуск для первого фото.

output_path = "RABOTA/img(2).jpg"
image_path = "slide (2).JPG"
text_x = 60 
text_y = 185
add_text_to_image(image_path, text, output_path, font_path, text_x, text_y) # Запуск для второго фото.

output_path = "RABOTA/img(3).jpg"
image_path = "slide (3).JPG"
text_x = 60 
text_y = 150 
add_text_to_image(image_path, text, output_path, font_path, text_x, text_y) # Запуск для третьего фото.

output_path = "RABOTA/img(4).jpg"
image_path = "slide (4).JPG"
text_x = 60 
text_y = 150 
add_text_to_image(image_path, text, output_path, font_path, text_x, text_y) # Запуск для четвертого фото.
