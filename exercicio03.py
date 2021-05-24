import random
valorCorreto = random.randint(0,10)
print("Senha: 1234")
senha = input("Digite a senha para entrar: ")
print()
repetir = True
qtdChute = 0
while repetir:
    if senha == "1234":
        print("Bem vindo ao jogo de adivinhação!")
        chute = 11
        while chute != valorCorreto:
            chute = int(input("Chute um valor: "))
            if chute < valorCorreto:
                print("MENOR! Tente novamente.\n")
                qtdChute += 1
            elif chute > valorCorreto:
                print("MAIOR! Tente novamente.\n")
                qtdChute += 1
            else:
                print("Parabens, você acertou!\n")
                qtdChute += 1
                repetir = False
    else:
        print("Senha incorreta. Tente novamente!")
        senha = input("Digite a senha para acessar: ")
        print()
print("Quantidade de chutes: ", qtdChute)