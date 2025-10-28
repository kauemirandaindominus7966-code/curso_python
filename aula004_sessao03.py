numero = input("Digite um número inteiro: ")

if numero.isdigit():  
    numero = int(numero)
    
    if numero % 2 == 0:
        print("O número é PAR.")
    else:
        print("O número é ÍMPAR.")
else:
    print("O valor digitado não é um número inteiro.")



