import numpy as np
import cv2
from scipy import signal

# Derivadas básicas
def derivadas(gray):
    Hx = np.array([[0.5, 0, -0.5]])
    dx = signal.convolve2d(gray, Hx, mode='same')

    Hy = Hx.T
    dy = signal.convolve2d(gray, Hy, mode='same')

    grad = np.sqrt(dx**2 + dy**2)

    return dx, dy, grad

# Sobel
def sobel(gray):
    sx = np.array([[-1,0,1],[-2,0,2],[-1,0,1]], dtype=np.float32)
    sy = np.array([[1,2,1],[0,0,0],[-1,-2,-1]], dtype=np.float32)

    gx = signal.convolve2d(gray, sx, mode='same')
    gy = signal.convolve2d(gray, sy, mode='same')

    return cv2.magnitude(gx, gy)

# Prewitt
def prewitt(gray):
    px = np.array([[-1,0,1],[-1,0,1],[-1,0,1]], dtype=np.float32)
    py = np.array([[1,1,1],[0,0,0],[-1,-1,-1]], dtype=np.float32)

    gx = signal.convolve2d(gray, px, mode='same')
    gy = signal.convolve2d(gray, py, mode='same')

    return cv2.magnitude(gx, gy)

# Laplaciano
def laplaciano(gray):
    kernel = np.array([[0,1,0],[1,-4,1],[0,1,0]])
    return signal.convolve2d(gray, kernel, mode='same')

# Canny
def canny(gray):
    blur = cv2.GaussianBlur(gray, (5,5), 1.2)
    return cv2.Canny(blur, 50, 150)