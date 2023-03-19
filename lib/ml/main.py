from easyocr import Reader

def get_text_from_image(image):
    reader = Reader(['ru'], gpu=False)
    results = reader.readtext(image, detail=0)

    return results
