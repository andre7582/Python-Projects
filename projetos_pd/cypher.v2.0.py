from cryptografia import criptografar, descriptografar, cifrardoc, decifrardoc
print('<<< Escolha uma tarefa >>>\n[1] Criptografar um texto.\n[2] Descriptografar um texto.\n[3] Criptografar '
      'um arquivo de texto.\n[4] Descriptografar um arquivo de texto.\n[9] Sair.')
sclh = int(input('Digite um número para representar a opção escolhida: '))
if sclh == 1:
    print('<<< Escolha um número para ser a chave de criptografia.>>>')
    chv = int(input("Chave: "))
    print('<<< Digite uma mensagem para ser criptografada.>>>')
    msg = input('Mensagem: ')
    cifrada = criptografar(msg, chv)
    print('Mensagem cifrada: ', cifrada)
elif sclh == 2:
    print('<<< Escolha um número para ser a chave de descriptografia.>>>')
    chv = int(input("Chave: "))
    print('<<< Digite uma mensagem para ser descriptografada.>>>')
    msg = input('Mensagem: ')
    decifrada = descriptografar(msg, chv)
    print('Mensagem decifrada: ', decifrada)
elif sclh == 3:
    print('<<< Escolha um número para ser a chave de criptografia.>>>')
    chv = int(input("Chave: "))
    tfon = str(input('Qual é o arquivo que será criptografado? '))
    tfin = str(input('Escolha um novo nome para o arquivo: '))
    cifrardoc(tfon, tfin, chv)
    print(str('Arquivo criptografado com sucesso!'))
    print('''Quer ver o resultado?
    [S] Sim.
    [N] Não.''')
    resu = str(input(': ')).upper()
    if resu == 'S':
        arq = open(tfin, "r")
        content = arq.read()
        print(content)
        print('Até mais :)')
    elif resu == 'N':
        print('Até mais :)')
elif sclh == 4:
    print('<<< Escolha um número para ser a chave de criptografia.>>>')
    chv = int(input("Chave: "))
    tfon = str(input('Qual é o arquivo que será descriptografado? '))
    tfin = str(input('Escolha um novo nome para o arquivo: '))
    decifrardoc(tfon, tfin, chv)
    print(str('A tentativa de descriptografia foi concluída com sucesso!'))
    print('''Quer ver o resultado?
    [S] Sim.
    [N] Não.''')
    resu = str(input(': ')).upper()
    if resu == 'S':
        arq = open(tfin, "r")
        content = arq.read()
        print(content)
        print('Até mais :)')
    elif resu == 'N':
        print('Até mais :)')
elif sclh == 9:
    print('Fechando o programa.')
else:
    print('Opção inválida!')
