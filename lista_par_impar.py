total=[[],[]]

for i in range(0,6):
    n=int(input(f"Insira o {i+1}º número inteiro: "))
    if n%2==0:
        total[0].append(n)
        total[0].sort()
    else:
        total[1].append(n)
        total[1].sort()
print(f'Os valores pares digitados foram {total[0]} e os números ímpares foram {total[1]}')
