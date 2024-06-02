from flask import Flask, render_template, request
from script import process_data

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 * 1024


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        data1 = request.form['data1']
        data2 = request.form['data2']

        # Получаем данные из формы

        # Обрабатываем данные сразу для обеих переменных
        processed_data1, processed_data2 = process_data(data1, data2)
        # Обработка других данных

        return render_template('index.html', processed_data1=processed_data1, processed_data2=processed_data2)
        # Передаем обработанные данные обратно в index.html для отображения

if __name__ == '__main__':
    app.run(debug=True)
