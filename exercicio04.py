from datetime import datetime
meses = [
    "Janeiro", 
    "Fevereiro", 
    "Março", 
    "Abril", 
    "Maio", 
    "Junho", 
    "Julho", 
    "Agosto", 
    "Setembro", 
    "Outubro",
    "Novembro",
    "Dezembro"
    ]
data = input("Digite a data no formato DD/MM/AAAA): ")

def imprimeData(data):
    dt = data.split("/")
    print(f'{dt[0]} de {meses[int(dt[1])-1]} de {dt[2]}')

def data_valida(data):
    try:
        datetime.strptime(data, '%d/%m/%Y')
        return True
    except ValueError:
        return False

if data_valida(data):
    imprimeData(data)
else:
    print("Data inválida!")