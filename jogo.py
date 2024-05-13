import random
continuar = "S"
perro = 0
pcerto = 0
while continuar.upper() == "S" :
    ns = random.randint(1,10)
    T = 3
    while(T > 0):
        print("voce tem", T, "tentativa")
        T = T - 1
        chute  = int(input("digite um numero entre 1 a 10: "))
        if (ns == chute):
            print("você acertou.")
            T = 0
            pcerto = pcerto + 1
        else:
            print("voce errou")
            perro = perro + 1
        print("Numero de acertos:",pcerto)
        print("Numero de erros:", perro)

    continuar = input("deseja continuar?(S)im")
