import os 
import sys
import numpy as np
import json 
import base64
import cv2
import pickle
import joblib
from flask import jsonify

from restfullSuperClass import RESTFullSuperClass

class RestfullSubClass(RESTFullSuperClass):
    def __init__(self,imageWidthResize=None,imageHeightResize=None):
        super().__init__()
        if imageWidthResize  is not None:
            self.image_width = imageHeightResize
        if imageHeightResize is not None:
            self.image_height = imageHeightResize
    def image_resize_opencv(self,image,arrayDim="1d"):
        imageArray = None
        try:
            imageDimension = (self.image_width,self.image_height)
            newImage = cv2.resize(image,imageDimension,interpolatin=cv2.INTER_AREA)
            imageArray = np.fromstring(newImage.tobytes(),dtype=np.uint8)
            if(arrayDim == "1d"):
                imageArray = imageArray.reshape((1,self.image_height*self.image_width))
        except:
            print("Image resize was not possible")
        return imageArray
    def imageClassiferJsonEnconding(self,request):
        print(request.data)
        encoding ="ISO-8859-1"
        print("I got here with this ")
        requestData = request.data 
        imageJson = json.loads(requestData)
        #get content as string
        imageText = imageJson["content"]
        #convert string to array of int
        arrayEncode = np.fromstring(imageText.encode(encoding),np.uint8)
        #decode the array to cv2 image
        image = cv2.imdecode(arrayEncode,cv2.IMREAD_GRAYSCALE)

            #image pre-processing
        imageArray = self.image_resize_opencv(image)
        XTest = self.image_data_cast_normalization(imageArray)
        print(XTest)

        #Classification Model
        projectPath = os.path.dirname(os.path.realpath(__file__))
        #classifierModelFile = open(os.path.join(projectPath,"first.pkl"),"rb")
        classifiermodel = joblib.load('first.joblib')
        #classifierModel = pickle.load(classifierModelFile)
        try:    
            #Predicition
            YPredict = classifierModel.predict(XTest)
            print("I got here")
            print(YPredict)
            #if YPredict == 1:
             #   result = "Good"
            #else:
             #   result = "Too bad"

            #Return response
            response = jsonify(result)
            response.status_code = 200
        except:
            result = "An error occured"
            response = jsonify(result)
            response.status_code = 400
        return response




