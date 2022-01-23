def substituir(ind, chave, inicio, fim):
    # função define letras e tamanho do alfabeto
    n = fim - inicio + 1
    k = (ind + chave) % (fim + 1) + ((ind + chave) // (fim + 1)) * inicio
    if ind + chave < inicio:
        k = k + n
    return chr(k)


def criptografar(mensagem, chave):
    naa, nzz, na, nz = ord('A'), ord('Z'), ord('a'), ord('z')
    cifrada = ""
    for caracter in mensagem:
        # achar no alfabeto a letra que esteja chave posições a frente
        ind = ord(caracter)
        nova_letra = caracter
        # Se estiver no intervalo de letras maiúsculas
        if naa <= ind <= nzz:
            nova_letra = substituir(ind, chave, naa, nzz)
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
