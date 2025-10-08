from rembg import remove


def limpar_fundo(path_base_origem, path_base_destino):
    with open(path_base_origem, "rb") as i:
        with open(path_base_destino, "wb") as o:
            input = i.read()
            output = remove(input)
            o.write(output)
