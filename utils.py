'''import tensorflow as tf

import keras
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, AveragePooling2D
from keras.layers import Dense, Activation, Dropout, Flatten
from keras.models import load_model
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from cv2 import cv2


model=load_model("model/ferlatest.h5")

def pipeline_model(path,filename):
    img=cv2.imread(path)
    predictions=model.predict(img)
    testing_img=np.array(img)
    testing_img=testing_img.reshape([48, 48])	
    plt.gray()
    plt.imshow(testing_img)
    plt.show()
    cv2.imwrite('static/predict/{}'.format(filename),img)'''