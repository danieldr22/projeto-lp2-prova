import os
import shutil
import google.generativeai as genai

try:
    genai.configure(api_key='AIzaSyCH3XRFAGQdWE8-7NKUMgLxzkJ6LNbiCJA')
except AttributeError:
    print("ERRO: Configure sua chave de API do Google!")
    exit()
model = genai.GenerativeModel('gemini-1.5-flash')

for pasta in [pasta_moto_azul, pasta_moto_vermelha, pasta_nao_moto]:
    if not os.path.exists(pasta):
        os.makedirs(pasta)
if not os.path.exists(pasta_origem):
    print(f"ERRO: A pasta '{pasta_origem}' não existe . Crie uma e adicione suas imagens.")
    exit()

for nome_arquivo in os.listdir(pasta_origem):
    caminho_arquivo = os.path.join(pasta_origem, nome_arquivo)

    if os.path.isfile(caminho_arquivo):
        print(f"Analisando '{nome_arquivo}'...")
        try:
            imagem = genai.upload_file(caminho_arquivo)


