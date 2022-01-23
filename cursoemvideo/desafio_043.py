print('====== Desafio 043 ======')
# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status de peso.
print()
print('< Cálculo de IMC >')
print('.' * 99)
pes = float(input('Qual é o seu peso? (em kg): '))
alt = float(input('Qual é a sua altura? (em m): '))
imc = pes / (alt ** 2)
print('Seu IMC (índice de massa corporal) é de {:.1f}.'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso ideal!')
elif imc < 25:
    print('Parabéns! Você está na faixa de peso considerada ideal!')
elif imc < 30:
    print('Você está com sobrepeso!')
elif imc < 40:
    print('Atenção! Você está obeso!')
elif imc >= 40:
    print('Você está com obesidade mórbida! Quer morrer, é?')
print('.' * 99)
