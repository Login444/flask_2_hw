# Создать страницу, на которой будет форма для ввода текста и
# кнопка "Отправить"
# При нажатии кнопки будет произведен подсчет количества слов
# в тексте и переход на страницу с результатом.


from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        text_for_calc = request.form.get('text')
        return f'В тексте {len(text_for_calc.split())} слов'
    return render_template('calc_text.html', title='Calculation')


if __name__ == '__main__':
    app.run(debug=True)