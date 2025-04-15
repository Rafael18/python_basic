# Salário mensal
salario = float(input('Digite o seu salário mensal: '))

# variaveis
despesaInput = 'nao'
valorDispesa = 0
despesaTotal = 0
saldo = 0

# laço de repetição
while despesaInput != 'sair':
    despesaInput = input("Digite a descrição da despesa (ou 'sair' para encerrar): ")
    if(despesaInput != 'sair'):
        valorDispesa = float(input(f"Digite o valor da despesa '{despesaInput}': "))
        despesaTotal += valorDispesa

saldo = salario - despesaTotal

print('\n---- Resumo ----')
print(f'Salario mensal: {salario}')
print(f'Total despesas: {despesaTotal}')


if saldo <= 1000:
    print(f'você esta no VERMELHO, sobra {saldo}')
elif saldo > 1000 and saldo <= 2000:
    print(f'Você está no AZUL, sobra {saldo}')
else:
    print(f'Você está no VERDE, sobra {saldo}')
