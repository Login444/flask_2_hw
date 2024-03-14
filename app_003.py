# Создать страницу, на которой будет форма для ввода логина
# и пароля
# При нажатии на кнопку "Отправить" будет произведена
# проверка соответствия логина и пароля и переход на
# страницу приветствия пользователя или страницу с
# ошибкой.


from flask import Flask, render_template, request


app = Flask(__name__)

LOGIN = 'login'
PASSWORD = '111'
@app.route('/', methods=['GET', 'POST'])
def login_():
    if request.method == 'GET':
        return render_template('login_page.html', title='LogIn')

    u_login = request.values.get('login')
    u_password = request.values.get('password')
    if u_login == LOGIN and u_password == PASSWORD:
        return render_template('index.html', title='Home')
    return render_template('error.html', title='error')


if __name__ == '__main__':
    app.run(debug=True)