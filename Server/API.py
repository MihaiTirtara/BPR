try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import sys
import time
import traceback
import json
import numpy as np 
import pandas as pd 
import io
from cv2 import  cv2
import joblib
from flask import jsonify
import scipy.sparse.linalg
from sklearn.feature_extraction.text import TfidfVectorizer

class Restfull():

    def downloadFile(self,file):
        print(file)
        in_memory_file = io.BytesIO()
        file.save(in_memory_file)
        data = np.fromstring(in_memory_file.getvalue(), dtype=np.uint8)
        color_image_flag = 1
        img = cv2.imdecode(data, color_image_flag)
        cv2.imwrite("uploads\\" + file.filename, img)
        print("uploads\\" + file.filename)
        return("uploads\\" + file.filename)

    def imageToText(self,filename):
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        ocrText = pytesseract.image_to_string(filename)
        print(ocrText)
        return ocrText
    
    def preprocessText(self,ocrText):
        vectorizer = joblib.load('vectorizer.joblib')
        textArray = [ocrText]
        vectorText = vectorizer.transform(textArray)
        vectorText = vectorText.reshape(1,-1)
        return vectorText

    def imageClassifier(self,obj):
        classifiermodel = joblib.load('svm.joblib')
        try:    
            #Prediction
            print('I am here')
            YPredict = classifiermodel.predict(obj)
            print("I got here")
            print(YPredict[0])
            if YPredict[0] == 0:
                result = 'The document is a Letter'
            elif YPredict[0] == 1:
                result = 'The document is a Form'
            elif YPredict[0] == 2:
                result = 'The document is a E-mail'  
            elif YPredict[0] == 3:
                result = 'The document is a Handwriten'       
            elif YPredict[0] == 4:
                result = 'The document is a Advertisment'
            elif YPredict[0] == 5:
                result = 'The document is a Scientific Report'
            elif YPredict[0] == 6:
                result = 'The document is a Scientific Publication'
            elif YPredict[0] == 7:
                result = 'The document is a Specification'
            elif YPredict[0] == 7:
                result = 'The document is a Specification'
            elif YPredict[0] == 8:
                result = 'The document is a File Folder'
            elif YPredict[0] == 9:
                result = 'The document is a News Article'
            elif YPredict[0] == 10:
                result = 'The document is a Budget'
            elif YPredict[0] == 11:
                result = 'The document is a Invoice'
            elif YPredict[0] == 12:
                result = 'The document is a Presentation'
            elif YPredict[0] == 13:
                result = 'The document is a Questionaire'
            elif YPredict[0] == 14:
                result = 'The document is a Resume'
            elif YPredict[0] == 15:
                result = 'The document is a Memo'
            else:
                result = 'No document'                                
            #Return response
            response = jsonify(result)
            response.status_code = 200
        except:
            result = "An error occured"
            response = jsonify(result)
            response.status_code = 400
        return response   