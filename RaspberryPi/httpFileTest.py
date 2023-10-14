import os
from flask import Flask, flash, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
from werkzeug.datastructures import ImmutableMultiDict
from requests_toolbelt.multipart import decoder
from multiprocessing import Value


UPLOAD_FOLDER = '../uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# declare counter variable
counter = Value('i', 0)

def save_img():
	with counter.get_lock():
		counter.value += 1
		return counter.value
	# print("Image Saved", end="\n") # debug
           

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
            file.save(os.path.join(app.root_path, "uploads/Foto.jpg"))
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
    
@app.route("/upload-image", methods=["GET", "POST"])
def upload_image():

    if request.method == "POST": #if we make a post request to the endpoint, look for the image in the request body
        print("f")
        image_raw_bytes = request.get_data()  #get the whole body
        
        number = save_img()
        print("dada" + str(number))

        save_location = (os.path.join(app.root_path, "uploads/image_"+str(number)+".jpg")) #save to the same folder as the flask app live in 

        f = open(save_location, 'wb') # wb for write byte data in the file instead of string
        f.write(image_raw_bytes) #write the bytes from the request body to the file
        f.close()

        print("Image saved")

        return "image saved"

    if request.method == "GET": #if we make a get request (for example with a browser) show the image.
    # The browser will cache this image so when you want to actually refresh it, press ctrl-f5
        return render_template("image_show.html")
    return "if you see this, that is bad request method"
    
@app.route('/up', methods=['POST'])
def upload():
	received = request
	img = None
	if received.files:
		print(received.files['file'])
		# convert string of image data to uint8
		file  = received.files['file']
		nparr = np.fromstring(file.read(), np.uint8)
		# decode image
		img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
		save_img(img)
		
		return "[SUCCESS] Image Received", 201
	else:
		return "[FAILED] Image Not Received", 204
    
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)
    
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=True)