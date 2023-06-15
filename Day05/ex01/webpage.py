from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
import json

app = Flask(__name__)
ALLOWED_EXTENSIONS = {'mp3', 'ogg', 'wav'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/list", methods=["GET"])
def get_list():
    list_of_files = []
    for filename in os.listdir('upload'):
        list_of_files.append(filename)
    response = app.response_class(
        response=json.dumps(list_of_files),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/upload/<name>')
def download_file(name):
    return send_from_directory(os.getcwd() + "/upload/", name)

@app.route("/")
def main():
    list_singls = 'upload/'
    with os.scandir(list_singls) as files:
        files = [file.name for file in files]

    return render_template('index.html', list_singls=files)


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':

        file = request.files['file']

        if allowed_file(file.filename):
            file.save(os.getcwd() + "/upload/{}".format(file.filename))
        else:
            return "Non-audio file detected"

    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True, port=8888)