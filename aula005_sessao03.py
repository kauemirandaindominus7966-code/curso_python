hora = input("Digite a hora atual (0 a 23): ")


if hora.isdigit():
    hora = int(hora)
    if 0 <= hora <= 11:
        print("Bom dia!")
    elif 12 <= hora <= 17:
        print("Boa tarde!")
    elif 18 <= hora <= 23:
        print("Boa noite!")
    else:
        print("Hora inválida! Digite um número entre 0 e 23.")
else:
    print("Por favor, digite um número inteiro válido.")