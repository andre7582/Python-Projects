aprovados = [
    "Laura Beatriz", "Laura Luiza", "Isabelly", "Maria Eduarda", "Thayná",
    "Isabel", "Hilda", "Analia", "Beatriz", "Amanda", "Laryssa", "Manuely"
]

vagas = int(input("Digite o número de vagas:"))


print("A lista: ", aprovados)
print("A primeira colocada: ", aprovados[0])

#1. Quantidade total de aprovados
len(aprovados)
print("Total de aprovados: ", len(aprovados))
#2. Primeira pessoa na condição de reserva
print("Primeiro reserva: ", aprovados[vagas])
#3. Verificar se alguém está na lista
if "Analia" in aprovados:
    print("Parabéns, Analia!")
else:
    print("Que Pena!")
#4. Lista de classificados
classificados = aprovados[0:vagas]
print("Classificados: ", classificados)
#5. Lista de reservas
reservas = aprovados[vagas:len(aprovados)]
print("Reservas: ", reservas)

print("Último classificado: ", classificados[-1])
print("Último reserva: ", reservas[-1])

aprovados.append("Ana Cláudia")
aprovados.remove("Analia")
print("Lista atualizada de aprovados: ", aprovados)
if "Analia" in aprovados:
    print("Parabéns, Analia!")
else:
    print("Que Pena, Analia!")

print("Obrigado a todos os candidatos!")
