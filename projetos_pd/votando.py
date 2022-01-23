#Quantos anos você tem?
#idade
#Se idade < 16 então
#- Você não pode votar!

idade = int(input("Quantos anos você tem?\nResp:"))
if idade < 16:
    print("Você não pode votar!")
else:
    if idade < 18:
        print("Você pode votar, mas é facultativo!")
    else:
        if idade <= 70:
            print("Você é obrigado a votar!")
        else:
            print("Você pode votar, mas é perda de tempo!")

print("FIM")
