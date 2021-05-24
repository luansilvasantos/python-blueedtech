from datetime import datetime
dados = dict()
dados['Nome'] = input('Nome: ')
nasc = int(input("Ano de Nascimento: "))
dados['Idade'] = datetime.now().year - nasc
dados['CTPS'] = int(input('Carteira de Trabalho: '))
dados['Contratacao'] = int(input('Ano de Contratação: '))
dados['Salario'] = float(input('Salário: R$'))
dados['Aposentadoria'] = dados['Idade'] + ((dados['Contratacao']+35)-datetime.now().year)
for chave, valor in dados.items():
    print(f"{chave}:{valor}")
print()
