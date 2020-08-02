from flask import render_template,request
from flask import url_for,redirect
import os
from PIL import Image
from keras.models import load_model
from utils import pipeline_model




upload_folder="static/uploads"
def base():
    return render_template("base.html")

def index():
    return render_template("index.html")

def emotion():
    if request.method=='POST':
        f=request.files['image']# image requested
        filename=f.filename #name of file uploaded
        path=os.path.join(upload_folder,filename)
        f.save(path)
        pipeline_model(path,filename)

        return render_template("eotion.html",fileupload=True,img_name=filename)
    return render_template("emotion.html",fileupload=False,img_name="random.png",w=300)

