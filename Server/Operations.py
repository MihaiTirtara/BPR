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
from cv2 import cv2
import joblib
from flask import jsonify
import scipy.sparse.linalg
from sklearn.feature_extraction.text import TfidfVectorizer


class Restfull():

    def downloadFile(self, document):
        file_content = bytes(document["FileContent"])
        np_array_encode = np.fromstring(file_content, np.uint8)
        image = cv2.imdecode(np_array_encode, 1)
        imagePath = "uploads\\test.png"
        cv2.imwrite(imagePath, image)
        return imagePath

    def imageToText(self, filename, tesseractPath):
        pytesseract.pytesseract.tesseract_cmd = tesseractPath
        ocrText = pytesseract.image_to_string(filename)
        print(ocrText)
        return ocrText

    def preprocessText(self, ocrText, vectorizerPath):
        vectorizer = joblib.load(vectorizerPath)
        textArray = [ocrText]
        vectorText = vectorizer.transform(textArray)
        vectorText = vectorText.reshape(1, -1)
        return vectorText

    def imageClassifier(self, obj, modelPath):
        types = ["Letter", "TooLazy"]
        try:
            classifiermodel = joblib.load(modelPath)
            # Prediction
            YPredict = classifiermodel.predict(obj)
            return {'groupName': types[YPredict[0]], 'error': None}
        except:
            return {'groupName': None, 'error': 'An error occurred while classifying'}
