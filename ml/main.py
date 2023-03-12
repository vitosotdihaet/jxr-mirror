from easyocr import Reader
import cv2

path = input('Full image\'s path:')

image = cv2.imread(path, 0)
print("[INFO] Performing OCR on input image...")

reader = Reader(['ru'], gpu=True) # gpu - only if you have CUDA
results = reader.readtext(fr'{path}')

for (bbox, text, prob) in results:
    print("[INFO] {:.4f}: {}".format(prob, text))
