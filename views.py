from flask import render_template,request
from flask import url_for,redirect
import os
from PIL import Image
from keras.models import load_model
#from utils import pipeline_model
from tensorflow.keras.models import model_from_json
import numpy as np
import tensorflow as tf
#from flask import Flask,Response
#from camera import VideoCamera



upload_folder="static/uploads"

def base():
    return render_template("base.html")

def index1():
    return render_template("index1.html")

'''
def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
    

def video_play():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
'''
'''

class FacialExpressionModel(object):
    
    EMOTIONS_LIST = ["Angry", "Disgust",
                     "Fear", "Happy",
                     "Neutral", "Sad",
                     "Surprise"]

    def __init__(self, model_json_file, model_weights_file):
        # load model from JSON file
        with open(model_json_file, "r") as json_file:
            loaded_model_json = json_file.read()
            self.loaded_model = model_from_json(loaded_model_json)

        # load weights into the new model
        self.loaded_model.load_weights(model_weights_file)
        #self.loaded_model._make_predict_function()

    def predict_emotion(self, img):
        self.preds = self.loaded_model.predict(img)
        return FacialExpressionModel.EMOTIONS_LIST[np.argmax(self.preds)]

def emotion():
    if request.method=='POST':
        f=request.files['image']# image requested
        filename=f.filename #name of file uploaded
        path=os.path.join(upload_folder,filename)
        f.save(path)
        pipeline_model(path,filename)

        return render_template("eotion.html",fileupload=True,img_name=filename)
    return render_template("emotion.html",fileupload=False,img_name="random.png",w=300)

'''