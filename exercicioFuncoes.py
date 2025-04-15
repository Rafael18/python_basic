lista = [1, 2, 3, 4, 5]

def epar(inteiro):
    if inteiro % 2 == 0:
        return True
    else:
        return False


try:
    quadrados = [item ** 2 for item in lista if True]
except Exception as e:
    print(e)
else:
    pares = [item for item in quadrados if epar(item)]
    impares = [item for item in quadrados if not (item in pares)]
    print(lista)
    print(f'Números ao quadrado: {quadrados}')
    print(f'Resultados pares {pares}')
    print(f'Resultados impares: {impares}')
finally:
    print('Programa Finalizado')
