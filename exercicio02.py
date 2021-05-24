frase = input("Digite a string de entrada: ").strip().lower()
a, e, i, o, u, index = 0, 0, 0, 0, 0, 0
total = tamanho = len(frase)
fraseReformulada=""
repetir = True #variavel de controle
index=0
while repetir:
    if index == tamanho:
        repetir = False
        break
    elif frase[index]=="a":
        a += 1
    elif frase[index]=="e":
        e += 1
    elif frase[index]=="i":
        i+=1
    elif frase[index]=="o":
        o+=1
    elif frase[index]=="u":
        u+=1
    else:
        fraseReformulada+=frase[index]
        total-=1  #subtrai o numero de caracteres que não são vogais, da frase. Assim, o que sobra é o total de vogais.
    index+=1
print(f'Total de vogais: {total}')
print(f'Total de ocorrência por vogal:\n [a]: {a} \n [e]: {e} \n [i]: {i} \n [o]: {o} \n [u]: {u} ')
print("Frase sem nenhuma vogal:",fraseReformulada)
