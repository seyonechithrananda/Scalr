#our web app framework!
#requests are objects that flask handles (get set post, etc)
#from site.views import app
from os.path import join, dirname, realpath
from flask import request, redirect, url_for, render_template, flash, send_from_directory
#from werkzeug.utils import secure_filename
from PIL import Image
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
from werkzeug.utils import secure_filename
from flask import Flask, render_template,request
#scientific computing library for saving, reading, and resizing images
from scipy.misc import imsave, imread, imresize
#for matrix math
import numpy as np
#for importing our keras model
import keras.models
#for regular expressions, saves time dealing with string data
import re
#system level operations (like loading files)
import sys 
#for reading operating system data
# import cv2
import os
import base64

from keras.models import load_model
#tell our app where our saved model is


# sys.path.append(os.path.abspath("./model"))
# from load import *


#initalize our flask app
app = Flask(__name__)
#global vars for easy reusability

# global model, graph

#initialize these variables
# model, graph = init()
#decoding an image from base64 into raw representation


UPLOAD_FOLDER = join(dirname(realpath(__file__)), 'static/uploads/')

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def convertImage(imgData1): 
	imgstr = re.search(b'base64,(.*)',imgData1).group(1) 
	#print(imgstr) 
	with open('output.png','wb') as output: 
		output.write(base64.b64decode(imgstr))
def debug():
	print('-------------------------------------------------------------------------')


# @app.route('/')
# def index():
# 	#initModel()
# 	#render out pre-built HTML file right on the index page
# 	return render_template("index.html")

@app.route('/upload_file', methods=['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		try:
			f = request.files['file']

			# f = base64.b64decode(f)
			debug()
			f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
			# return redirect(url_for('hello', filename=f.filename))
		except Exception as e:
			print(e)
	return redirect(url_for('/uploads/<filename>'))

@app.route('/uploads/<filename>')
def view_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# @app.route('/return_file/<filename>')
# def return_file(filename):
#     return send_from_directory(UPLOAD_FOLDER, filename, as_attachment = True)

def convert(img):
	x = cv2.imread(img)
	x = resize(x,(25,25))
	x = np.array(x)
	x = x.astype('float32')
	x /=255
	return x

@app.route('/enlarge/<filename>')
def denoise(filename):
	img = 0
	debug()
	print('It has begun')
	imgData= os.path.join(app.config['UPLOAD_FOLDER'], filename)
	debug()
	print(imgData)
	print('Data transfered')
	#convertImage(imgData)
	x = cv2.imread('/static/uploads/output.png')
	# x = imread('output.png', mode = 'RGB')
	print('New cv2 Worked')
	x = cv2.imresize(x,(100,100))
	debug()
	x = np.array(x)
	x = x.astype('float32')
	print('Image is float 32')
	print(type(x))
	x /= 255
	print('it worked')
	x = x.reshape(1,100,100,3)
	print('scaled it down')
	print('test the values')
    # Image processing 
	print(x[0,0:3,24,2])
	debug()
	with graph.as_default():
		model=load_model('model\medical_SRGAN.h5')
		img = model.predict(x)
		img = img [0, : , :, :]
		debug()
		print('model works')
		print (np.argmax(img,axis=1))
		#cleaned_path = UPLOAD_FOLDER + 'cleaned-' + filename
		debug()
		print(img.shape)
		# img = Image.fromarray(img)
		img =(img * 255).astype(np.uint8)
		print(type(img))
		debug()
		print('convertimage worked')
		Image.fromarray(img).save("/static/uploads/enlarged.png")
		print('SAVED image')
		# img.save(cleaned_path)
		# return render_template('DeepGalaxyDemo.html',  filename=filename, cleaned_path='cleaned-'+filename )

if __name__ == "__main__":
	#decide what port to run the app in
	port = int(os.environ.get('PORT', 5000))
	print("running on port 5000")
	#run the app locally on the givn port
	app.run(host='0.0.0.0', port=port)
	#optional if we want to run in debugging mode
	app.run(debug=True)
