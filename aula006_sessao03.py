nome = input("Digite seu primeiro nome: ").strip()

tamanho = len(nome)

if tamanho <= 4:
    print("Seu nome é curto.")
elif 5 <= tamanho <= 6:
    print("Seu nome é normal.")
else:
    print("Seu nome é muito grande.")
