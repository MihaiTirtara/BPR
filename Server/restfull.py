try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

class Restfull(implements(RestfulInterface)):

    def downloadFile(self,file):
        filename = file.filename
        print(file)
        in_memory_file = io.BytesIO()
        file.save(in_memory_file)
        data = np.fromstring(in_memory_file.getvalue(), dtype=np.uint8)
        color_image_flag = 1
        img = cv2.imdecode(data, color_image_flag)
        cv2.imwrite("uploads\\" + file.filename, img)

    def imageToText(self,file):
        imageFilename = file.filename
        ocrText = pytesseract.image_to_string(imageFilename)
        return ocrText
    
    def vectorizeObject(self,ocrText):
        return obj
    def imageClassifier(self,obj):
        #Classification Model
        projectPath = os.path.dirname(os.path.realpath(__file__))
        #classifierModelFile = open(os.path.join(projectPath,"first.pkl"),"rb")
        classifiermodel = joblib.load('first.joblib')
        #classifierModel = pickle.load(classifierModelFile)
        try:    
            #Predicition
            YPredict = classifierModel.predict(obj)
            print("I got here")
            print(YPredict)
            #if YPredict == 1:
             #   result = "Good"
            #else:
             #   result = "Too bad"

            #Return response
            response = jsonify(result)
            response.status_code = 200
        except:
            result = "An error occured"
            response = jsonify(result)
            response.status_code = 400
        return response   