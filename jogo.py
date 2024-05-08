import random
continuar = "S"

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
        else:
            print("voce errou")

    continuar = input("deseja continuar?(S)im")
