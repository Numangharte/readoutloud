import easyocr
reader = easyocr.Reader(['en'])
reader.readtext('/static/images/GHARDA.png')
print(result)
