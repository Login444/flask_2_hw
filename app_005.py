# Создать страницу, на которой будет форма для ввода двух
# чисел и выбор операции (сложение, вычитание, умножение
# или деление) и кнопка "Вычислить"
# При нажатии на кнопку будет произведено вычисление
# результата выбранной операции и переход на страницу с
# результатом.

from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def calculation():
    if request.method == 'POST':
        first_num = int(request.form.get('first_number'))
        second_num = int(request.form.get('second_number'))
        operation_type = request.form.get('operation_type')
        if operation_type == 'plus':
            res_calc = first_num + second_num
        elif operation_type == 'minus':
            res_calc = first_num - second_num
        elif operation_type == 'multiple':
            res_calc = first_num * second_num
        elif operation_type == 'division':
            if second_num == 0:
                return 'Делить на 0 нельзя!'
            else:
                res_calc = first_num / second_num
        return render_template('calculator_res.html', result=str(res_calc), title='Result')
    return render_template('calculator.html', title='Calculator')


if __name__ == '__main__':
    app.run(debug=True)