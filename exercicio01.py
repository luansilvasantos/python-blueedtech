
firstValue = float(input("Digite um valor: "))
secondValue = float(input("Digite outro valor: "))
print()
sumResult = firstValue + secondValue
multResult = firstValue * secondValue
divResult = int(firstValue // secondValue)
def highestValue(x, y):
    if x > y:
        return f"O\033[34m MAIOR VALOR\033[0;0m de entrada é: \033[91m {x} \033[0;0m."
    else:
        return f"O\033[34m MAIOR VALOR\033[0;0m de entrada é: \033[91m {y} \033[0;0m."
def checkEvenOrOdd(sumResult):
    if (sumResult % 2) > 0:
        return "O resultado da soma é um número: \033[91m ÍMPAR\033[0;0m"
    return "O resultado da soma é um número: \033[91m PAR\033[0;0m"

def fortyValidate(multResult, divResult):
    if multResult > 40:
        if divResult > 0:        
            return f'A multiplicação é \033[34m MAIOR QUE 40\033[0;0m. Logo, o resultado da divisão é:\033[91m {multResult / divResult}\033[0;0m'
        else: 
            return "\033[91mErro\033[0;0m: O resultado da multiplicação é maior que 40, porém, como o resultado da primeira divisão é igual a 0, não é possível chegar a um valor."
    else:
        return "O resultado da multiplicação é: \033[34m MENOR QUE 40\033[0;0m."
    return
print(f"O Resuldado da\033[34m SOMA\033[0;0m é:\033[91m {sumResult} \033[0;0m")
print(f"O Resuldado da\033[34m MULTIPLICAÇÃO\033[0;0m é:\033[91m {multResult} \033[0;0m")
print(f"O Resuldado da\033[34m DIVISÃO\033[0;0m é:\033[91m {divResult} \033[0;0m")
print(highestValue(firstValue, secondValue))
print(checkEvenOrOdd(sumResult))
print(fortyValidate(multResult, divResult))
print()