# Создать страницу, на которой будет изображение и ссылка
# на другую страницу, на которой будет отображаться форма
# для загрузки изображений.


from flask import Flask, render_template, request
from pathlib import PurePath, Path
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('upload_files.html', title='Upload Files')


@app.route('/upload_form/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files.get('file')
        file_name = secure_filename(file.filename)
        file.save(PurePath.joinpath(Path.cwd(), 'uploads',
                                    file_name))
        # Уточнение если не будет создана директория uploads
        # - то будут ошибки не найденных путей
        return f"Файл {file_name} загружен на сервер"
    return render_template('upload.html')


if __name__ == '__main__':
    app.run(debug=True)