nums = [[],[]]
for i in range(1,8):
    val = int(input(f"Digitel o {i}º valor: "))
    if val % 2 == 0:
        nums[0].append(val)
    else:
        nums[1].append(val)
nums[0].sort()
nums[1].sort()        
print("Valores pares: ", nums[0])
print("Valores ímpares: ", nums[1])
