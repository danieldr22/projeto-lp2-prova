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


#Solução de Problemas (Troubleshooting)

Se o script não estiver funcionando como esperado, verifique os seguintes pontos:
Chave de API:
Certifique-se de que sua chave de API do Google Gemini está correta e ativa. Uma chave inválida ou expirada pode impedir a comunicação com a API.
Verifique se a chave foi inserida corretamente no script, sem espaços extras ou caracteres incorretos.
Conexão com a Internet:
O script requer uma conexão ativa com a internet para se comunicar com a API do Google Gemini. Verifique sua conexão.
Dependências:
Confirme se a biblioteca google-generativeai foi instalada corretamente. Tente reinstalá-la usando pip install google-generativeai --upgrade para garantir que você tenha a versão mais recente.
Caminho da Pasta:
Verifique se o caminho da pasta de imagens que você informou ao script está correto. Erros de digitação ou caminhos inexistentes impedirão o script de encontrar suas imagens.
Formatos de Imagem:
Certifique-se de que as imagens na sua pasta estão nos formatos suportados (jpg, jpeg, png, webp). O script pode ignorar ou falhar ao processar outros formatos.
Caso suas imagens estejam em outros formatos, você pode convertê-las ou adaptar o script para suportá-los.
Permissões:
Verifique se o script tem permissão para ler as imagens na pasta de origem e para criar/mover arquivos nas pastas de destino. Problemas de permissão podem ocorrer em sistemas operacionais como Linux/macOS ou em redes.
Saída do Script (Logs):
Observe qualquer mensagem de erro ou aviso exibida no terminal enquanto o script está em execução. Essas mensagens podem fornecer pistas sobre a causa do problema.
Limite de Requisições da API:
Se você estiver processando um grande volume de imagens rapidamente, pode ser que você atinja o limite de requisições da API do Gemini. Consulte a documentação da API para verificar os limites e considerar adicionar pausas no script (usando time.sleep()) entre as requisições se isso for um problema.
