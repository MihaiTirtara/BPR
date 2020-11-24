import sys
import time
import traceback
import json
import numpy as np 
import pandas as pd 

from flask import jsonify

class RESTFullSuperClass(object):
    def __init__(self):
        pass

    def is_json_data(self,data):
        json_data = None
        try:
            json_data = json.loads(data)
            return json_data,True
        except:
            return json_data, False

    def image_data_cast_normalization(self,image_1d_array,cast_data_type="float32"):
        try:
            imageDataFrame = pd.DataFrame(image_1d_array)
            XMin = 0
            XMax = 255 
            imageDataFrame = (imageDataFrame.astype(cast_data_type) - XMin)/(XMax-XMin)
        except:
            print("Image could not be casted")
        return imageDataFrame            


