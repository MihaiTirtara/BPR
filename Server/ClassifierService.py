import io

from PIL import Image
import pytesseract
import joblib
import fitz


class ClassifierService:
    documentTypes = ["Letter", "Form", "Email", "Handwritten", "Advertisement", "Scientific Report",
                     "Scientific Publication", "Specification", "File Folder", "News Article", "Budget", "Invoice",
                     "Presentation", "Questionnaire", "Resume", "Memo"]

    def __init__(self, tesseractPath, vectorizerPath, modelPath):
        pytesseract.pytesseract.tesseract_cmd = tesseractPath
        self.Vectorizer = joblib.load(vectorizerPath)
        self.ClassifierModel = joblib.load(modelPath)

    # Reads the bytes from the request and converts them from PDF bytes to text, either by extracting text or converting PDF to an image and extracting the text using OCR.
    def pdfBytesToText(self, document):
        file_bytes = bytes(document["FileContent"])
        pdf_stream = io.BytesIO(file_bytes)
        # Load the stream as PDF and select the 1st page, it's OK as only 1 page PDFs are going to be sent anyways.
        pdf_document = fitz.open(stream=pdf_stream, filetype="pdf")
        page = pdf_document.loadPage(0)
        pdf_text = "" + page.getText()
        print("Pdf text:\n" + pdf_text)
        if pdf_text == "":  # if there's no text in PDF extract it by converting to an Image and extracting the text using OCR.
            pix_map = page.getPixmap()
            image_bytes = pix_map.getPNGData()
            image_stream = io.BytesIO(image_bytes)
            image = Image.open(image_stream)
            pdf_text = pytesseract.image_to_string(image)
            print("OCRed text:\n" + pdf_text)
        return pdf_text

    def preprocessText(self, ocr_text):
        textArray = [ocr_text]
        vectorText = self.Vectorizer.transform(textArray)
        vectorText = vectorText.reshape(1, -1)
        return vectorText

    def classifyText(self, obj):
        try:
            # Prediction
            YPredict = self.ClassifierModel.predict(obj)
            return {'groupName': ClassifierService.documentTypes[YPredict[0]], 'error': None}
        except:
            return {'groupName': None, 'error': 'An error occurred while classifying'}
