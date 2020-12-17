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
def automaticallyClassifyDocuments():
    # Trying to decode the image
    autoClassificationsDocuments = request.json
    classificationResults = []
    for document in autoClassificationsDocuments:
        imagePath = rest.downloadFile(document)
        ocrText = rest.imageToText(imagePath, app.config['TESSCONFIG'])
        processedText = rest.preprocessText(ocrText, app.config['VECTORIZER'])
        classificationResult = rest.imageClassifier(processedText, app.config['MODEL'])
        classificationResults.append(classificationResult)
    return jsonify(classificationResults)


def manuallyClassifyDocuments(documents):
    print("Not implemented")


if __name__ == "__main__":
    global rest
    rest = Restfull()
    app.run(debug=True)
    #     run flask application in debug mode
    app.run(debug=True)
