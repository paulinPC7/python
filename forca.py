import os
import random

def Forca(Tentativa):
    f1 = "    +-------+  " 
    f2 = "    |          "
    f3 = "    |          "
    f4 = "    |          "
    f5 = "    |          "
    f6 = "    |          "
    f7 = "____|______    "

    if Tentativa >= 1:
        f2 = "    |       |  "
    if Tentativa >= 2:
        f3 = "    |       O  "
    if Tentativa >= 3:
        f4 = "    |       |   "
    if Tentativa >= 4:
        f4 = "    |      /|  "
    if Tentativa >= 5:
        f4 = "    |      /|\ "
    if Tentativa >= 6:
        f5 = "    |       |  "
    if Tentativa >= 7:
        f6 = "    |      /   "
    if Tentativa >= 8:
        f6 = "    |      / \ "

    print(f1)
    print(f2)
    print(f3)
    print(f4)
    print(f5)
    print(f6)
    print(f7)

def Continua():
    while True:
        print("-" * 20)
        novamente = input("Quer jogar de novo S/N: ").upper()
        if novamente == "S":
            return True
        elif novamente == "N":
            return False
        else:
            print("Digite S ou N ")

def SorteiaPalavra():
    lista = ["AMOR", "MELANCIA", "CATEDRAL", "ESCOLA", "MATEMÁTICA",
             "REFEITÓRIO", "DIRETORIA", "CAMINHÃO", "CACHORRO"]
    return random.choice(lista)

def ApresentaPalavra(letras, palavra):
    PalavraCifrada = "_ " * len(palavra)
    for l in range(len(letras)):
        for p in range(len(palavra)):
            if palavra[p] == letras[l]:
                PalavraCifrada = PalavraCifrada[0:(p*2)] + palavra[p] + " " + PalavraCifrada[(p*2)+2:] 
    print(PalavraCifrada)

def DigiteUmaLetra(listaletra):
    novaLetra = input("Digite uma letra da Palavra: ").upper()
    while True:
        if novaLetra in listaletra:
            novaLetra = input("Letra já digitada. Digite outra letra da Palavra: ").upper()
        else:
            break

    listaletra += novaLetra
    return listaletra

def AcertouQuantas(letras, palavra):
    corretas = 0
    for l in range(len(letras)):
        for p in range(len(palavra)):
            if palavra[p] == letras[l]:
                corretas += 1
    return corretas

def Placar(Ganhou, Perdeu):
    T = 27
    print("=" * T)
    print(f'= Ganhou: {Ganhou:-2} | Perdeu: {Perdeu:-2} =')
    print("=" * T)

def salvar_placar(ganhou, perdeu):
    try:
        with open('placar.txt', 'a') as arquivo:
            arquivo.write(f'{ganhou},{perdeu}\n')
        print("Placar salvo com sucesso!")
    except Exception as e:
        print(f"Erro ao salvar o placar: {e}")

def recuperar_placar():
    try:
        with open('placar.txt', 'r') as arquivo:
            conteudo = arquivo.readlines()
            placares = []
            for linha in conteudo:
                if linha.strip():  
                    ganhou, perdeu = linha.strip().split(',')
                    placares.append((int(ganhou), int(perdeu)))
            return placares
    except FileNotFoundError:
        print("Arquivo de placar não encontrado.")
        return []
    except Exception as e:
        print(f"Erro ao recuperar o placar: {e}")
        return []


def jogo_da_forca():
    Jogar = True
    placares = recuperar_placar()
    if placares:
        total_ganhou = sum(p[0] for p in placares)
        total_perdeu = sum(p[1] for p in placares)
        print(f"Placar Total - Ganhou: {total_ganhou}, Perdeu: {total_perdeu}")

    while Jogar:
        PalavraSorteada = SorteiaPalavra()
        ListaLetra = " "
        Tentativas = 7
        NaoAcertou = True
        SituacaoForca = -1
        AcertosAnterior = 0

        while SituacaoForca != Tentativas:
            os.system('cls' if os.name == 'nt' else 'clear')
            Acertos = AcertouQuantas(ListaLetra, PalavraSorteada)

            if Acertos == len(PalavraSorteada):
                ganhou = 1
                perdeu = 0
                Placar(ganhou, perdeu)
                print("Parabéns, você acertou.")
                ApresentaPalavra(ListaLetra, PalavraSorteada)
                NaoAcertou = False
                break

            if Acertos == AcertosAnterior:
                SituacaoForca += 1

            AcertosAnterior = Acertos
            Placar(sum(p[0] for p in placares), sum(p[1] for p in placares))
            Forca(SituacaoForca)
            ApresentaPalavra(ListaLetra, PalavraSorteada)
            print("Letras já digitadas: " + ListaLetra)
            ListaLetra = DigiteUmaLetra(ListaLetra)

        if NaoAcertou:
            os.system('cls' if os.name == 'nt' else 'clear')
            ganhou = 0
            perdeu = 1
            Placar(ganhou, perdeu)
            Forca(SituacaoForca + 1)
            ApresentaPalavra(ListaLetra, PalavraSorteada)
            print("Você errou, Tente novamente.")

        salvar_placar(ganhou, perdeu)
        Jogar = Continua()

jogo_da_forca()
