nome = (input('Qual é o seu nome? ')).upper()
if nome == 'LAURA':
    print('Bom dia {}! Que nome lindo você tem!'.format(nome))
else:
    print('Bom dia, {}!'.format(nome))
n1 = float(input('Digite a primeira nota (de 0 a 10): '))
n2 = float(input('Digite a segunda nota (de 0 a 10): '))
m =(n1 + n2)/2
print('A sua média foi {:.1f}'.format(m))
print('Parabéns!'if m >= 6 else 'Você precisa estudar mais!' )
