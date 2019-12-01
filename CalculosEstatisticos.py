from math import sqrt
from os import system

ALTURA = 1
PRODUCAO = 2
FOSFORO = 3
POTASSIO = 4
CALCIO = 5

def gerarMatriz():
    #Arquivo txt colocado no C: do computador
    arq = open('C:/dados.txt', 'r')
    print("Lendo arquivo C:\dados.txt...\n")
    texto = arq.readlines()
    dados = []
    for linha in texto:
        a = linha.split('\n')
        dados += [a[0].split(' ')]
    arq.close()
    print("Total de Parcelas: %d" %(len(dados)-1))
    print("Total de Variaveis: %d" %(len(dados[0])-1))
    print("\nArquivo lido com sucesso!\n")
    system("pause")
    return dados

def dadosTipo(dados, tipo):
    return [float(dados[i][tipo]) for i in range(1, len(dados))]

def dadosParcela(dados, parcela):
    return [float(dados[parcela][i]) for i in range(1, len(dados[0]))]

def calcularMedia(dados, tipo):
    soma = 0
    for i in range(1, len(dados)):
        soma += float(dados[i][tipo])
    return soma / (len(dados) - 1)

def calcularMediaParcela(dados, parcela):
    soma = 0
    for i in range(1, len(dados[0])):
        soma += float(dados[parcela][i])
    return (soma/(len(dados[0])-1))

def calcularMediana(dados, tipo):
    dTipo = dadosTipo(dados, tipo)
    List = sorted(dTipo)
    x = len(dTipo) / 2

    if len(dTipo) % 2 == 0:
        a = List[int(x)-1]
        b = List[int(x)]
        return float(("%.2f" %((float(a) + float(b)) / 2)))

    return float(("%.2f" %float(List[int(x)])))

def calcularMedianaParcela(dados, parcela):
    dParcela = dadosParcela(dados, parcela)
    List = sorted(dParcela)
    x = len(dParcela) / 2

    if len(dParcela) % 2 == 0:
        a = List[int(x)-1]
        b = List[int(x)]
        return float(("%.2f" %((float(a) + float(b)) / 2)))

    return float(("%.2f" %float(List[int(x)])))

def calcularModa(dados, tipo):
    dTipo = dadosTipo(dados, tipo)

    repeticao = 0
    for i in dTipo:
        aparicoes = dTipo.count(i)
        if aparicoes > repeticao:
            repeticao = aparicoes

    modas = []
    for i in dTipo:
        aparicoes = dTipo.count(i)
        if aparicoes == repeticao and i not in modas:
            modas.append(i)

    msg = ''

    if(len(modas) == len(dTipo)):
         msg = ("Amodal")
    elif(len(modas) == 1):
         msg = ("Unimodal (" + str(modas[0])) + ")"
    elif (len(modas) == 2):
        msg = ("Bimodal (%.2f, %.2f)" %(modas[0], modas[1]))
    else:
        msg = ("Multimodal (")

        for i in range(len(modas)):
            if i == len(modas)-1:
                msg += str(modas[i]) + ")"
            else:
                msg += (str(modas[i]) + ", ")
    return msg

def calcularModaParcela(dados, parcela):
    dParcela = dadosParcela(dados, parcela)

    repeticao = 0
    for i in dParcela:
        aparicoes = dParcela.count(i)
        if aparicoes > repeticao:
            repeticao = aparicoes

    modas = []
    for i in dParcela:
        aparicoes = dParcela.count(i)
        if aparicoes == repeticao and i not in modas:
            modas.append(i)

    msg = ''

    if(len(modas) == len(dParcela)):
         msg = ("Amodal")
    elif(len(modas) == 1):
         msg = ("Unimodal (" + str(modas[0])) + ")"
    elif (len(modas) == 2):
        msg = ("Bimodal (%.2f, %.2f)" %(modas[0], modas[1]))
    else:
        msg = ("Multimodal (")

        for i in range(len(modas)):
            if i == len(modas)-1:
                msg += str(modas[i]) + ")"
            else:
                msg += (str(modas[i]) + ", ")
    return msg

def calcularVariancia(dados, tipo):
    dTipo = dadosTipo(dados, tipo)

    media = calcularMedia(dados, tipo)

    soma = 0


    for i in range(len(dTipo)):
        soma += (pow((dTipo[i] - media), 2))

    return (soma/len(dTipo))

def calcularVarianciaParcela(dados, parcela):
    dParcela = dadosParcela(dados, parcela)

    media = calcularMediaParcela(dados, parcela)

    soma = 0


    for i in range(len(dParcela)):
        soma += (pow((dParcela[i] - media), 2))

    return (soma/len(dParcela))

def calcularDesvioPadrao(dados, tipo):
    var = calcularVariancia(dados, tipo)
    return (sqrt(var))

def calcularDesvioPadraoParcela(dados, parcela):
    var = calcularVarianciaParcela(dados, parcela)
    return (sqrt(var))

def main():
    dados = gerarMatriz()

    print("\nMédia Altura: %.2f" % calcularMedia(dados, ALTURA))
    print("Média Produção: %.2f" % calcularMedia(dados, PRODUCAO))
    print("Média Fósforo (P): %.2f" % calcularMedia(dados, FOSFORO))
    print("Média Potássio (K): %.2f" % calcularMedia(dados, POTASSIO))
    print("Média Cálcio (Ca): %.2f" % calcularMedia(dados, CALCIO))

    print("\nMediana Altura: %.2f" % calcularMediana(dados, ALTURA))
    print("Mediana Produção: %.2f" % calcularMediana(dados, PRODUCAO))
    print("Mediana Fósforo (P): %.2f" % calcularMediana(dados, FOSFORO))
    print("Mediana Potássio (K): %.2f" % calcularMediana(dados, POTASSIO))
    print("Mediana Cálcio (Ca): %.2f" % calcularMediana(dados, CALCIO))

    print("\nModa Altura: " + calcularModa(dados, ALTURA))
    print("Moda Produção: " + calcularModa(dados, PRODUCAO))
    print("Moda Fósforo (P): " + calcularModa(dados, FOSFORO))
    print("Moda Potássio (K): " + calcularModa(dados, POTASSIO))
    print("Moda Cálcio(Ca): " + calcularModa(dados, CALCIO))

    print("\nDesvio Padrão Altura: %.5f" % calcularDesvioPadrao(dados,ALTURA))
    print("Desvio Padrão Produção: %.5f" % calcularDesvioPadrao(dados, PRODUCAO))
    print("Desvio Padrão Fósforo (P): %.5f" % calcularDesvioPadrao(dados, FOSFORO))
    print("Desvio Padrão Potássio (K): %.5f" % calcularDesvioPadrao(dados, POTASSIO))
    print("Desvio Padrão Cálcio (Ca): %.5f" % calcularDesvioPadrao(dados, CALCIO))


    for i in range(1, len(dados)):
        print(("\nMédia Parcela %d: %.2f") %(i, calcularMediaParcela(dados,i)))
        print(("Mediana Parcela %d: %.2f") %(i, calcularMedianaParcela(dados,i)))
        print(("Moda Parcela %d: ") %i + calcularModaParcela(dados,i) )
        print(("Desvio Padrão Parcela %d: %.2f") %(i, calcularDesvioPadraoParcela(dados, i)))

    print()
    system("pause")

main()
