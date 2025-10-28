nome=input('digite seu nome:')
idade=input('digite sua idade:')

if idade and nome:
    print (f'\n seu nome e {nome}')
    print (f'seu nome ivertido e {nome[::-1]}')
if ' ' in nome:
        print('Seu nome contém espaços')
else:
        print('Seu nome não contém espaços')

print(f'Seu nome tem {len(nome)} letras')
print(f'A primeira letra do seu nome é {nome[0]}')
print(f'A última letra do seu nome é {nome[-1]}')


 