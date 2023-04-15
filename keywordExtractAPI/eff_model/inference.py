import os
import sys

import numpy as np
from skimage.io import imread

#import keras
#import tensorflow
#from keras import backend

from efficientnet.tfkeras import EfficientNetB7
from efficientnet.tfkeras import center_crop_and_resize, preprocess_input
from keras.applications.imagenet_utils import decode_predictions

from googletrans import Translator    #추출된 키워드를 한국어로 번역
import segmentation_models as sm #module 'keras.utils' has no attribute 'get_file' error 수정
sm.set_framework('tf.keras')
sm.framework()

#model = EfficientNetB0(weights='imagenet')
#image_path="./test.jpg"

#키워드 추출 함수
def inference(model, image_path):
    #print("@@@@@inference")
    #print(image_path)
    result_dic = []

    image = imread(image_path)
    image_size = model.input_shape[1]  # 224
    #print("@@@@efn 쓰기전출력")
    #print("image:")
    #print(image)
    #print("image_size")
    #print(image_size)
    #print("cx :")
    cx = center_crop_and_resize(image, image_size=image_size)
    #print(cx)
    #print("@@@@efn 쓴 후 출력")
    x = preprocess_input(cx)
    x = np.expand_dims(x, 0)
    
    y = model.predict(x)
    #print("model.predict")
    #print(y)
    dy = decode_predictions(y)[0]

    for idx, label, confidence in dy:
        new_dic = {'idx': idx, 'label': label, 'confidence': confidence}
        result_dic.append(new_dic)     #이때 result_dic은 list타입이지만, list 안에 딕셔너리가 들어있음. 즉 result_dic[0]의 타입은 딕셔너리인거임.
        # print('%s: %.2f%%' % (label, confidence * 100))
        keyword = result_dic[0]['label']
    return keyword
#print("keras:")
#print(keras.__version__)
#print("tensorflow:")
#print(tensorflow.__version__)
#print(inference(model,image_path))

#키워드 번역 함수
def transWord(model, image_path):
    word = inference(model, image_path)  #change filename in post>models.py
    print("word:")
    print(word)
    translator = Translator()
    trans = translator.translate(word, dest='ko', src='en')
    print("trans:")
    print(trans)
    trans_word = trans.text
    return trans_word
