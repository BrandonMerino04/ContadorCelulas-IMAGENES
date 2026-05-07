
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import cv2
import matplotlib.pyplot as plt

from contador.preprocesar import rgbagray
from contador.filtros import filtro
from contador.bordes import derivadas, sobel, prewitt, laplaciano, canny
from contador.segmentacion import otsu, componentes
from contador.contador import contar
from contador.caracteristicas import harris
from contador.hough import hough

img = cv2.imread("C:/Users/Yolom/Desktop/istockphoto-1018902728-612x612.jpg")

gray = rgbagray(img)
blur = filtro(gray)

# Bordes
dx, dy, grad = derivadas(gray)
sob = sobel(gray)
pre = prewitt(gray)
lap = laplaciano(gray)
edges = canny(gray)

# Segmentación
binaria = otsu(blur)
num_labels, labels, stats, centroids = componentes(binaria)

# Conteo
celdas = contar(stats)

# Harris
harris_img, _ = harris(img, gray)

# Hough
circulos = hough(gray, img)

print("Número de células:", celdas)

# Visualización
plt.figure(figsize=(12,8))

plt.subplot(2,3,1), plt.imshow(gray, cmap='gray'), plt.title("Gris")
plt.subplot(2,3,2), plt.imshow(grad, cmap='gray'), plt.title("Gradiente")
plt.subplot(2,3,3), plt.imshow(sob, cmap='gray'), plt.title("Sobel")
plt.subplot(2,3,4), plt.imshow(binaria, cmap='gray'), plt.title("Otsu")
plt.subplot(2,3,5), plt.imshow(edges, cmap='gray'), plt.title("Canny")
plt.subplot(2,3,6), plt.imshow(cv2.cvtColor(circulos, cv2.COLOR_BGR2RGB)), plt.title("Hough")

plt.show()