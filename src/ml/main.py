from easyocr import Reader

def process(image):
    print("[INFO] Performing OCR on input image...")
    reader = Reader(['ru'], gpu=False)
    results = reader.readtext(image)

    for (bbox, text, prob) in results:
        print("[INFO] {:.4f}: {}".format(prob, text))
    return image
