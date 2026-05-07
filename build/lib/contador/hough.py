import cv2
import numpy as np

def hough(gray, img):
    circles = cv2.HoughCircles(
        gray,
        cv2.HOUGH_GRADIENT,
        dp=1.2,
        minDist=40,
        param1=100,
        param2=20,
        minRadius=20,
        maxRadius=90
    )

    vis = img.copy()

    if circles is not None:
        circles = np.round(circles[0, :]).astype(int)
        for (x, y, r) in circles:
            cv2.circle(vis, (x, y), r, (0,255,0), 2)

    return vis