def contar_linhas_validas(caminho_arquivo):
    """Lê um arquivo e conta quantas linhas não estão vazias."""
    with open(caminho_arquivo) as f:
        linhas = f.readlines()
    return sum(1 for linha in linhas if linha.strip())