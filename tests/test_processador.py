from processador import contar_linhas_validas

#Teste de caso normal

def test_contar_linhas_validas(tmp_path):
    #Arrange
    arquivo = tmp_path / "arquivo.csv"
    arquivo.write_text("1\n1\n1\n1\n1")
    #Act
    resultado = contar_linhas_validas(str(arquivo))    
    #Assert
    assert resultado == 5
    
#Teste de caso com linhas vazias

def test_contar_linhas_validas_ignorando_vazias(tmp_path):
    #Arrange
    arquivo = tmp_path / "arquivo.csv"
    arquivo.write_text("1\n\n1\n1\n\n\n\n1\n1\n\n\n1")
    #Act
    resultado = contar_linhas_validas(str(arquivo))    
    #Assert
    assert resultado == 6
    
#Arquivo vazio

def test_contar_linhas_validas_arquivo_vazio(tmp_path):
    #Arrange
    arquivo = tmp_path / "arquivo.csv"
    arquivo.write_text("")
    #Act
    resultado = contar_linhas_validas(str(arquivo))    
    #Assert
    assert resultado == 0