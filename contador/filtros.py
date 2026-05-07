import cv2

def filtro(img):
    return cv2.GaussianBlur(img, (5,5), 0)