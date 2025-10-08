import os
import shutil


def salvar_imagem(path_destino, path_origem):
    # se nao for azul copiar a imagem para a pasta outras_imagens
    nome_arquivo = os.path.basename(path_origem)
    caminho_destino = os.path.join(
        path_destino, f"{len(os.listdir(path_destino))}-{nome_arquivo}"
    )

    shutil.copy(path_origem, caminho_destino)
