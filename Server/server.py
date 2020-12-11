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
@app.route("/api/v1.0/csharp_python_restfulapi", methods=["POST"])
def csharp_python_restfulapi():

    file = request.files['content']
    image = rest.downloadFile(file)
    ocrText = rest.imageToText(image)
    processedText = rest.preprocessText(ocrText)
    response = rest.imageClassifier(processedText)
    
    return response

if __name__ == "__main__":
    global rest
    rest = Restfull()
    app.run(debug=True)
#     run flask application in debug mode
    app.run(debug=True)