mais_pesada=mais_leve=0
pessoas=list()

while True:
    nome=str(input("Insira o nome: "))
    peso=float(input(f'Digite o peso de {nome}: '))
    pessoas.append([nome,peso])
    resposta=str(input("Deseja continuar? [S/N] ")).upper().strip()
    if resposta == "N":
        break
    while resposta!="N" and resposta!="S":
        resposta=str(input("Resposta inválida! Deseja continuar? [S/N] "))

for i in pessoas:
    if i[1] >= 70:
        mais_pesada+=1
    else:
        mais_leve+=1


print (f'Foram cadastradas {len(pessoas)} pessoas')
print(f'Das pessoas cadastradas, {mais_leve} tem menos de 70 Kg e {mais_pesada} tem mais de 70 KG')
print(f'A pessoa com maior peso é {max(pessoas)[0]} e ele tem {max(pessoas)[1]} KG')
print(f'A pessoa com menor peso é {min(pessoas)[0]} e ele tem {min(pessoas)[1]} KG')
