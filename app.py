#our web app framework!
#Generating HTML from within Python is not fun, and actually pretty cumbersome because you have to do the
#HTML escaping on your own to keep the application secure. Because of that Flask configures the Jinja2 template engine 
#for you automatically.
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
#tell our app where our saved model is
sys.path.append(os.path.abspath("./model"))
from model import load 
#initalize our flask app
app = Flask(__name__)
#global vars for easy reusability
global model, graph
#initialize these variables
model, graph = init()

#decoding an image from base64 into raw representation

# def convertImage(imgData1): 
# 	imgstr = re.search(b'base64,(.*)',imgData1).group(1) #print(imgstr) 
# 	with open('output.png','wb') as output: 
# 		output.write(base64.b64decode(imgstr))	
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


@app.route('/')
def index():
	#initModel()
	#render out pre-built HTML file right on the index page
	return render_template("index.html")
@app.route('/learn.html')
def learn():
	#initModel()
	#render out pre-built HTML file right on the index page
	return render_template("learn.html")
@app.route('/DeepGalaxy.html')
def DeepGalaxy():
	#initModel()
	#render out pre-built HTML file right on the index page
	return render_template("DeepGalaxy.html")
@app.route('/DeepGalaxyDemo.html')
def DeepGalaxyDemo(filename="", cleaned_path="", error=""):
	#initModel()
	#render out pre-built HTML file right on the index page
	return render_template('DeepGalaxyDemo.html', filename=filename, cleaned_path=cleaned_path, error=error)
@app.route('/research.html')
def research():
	#initModel()
	#render out pre-built HTML file right on the index page
	return render_template("research.html")
@app.route('/team.html')
def team():
	#initModel()
	#render out pre-built HTML file right on the index page
	return render_template("team.html")
@app.route('/index.html')
def home():
	#initModel()
	#render out pre-built HTML file right on the index page
	return render_template("index.html")





# @app.route('/denosise/learn.html')
# def learn():
# 	#initModel()
# 	#render out pre-built HTML file right on the index page
# 	return render_template("learn.html")
# @app.route('/denosise/DeepGalaxy.html')
# def DeepGalaxy():
# 	#initModel()
# 	#render out pre-built HTML file right on the index page
# 	return render_template("DeepGalaxy.html")
# @app.route('/denosise/DeepGalaxyDemo.html')
# def DeepGalaxyDemo(filename="", cleaned_path="", error=""):
# 	#initModel()
# 	#render out pre-built HTML file right on the index page
# 	return render_template('DeepGalaxyDemo.html', filename=filename, cleaned_path=cleaned_path, error=error)
# @app.route('/denosise/research.html')
# def research():
# 	#initModel()
# 	#render out pre-built HTML file right on the index page
# 	return render_template("research.html")
# @app.route('/denosise/team.html')
# def team():
# 	#initModel()
# 	#render out pre-built HTML file right on the index page
# 	return render_template("team.html")
# @app.route('/denosise/index.html')
# def home():
# 	#initModel()
# 	#render out pre-built HTML file right on the index page
# 	return render_template("index.html")


# @app.route('/upload_file/learn.html')
# def learn():
# 	#initModel()
# 	#render out pre-built HTML file right on the index page
# 	return render_template("learn.html")
# @app.route('/upload_file/DeepGalaxy.html')
# def DeepGalaxy():
# 	#initModel()
# 	#render out pre-built HTML file right on the index page
# 	return render_template("DeepGalaxy.html")
# @app.route('/upload_file/DeepGalaxyDemo.html')
# def DeepGalaxyDemo(filename="", cleaned_path="", error=""):
# 	#initModel()
# 	#render out pre-built HTML file right on the index page
# 	return render_template('DeepGalaxyDemo.html', filename=filename, cleaned_path=cleaned_path, error=error)
# @app.route('/upload_file/research.html')
# def research():
# 	#initModel()
# 	#render out pre-built HTML file right on the index page
# 	return render_template("research.html")
# @app.route('/upload_file/team.html')
# def team():
# 	#initModel()
# 	#render out pre-built HTML file right on the index page
# 	return render_template("team.html")
# @app.route('/upload_file/index.html')
# def home():
# 	#initModel()
# 	#render out pre-built HTML file right on the index page
# 	return render_template("index.html")


# @app.route('/uploads/learn.html')
# def learn():
# 	#initModel()
# 	#render out pre-built HTML file right on the index page
# 	return render_template("learn.html")
# @app.route('/uploads/DeepGalaxy.html')
# def DeepGalaxy():
# 	#initModel()
# 	#render out pre-built HTML file right on the index page
# 	return render_template("DeepGalaxy.html")
# @app.route('/uploads/DeepGalaxyDemo.html')
# def DeepGalaxyDemo(filename="", cleaned_path="", error=""):
# 	#initModel()
# 	#render out pre-built HTML file right on the index page
# 	return render_template('DeepGalaxyDemo.html', filename=filename, cleaned_path=cleaned_path, error=error)
# @app.route('/uploads/research.html')
# def research():
# 	#initModel()
# 	#render out pre-built HTML file right on the index page
# 	return render_template("research.html")
# @app.route('/uploads/team.html')
# def team():
# 	#initModel()
# 	#render out pre-built HTML file right on the index page
# 	return render_template("team.html")
# @app.route('/uploads/index.html')
# def home():
# 	#initModel()
# 	#render out pre-built HTML file right on the index page
# 	return render_template("index.html")


# @app.route('/return_file/learn.html')
# def learn():
# 	#initModel()
# 	#render out pre-built HTML file right on the index page
# 	return render_template("learn.html")
# @app.route('/return_file/DeepGalaxy.html')
# def DeepGalaxy():
# 	#initModel()
# 	#render out pre-built HTML file right on the index page
# 	return render_template("DeepGalaxy.html")
# @app.route('/return_file/DeepGalaxyDemo.html')
# def DeepGalaxyDemo(filename="", cleaned_path="", error=""):
# 	#initModel()
# 	#render out pre-built HTML file right on the index page
# 	return render_template('DeepGalaxyDemo.html', filename=filename, cleaned_path=cleaned_path, error=error)
# @app.route('/return_file/research.html')
# def research():
# 	#initModel()
# 	#render out pre-built HTML file right on the index page
# 	return render_template("research.html")
# @app.route('/return_file/team.html')
# def team():
# 	#initModel()
# 	#render out pre-built HTML file right on the index page
# 	return render_template("team.html")
# @app.route('/return_file/index.html')
# def home():
# 	#initModel()
# 	#render out pre-built HTML file right on the index page
# 	return render_template("index.html")


@app.route('/upload_file', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        try:
            f = request.files['file']
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
            # return redirect(url_for('hello', filename=f.filename))
            return render_template('DeepGalaxyDemo.html', filename=f.filename)
        except Exception as e:
            return render_template('DeepGalaxyDemo.html', error=e)
    return redirect(url_for('hello'))


@app.route('/uploads/<filename>')
def view_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route('/return_file/<filename>')
def return_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename, as_attachment = True)

@app.route('/denosise/<filename>')
def denoise(filename):
	img = 0
	debug()
	print('It has begun')
	debug()
	imgData= os.path.join(app.config['UPLOAD_FOLDER'], filename)
	debug()
	print(imgData)
	print('Data transfered')
	#convertImage(imgData)
	x = cv2.imread('output.png')
	# x = imread('output.png', mode = 'RGB')
	print('New cv2 Worked')
	x = cv2.imresize(x,(25,25))
	debug()
	x = np.array(x)
	x = x.astype('float32')
	print('Image is float 32')
	print(type(x))
	x /= 255
	print('it worked')
	x = x.reshape(1,25,25,3)
	print('scaled it down')
	print('test the values')
	print(x[0,0:3,24,2])
	debug()
	with graph.as_default():
		img = model.predict(x)
		img = img [0, : , :, :]
		debug()
		print('model works')
		print (np.argmax(img,axis=1))
		cleaned_path = UPLOAD_FOLDER + 'cleaned-' + filename
		debug()
		print(img.shape)
		# img = Image.fromarray(img)
		img =(img * 255).astype(np.uint8)
		print(type(img))
		debug()
		print('convertimage worked')
		Image.fromarray(img).save(cleaned_path)
		print('SAVED image')
		# img.save(cleaned_path)
		return render_template('DeepGalaxyDemo.html',  filename=filename, cleaned_path='cleaned-'+filename )

if __name__ == "__main__":
	#decide what port to run the app in
	port = int(os.environ.get('PORT', 5000))
	#run the app locally on the givn port
	app.run(host='0.0.0.0', port=port)
	#optional if we want to run in debugging mode
	app.run(debug=True)