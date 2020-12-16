global texto

def ler():
    global texto
    arq = open('Receita de Ano Novo.txt', 'r')
    texto = arq.read()
    arq.close()

def contagem():
    global texto
    contagem_maiuscula = 0
    space = 0
    contagem_minuscula = 0
    maior = 0
    for i in texto:
        if chr(32) == i:
            space = space + 1
    print('numero de espaco', space)

    for j in range(65,91):
        contagem_maiuscula = 0
        for i in texto:
            if chr(j) == i:
                  contagem_maiuscula = contagem_maiuscula + 1
        if maior < contagem_maiuscula:
            maior = contagem_maiuscula
            letra = chr(j)
        print(chr(j),'numero de vezes que aparece: ',contagem_maiuscula)

    for k in range(97,123):
        contagem_minuscula = 0
        for i in texto:
            if chr(k) == i:
                  contagem_minuscula = contagem_minuscula + 1
        if maior < contagem_minuscula:
            maior = contagem_minuscula
            letra = chr(k)
        print(chr(k),'numero de vezes que aparece: ',contagem_minuscula)
            
    print('letra que aparece mais vezes: ',letra,' numero de vezes: ', maior)  


def main():
    ler()
    contagem()

main()

