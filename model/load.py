
import numpy as np
import keras.models
from keras.models import model_from_json
from scipy.misc import imread, imresize,imshow
import tensorflow as tf
from keras.optimizers import SGD,RMSprop,adam



def init(): 
	json_file = open('model/gen.json','r')
	loaded_model_json = json_file.read()
	json_file.close()
	loaded_model = model_from_json(loaded_model_json)
	#load woeights into new model
	loaded_model.load_weights("model\medical_SRGAN.h5")
	print("Loaded Model from disk")
	sgd = SGD(lr=1, clipnorm=1, clipvalue=0.5)
	#compile and evaluate loaded model
	loaded_model.compile(loss='mean_squared_logarithmic_error',optimizer=sgd ,metrics=['accuracy'])
	#loss,accuracy = loaded_model.evaluate(X_test,y_test)
	#print('loss:', loss)
	#print('accuracy:', accuracy)
	graph = tf.get_default_graph()
	return loaded_model,graph