nome = input ("Digite seu nome").lower()
idade = int (input ("Digite sua idade"))

if (nome == "pedro" and idade ==22) or nome == "drake":
    print("Salve Drake")
elif nome == "murilo":
    print("Salve Henrique Henrique")
else: 
    print("Você não é o Drake")

numero = 0
while numero < 5:
    print (numero)
    numero = numero + 1

lista = ["cubo magico", "pagode japones", "skate", "manga com leite"]

# imprime todos os itens

for item in lista:
    print(item)

# imprime todos os itens

# imprime de 2 em 2

for i in range(0, len(lista), 2):
    print(lista[i])

# imprime de 2 em 2

# imprime de 2 em 2 ao contrario 

for i in range(len(lista)-1, 0, -2):
    print(lista[i])

# imprime de 2 em 2 ao contrario 

# imprime todos os itens facilitado

for i in range(len(lista)):
    print(lista[i])

# imprime todos os itens facilitado
