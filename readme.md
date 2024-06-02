### Добро пожаловать!
*** 
В представленном архиве вы можете увидеть следующие папки и файлы

1. Папка **venv** - виртуальное окружение.
2. Файл **app.py** - приложение на Flask.
3. Папка **Файлы img..., файлы slide...** - Основные фото проекта
4. Файл **script.py** - генератор изображений.
3. Папка **Файлы img..., файлы silde...** - Основные фото проекта

***

##### Вашей задачей будет разработка генеративной модели для изображений на основе текстов и стандартов брендбуков.

Запуск приложения:
В терминале прописываем:

1. python -m venv venv 
2. .\venv\Scripts\activate

3. Установить библиотеки  
import requests
    import json
    import time
    import base64
    import random
    from PIL import Image, ImageDraw, ImageFont
    from flask import Flask, render_template, request
    import asyncio
4. python app.py

#   УРА!