print('====== Desafio 040 ======')
# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem final de acordo com a
# média atingida: < 5.0 : reprovado, entre 5.0 e 6.9 : recuperação, e => 7.0 : aprovado.
print()
print('< Resultado Final do Curso >')
print('.' * 99)
n1 = float(input('Primeira nota: '))
if n1 < 10:
    n2 = float(input('Segunda nota: '))
    if n2 < 10:
        me = (n1 + n2) / 2
        if me < 5:
            print('O aluno ficou com {:.1f} de média e portando está \033[31mREPROVADO\033[m.'.format(me))
        elif 7 > me >= 5:
            print('O aluno ficou com {:.1f} de média e portando ficará de \033[33mRECUPERAÇÃO\033[m.'.format(me))
        elif 7 <= me <= 10:
            print('O aluno ficou com {:.1f} de média e portando está \033[32mAPROVADO\033[m.'.format(me))
    elif n2 > 10:
        print('Ocorreu um erro na coleta dos dados! Por favor, digite um valor de 0 até 10')
else:
    print('Ocorreu um erro na coleta dos dados! Por favor, digite um valor de 0 até 10')
print('.' * 99)
