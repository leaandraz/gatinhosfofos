# def somar():
#     num1 = float(input("Digite um numero"))
#     num2 = float(input("Digite um numero"))
#     return num1+num2

# print(somar())


# cliar classes 
class Animal(): #por boas práticas nomes iniciam em letra maiuscula
    olhos = 2
    patas = 4

#self é como se fosse os parametros a serem utilizados
    def __init__(self, pele, especie, rabo, cor):
        self.pele = pelo
        self.especie = especie
        self.rabo = rabo
        self.cor = cor

    def comer (self):
        print("comi")
    def fazer_som (self):
        print("ruído")

mamifero = Animal("curto", "doguinho", True, "caramelo")
mamifero2 = Animal("longo", "agrarios monata", False, "purple")

mamifero.comer()

print(mamifero.especie)
print(mamifero2.especie)