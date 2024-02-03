import os
import glob
import datetime
from flask import Flask, flash, request, redirect, url_for, send_from_directory, jsonify
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename
from werkzeug.datastructures import ImmutableMultiDict
from multiprocessing import Value

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

    
@app.route('/files', methods=["GET"])
@cross_origin()
def send_files():
    jpg_files = glob.glob(os.path.join(app.root_path, 'uploads', '*.jpg'))
    image_names = [os.path.basename(file) for file in jpg_files]
    return jsonify(image_names)


@app.route("/upload-image", methods=["POST"])
def upload_image():
    if request.method == "POST":
        print("Received image")
        image_raw_bytes = request.get_data()
        
        now = datetime.datetime.now()
        #save to the same folder as the flask app live in 
        save_location = (os.path.join(app.root_path, f"uploads/image_{now.year}-{now.month}-{now.day}-{now.hour}-{now.minute}-{now.second}.jpg")) 

        f = open(save_location, 'wb')
        f.write(image_raw_bytes)   # write the bytes from the request body to the file
        f.close()
        return "image saved"

      
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(os.path.join(app.root_path, "uploads/"),
                               filename)


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000, debug=True)