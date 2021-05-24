nivelCulpa = 0
perguntas = [   "Telefonou para a vítima?: ",
                "Esteve no local do crime?: ",
                "Mora perto da vítima?: ",
                "Devia para a vítima?: ",
                "Já trabalhou com a vítima?: "
            ]

for i in range(5):
    resposta = input(perguntas[i]).strip().lower()[0]
    loop = True
    while loop:
        if resposta == "s":
            nivelCulpa += 1
            loop = False
        elif resposta == "n":
            loop = False
        else:
            resposta = input(perguntas[i]).strip().lower()[0]

if nivelCulpa < 2:
    print("Inocente")
elif nivelCulpa < 3:
    print("Suspeita")
elif nivelCulpa < 5:
    print("Cúmplice")
else:
    print("Assassino")
