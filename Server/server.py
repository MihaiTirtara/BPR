# import flask microframework library
from flask import Flask
 
# initialize the flask application
app = Flask(__name__)
 
if __name__ == "__main__":
#     run flask application in debug mode
    app.run(debug=True)