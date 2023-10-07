import os
from flask import Flask, flash, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
from werkzeug.datastructures import ImmutableMultiDict
from requests_toolbelt.multipart import decoder


UPLOAD_FOLDER = '../uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        print("1")
        if 'file' not in request.files:
            print("2")
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            print("3")
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            print("4")
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return "Success", 200
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''
    
@app.route('/up', methods=['POST'])
def up_file():
    file = request.files['file']
    print("te")
    if request.method == 'POST':
        # check if the post request has the file part
        print("a")
        testEnrollResponse = requests.post(...)
        multipart_data = decoder.MultipartDecoder.from_response(testEnrollResponse)

        for part in multipart_data.parts:
            print(part.content)  # Alternatively, part.text if you want unicode
            print(part.headers)
        data = dict(request.form)
        print("data")
        print(data)
        if 'file' not in request.files:
            print("2")
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            print("3")
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            print("4")
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    '''
    
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)
    
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=True)