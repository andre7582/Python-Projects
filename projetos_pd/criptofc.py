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


print('''Escolha o que você quer fazer:
[1] Criptografar uma mensagem.
[2] Descriptografar uma mensagem.''')
sclh = int(input(': '))
if sclh == 1:
    mnsgm = str(input("Digite a mensagem a ser criptografada: "))
    chv = int(input("Digite um número para ser a chave da criptografia: "))
    cifrada = criptografar(mnsgm, chv)
    print("Mensagem cifrada: ", cifrada)
elif sclh == 2:
    mnsgm = str(input("Digite a mensagem a ser descriptografada: "))
    chv = int(input("Digite um número que deve ser a chave da descriptografia: "))
    decifrada = descriptografar(mnsgm, chv)
    print("Mensagem decifrada: ", decifrada)
