lista = ['João', 'Pedro', 'Mateus', 'Marcos']

dicionario = {'nome': 'Rafael', 'idade': 20, 'telefone': '81983379052'}

tupla = ('rafael', '123456')




print(dicionario['nome'])
print(dicionario['idade'])

del dicionario['idade']
print(dicionario)
print(dicionario.keys())
print(dicionario.values())
print(dicionario.items())

if  "nome" in dicionario:
    print('A palavra nome está no dicionário')
else:
    print('A palavra não está no dicionário')



if  20 in dicionario.values():
    print('O numeral está no dicionário')
else:
    print('O numeral não está no dicionário')


for key, value in dicionario.items():
    print(f'A chave é {key} e o valor {value}')