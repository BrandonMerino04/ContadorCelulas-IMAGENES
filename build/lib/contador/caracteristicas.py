import cv2
import numpy as np

def harris(img, gray):
    gray = np.float32(gray)

    h = cv2.cornerHarris(gray, 2, 3, 0.04)
    h = cv2.dilate(h, None)

    resultado = img.copy()
    resultado[h > 0.01 * h.max()] = [0, 0, 255]

    return resultado, h