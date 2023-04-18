try:
    with open('arquivo.txt', 'r') as f:
        conteudo = f.read()
except FileNotFoundError:
    print('Arquivo não encontrado!')
except PermissionError:
    print('Sem permissão para abrir o arquivo!')
except Exception as e:
    try:
        raise Exception('Erro ao ler arquivo!') from e
    except Exception:
        print('Ocorreu um erro ao ler o arquivo!')