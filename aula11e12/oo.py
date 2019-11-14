# def somar():
#     num1 = float(input("Digite um numero"))
#     num2 = float(input("Digite um numero"))
#     return num1+num2

# print(somar())


# cliar classes 
# class Mamifero(): #por boas práticas nomes iniciam em letra maiuscula
#     olhos = 2
#     patas = 4

# #self é como se fosse os parametros a serem utilizados
#     def __init__(self, pelo, especie, rabo, cor):
#         self.pelo = pelo
#         self.especie = especie
#         self.rabo = rabo
#         self.cor = cor

#     def comer (self):
#         print("comi")
#     def fazer_som (self):
#         print("ruído")

# mamifero = Mamifero("curto", "doguinho", True, "caramelo")
# mamifero2 = Mamifero("longo", "agrarios monata", False, "purple")

# mamifero.comer()
# mamifero.fazer_som()
# print(mamifero.especie)
# print(mamifero2.especie)

# class Gato(Mamifero):
#     def __init__(self, pelo, especie, rabo, cor, bigodes):
#         super().__init__(pelo, especie, rabo, cor)
#         self.bigodes = bigodes
#     def fazer_som(self):
#         print("MIIIIIAU")

# gatinho = Gato("super curto", "pelado egiptium", True, "bege", 6)

# print(gatinho.especie)
# print(gatinho.bigodes)
# gatinho.fazer_som()
# gatinho.comer()

# def Soma():
#     num1 = int(input("digite um numero"))   
#     num2 = int(input("digite um numero"))   
#     num3 = int(input("digite um numero"))   
#     num4 = int(input("digite um numero"))
#     return (num1+num2+num3+num4)/4

# print (Soma())

# class Funcionario():
#     sal_hora = 50

#     def __init__(self, nome, horas_trabalhadas):
#         self.nome = nome
#         self.horas_trabalhadas = horas_trabalhadas

#     def calcular(self):
#         calculo = self.horas_trabalhadas * Funcionario.sal_hora
#         print (calculo)

# funcionario1 = Funcionario("Armando", 200)
# funcionario1.calcular()

# print(funcionario1.nome)

# def Palavra():
#     frase = input("Digite algo")
#     return len(frase)

# print (Palavra())

# class Pessoa ():
#     pass

#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade
#     def dados(self):
#         print(pessoa1.nome)
#         print(pessoa1.idade) 

# pessoa1 = Pessoa ("Leandra", 24)

# pessoa1.dados()

# class Pet ():
#     pass

#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade

#     def dadospet (self):
#         print(pet1.nome)
#         print(pet1.idade)

# pet1 = Pet ("Aquiles", 2)

# pet1.dadospet()