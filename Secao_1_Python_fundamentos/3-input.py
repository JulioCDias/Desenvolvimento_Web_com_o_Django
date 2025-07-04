# utilizando input

name = input("Qual o seu nome? ")
print("Olá", name)

idade = input("Qual a sua idade? \n")
print("Você tem", idade, "anos")

altura = input("Qual a sua altura? \n")
print("Você tem", altura, "de altura")
print(type(altura))

print("Fazendo casting (Conversao) ______________")

# fasendo Casting
altura = float(input("Qual a sua altura? \n"))
print("Você tem", altura, "de altura")
print(type(altura))
