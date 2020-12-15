from abc import ABC

class Document(ABC):
    def __init__(self,request):
        self.FileContent = request
class AutoClassificationDocument(Document):
    def __init__(self,request):
        super().__init__(request)
class ManualClassificationDocument(Document):
    def __init__(self,request,GroupName):
        super().__init__(request)
        self.GroupName = GroupName
                             
