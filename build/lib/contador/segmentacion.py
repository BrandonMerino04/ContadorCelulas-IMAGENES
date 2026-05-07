import cv2
import matplotlib.pyplot as plt

# Umbral global
def umbral_global(gray):

    th_global = cv2.threshold(
        gray,
        170,
        255,
        cv2.THRESH_BINARY
    )

    return th_global[1]


# Umbral Otsu
def otsu(gray):

    th_otsu = cv2.threshold(
        gray,
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )

    return th_otsu[1]


# Componentes conectados
def componentes(binaria):

    num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(
        binaria,
        8
    )

    return num_labels, labels, stats, centroids