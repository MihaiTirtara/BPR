# import flask microframework library
from flask import Flask
from flask import request
from flask import jsonify

from ClassifierService import ClassifierService

# initialize the flask application
app = Flask(__name__)
app.config.from_object('config.Config')


@app.route("/api/v1.0/documents/classification/automatic", methods=["POST"])
def automaticallyClassifyDocuments():
    autoClassificationsDocuments = request.json # Read the request body as a dictionary.
    classificationResults = []
    for document in autoClassificationsDocuments:
        pdfText = classifierService.pdfBytesToText(document)
        preprocessed_text = classifierService.preprocessText(pdfText)
        classificationResult = classifierService.classifyText(preprocessed_text)
        classificationResults.append(classificationResult)
    return jsonify(classificationResults)


def manuallyClassifyDocuments(documents):
    print("Not implemented") # Theoretically could just return that the classification was successful.


if __name__ == "__main__":
    global classifierService
    classifierService = ClassifierService(app.config['TESSCONFIG'], app.config['VECTORIZER'], app.config['MODEL'])
    # run flask application in debug mode
    app.run(debug=True)
