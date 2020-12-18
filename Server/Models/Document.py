# Not using models because "Python JSON serialization to custom classes" world is not the most sane one.

class Document:
    def __init__(self, fileContent):
        self.FileContent = fileContent


class AutoClassificationDocument(Document):
    def __init__(self, request):
        super().__init__(request)


class ManualClassificationDocument(Document):
    def __init__(self,request, groupName):
        super().__init__(request)
        self.GroupName = groupName
