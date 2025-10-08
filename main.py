import os

import cv2

from detecta_cor_dominante import detectar_cor_dominante
from limpar_fundo import limpar_fundo
from salvar_imagem import salvar_imagem

FROZENINFERENCE = "storage/frozen_inference_graph.pb"
SSDMOBILENET = "storage/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt"

PATHIMAGES = "imagens"
PATHIMAGESVERMELHA = "motos_vermelha"
PATHIMAGESAZUL = "motos_azul"
PATHOUTROSIMAGENS = "outras_imagens"
PATHTEMP = "temp"


def detecta_imagem(model, imagem, path_normal):
    class_id, _, box = model.detect(imagem, 0.5)

    if len(class_id) == 0:
        print("Nenhum objeto detectado")
        return

    for i, clas in enumerate(class_id):
        if clas == 4:  # Classe 4 = moto
            # Extrair a região da moto detectada
            x, y, w, h = box[i]
            roi = imagem[y : y + h, x : x + w]

            if roi.size > 0:  # Verificar se a ROI é válida
                cor, percentual = detectar_cor_dominante(roi)

                if cor in ["vermelha", "azul"]:
                    # Salvar imagem na pasta correspondente
                    print(f"Moto {cor} detectada! ({percentual:.1f}% da cor)")
                    if cor == "vermelha":
                        salvar_imagem(PATHIMAGESVERMELHA, path_normal)
                        return
                    else:
                        salvar_imagem(PATHIMAGESAZUL, path_normal)
                        return

                else:
                    print(f"Moto detectada, mas não é vermelha nem azul")
                    salvar_imagem(PATHOUTROSIMAGENS, path_normal)
            return

    salvar_imagem(PATHOUTROSIMAGENS, path_normal)
    print("Nenhuma moto vermelha ou azul detectada")
    return False


def criar_pastas():
    os.makedirs(PATHIMAGESVERMELHA, exist_ok=True)
    os.makedirs(PATHIMAGESAZUL, exist_ok=True)
    os.makedirs(PATHOUTROSIMAGENS, exist_ok=True)
    os.makedirs(PATHTEMP, exist_ok=True)


if __name__ == "__main__":

    criar_pastas()

    model = cv2.dnn_DetectionModel(FROZENINFERENCE, SSDMOBILENET)

    model.setInputSize(320, 320)
    model.setInputScale(1.0 / 127.5)
    model.setInputMean((127.5, 127.5, 127.5))
    model.setInputSwapRB(True)

    delete_list = []

    for img_name in os.listdir(PATHIMAGES):
        print(f"Processando {img_name}")
        path_imagem = os.path.join(PATHIMAGES, img_name)
        path_temp = os.path.join(PATHTEMP, f"{len(os.listdir(PATHTEMP))}_{img_name}")
        limpar_fundo(path_imagem, path_temp)

        img = cv2.imread(path_temp)
        detecta_imagem(model, img, path_imagem)
        delete_list.append(path_temp)

    for item in delete_list:
        if os.path.exists(item):
            os.remove(item)
