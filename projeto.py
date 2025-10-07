import os
import shutil
import google.generativeai as genai


try:
    genai.configure(api_key='SUA_CHAVE_AQUI')  # coloque sua chave aqui
except AttributeError:
    print("ERRO: Configure sua chave de API do Google!")
    exit()

model = genai.GenerativeModel('gemini-2.5-flash')


pasta_origem = ""
while not os.path.isdir(pasta_origem):
    print("\nPor favor, arraste a pasta que contém suas imagens para esta janela e pressione Enter.")
    pasta_origem = input("Caminho da pasta: ").strip().strip("'\"")

    if not os.path.isdir(pasta_origem):
        print("Caminho inválido ou não é uma pasta. Tente novamente.")

print(f"\nPasta selecionada: {pasta_origem}\n")


pasta_moto_azul = 'motos_azuis_classificadas'
pasta_moto_vermelha = 'motos_vermelhas_classificadas'
pasta_nao_moto = 'outras_imagens_classificadas'

for pasta in [pasta_moto_azul, pasta_moto_vermelha, pasta_nao_moto]:
    os.makedirs(pasta, exist_ok=True)


extensoes_validas = ['.jpg', '.jpeg', '.png', '.webp']


for nome_arquivo in os.listdir(pasta_origem):
    caminho_arquivo = os.path.join(pasta_origem, nome_arquivo)

    if os.path.isfile(caminho_arquivo) and any(nome_arquivo.lower().endswith(ext) for ext in extensoes_validas):
        print(f"Analisando '{nome_arquivo}'...")
        try:
            imagem = genai.upload_file(caminho_arquivo)

            prompt = """
            Analise a imagem e responda APENAS com uma das 3 opções:
            - moto cor azul
            - moto cor vermelha
            - não moto
            """

            response = model.generate_content([prompt, imagem])
            classificacao = response.text.strip().lower()

            if "moto cor azul" in classificacao:
                shutil.move(caminho_arquivo, os.path.join(pasta_moto_azul, nome_arquivo))
                print(f"-> Resultado: Moto Azul. Movido para '{pasta_moto_azul}'")
            elif "moto cor vermelha" in classificacao:
                shutil.move(caminho_arquivo, os.path.join(pasta_moto_vermelha, nome_arquivo))
                print(f"-> Resultado: Moto Vermelha. Movido para '{pasta_moto_vermelha}'")
            else:
                shutil.move(caminho_arquivo, os.path.join(pasta_nao_moto, nome_arquivo))
                print(f"-> Resultado: Não é uma moto (ou cor diferente). Movido para '{pasta_nao_moto}'")

        except Exception as e:
            print(f"** Erro ao processar o arquivo '{nome_arquivo}': {e} **")

print("\n✅ Processo concluído!")
