def substituir(ind, chave, inicio, fim):
    # função define letras e tamanho do alfabeto
    n = fim - inicio + 1
    k = (ind + chave) % (fim + 1) + ((ind + chave) // (fim + 1)) * inicio
    if ind + chave < inicio:
        k = k + n
    return chr(k)


def criptografar(mensagem, chave):
    nA, nZ, na, nz = ord('A'), ord('Z'), ord('a'), ord('z')
    cifrada = ""
    for caracter in mensagem:
        # achar no alfabeto a letra que esteja chave posições a frente
        ind = ord(caracter)
        nova_letra = caracter
        # Se estiver no intervalo de letras maiúsculas
        if nA <= ind <= nZ:
            nova_letra = substituir(ind, chave, nA, nZ)
        # Outra forma de verificar se está no intervalo de letras (agora) minúsculas
        # lembrar que range gera intervalos da forma [a, b), portanto somamos 1
        elif ind in range(na, nz + 1):
            nova_letra = substituir(ind, chave, na, nz)
        # substituir na mensagem a letra pela nova_letra
        cifrada = cifrada + nova_letra
    return cifrada


def descriptografar(mensagem, chave):
    return criptografar(mensagem, -chave)


def cifrardoc(fonte, destino, chave):
    arquivo = open(fonte, "r")
    conteudo = arquivo.read()
    arquivo.close()

    cifrada = criptografar(conteudo, chave)

    arquivo = open(destino, "w")
    arquivo.write(cifrada)
    arquivo.close()


def decifrardoc(fonte, destino, chave):
    return cifrardoc(fonte, destino, -chave)


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
