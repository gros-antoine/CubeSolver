'''PROGRAMME INCLUANT QUELQUES METHODES'''
'''     UTILES ET UTILISEES SOUVENT    '''

import time
import random

# Liste des indices à échanger en fonction du mouvement à réaliser
R = [2, 5, 8, 29, 32, 35, 47, 50, 53, 9, 12, 15, 36, 37, 42, 39, 44, 43, 38, 41]
Rp = [47, 50, 53, 29, 32, 35, 2, 5, 8, 9, 12, 15, 36, 37, 38, 41, 44, 43, 42, 39]
R2 = [29, 32, 35, 15, 12, 9, 2, 5, 8, 47, 50, 53, 36, 37, 44, 43, 38, 41, 42, 39]

L = [45, 48, 51, 27, 30, 33, 0, 3, 6, 11, 14, 17, 18, 19, 24, 21, 26, 25, 20, 23]
Lp = [0, 3, 6, 27, 30, 33, 45, 48, 51, 11, 14, 17, 18, 19, 20, 23, 26, 25, 24, 21]
L2 = [0, 3, 6, 45, 48, 51, 27, 30, 33, 17, 14, 11, 18, 19, 26, 25, 20, 23, 24, 21]

F = [6, 7, 8, 26, 23, 20, 47, 46, 45, 36, 39, 42, 27, 28, 33, 30, 35, 34, 29, 32]
Fp = [6, 7, 8, 36, 39, 42, 47, 46, 45, 26, 23, 20, 27, 28, 29, 32, 35, 34 ,33, 30]
F2 = [6, 7, 8, 47, 46, 45, 20, 23, 26, 42, 39, 36, 27, 28, 35, 34, 29, 32, 33, 30]

B = [0, 1, 2, 38, 41, 44, 53, 52, 51, 24, 21, 18, 9, 10, 15, 12, 17, 16, 11, 14]
Bp = [0, 1, 2, 24, 21, 18, 53, 52, 51, 38, 41, 44, 9, 10, 11, 14, 17, 16, 15, 12]
B2 = [0, 1, 2, 53, 52, 51, 18, 21, 24, 44, 41, 38, 9, 10, 17, 16, 11, 14, 15, 12]

U = [27, 28, 29, 36, 37, 38, 9, 10, 11, 18, 19, 20, 0, 1, 6, 3, 8, 7, 2, 5]
Up = [27, 28, 29, 18, 19, 20, 9, 10, 11, 36, 37, 38, 0, 1, 2, 5, 8, 7, 6, 3]
U2 = [27, 28, 29, 9, 10, 11, 36, 37, 38, 18, 19, 20, 0, 1, 8, 7, 2, 5, 6, 3]

D = [33, 34, 35, 24, 25, 26, 15, 16 ,17, 42, 43, 44, 45 ,46, 51, 48, 53, 52, 47, 50]
Dp = [33, 34, 35, 42, 43, 44, 15, 16, 17, 24, 25, 26, 45, 46, 47, 50, 53, 52, 51, 48]
D2 = [33, 34, 35, 15, 16, 17, 42, 43, 44, 24, 25, 26, 45, 46, 53, 52, 47, 50, 51, 48]

S = [3, 4, 5, 25, 22, 19, 50, 49, 48, 37, 40, 43]
Sp = [3, 4, 5, 37, 40, 43, 50, 49, 48, 25, 22, 19]
S2 = [3, 4, 5, 50, 49, 48, 19, 22, 25, 43, 40 ,37]

M = [1, 4, 7, 16, 13, 10, 46, 49, 52, 28, 31, 34]
Mp = [1, 4, 7, 28, 31, 34, 46, 49, 52, 16, 13, 10]
M2 = [1, 4, 7, 46, 49, 52, 28, 31, 34, 16, 13, 10]

E = [30, 31, 32, 21, 22, 23, 12, 13, 14, 39, 40, 41]
Ep = [30, 31, 32, 39, 40, 41, 12, 13, 14, 21, 22, 23]
E2 = [30, 31, 32, 12, 13, 14, 21, 22, 23, 39, 40, 41]

cube = [2,5,1,4,0,2,4,2,3,
        5,1,1,0,3,5,0,4,4,
        5,0,0,4,4,3,0,3,5,
        3,5,2,5,1,2,3,3,1,
        5,1,4,0,2,1,0,1,2,
        4,2,2,0,5,4,1,3,3]



def ESM(c, index):

    buf = c[index[0]], c[index[1]], c[index[2]]
    c[index[0]], c[index[1]], c[index[2]] = c[index[3]], c[index[4]], c[index[5]]
    c[index[3]], c[index[4]], c[index[5]] = c[index[6]], c[index[7]], c[index[8]]
    c[index[6]], c[index[7]], c[index[8]] = c[index[9]], c[index[10]], c[index[11]]
    c[index[9]], c[index[10]], c[index[11]] = buf[0], buf[1], buf[2]

    return c

def ESM2(c, index):

    c[index[0]], c[index[1]], c[index[2]], c[index[3]], c[index[4]], c[index[5]] = c[index[3]], c[index[4]], c[index[5]], c[index[0]], c[index[1]], c[index[2]]
    c[index[6]], c[index[7]], c[index[8]], c[index[9]], c[index[10]], c[index[11]] = c[index[9]], c[index[10]], c[index[11]], c[index[6]], c[index[7]], c[index[8]]

    return c

#---------------Méthode UDFBRL---------------#
# Execute le mouvement passé en paramètres
# sur le cube passé en paramètres (seulement
# les mouvements sans "2" sont acceptés)
# 
def UDFBRL(c, index):
    
    buf = c[index[0]], c[index[1]], c[index[2]]
    c[index[0]], c[index[1]], c[index[2]] = c[index[3]], c[index[4]], c[index[5]]
    c[index[3]], c[index[4]], c[index[5]] = c[index[6]], c[index[7]], c[index[8]]
    
    if index[1] == 5 or index[1] == 50 or index[1] == 32 or index[1] == 48 or index[1] == 3:

        c[index[6]], c[index[7]], c[index[8]] = c[index[11]], c[index[10]], c[index[9]]
        c[index[9]], c[index[10]], c[index[11]] = buf[2], buf[1], buf[0]

    else:

        c[index[6]], c[index[7]], c[index[8]] = c[index[9]], c[index[10]], c[index[11]]
        c[index[9]], c[index[10]], c[index[11]] = buf[0], buf[1], buf[2]    

    buf = c[index[12]], c[index[13]]
    c[index[12]], c[index[13]] = c[index[14]], c[index[15]]
    c[index[14]], c[index[15]] = c[index[16]], c[index[17]]
    c[index[16]], c[index[17]] = c[index[18]], c[index[19]]
    c[index[18]], c[index[19]] = buf[0], buf[1]
    
    return c


#---------------Méthode UDFBRL2---------------#
# Execute le mouvement passé en paramètres
# sur le cube passé en paramètres (seulement
# les mouvements en "2" sont acceptés)
# 
def UDFBRL2(c, index):
    
    c[index[0]], c[index[1]], c[index[2]], c[index[3]], c[index[4]], c[index[5]] = c[index[3]], c[index[4]], c[index[5]], c[index[0]], c[index[1]], c[index[2]]
    c[index[6]], c[index[7]], c[index[8]], c[index[9]], c[index[10]], c[index[11]] = c[index[9]], c[index[10]], c[index[11]], c[index[6]], c[index[7]], c[index[8]]

    c[index[12]], c[index[13]], c[index[14]], c[index[15]] = c[index[14]], c[index[15]], c[index[12]], c[index[13]]
    c[index[16]], c[index[17]], c[index[18]], c[index[19]] = c[index[18]], c[index[19]], c[index[16]], c[index[17]]
    
    return c

def numberMove(num, c):
    
    if num == 0:
        c = UDFBRL(c, R)
    elif num == 1:
        c = UDFBRL(c, Rp)
    elif num == 2:
        c = UDFBRL2(c, R2)
    elif num == 3:
        c = UDFBRL(c, L)
    elif num == 4:
        c = UDFBRL(c, Lp)
    elif num == 5:
        c = UDFBRL2(c, L2)
    elif num == 6:
        c = UDFBRL(c, F)
    elif num == 7:
        c = UDFBRL(c, Fp)
    elif num == 8:
        c = UDFBRL2(c, F2)
    elif num == 9:
        c = UDFBRL(c, B)
    elif num == 10:
        c = UDFBRL(c, Bp)
    elif num == 11:
        c = UDFBRL2(c, B2)
    elif num == 12:
        c = UDFBRL(c, U)
    elif num == 13:
        c = UDFBRL(c, Up)
    elif num == 14:
        c = UDFBRL2(c, U2)
    elif num == 15:
        c = UDFBRL(c, D)
    elif num == 16:
        c = UDFBRL(c, Dp)
    elif num == 17:
        c = UDFBRL2(c, D2)

#---------------Méthode minMove---------------#
# Compare deux listes de mouvements entrées en
# paramètres et retourne la plus petite (en
# prenant en compte que les mouvements en
# "2" comptent comme 2 mouvements)
#
def minMove(moves1, moves2):

    len1 = 0
    len2 = 0

    # Calcul de la longueur de la liste n°1
    for move in moves1:

        if (move == "0" and move == "1"
           or move == "3" and move == "4"
           or move == "6" and move == "7"
           or move == "9" and move == "A"
           or move == "C" and move == "D"
           or move == "F" and move == "G"):
            len1 += 1
        else:
            len1 += 2
    # Calcul de la longueur de la liste n°2
    for move in moves2:

        if (move == "0" or move == "1"
           or move == "3" or move == "4"
           or move == "6" or move == "7"
           or move == "9" or move == "A"
           or move == "C" or move == "D"
           or move == "F" or move == "G"):
            len2 += 1
        else:
            len2 += 2

    if len1 > len2:
        return moves2
    else:
        return moves1


#---------------optimizeMove---------------#
# Optimise la liste de mouvements entrée en
# paramètres et la retourne (RR -> R2,
# RR' -> /, ...)
#
def optimizeMove(moves):

    optimizedMove = ""

    i = 0
    
    while i < len(moves):
        
        if i != len(moves) - 1:

            if (moves[i] == "0" and moves[i+1] == "1"
               or moves[i] == "1" and moves[i+1] == "0"
               or moves[i] == "3" and moves[i+1] == "4"
               or moves[i] == "4" and moves[i+1] == "3"
               or moves[i] == "6" and moves[i+1] == "7"
               or moves[i] == "7" and moves[i+1] == "6"
               or moves[i] == "9" and moves[i+1] == "A"
               or moves[i] == "A" and moves[i+1] == "9"
               or moves[i] == "C" and moves[i+1] == "D"
               or moves[i] == "D" and moves[i+1] == "C"
               or moves[i] == "F" and moves[i+1] == "G"
               or moves[i] == "G" and moves[i+1] == "F"
               or moves[i] == "2" and moves[i+1] == "2"
               or moves[i] == "5" and moves[i+1] == "5"
               or moves[i] == "8" and moves[i+1] == "8"
               or moves[i] == "B" and moves[i+1] == "B"
               or moves[i] == "E" and moves[i+1] == "E"
               or moves[i] == "H" and moves[i+1] == "H"):
                   i += 1

            elif moves[i] == "0" and moves[i+1] == "0" or moves[i] == "1" and moves[i+1] == "1":
                optimizedMove += "2"
                i += 1
            elif moves[i] == "3" and moves[i+1] == "3" or moves[i] == "4" and moves[i+1] == "4":
                optimizedMove += "5"
                i += 1
            elif moves[i] == "6" and moves[i+1] == "6" or moves[i] == "7" and moves[i+1] == "7":
                optimizedMove += "8"
                i += 1
            elif moves[i] == "9" and moves[i+1] == "9" or moves[i] == "A" and moves[i+1] == "A":
                optimizedMove += "B"
                i += 1
            elif moves[i] == "C" and moves[i+1] == "C" or moves[i] == "D" and moves[i+1] == "D":
                optimizedMove += "E"
                i += 1
            elif moves[i] == "F" and moves[i+1] == "F" or moves[i] == "G" and moves[i+1] == "G":
                optimizedMove += "H"
                i += 1

            elif moves[i] == "0" and moves[i+1] == "2" or moves[i] == "2" and moves[i+1] == "0":
                optimizedMove += "1"
                i += 1
            elif moves[i] == "1" and moves[i+1] == "2" or moves[i] == "2" and moves[i+1] == "1":
                optimizedMove += "0"
                i += 1
            elif moves[i] == "3" and moves[i+1] == "5" or moves[i] == "5" and moves[i+1] == "3":
                optimizedMove += "4"
                i += 1
            elif moves[i] == "4" and moves[i+1] == "5" or moves[i] == "5" and moves[i+1] == "4":
                optimizedMove += "3"
                i += 1
            elif moves[i] == "6" and moves[i+1] == "8" or moves[i] == "8" and moves[i+1] == "6":
                optimizedMove += "7"
                i += 1
            elif moves[i] == "7" and moves[i+1] == "8" or moves[i] == "8" and moves[i+1] == "7":
                optimizedMove += "6"
                i += 1
            elif moves[i] == "9" and moves[i+1] == "B" or moves[i] == "B" and moves[i+1] == "9":
                optimizedMove += "A"
                i += 1
            elif moves[i] == "A" and moves[i+1] == "B" or moves[i] == "B" and moves[i+1] == "A":
                optimizedMove += "9"
                i += 1
            elif moves[i] == "C" and moves[i+1] == "E" or moves[i] == "E" and moves[i+1] == "C":
                optimizedMove += "D"
                i += 1
            elif moves[i] == "D" and moves[i+1] == "E" or moves[i] == "E" and moves[i+1] == "D":
                optimizedMove += "C"
                i += 1
            elif moves[i] == "F" and moves[i+1] == "H" or moves[i] == "H" and moves[i+1] == "F":
                optimizedMove += "G"
                i += 1
            elif moves[i] == "G" and moves[i+1] == "H" or moves[i] == "H" and moves[i+1] == "G":
                optimizedMove += "F"
                i += 1

            else:

                optimizedMove += moves[i]
                if i == len(moves) - 2:

                    optimizedMove += moves[len(moves)-1]
                    i+=1
        else:
            optimizedMove += moves[i]
            
        i += 1
        
    return optimizedMove

def applyLetterMove(moves, c):

    for move in moves:

        if move == "0":
            c = UDFBRL(c, R)
        elif move == "1":
            c = UDFBRL(c, Rp)
        elif move == "2":
            c = UDFBRL2(c, R2)
        elif move == "3":
            c = UDFBRL(c, L)
        elif move == "4":
            c = UDFBRL(c, Lp)
        elif move == "5":
            c = UDFBRL2(c, L2)
        elif move == "6":
            c = UDFBRL(c, F)
        elif move == "7":
            c = UDFBRL(c, Fp)
        elif move == "8":
            c = UDFBRL2(c, F2)
        elif move == "9":
            c = UDFBRL(c, B)
        elif move == "A":
            c = UDFBRL(c, Bp)
        elif move == "B":
            c = UDFBRL2(c, B2)
        elif move == "C":
            c = UDFBRL(c, U)
        elif move == "D":
            c = UDFBRL(c, Up)
        elif move == "E":
            c = UDFBRL2(c, U2)
        elif move == "F":
            c = UDFBRL(c, D)
        elif move == "G":
            c = UDFBRL(c, Dp)
        elif move == "H":
            c = UDFBRL2(c, D2)
        

def lenghtMove(moves):

    l = 0

    for move in moves:

        if move in ["2", "5", "8", "B", "E", "H"]:
            l += 2
        else:
            l += 1
            
    return l

#---------------Méthode printCube---------------#
# Affiche une représentation du cube entré
# en paramètres avec cette forme ci :
#     U0 U1 U2
#     U3 U4 U5
#     U6 U7 U8
#
#     B0 B1 B2
#     B3 B4 B5
#     B6 B7 B8
#
#     L0 L1 L2
#     L3 L4 L5
#     L6 L7 L8
#
#     F0 F1 F2
#     F3 F4 F5
#     F6 F7 F8
#
#     R0 R1 R2
#     R3 R4 R5
#     R6 R7 R8
#
#     D0 D1 D2
#     D3 D4 D5
#     D6 D7 D8
#
def printCube(c):
    
    for i in range(len(c)):
        if(i%3 == 2):
            print(c[i])
        else:
            print(c[i], end=" ")

        if(i%9 == 8):
            print()


#---------------Méthode printMoves---------------#
# Convertie la suite de mouvements entrés en
# paramètres (les mouvements étants indiqués avec la
# représentation du programme) en mouvements écrits
# avec la représentation algorithmique et l'affiche
#
def printMove(nums):

    moves = ""
    
    for num in nums:

        # Conversion du mouvement
        if num == "0":
            moves += "R"
        elif num == "1":
            moves += "R'"
        elif num == "2":
            moves += "R2"
        elif num == "3":
            moves += "L"
        elif num == "4":
            moves += "L'"
        elif num == "5":
            moves += "L2"
        elif num == "6":
            moves += "F"
        elif num == "7":
            moves += "F'"
        elif num == "8":
            moves += "F2"
        elif num == "9":
            moves += "B"
        elif num == "A":
            moves += "B'"
        elif num == "B":
            moves += "B2"
        elif num == "C":
            moves += "U"
        elif num == "D":
            moves += "U'"
        elif num == "E":
            moves += "U2"
        elif num == "F":
            moves += "D"
        elif num == "G":
            moves += "D'"
        elif num == "H":
            moves += "D2"

    print(moves)
        

#---------------Méthode applyMove---------------#
# Exécute les mouvements sur le cube entré en
# paramètres (les mouvements étants indiqués avec
# la représentation algorithmique)
#
def applyMove(c, moves):
    
    for i in range(len(moves)):
        
        move = moves[i]

        # Les mouvements étant indiqués littéralement
        # (R', R, ...), il faut vérifier le caractère
        # suivant afin de vérifier si le mouvement est
        # en "'" ou "2"
        try:
            
            if moves[i+1] == "'":

                move += "'"
            elif moves[i+1] == "2":

                move += "2"
        except:
            pass

        # Exécution des mouvements
        if move == "R":
            c = UDFBRL(c, R)
        elif move == "R'":
            c = UDFBRL(c, Rp)
        elif move == "R2":
            c = UDFBRL2(c, R2)
        elif move == "L":
            c = UDFBRL(c, L)
        elif move == "L'":
            c = UDFBRL(c, Lp)
        elif move == "L2":
            c = UDFBRL2(c, L2)
        elif move == "F":
            c = UDFBRL(c, F)
        elif move == "F'":
            c = UDFBRL(c, Fp)
        elif move == "F2":
            c = UDFBRL2(c, F2)
        elif move == "B":
            c = UDFBRL(c, B)
        elif move == "B'":
            c = UDFBRL(c, Bp)
        elif move == "B2":
            c = UDFBRL2(c, B2)
        elif move == "U":
            c = UDFBRL(c, U)
        elif move == "U'":
            c = UDFBRL(c, Up)
        elif move == "U2":
            c = UDFBRL2(c, U2)
        elif move == "D":
            c = UDFBRL(c, D)
        elif move == "D'":
            c = UDFBRL(c, Dp)
        elif move == "D2":
            c = UDFBRL2(c, D2)
        elif move == "E":
            c = ESM(c, E)
        elif move == "E'":
            c = ESM(c, Ep)
        elif move == "E2":
            c = ESM2(c ,E2)
        elif move == "M":
            c = ESM(c, M)
        elif move == "M'":
            c = ESM(c , Mp)
        elif move == "M2":
            c = ESM2(c, M2)
        elif move == "S":
            c = ESM(c , S)
        elif move == "S'":
            c = ESM(c, Sp)
        elif move == "S2":
            c = ESM2(c , S2)
    
    return c

def inverse(moves):

    inv = ""

    moves = moves[::-1]
    
    for move in moves:
        
        if move == "0":
            inv += "1"
        elif move == "1":
            inv += "0"
        elif move == "2":
            inv += "2"
        elif move == "3":
            inv += "4"
        elif move == "4":
            inv += "3"
        elif move == "5":
            inv += "5"
        elif move == "6":
            inv += "7"
        elif move == "7":
            inv += "6"
        elif move == "8":
            inv += "8"
        elif move == "9":
            inv += "A"
        elif move == "A":
            inv += "9"
        elif move == "B":
            inv += "B"
        elif move == "C":
            inv += "D"
        elif move == "D":
            inv += "C"
        elif move == "E":
            inv += "E"
        elif move == "F":
            inv += "G"
        elif move == "G":
            inv += "F"
        elif move == "H":
            inv += "H"
    
    return inv

def invMove(moves):

    conv = ""
        
    for i in range(len(moves)):
        
        move = moves[i]

        # Les mouvements étant indiqués littéralement
        # (R', R, ...), il faut vérifier le caractère
        # suivant afin de vérifier si le mouvement est
        # en "'" ou "2"
        try:
            
            if moves[i+1] == "'":

                move += "'"
            elif moves[i+1] == "2":

                move += "2"
        except:
            pass

        # Exécution des mouvements
        if move == "R":
            conv += "R'"
        elif move == "R'":
            conv += "R"
        elif move == "R2":
            conv += move
        elif move == "L":
            conv += "L'"
        elif move == "L'":
            conv += "L"
        elif move == "L2":
            conv += move
        elif move == "F":
            conv += "F'"
        elif move == "F'":
            conv += "F"
        elif move == "F2":
            conv += move
        elif move == "B":
            conv += "B'"
        elif move == "B'":
            conv += "B"
        elif move == "B2":
            conv += move
        elif move == "U":
            conv += "U'"
        elif move == "U'":
            conv += "U"
        elif move == "U2":
            conv += move
        elif move == "D":
            conv += "D'"
        elif move == "D'":
            conv += "D"
        elif move == "D2":
            conv += move
        elif move == "E":
            conv += "E'"
        elif move == "E'":
            conv += "E"
        elif move == "E2":
            conv += move
        elif move == "M":
            conv += "M'"
        elif move == "M'":
            conv += "M"
        elif move == "M2":
            conv += move
        elif move == "S":
            conv += "S'"
        elif move == "S'":
            conv += "S"
        elif move == "S2":
            conv += move
    
    return conv

faces = ["RX", "LX", "UY", "DY", "FZ", "BZ"]

def randomRotation():

    r = random.randint(0, 2)

    if r == 0:
        return ""
    elif r == 1:
        return "'"
    else:
        return "2"

def randomFace(lastFace):

    face = faces[random.randint(0, 5)]

    if face[1] == lastFace[1]:
        return randomFace(lastFace)
    else:
        return face

def generateScramble():

    scramble = ''
    lastFace = '  '

    for i in range(24):
        lastFace = randomFace(lastFace)
        scramble += lastFace[0] + randomRotation() + ' '

    return scramble[:-1]
