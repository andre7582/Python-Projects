def analisa_notas(*notas):    #   ==> trecho sem efeito no programa    -->  , sit=False):



    '''

    Função para analisar as notas, médias e situações de vários alunos.

    :param notas: uma ou mais notas dos alunos (aceita várias)

    :param sit (ELIMINADO): valor opcional, indicando se deve ou não adicionar a situação para a média apresentada

    :return: dicionário com várias informações relativa as notas lançadas de entrada

    '''



    if notas[-1] == True:

        sit = True

    else:

        sit = False



    valores = dict()

    maior = 0

    menor = 10

    soma = 0

    media = 0

    situacao = ''



    for cont in range(0, len(notas) - 1, 1):
  #   usei len(notas) - 1 para eliminar o que seria o sit = True ou False
        if cont < len(notas) - 1:

            if float(notas[cont]) > maior:

                maior = float(notas[cont])

            if float(notas[cont]) < menor:

                menor = float(notas[cont])

            soma += float(notas[cont])



    media = float(soma / (len(notas) - 1))



    if media <= 5:

        situacao = 'Ruim'

    elif media > 5 and media <= 7.5:

        situacao = 'Boa'

    elif media > 7.5 and media < 9.5:

        situacao = 'Ótima'

    else:

        situacao = 'Excelente'



    valores['total de notas'] = len(notas) - 1

    valores['maior nota'] = maior

    valores['menor nota'] = menor

    valores['media'] = media



    if sit:

        valores['situação'] = situacao



    return valores







#PROGRAMA PRINCIPAL

qtd_notas = list()

seq = 1

print()

while True:

    while True:

        nota = input(f'Digite a {seq}ª nota ====> (ou AJUDA):')

        if nota.upper() == 'AJUDA':

            help(analisa_notas)

        elif nota.isalpha() or nota == '':

            print('Digite uma nota válida!')

        elif float(nota) < 0 or float(nota) > 10:

            print('Digite uma nota entre 0 e 10!')

        else:

            qtd_notas.append(float(nota))

            seq += 1

            print('-' * 120)

            print()

            break



    while True:

        resp = str(input('Mais notas? [S/N]').strip().upper())

        if resp != 'S' and resp != 'N':

            print('digite S ou N')

        else:

            break



    if resp == 'N':

        print()

        print('-' * 120)

        while True:

            resp_2 = str(input('Deseja mostrar a situação? [S/N]').strip().upper())

            if resp_2 != 'S' and resp_2 != 'N':

                print('Digite S ou N')

            else:

                print()

                print('=' * 120)

                print()

                break

        if resp_2 == 'S':

            situa = True

        else:

            situa = False

        break



resposta = analisa_notas(*qtd_notas, situa)

print(resposta)

print()

print('=' * 120)