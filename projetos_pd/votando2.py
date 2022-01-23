#Quantos anos você tem?
#idade
#Se idade < 16 então
#- Você não pode votar!

print("Quantos anos você tem?")
idade = int(input("Resp: "))
if idade < 16:
    print("Você não pode votar!")
if idade >= 16:
    print("Você pode votar!")
