import cv2
import numpy as np


def detectar_cor_dominante(roi_img):
    """
    Detecta se a cor dominante na região é vermelha ou azul
    """
    # Converter para HSV para melhor detecção de cores
    hsv = cv2.cvtColor(roi_img, cv2.COLOR_BGR2HSV)

    # Definir ranges de cores em HSV
    # Vermelho (dois ranges devido ao wrap-around do hue)
    lower_red1 = np.array([0, 50, 50])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 50, 50])
    upper_red2 = np.array([180, 255, 255])

    # Azul
    lower_blue = np.array([100, 50, 50])
    upper_blue = np.array([130, 255, 255])

    # Criar máscaras para cada cor
    mask_red1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask_red2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask_red = mask_red1 + mask_red2
    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)

    # Calcular percentual de pixels de cada cor
    total_pixels = roi_img.shape[0] * roi_img.shape[1]
    red_pixels = cv2.countNonZero(mask_red)
    blue_pixels = cv2.countNonZero(mask_blue)

    red_percentage = (red_pixels / total_pixels) * 100
    blue_percentage = (blue_pixels / total_pixels) * 100

    # Definir threshold mínimo para considerar que a cor está presente
    threshold = 15  # 15% da área deve ter a cor

    if red_percentage > threshold:
        return "vermelha", red_percentage
    elif blue_percentage > threshold:
        return "azul", blue_percentage
    else:
        return None, 0
