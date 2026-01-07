def carregar_dados():
    dados = [
        {"nome": "Ana", "idade": 25},
        {"nome": "Bruno", "idade": 30},
        {"nome": "Carlos", "idade": 28}
    ]
    return dados
def calcular_media_idade(dados):
    total = sum(p["idade"] for p in dados)
    return total / len(dados)
def main():
    dados = carregar_dados()
    media = calcular_media_idade(dados)
    print("Média de idade:", media)
if name == "__main__":
    main()
  
