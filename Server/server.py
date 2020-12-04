# import flask microframework library
from flask import Flask
from flask import request
from flask import jsonify
import json 
import sys
import io
import numpy as np

from restfull import Restfull
 
# initialize the flask application
app = Flask(__name__)
@app.route("/api/v1.0/csharp_python_restfulapi_json", methods=["POST"])
def csharp_python_restfulapi_json():

    """
    simple c# test to call python restful api web service
    """
    file = request.files['content']
    image = rest.downloadFile(file)
    ocrText = rest.imageToText(image)
    processedText = rest.preprocessText(ocrText)
    response = rest.imageClassifier(processedText)
    
    #response =  restful.imageClassiferJsonEnconding(request)
    return response

if __name__ == "__main__":
    global rest
    rest = Restfull()
    app.run(debug=True)
#     run flask application in debug mode
    app.run(debug=True)