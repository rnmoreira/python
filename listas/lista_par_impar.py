#Criar duas listas dentro de uma lista principal
total=[[],[]]

#No intervalo de 0 a 5 (o range desconsidera a última posição), será pedido ao usuário para inserir um número
for i in range(0,6):
    n=int(input(f"Insira o {i+1}º número inteiro: "))
#Identifica que o número é par. Se for par, será acrescentado à lista total[0]. Em seguida a lista é reordenada em ordem crescente.
    if n%2==0:
        total[0].append(n)
        total[0].sort()
#Caso não seja divisível por 2, é um número ímpar, logo será acrescentado na lista total[1] e a lista será novamente reordenada
    else:
        total[1].append(n)
        total[1].sort()
# Simplesmente exibe na tela os valores da  total[0] e total[1] já em ordem crescente.
print(f'Os valores pares digitados foram {total[0]} e os números ímpares foram {total[1]}')
