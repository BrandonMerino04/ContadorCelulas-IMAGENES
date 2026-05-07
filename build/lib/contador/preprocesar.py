import cv2
import numpy as np

def rgbagray(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def normalizar(img):

    minimo = np.min(img)
    maximo = np.max(img)

    norm = ((img - minimo) / (maximo - minimo)) * 255

    return norm.astype(np.uint8)