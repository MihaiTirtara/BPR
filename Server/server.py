# import flask microframework library
from flask import Flask, Response
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
    autoClassificationsDocuments = request.json
    classificationResults = []
    for document in autoClassificationsDocuments:
        file_content = bytes(document["FileContent"])
        np_array_encode = np.fromstring(file_content, np.uint8)
        image = cv2.imdecode(np_array_encode, 1)
        imagePath = "uploads\\test.png"
        cv2.imwrite(imagePath, image)
        ocrText = rest.imageToText(imagePath,app.config['TESSCONFIG'])
        processedText = rest.preprocessText(ocrText,app.config['VECTORIZER'])
        response = rest.imageClassifier(processedText,app.config['MODEL'])
        classificationResults.append({'groupName': response, 'error': None})

    return jsonify(classificationResults)

    
    #return response

def manualyClassifyDocuments(documents):
    print("Not implemented")


if __name__ == "__main__":
    global rest
    rest = Restfull()
    app.run(debug=True)
#     run flask application in debug mode
    app.run(debug=True)
