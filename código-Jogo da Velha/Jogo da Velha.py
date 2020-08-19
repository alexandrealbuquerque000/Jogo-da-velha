#Alexandre Maia Aquino de Albuquerque

from random import randint
import time
import os

#Função para mostrar a matriz:
def mostramatrizjogo():
    global matriz
    global matrizprint
    global quadrado
    for mtz in range(quadrado):
        matrizprint=(str(matriz[mtz]).replace(",", " ")[1:-1])
        for mtz2 in range(quadrado):
            matrizprint=matrizprint.replace(str(mtz2+1), ' ')
            matrizprint=matrizprint.replace("'", "|")
        print("{:^50}".format(matrizprint))
    print('\n')


#Função para moldar matriz:
def moldmatriz():
    global quadrado
    global matriz
    matriz=[[]]
    for aux in range(1, quadrado+1):
        auxmatriz=aux
        matriz[0].append(str(auxmatriz))
    auxmatriz=matriz[0]
    for aux2 in range(quadrado-1):
        matriz.append(list(auxmatriz))


#Função para ler apenas letras:
def leiastr(msg):
    while True:
        print()
        verif=str(input(msg).strip().replace(" ", ""))
        if verif.isalpha() == False:
            print()
            print("ERRO:""\nDigite apenas letras.")
            continue
        else:
            verif=verif.lower()
            return verif


#Função verificadora de números inteiros
def leiaint(msg):
    while True:
        try:
            print()
            N=int(input(msg).strip().replace(" ", ""))
        except (ValueError, TypeError, IndexError):
            print()
            print("ERRO:""\nDigite apenas números inteiros.")
            continue
        else:
            return N

def run():
    global matriz, matrizprint, quadrado
        
    reiniciar="s"
    while "s" in reiniciar:
        print("-"*19)
        print("   Jogo da Velha")
        print("-"*19)
        #Obtendo a informação sobre o tamanho do quadrado
        quadrado=str("Digite o tamanho do lado do quadrado: ")
        quadrado=leiaint(quadrado)
        if quadrado==0:
            quadrado=3
        elif quadrado<0:
            quadrado=-quadrado
        moldmatriz()
        matrizlinhas=[]
        conferemagico=[]
        player=str("Desenha jogar contra o computador ou contra outra pessoa? ")
        player=leiastr(player)
        if "pe" not in player:
            jogadorpc='true'
        else:
            jogadorpc='false'
        nomejg1=str("Digite o nome do jogador 1: ")
        nomejg1=leiastr(nomejg1)
        nomejg1=nomejg1.title()
        if jogadorpc=='true':
            nomejg2="Computador"
        else:
            nomejg2=str("Digite o nome do jogador 2: ")
            nomejg2=leiastr(nomejg2)
            nomejg2=nomejg2.title()
        print()
        jogador1=input(f"Digite o símbolo utilizado pelo jogador 1 ({nomejg1}): ")
        while jogador1=='' or " " in jogador1 or jogador1==None:
            print()
            print("Esse símbolo não é válido")
            print()
            jogador1=input(f"Digite o símbolo utilizado pelo jogador 1 ({nomejg1}): ")
        jogador1=jogador1.strip().title()
        if jogadorpc=='true':
            if jogador1=="X":
                jogador2="O"
            elif jogador1=="O":
                jogador2="X"
            else:
                jogador2="pc"
        else:
            print()
            jogador2=input(f"Digite o símbolo utilizado pelo jogador 2 ({nomejg2}): ")
            while jogador2=='' or " " in jogador2 or jogador2==None:
                print()
                print("Esse símbolo não é válido")
                print()
                jogador2=input(f"Digite o símbolo utilizado pelo jogador 2 ({nomejg2}): ")
            jogador2=jogador2.strip().title()
        while jogador1==jogador2:
            print()
            print("Os símbolos não podem ser iguais.")
            print()
            jogador2=input(f"Digite o símbolo utilizado pelo jogador 2 ({nomejg2}): ")
        partida=str("Deseja jogar quantas partidas seguidas? ")
        partida=leiaint(partida)
        partida=int(partida)
        print()
        if partida<=0:
            partida=1
        placar1=0
        placar2=0
        for part in range(partida):
            os.system("cls")
            print()
            print(f"__Rodada {part+1}__")
            time.sleep(1)
            print()
            jogcomeça=(randint(1,2))
            if jogcomeça==1:
                nome=nomejg1
            else:
                nome=nomejg2
            print(f"O jogador {jogcomeça} ({nome}) começará.")
            #Obtendo a informação sobre os elementos dentro do quadrado
            testevelha=1
            for cont in range(9):
                if testevelha==1:
                    pass
                else:
                    cont=9
                    break
                if jogcomeça==1:
                    print()
                    time.sleep(1)
                    print(f"Jogada do jogador 1 ({nomejg1}):")
                    simbjg=jogador1
                    jogcomeça=2
                else:
                    print()
                    time.sleep(1)
                    print(f"Jogada do jogador 2 ({nomejg2}):")
                    if jogadorpc=='true':
                        time.sleep(2)
                    else:
                        pass
                    simbjg=jogador2
                    jogcomeça=1
                testepos="true"
                while testepos=="true":
                    if jogadorpc=='true' and jogcomeça==1:
                        elemlin=(randint(1, quadrado))
                        elemcol=(randint(1, quadrado))
                    else:
                        if cont==0:
                            print('\n\n')
                            mostramatrizjogo()
                        else:
                            pass
                        elemlin=str("Digite a linha desejada: ")
                        elemlin=leiaint(elemlin)
                        elemlin=int(elemlin)
                        while elemlin==0:
                            print()
                            print(f"Esse é um quadrado {quadrado}x{quadrado}.")
                            print()
                            print("Tente novamente")
                            elemlin=str("Digite a linha desejada: ")
                            elemlin=leiaint(elemlin)
                            elemlin=int(elemlin)
                        if elemlin<0:
                            elemlin=-elemlin
                        while elemlin>int(quadrado):
                            print()
                            print(f"Esse é um quadrado {quadrado}x{quadrado}.")
                            print()
                            print("Tente novamente")
                            elemlin=str("Digite a linha desejada: ")
                            elemlin=leiaint(elemlin)
                        elemcol=str("Digite a coluna desejada: ")
                        elemcol=leiaint(elemcol)
                        elemcol=int(elemcol)
                        while elemcol==0:
                            print()
                            print(f"Esse é um quadrado {quadrado}x{quadrado}.")
                            print()
                            print("Tente novamente")
                            elemcol=str("Digite a coluna desejada: ")
                            elemcol=leiaint(elemcol)
                            elemcol=int(elemcol)
                        if elemcol<0:
                            elemcol=-elemcol
                        while elemcol>int(quadrado):
                            print()
                            print(f"Esse é um quadrado {quadrado}x{quadrado}.")
                            print()
                            print("Tente novamente")
                            elemcol=str("Digite a coluna desejada: ")
                            elemcol=leiaint(elemcol)
                    if matriz[elemlin-1][elemcol-1]==jogador1 or matriz[elemlin-1][elemcol-1]==jogador2:
                        if jogadorpc=='true' and jogcomeça==1:
                            continue
                        else:
                            print()
                            print("Essa posição já está ocupada.")
                            testepos="true"
                            continue
                    else:
                        testepos="false"
                        pass
                matriz[elemlin-1][elemcol-1]=str(simbjg)
                print()
                os.system("cls")
                print('\n\n\n')
                #Mostrando a matriz formada
                mostramatrizjogo()
                #Analizando a soma dos elementos das linhas
                magicototal=0
                for num in range(quadrado):
                    for num2 in range(quadrado):
                        magico=str(matriz[num][num2])
                        magicototal=str(magicototal)+magico
                    conferemagico.append(magicototal)
                    magicototal=0
                #Analizando a soma dos elementos das colunas
                for num in range(quadrado):
                    for num2 in range(quadrado):
                        magico=str(matriz[num2][num])
                        magicototal=str(magicototal)+magico
                    conferemagico.append(magicototal)
                    magicototal=0
                #Analizando a soma dos elementos na diagonal decrescente da esquerda para a direita
                for num in range(quadrado):
                    magico=str(matriz[num][num])
                    magicototal=str(magicototal)+magico
                conferemagico.append(magicototal)
                magicototal=0
                i=-1
                #Analizando a soma dos elementos na diagonal decrescente da direita para a esquerda
                for num in reversed(range(quadrado)):
                    while i!=quadrado:
                        i=i+1
                        break
                    magico=str(matriz[num][i])
                    magicototal=str(magicototal)+magico
                conferemagico.append(magicototal)
                #Conferindo se o quadrado é mágico e mostrando a resposta
                if any(mg ==str(0)+jogador1*quadrado for mg in (conferemagico)):
                    print()
                    print(f"O jogador 1 ({nomejg1}) venceu!")
                    testevelha=0
                    placar1=placar1+1
                    pass
                elif any(mg ==str(0)+jogador2*quadrado for mg in (conferemagico)):
                    print()
                    print(f"O jogador 2 ({nomejg2}) venceu!")
                    testevelha=0
                    placar2=placar2+1
                    pass
                else:
                    testevelha=1
                    pass
            if testevelha==1:
                print()
                print("Deu velha!")
                placar1=placar1+1
                placar2=placar2+1   
            print()
            print(f"Placar = {placar1}x{placar2}")
            time.sleep(2)
            print()
            moldmatriz()
            conferemagico=[]
        if placar1>placar2:
            print(f"O vencedor geral é o jogador 1 ({nomejg1})!")
        elif placar1<placar2:
            print(f"O vencedor geral é o jogador 2 ({nomejg2})!")
        else:
            print("O jogo terminou em empate!")
        reiniciar=str("Deseja reiniciar o programa?  ")
        reiniciar=leiastr(reiniciar)
        if "s" in reiniciar:
            os.system("cls")
            print()
            continue
                

run()







