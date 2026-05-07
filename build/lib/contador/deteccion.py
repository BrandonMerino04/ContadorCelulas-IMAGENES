import cv2
import numpy as np

def canny(img):
    return cv2.Canny(img, 100, 200)

def circulos(img):
    circulos = cv2.HoughCircles(
        img,
        cv2.HOUGH_GRADIENT,
        dp=1,
        minDist=20,
        param1=50,
        param2=30,
        minRadio=5,
        maxRadio=50
    )
    return circulos