import numpy as np


rng = np.random.default_rng()

# img is a numpy array
def process_img(img):
    return img

def high_contrast(img):
    return (img * 2).astype(np.uint8)

def dim_img(img):
    return (img // 2).astype(np.uint8)

def random(img):
    return rng.integers(50, high=100, size=img.shape).astype(np.uint8)

def flip(img):
    return np.flip(img, axis=[0, 1])

def reverse_colors(img):
    return np.flip(img, axis=2)

def blank(img):
    return np.zeros_like(img)