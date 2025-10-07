import os
import shutil
import google.generativeai as genai

try:
    genai.configure(api_key='AIzaSyCH3XRFAGQdWE8-7NKUMgLxzkJ6LNbiCJA')
except AttributeError:
    print("ERRO: Configure sua chave de API do Google!")
    exit()
model = genai.GenerativeModel('gemini-1.5-flash')


