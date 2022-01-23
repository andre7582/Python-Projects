def criptografar(mensagem, chave):
    nA = ord('A')
    nZ = ord('Z')
    na = ord('a')
    nz = ord('z')
    cifrada = ""
    for caracter in mensagem:
        ind = ord(caracter)
        if nA <= ind <= nZ:
            nova_letra = chr((ind + chave)%(nZ+1) + ((ind + chave)//(nZ+1))*nA)
            cifrada = cifrada + nova_letra
        elif ind in range(na, nz +1):
            nova_letra = chr((ind + chave) % (nz + 1) + ((ind + chave) // (nz + 1)) * nA)
            cifrada = cifrada + nova_letra
        else:
            cifrada = cifrada + caracter

    print("Origianl: ", mensagem)
    print("Cifrada: ", cifrada)

chv = 3
mnsgm = "sapo"

criptografar(mnsgm, chv)
