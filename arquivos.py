# conteudo = open('texto.txt', 'r').read()

# print(conteudo)

with open('texto.txt', 'r') as arquivo:
    # print(arquivo.read())
    print(arquivo.read().split('\n'))
    arquivo.close()