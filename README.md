# projeto-lp2-prova

Projeto de Detecção e Classificação de Motos por Cor
Este projeto Python utiliza Visão Computacional para detectar motos em imagens, limpar seus fundos, e classificar as motos detectadas como "vermelhas" ou "azuis" com base na cor dominante. Imagens que não contêm motos vermelhas ou azuis são movidas para uma pasta de "outras imagens".


Estrutura do Projeto
code
Code
.
├── storage/
│   ├── frozen_inference_graph.pb  # Modelo SSD MobileNet V3 pré-treinado (pesos)
│   └── ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt # Arquivo de configuração do modelo
├── imagens/                     # Pasta onde as imagens de entrada devem ser colocadas
├── motos_vermelha/              # Saída: Motos detectadas e classificadas como vermelhas
├── motos_azul/                  # Saída: Motos detectadas e classificadas como azuis
├── outras_imagens/              # Saída: Imagens que não se enquadram nas categorias acima
├── temp/                        # Pasta temporária para imagens com fundo limpo
├── detecta_cor_dominante.py     # Módulo para detecção da cor dominante
├── limpar_fundo.py              # Módulo para remoção de fundo
├── salvar_imagem.py             # Módulo para salvar imagens nas pastas corretas
└── main.py                      # Script principal que orquestra o processo

Funcionalidades

Detecção de Objetos: Utiliza um modelo pré-treinado SSD MobileNet V3 para identificar motos em imagens.

Remoção de Fundo: Antes da detecção de cor, o fundo da imagem é removido para isolar o objeto principal (a moto).

Detecção de Cor Dominante: Analisa a região da moto detectada para determinar sua cor dominante (vermelha, azul ou outras).

Classificação e Organização: Salva as imagens originais das motos detectadas em pastas específicas (motos_vermelha, motos_azul) ou em outras_imagens se a moto não for vermelha ou azul, ou se nenhuma moto for detectada.

Tecnologias Utilizadas
Python 3.x
OpenCV (cv2): Para processamento de imagem, detecção de objetos e operações de arquivo.
DNN (Deep Neural Network) Module do OpenCV: Para carregar e executar o modelo de detecção de objetos.
SSD MobileNet V3: Modelo de detecção de objetos pré-treinado no conjunto de dados COCO.

Como Configurar e Executar
Pré-requisitos

Certifique-se de ter o Python 3.x e o OpenCV instalados. Você pode instalar o OpenCV com pip:
pip install opencv-python numpy

Preparação do Ambiente
Clone o repositório:
git clone https://github.com/danieldr22/projeto-lp2-prova.git # Se este for o seu repositório
cd projeto-lp2-prova

Modelos DNN: Certifique-se de que os arquivos do modelo DNN (frozen_inference_graph.pb e ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt) estejam presentes na pasta storage/. Se não estiverem, você precisará baixá-los. (Geralmente, esses modelos podem ser encontrados em repositórios do OpenCV ou TensorFlow).

Imagens de Entrada: Coloque as imagens que você deseja processar na pasta imagens/.

Executando o Script
Abra o terminal na raiz do projeto.

Execute o script principal:
python main.py

O script criará as pastas de saída (motos_vermelha, motos_azul, outras_imagens, temp) se elas não existirem, processará cada imagem em imagens/, e organizará as imagens resultantes.
Observações

O script criará arquivos temporários na pasta temp/ para as imagens com fundo limpo. Esses arquivos são excluídos ao final da execução.
A precisão da detecção de cor pode variar dependendo da iluminação da imagem e da complexidade do objeto.
Detalhes dos Módulos

detecta_cor_dominante.py: Provavelmente contém uma função que recebe uma imagem (ROI) e retorna a cor dominante (e talvez sua porcentagem).
limpar_fundo.py: Contém uma função que recebe o caminho de uma imagem e retorna (ou salva) a imagem com o fundo removido. Isso geralmente envolve técnicas como GrabCut ou modelos de segmentação de fundo.

salvar_imagem.py: Contém uma função utilitária para copiar ou mover imagens para as pastas de destino especificadas.
