'''
This piece of code is going to be used for getting information about read image

Input and output images are numpy arrays

The process is simple:
    get image -> process it with ML model and get some kind of structure out of it ->
    -> get tracking info directly from structure, get info about medicine from database by its name -> 
    -> generate a new image -> return
'''

import numpy as np


#! DEBUG PURPOSE FUNCTIONS!
rng = np.random.default_rng()

def process(img):
    return img

def high_contrast(img):
    return (img * 2).astype(np.uint8)

def dim(img):
    return (img // 2).astype(np.uint8)

def random(img):
    return rng.integers(0, high=256, size=img.shape).astype(np.uint8)

def flip(img):
    return np.flip(img, axis=[0, 1])

def reverse_color_bytes(img):
    return np.flip(img, axis=2)

def blank(img):
    return np.zeros_like(img)