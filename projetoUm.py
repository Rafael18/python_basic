def processar_vendas(arquivo):
    totais = {}

    with open(arquivo, 'r') as arq:
        linhas = arq.readlines()

        for linha in linhas:
            produto, quantidade, preco = linha.strip().split(',')
            quantidade = int(quantidade)
            preco = float(preco)

            if produto not in totais:
                totais[produto] = {"quantidade": 0, "total": 0.0}

            totais[produto]['quantidade'] += quantidade
            totais[produto]['total'] += quantidade * preco
    
    return totais

def gerar_relatorio(totais, arquivo_saida):
    with open(arquivo_saida, 'w') as arq:
        arq.write("Relatório de Vendas\n")
        arq.write("=" * 20 + "\n\n")

        for produto, dados in totais.items():
            arq.write(f'Produto: {produto}\n')
            arq.write(f'  Quantidade Vendida: {dados['quantidade']}\n')
            arq.write(f'  Total arracadado: R$ {dados['total']:.2f}\n\n')
    print(f"Relatório gerado em '{arquivo_saida}'.")


totais = processar_vendas('vendas.txt')
print(totais)
gerar_relatorio(totais, 'relatorio_vendas.txt')