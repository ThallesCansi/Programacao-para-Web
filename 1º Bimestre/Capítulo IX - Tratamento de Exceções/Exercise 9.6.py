try:
    with open("arquivo.txt", "r") as arquivo:
        conteudo = arquivo.read()
except FileNotFoundError:
    print("Erro: arquivo não encontrado!")