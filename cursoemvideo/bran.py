# Estruturas de controle: condiões aninhadas
nome = str(input('Qual seu nome? ')).upper()
if nome == "LAURA":
    print('Que nome lindo, {}!'.format(nome))
elif nome == 'MARIA':
    print('{}, seu nome é bem popular!'.format(nome))
elif nome in 'ISABEL ANA ISABELY':
    print('Que belo nome feminino!')
else:
    print('Seu nome é bem normal.')
print('Ok, {}, tenha um bom dia!'.format(nome))
