# import flask microframework library
from flask import Flask
from flask import request
from flask import jsonify
import json 
import sys
import io
import numpy as np
import cv2

from restfullSubClass import RestfullSubClass
 
# initialize the flask application
app = Flask(__name__)
@app.route("/api/v1.0/csharp_python_restfulapi_json", methods=["POST"])
def csharp_python_restfulapi_json():

    """
    simple c# test to call python restful api web service
    """
    file = request.files['content']
    filename = file.filename
    print(file)
    in_memory_file = io.BytesIO()
    file.save(in_memory_file)
    data = np.fromstring(in_memory_file.getvalue(), dtype=np.uint8)
    color_image_flag = 1
    img = cv2.imdecode(data, color_image_flag)
    
    cv2.imwrite("uploads\\" + file.filename, img)
    #response =  restful.imageClassiferJsonEnconding(request)
    return("Woroks")

if __name__ == "__main__":
    global restfull
    restful = RestfullSubClass(100,100)
    app.run(debug=True)
#     run flask application in debug mode
    app.run(debug=True)