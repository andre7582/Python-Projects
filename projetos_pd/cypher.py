print('''Escolha o que você quer fazer:
[1] Criptografar um arquivo de texto.
[2] Descriptografar um arquivo de texto.''')
sclh = int(input(': '))
chv = int(input("Digite um número para ser a chave de criptografia: "))
tfon = str(input('Qual é o arquivo que será criptografado/descriptografado? '))
tfin = str(input('Escolha um novo nome para o arquivo: '))
if sclh == 1:
    cifrardoc(tfon, tfin, chv)
    print(str('Arquivo criptografado com sucesso!'))
elif sclh == 2:
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
