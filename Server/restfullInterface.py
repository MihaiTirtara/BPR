from inteface import Interface

class RestfullInterface(Interface):
    def downloadFile(self,file):
        pass
    def imageToText(self,file):
        pass
    def vectorizeObject(self,ocrText):
        pass
    def imageClassifier(self,obj):
        pass
    