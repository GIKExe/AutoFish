# системные
# глобальные
from pytesseract import pytesseract
# локальные


__all__ = ['proc']
pytesseract.tesseract_cmd = R"C:\Program Files\Tesseract-OCR\tesseract.exe"
# print(pytesseract.get_languages(config=''))  eng rus
# exit()

def proc(image, lang='rus'):
	return pytesseract.image_to_string(image, lang=lang).replace('\n\n\n', '\n').replace('\n\n', '\n')