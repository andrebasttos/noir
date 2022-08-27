#Saudação
print("Olá!\nEu sou o inspetor de NOIR versão 2.0")
print("Para iniciar o jogo preciso de algumas informações, tudo bem?")
Inicio = int(input("1-SIM 2-NÃO: "))
if(Inicio == 2):
    print("Até uma próxima vez!")
    #PRECISO TERMINAR O JOGO AQUI.... COMO?
else:
    print("Vamos jogar!")

#Escolher a forma como as cartas serão distribuídas no tabuleiro
Arrumar = int(input("As cartas serão colocadas na forma padrão?\n1-SIM 2-NÃO: "))
m = 5
n = 5
if(Arrumar == 1):
    elemento = 0
    Mesa = []
    for i in range(m):
        Mesa.append([])
        for j in range(n):
            Mesa[i].append(elemento)
            elemento = elemento + 1
    #exibir o tabuleiro para verificação
    print("O Tabuleiro ficou assim: ")
    for i in range(0,len(Mesa)):
        for j in range(0,len(Mesa[i])):
            print("\t%s" %Mesa[i][j], end = " ")
        print()   

else:
    Mesa = []
    for i in range(m):
        Mesa.append([])
        for j in range(n):
            elemento = input("Elemento da %da. linha, %da. coluna: " %(i+1,j+1))
            Mesa[i].append(elemento)
    #exibir o tabuleiro para verificação
    for i in range(0,len(Mesa)):
            for j in range(0,len(Mesa[i])):
                print("\t%s" %Mesa[i][j], end = " ")
            print()   
 
#Ler as cartas do monte físico
A = int(input("Primeira carta: "))
for i in range(0,len(Mesa)):
    for j in range(0,len(Mesa[i])):
        if (A == Mesa[i][j]):
            break
            
            print()   

B = int(input("Segunda carta: "))
C = int(input("Terceira carta: "))
D = int(input("Quarta carta: "))

#Escolha de personalidade e inocentes
if (A != Mesa[0][0] and A != Mesa[0][4] and A != Mesa[4][0] and A != Mesa[4][4]):
    Det = A
    Inoc = [B,C,D]
elif(B != Mesa[0][0] and B != Mesa[0][4] and B != Mesa[4][0] and B != Mesa[4][4]):
    Det = B
    Inoc = [A,C,D]
elif(C != Mesa[0][0] and C != Mesa[0][4] and C != Mesa[4][0] and C != Mesa[4][4]):
     Det = C
     Inoc = [A,B,D]
elif(D != Mesa[0][0] and D != Mesa[0][4] and D != Mesa[4][0] and D != Mesa[4][4]):
     Det = D
     Inoc = [A,B,C]
#Caso todas as quatro cartas tenha sido extremidades
#Escolha como padrão Det = A
else:
    Det = A
    Inoc = [B,C,D]
print("Inocentes: ",Inoc)
print("Detetive: ",Det)

#Ler qual a primeira vítima
Vit = int(input("Qual a primeira vítima: "))

#A partir da vítima determinar quais os suspeitos
#Esse módulo está considerando a partir da qui que as cartas
#foram arrumadas de forma padrão ou seja as cartas são
#números inteiros, caso entre com os valores das cartas
#será necessário desenvolver módulos para cartas sem ser inteiros

#determina a posição da vítima no tabuleiro
for i in range(m):
    for j in range(n):
        if (Vit == Mesa[i][j]):
            LVit = i
            CVit = j
print("A Vítima está na posição\nLinha: %d\nColuna: %d" % (LVit,CVit))

#Montar vetor de suspeitos

#Vítima primeira linha
if(LVit == 0 and CVit == 0):
    Susp = [Mesa[0][1],Mesa[1][0],Mesa[1][1]]
elif(LVit == 0 and CVit == 4):
    Susp = [Mesa[0][3],Mesa[1][3],Mesa[1][4]]
elif(LVit == 0):
    Susp = [Mesa[LVit][CVit-1],Mesa[LVit+1][CVit-1],Mesa[LVit+1][CVit],Mesa[LVit+1][CVit+1],Mesa[LVit][CVit+1]]



#==============================================
    #criar uma função que sirva para qualquer tamanho de matriz

#Vítima última linha
if(LVit == 0 and CVit == len(Mesa[0])):
    Susp = [Mesa[0][1],Mesa[1][0],Mesa[1][1]]
elif(LVit == 0 and CVit == 4):
    Susp = [Mesa[0][3],Mesa[1][3],Mesa[1][4]]
elif(LVit == 0):
    Susp = [Mesa[LVit][CVit-1],Mesa[LVit+1][CVit-1],Mesa[LVit+1][CVit],Mesa[LVit+1][CVit+1],Mesa[LVit][CVit+1]]


    
print(Susp)
