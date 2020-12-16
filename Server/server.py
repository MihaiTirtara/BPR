# import flask microframework library
from flask import Flask
from flask import request
from flask import jsonify
import json 
import sys
import io
import numpy as np
import base64
from cv2 import cv2

from Operations import Restfull
 
# initialize the flask application
app = Flask(__name__)
app.config.from_object('config.Config')
@app.route("/api/v1.0/documents/classification/automatic", methods=["POST"])
def automaticallyClasifyDocuments(): 
    #Trying to decode the image
    request_data = request.data
    image_string = base64.b64decode(request_data)
    np_array_encode = np.fromstring(image_string, np.uint8)    
    image = cv2.imdecode(np_array_encode, cv2.IMREAD_GRAYSCALE)
    print(image)

    #file = request.files['content']
    #image = rest.downloadFile(file)
    #ocrText = rest.imageToText(image,app.config['TESSCONFIG'])
    #processedText = rest.preprocessText(ocrText,app.config['VECTORIZER'])
    #response = rest.imageClassifier(processedText,app.config['MODEL'])
    
    #return response

def manualyClassifyDocuments(documents):
    print("Not implemented")


if __name__ == "__main__":
    global rest
    rest = Restfull()
    app.run(debug=True)
#     run flask application in debug mode
    app.run(debug=True)
