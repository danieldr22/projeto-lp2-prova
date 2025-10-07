# projeto-lp2-prova

Classificador de Imagens de Motos

Este projeto em Python utiliza a API do Google Gemini para classificar imagens em três categorias: moto cor azul, moto cor vermelha e não moto. O script analisa todas as imagens em uma pasta de origem e as move automaticamente para pastas separadas de acordo com a classificação.

Para usar o projeto, siga estes passos:

Instale Python 3.9 ou superior.

Instale a biblioteca necessária com o comando: pip install google-generativeai

Obtenha uma chave de API do Google Gemini e insira no script na linha: genai.configure(api_key="SUA_CHAVE_AQUI")

Crie uma pasta com suas imagens. O script suporta arquivos nos formatos jpg, jpeg, png e webp.

Execute o script. Ele pedirá que você informe o caminho da pasta de imagens.

O script criará três pastas de saída automaticamente: motos_azuis_classificadas motos_vermelhas_classificadas outras_imagens_classificadas e moverá cada imagem para a pasta correta de acordo com a classificação.

Após a execução, todas as imagens estarão organizadas de forma automática, separadas por tipo e cor.

Versão 1.0.0 – solução mínima funcional com Google Gemini para classificação de imagens de motos, pronta para uso ou para melhorias futuras.
