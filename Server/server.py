# import flask microframework library
from flask import Flask
from flask import request
from flask import jsonify
import json 
import sys
import io
import numpy as np

from Operations import Restfull
 
# initialize the flask application
app = Flask(__name__)
app.config.from_object('config.Config')
@app.route("/api/v1.0/documents/classification/automatic", methods=["POST"])
def csharp_python_restfulapi():

    file = request.files['content']
    image = rest.downloadFile(file)
    ocrText = rest.imageToText(image,app.config['TESSCONFIG'])
    processedText = rest.preprocessText(ocrText,app.config['VECTORIZER'])
    response = rest.imageClassifier(processedText,app.config['MODEL'])
    
    return response

if __name__ == "__main__":
    global rest
    rest = Restfull()
    app.run(debug=True)
#     run flask application in debug mode
    app.run(debug=True)
