# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 21:04:26 2021

@author: z0043zrx
"""

from flask import Flask, render_template, Response, request, redirect, flash, url_for
import cv2
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

#camera declaratie (welke input?)
camera = cv2.VideoCapture(0)

#declaraties voor uploads:  
UPLOAD_FOLDER = "./static/uploads"
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

#def Toegestaande uploads:
def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

#Livecam
def gen_frames():
    while True:
        success, frame = camera.read()  #read camera frame
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'r\n') #concat frame one by one and show result
            
#livestream pagina
@app.route('/livestream')
def cam():
    return render_template('cam.html')

#camerabeeld (wordt weergegeven op livestream pagina)
@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

# pagina voor uploaden 
@app.route('/')
def upload_form():
	return render_template('upload.html')

# functionaliteit uploaden
@app.route('/', methods=['POST'])
def upload_image():
    if 'files[]' not in request.files:
        flash('No file part')
        return redirect(request.url)
    files = request.files.getlist('files[]')
    file_names = []
    for file in files:
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_names.append(filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            callProgram = str("python detect.py --source .\\static\\uploads\\" + filename + " --weights weights\\best.pt")
            os.system(callProgram)
		#else:
		#	flash('Allowed image types are -> png, jpg, jpeg, gif')
		#	return redirect(request.url)

    return render_template('upload.html', filenames=file_names)

# weergeven geuploadde afbeeldingen
@app.route('/static/recognized/<filename>')
def display_image(filename):
 	# print('display_image filename: ' + filename)
	return redirect(url_for('static', filename='Recognized/' + filename), code=301)

# weergeven geuploadde afbeeldingen
@app.route('/info')
def info():
	return render_template("info.html")
    
# pagina voor gallerij 
@app.route('/gallery')
def gallery():
	return render_template("gallery.html")

# main
if __name__ == "__main__":
    app.run(debug=True)  #connect to http://127.0.0.1:5000/
    #app.run(debug=True, host= '172.20.10.3') #connect to http://172.20.10.3:5000/


#####VOID#####

# @app.route('/home')
# def home():
#     return render_template('index.html')


# @app.route('/index')
# def index():
#     return render_template('index.html')

# @app.route("/upload-image", methods=["GET", "POST"])
# def upload_image():
#     app.config["IMAGE_UPLOADS"] = UploadDir
#     if request.method == "POST":

#         if request.files:

#             image = request.files["image"]
            
#             image.save(os.path.join(os.path.abspath(__file__),'..', UploadDir, image.filename))

#             print("image saved")

#             return redirect(request.url)


#     return render_template("upload_image.html")

# @app.route("/uploaded")
# def Pictures():
#     pics = os.listdir(UploadDir)
#     # pics = ['picture/' + file for file in pics]
#     return render_template('uploaded.html', pics = pics)
