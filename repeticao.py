lista =['Cookie', 'Milk Shake', 'Danone', 'Granola', 'Peixe']

# FOR
for item in lista:
    if item == 'Granola':
        print(f'{item} é bom, porém, substitua por Aveia')
    elif item == 'Peixe':
            print(f'{item} é top para ganhar proteina')
    else:
        print(f'Alerta....!!! {item}, isso engorda seu bola 9')

# WHILE

comidaFavorita = 'GRANOLA'
comida = input('Digite meu tipo de comida favorita: ').upper()
print(f'Comida digitada foi {comida}')

while comida != comidaFavorita:
    print(f'Errou, essa __ {comida} __ não é minha comida favorita')
    print('Tente novamente')
    comida = input('Digite meu tipo de comida favorita: ').upper()

print('Parabéns... você acetou minha comida favorita é: ')