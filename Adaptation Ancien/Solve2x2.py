from Coin import *
from outils import *
import random
import time

JAUNE = 0
BLEU = 1
ROUGE = 2
VERT = 3
ORANGE = 4
BLANC = 5

BOBllibre = True
BRBllibre = True
RVBllibre = True
VOBllibre = True

pllT = "R'FR'F2RU'R'F2R2"
diag = "RU'R'U'F2U'RUR'DR2U"
inv = "R2U'R2U2B2U'B2"
pllTdiag = "RU'RF2R'UR'"
doublediag = "R2F2R2"

chaise = "RUR'URU2R'"
chaiseinv = "R'ULU'RUL'"
Pi = "R'UR2U'R2U'R2UR'"
frere = "FRUR'U'F'"
L = "FR'F'RURU'R'"
T = "RUR'U'R'FRF'"
H = "R2U2RU2R2"

JVOj = "LU2L'U'LUL'"
JVOv = "B'U'B"
JVOo = "LUL'"
JRVj = "BU2B'U'BUB'"
JRVr = "R'U'R"
JRVv = "BUB'"
JBRj = "RU2R'U'RUR'"
JBRb = "F'U'F"
JBRr = "RUR'"
JBOj = "L'U2LUL'U'L"
JBOb = "FUF'"
JBOo = "L'U'L"
BOBlb = "FUF'U'FUF'"
BOBlo = "L'U'LUL'U'L"
BRBlb = "F'U'FUF'U'F"
BRBlr = "RUR'U'RUR'"
RVBlr = "R'U'RUR'U'R"
RVBlv = "BUB'U'BUB'"
VOBlv = "B'U'BUB'U'B"
VOBlo = "LUL'U'LUL'"

facejaune = []
comptjaune = 0
Fcompt = 0
Rcompt = 0
Lcompt = 0
Bcompt = 0

jaunef = False
jauneplltF = False
jauneplltR = False
jauneplltB = False
jauneplltL = False
jaunediag = False
jaunediagF = False
jaunediagR = False
blancf = False
blancplltF = False
blancplltR = False
blancplltB = False
blancplltL = False
blancdiag = False
blancdiagR = False
blancdiagF = False

Resolution = ''

def randomCube(c):
    
    mel = ""
    
    for i in range(24):

        r = random.randint(0, 17)
        mel += str(r) + " "
        numberMove(r, c)

    return mel

def colorOpposed(c1, c2):

    if(c1 == VERT and c2 == BLEU or
       c1 == BLEU and c2 == VERT):
        return True

    elif(c1 == ORANGE and c2 == ROUGE or
         c1 == ROUGE and c2 == ORANGE):
        return True

    return False

def yConversion(alg):

    conv = ''
    
    for c in alg:

        if c == 'R':
            conv += 'B'
        elif c == 'L':
            conv += 'F'
        elif c == 'B':
            conv += 'L'
        elif c == 'F':
            conv += 'R'
        else:
            conv += c

    return conv

def ypConversion(alg):
    
    conv = ''

    for c in alg:

        if c == 'R':
            conv += 'F'
        elif c == 'L':
            conv += 'B'
        elif c == 'B':
            conv += 'R'
        elif c == 'F':
            conv += 'L'
        else:
            conv += c

    return conv

def y2Conversion(alg):
    
    conv = ''

    for c in alg:

        if c == 'R':
            conv += 'L'
        elif c == 'L':
            conv += 'R'
        elif c == 'B':
            conv += 'F'
        elif c == 'F':
            conv += 'B'
        else:
            conv += c

    return conv
    
def xConversion(alg):

    conv = ''

    for c in alg:

        if c == 'R':
            conv += 'L'
        elif c == 'U':
            conv += 'D'
        elif c == 'L':
            conv += 'R'
        elif c == 'D':
            conv += 'U'
        else:
            conv += c

    return conv

#---------------Méthode chooseCorner---------------#
# Choisi un coin de la face du bas qui est libre
# afin d'y placer la coin du dessus
def chooseCorner(coin, reso, c):

    global BOBllibre
    global BRBllibre
    global RVBllibre
    global VOBllibre
    
    if coin == 'JVO':

        if RVBllibre:

            if BRBllibre:

                if c == 'j':

                    BRBllibre = False
                    return "UR2"

                elif c == 'v':

                    BRBllibre = False
                    return "U2R'"

                elif c == 'o':

                    RVBllibre = False
                    return "UR"

            else:

                RVBllibre = False
                return "U" + ypConversion(reso)

        elif BOBllibre:
            
            if BRBllibre:

                if c == 'j':

                    BRBllibre = False
                    return "U'F2"

                elif c == 'v':

                    BOBllibre = False
                    return "U'F'"

                elif c == 'o':

                    BRBllibre = False
                    return "U2F"

            else:

                BOBllibre = False
                return "U'" + yConversion(reso)
        else:

            BRBllibre = False
            return "U2" + y2Conversion(reso)

    elif coin == 'JRV':

        if VOBllibre:

            if BOBllibre:

                if c == 'j':

                    BOBllibre = False
                    return "U'L2"

                elif c == 'r':

                    VOBllibre = False
                    return "U'L'"

                elif c == 'v':

                    BOBllibre = False
                    return "U2L"

            else:

                VOBllibre = False
                return "U'" + yConversion(reso)

        elif BRBllibre:

            if BOBllibre:

                if c == 'j':

                    BOBllibre = False
                    return "UF2"

                elif c == 'r':

                    BOBllibre = False
                    return "U2F'"

                elif c == 'v':

                    BRBllibre = False
                    return "UF"

            else:

                BRBllibre = False
                return "U" + ypConversion(reso)

        else:

            BOBllibre = False
            return "U2" + y2Conversion(reso)

    elif coin == 'JBR':
        
        if RVBllibre:

            if VOBllibre:

                if c == 'j':

                    VOBllibre = False
                    return "U'B2"

                elif c == 'b':

                    RVBllibre = False
                    return "U'B'"

                elif c == 'r':

                    VOBllibre = False
                    return "U2B"

            else:

                RVBllibre = False
                return "U'" + yConversion(reso)

        elif BOBllibre:

            if VOBllibre:

                if c == 'j':

                    VOBllibre = False
                    return "UL2"

                elif c == 'b':

                    VOBllibre = False
                    return "U2L'"

                elif c == 'r':

                    BOBllibre = False
                    return "UL"

            else:

                BOBllibre = False
                return "U" + ypConversion(reso)

        else:

            VOBllibre = False
            return "U2" + y2Conversion(reso)

    elif coin == 'JBO':

        if BRBllibre:

            if RVBllibre:

                if c == 'j':

                    RVBllibre = False
                    return "U'R2"

                elif c == 'b':

                    RVBllibre = False
                    return "U2R"

                elif c == 'o':

                    BRBllibre = False
                    return "U'R'"

            else:

                BRBllibre = False
                return "U'" + yConversion(reso)

        elif VOBllibre:

            if RVBllibre:

                if c == 'j':

                    RVBllibre = False
                    return "UB2"

                elif c == 'b':

                    VOBllibre = False
                    return "UB"

                elif c == 'o':

                    RVBllibre = False
                    return "U2B'"

            else:

                VOBllibre = False
                return "U" + ypConversion(reso)
        else:

            RVBllibre = False
            return "U2" + y2Conversion(reso)

def solve(cube):

    #print(randomCube(cube))

    global JAUNE
    global BLEU
    global ROUGE
    global VERT
    global ORANGE
    global BLANC

    global BOBllibre
    global BRBllibre
    global RVBllibre
    global VOBllibre

    global pllT
    global diag
    global inv
    global pllTdiag
    global doublediag

    global chaise
    global chaiseinv
    global Pi
    global frere
    global L
    global T
    global H

    global JVOj
    global JVOv
    global JVOo
    global JRVj
    global JRVr
    global JRVv
    global JBRj
    global JBRb
    global JBRr
    global JBOj
    global JBOb
    global JBOo
    global BOBlb
    global BOBlo
    global BRBlb
    global BRBlr
    global RVBlr
    global RVBlv
    global VOBlv
    global VOBlo

    global facejaune
    global comptjaune
    global Fcompt
    global Rcompt
    global Lcompt
    global Bcompt

    global jaunef
    global jauneplltF
    global jauneplltR
    global jauneplltB
    global jauneplltL
    global jaunediag
    global jaunediagF
    global jaunediagR
    global blancf
    global blancplltF
    global blancplltR
    global blancplltB
    global blancplltL
    global blancdiag
    global blancdiagR
    global blancdiagF

    global Resolution
    
    '''cube = [0,1,2,1,0,3,4,0,3,
            5,4,1,0,3,2,0,5,2,
            2,2,3,5,4,3,3,4,3,
            5,1,4,2,1,2,2,5,5,
            0,4,1,0,2,3,4,0,4,
            0,3,1,5,5,4,5,1,1]'''

    '''R F2 D F R B2 L F' R2 B2 U' F B D2 R U2 D2 B2 R U F' B' D' L2 D'''

    JVO = Coin(cube[0], cube[11], cube[18])
    JRV = Coin(cube[2], cube[38], cube[9])
    JBR = Coin(cube[8], cube[29], cube[36])
    JBO = Coin(cube[6], cube[27], cube[20])
    BOBl = Coin(cube[33], cube[26], cube[45])
    BRBl = Coin(cube[35], cube[42], cube[47])
    RVBl = Coin(cube[44], cube[15], cube[53])
    VOBl = Coin(cube[17], cube[24], cube[51])

    if BOBl.getCouleur(3) == BLANC:
        BOBllibre = False
    if BRBl.getCouleur(3) == BLANC:
        BRBllibre = False
    if RVBl.getCouleur(3) == BLANC:
        RVBllibre = False
    if VOBl.getCouleur(3) == BLANC:
        VOBllibre = False
        
    while(BOBllibre or BRBllibre or RVBllibre or VOBllibre):

        partReso = ''
        reso = ''
        coin = ''
        ori = ''

        JVO = Coin(cube[0], cube[11], cube[18])
        JRV = Coin(cube[2], cube[38], cube[9])
        JBR = Coin(cube[8], cube[29], cube[36])
        JBO = Coin(cube[6], cube[27], cube[20])
        BOBl = Coin(cube[33], cube[26], cube[45])
        BRBl = Coin(cube[35], cube[42], cube[47])
        RVBl = Coin(cube[44], cube[15], cube[53])
        VOBl = Coin(cube[17], cube[24], cube[51])

        if BOBl.getCouleur(3) == BLANC:
            BOBllibre = False
        if BRBl.getCouleur(3) == BLANC:
            BRBllibre = False
        if RVBl.getCouleur(3) == BLANC:
            RVBllibre = False
        if VOBl.getCouleur(3) == BLANC:
            VOBllibre = False

        if JVO.has(BLANC):

            print('JVO')
            if JVO.getCouleur(1) == BLANC:

                if(not VOBllibre):

                    partReso = JVOj
                    coin = 'JVO'
                    ori = 'j'

                elif(BOBllibre and VOBllibre):

                    reso += "L2"
                    BOBllibre = False

                elif(VOBllibre and RVBllibre):

                    reso += "B2"
                    RVBllibre = False

                else:

                    reso += JVOj
                    VOBllibre = False

            elif JVO.getCouleur(2) == BLANC:

                if(not VOBllibre):

                    partReso = JVOv
                    coin = 'JVO'
                    ori = 'v'

                elif(BOBllibre and VOBllibre):

                    reso += "L'"
                    VOBllibre = False

                else:

                    reso += JVOv
                    VOBllibre = False

            elif JVO.getCouleur(3) == BLANC:

                if(not VOBllibre):
                    
                    print('oui')
                    partReso = JVOo
                    coin = 'JVO'
                    ori = 'o'

                elif(RVBllibre and VOBllibre):

                    reso += "B"
                    VOBllibre = False

                else:

                    reso += JVOo
                    VOBllibre = False

        elif JRV.has(BLANC):

            print('JRV')
            if JRV.getCouleur(1) == BLANC:

                if(not RVBllibre):

                    partReso = JRVj
                    coin = 'JRV'
                    ori = 'j'

                elif(RVBllibre and VOBllibre):

                    reso += "B2"
                    VOBllibre = False

                elif(RVBllibre and BRBllibre):

                    reso += "R2"
                    BRBllibre = False

                else:

                    reso += JRVj
                    RVBllibre = False

            elif JRV.getCouleur(2) == BLANC:

                if(not RVBllibre):

                    partReso = JRVr
                    coin = 'JRV'
                    ori = 'r'

                elif(RVBllibre and VOBllibre):

                    reso += "B'"
                    RVBllibre = False

                else:

                    reso += JRVr
                    RVBllibre = False

            elif JRV.getCouleur(3) == BLANC:

                if(not RVBllibre):

                    partReso = JRVv
                    coin = 'JRV'
                    ori = 'v'

                elif(BRBllibre and RVBllibre):

                    reso += "R"
                    RVBllibre = False

                else:

                    reso += JRVv
                    RVBllbre = False
        elif JBR.has(BLANC):

            print('JBR')
            if JBR.getCouleur(1) == BLANC:

                if(not BRBllibre):

                    partReso = JBRj
                    coin = 'JBR'
                    ori = 'j'

                elif(BRBllibre and RVBllibre):

                    reso += "R2"
                    RVBllibre = False

                elif(BRBllibre and BOBllibre):

                    reso += "F2"
                    BOBllibre = False

                else:

                    reso += JBRj
                    BRBllibre = False

            elif JBR.getCouleur(2) == BLANC:

                if(not BRBllibre):

                    partReso = JBRb
                    coin = 'JBR'
                    ori = 'b'

                elif(BRBllibre and RVBllibre):

                    reso += "R'"
                    BRBllibre = False

                else:

                    reso += JBRb
                    BRBllibre = False

            elif JBR.getCouleur(3) == BLANC:

                if(not BRBllibre):

                    partReso = JBRr
                    coin = 'JBR'
                    ori = 'r'

                elif(BOBllibre and BRBllibre):

                    reso += "F"
                    BRBllibre = False

                else:

                    reso += JBRr
                    BRBllibre = False
                    
        elif JBO.has(BLANC):

            print('JBO')
            if JBO.getCouleur(1) == BLANC:

                if(not BOBllibre):

                    partReso = JBOj
                    coin = 'JBO'
                    ori = 'j'

                elif(BOBllibre and BRBllibre):

                    reso += "F2"
                    BRBllibre = False

                elif(BOBllibre and VOBllibre):

                    reso += "L2"
                    VOBllibre = False

                else:

                    reso += JBOj
                    BOBllibre = False

            elif JBO.getCouleur(2) == BLANC:

                if(not BOBllibre):

                    partReso = JBOb
                    coin = 'JBO'
                    ori = 'b'

                elif(BOBllibre and VOBllibre):

                    reso = reso + "L"
                    BOBllibre = False

                else:

                    reso += JBOb
                    BOBllibre = False

            elif JBO.getCouleur(3) == BLANC:

                if(not BOBllibre):

                    partReso = JBOo
                    coin = 'JBO'
                    ori = 'o'

                elif(BOBllibre and BRBllibre):

                    reso += "F'"
                    BOBllibre = False

                else:

                    reso += JBOo
                    BOBllibre = False

        elif BOBl.has(BLANC) and BOBllibre:

            print('BOBl')
            if BOBl.getCouleur(1) == BLANC:

                if(not VOBllibre):

                    reso += BOBlb
                    BOBllibre = False

                else:

                    reso += "L"
                    VOBllibre = Fas

            elif BOBl.getCouleur(2) == BLANC:

                if(not BRBllibre):

                    reso += BOBlo
                    BOBllibre = False

                else:

                    reso += "F'"
                    BRBllibre = False
                    
        elif BRBl.has(BLANC) and BRBllibre:

            print('BRBl')
            if BRBl.getCouleur(1) == BLANC:

                if(not RVBllibre):

                    reso += BRBlb
                    BRBllibre = False

                else:

                    reso += "R'"
                    RVBllibre = False

            elif BRBl.getCouleur(2) == BLANC:

                if(not BOBllibre):

                    reso += BRBlr
                    BRBllibre = False

                else:

                    reso += "F"
                    BOBllibre = False

        elif RVBl.has(BLANC) and RVBllibre:

            print('RVBl')
            if RVBl.getCouleur(1) == BLANC:

                if(not VOBllibre):

                    reso += RVBlr
                    RVBllibre = False

                else:

                    reso += "B'"
                    VOBllibre = False

            elif RVBl.getCouleur(2) == BLANC:

                if(not BRBllibre):

                    reso += RVBlv
                    RVBllibre = False

                else:

                    reso += "R"
                    BRBllibre = False
                    
        elif VOBl.has(BLANC) and VOBllibre:

            print('VOBl')
            if VOBl.getCouleur(1) == BLANC:

                if(not BOBllibre):

                    reso += VOBlv
                    VOBllibre = False

                else:

                    reso += "L'"
                    BOBllibre = False

            elif VOBl.getCouleur(2) == BLANC:

                if(not RVBllibre):

                    reso += VOBlo
                    VOBllibre = False

                else:

                    reso += "B"
                    RVBllibre = False

        
        if(partReso != ''):
            reso += chooseCorner(coin, partReso, ori)
        
        Resolution += reso
        print(reso)
        cube = applyMove(cube, reso)
        printCube(cube)
        
    reso = ''

    JVO = Coin(cube[0], cube[11], cube[18])
    JRV = Coin(cube[2], cube[38], cube[9])
    JBR = Coin(cube[8], cube[29], cube[36])
    JBO = Coin(cube[6], cube[27], cube[20])
    BOBl = Coin(cube[33], cube[26], cube[45])
    BRBl = Coin(cube[35], cube[42], cube[47])
    RVBl = Coin(cube[44], cube[15], cube[53])
    VOBl = Coin(cube[17], cube[24], cube[51])

    if JVO.getCouleur(1) == JAUNE:

        comptjaune += 1
        facejaune.append('JVO')

    if JRV.getCouleur(1) == JAUNE:

        comptjaune += 1
        facejaune.append('JRV')

    if JBR.getCouleur(1) == JAUNE:

        comptjaune += 1
        facejaune.append('JBR')

    if JBO.getCouleur(1) == JAUNE:

        comptjaune += 1
        facejaune.append('JBO')

    if('JVO' not in facejaune):

        if JVO.getCouleur(2) == JAUNE:

            facejaune.append('JVOv')
            Bcompt += 1

        else:

            facejaune.append('JVOo')
            Lcompt += 1

    if('JRV' not in facejaune):

        if JRV.getCouleur(2) == JAUNE:

            facejaune.append('JRVr')
            Rcompt += 1

        else:

            facejaune.append('JRVv')
            Bcompt += 1

    if('JBR' not in facejaune):

        if JBR.getCouleur(2) == JAUNE:

            facejaune.append('JBRb')
            Fcompt += 1

        else:

            facejaune.append('JBRr')
            Rcompt += 1

    if('JBO' not in facejaune):

        if JBO.getCouleur(2) == JAUNE:

            facejaune.append('JBOb')
            Fcompt += 1

        else:

            facejaune.append('JBOo')
            Lcompt += 1

    if comptjaune != 4:

        if comptjaune == 0:

            if(Fcompt == 2 and Bcompt == 2 or
               Rcompt == 2 and Lcompt == 2):

                if Fcompt == 2:
                    reso += H

                else:
                    reso += ypConversion(H)

            else:

                if Fcompt == 2:
                    reso += yConversion(Pi)

                elif Rcompt == 2:
                    reso += y2Conversion(Pi)

                elif Lcompt == 2:
                    reso += Pi

                else:
                    reso += ypConversion(Pi)

        elif comptjaune == 1:

            if 'JVO' in facejaune:
                
                if 'JBOb' in facejaune:
                    reso += chaiseinv

                else:
                    reso += ypConversion(chaise)

            elif 'JRV' in facejaune:

                if 'JVOv' in facejaune:
                    reso += y2Conversion(chaise)
                
                else:
                    reso += ypConversion(chaiseinv)

            elif 'JBR' in facejaune:

                if 'JRVr' in facejaune:
                    reso += yConversion(chaise)

                else:
                    reso += y2Conversion(chaiseinv)

            elif 'JBO' in facejaune:

                if 'JBRb' in facejaune:
                    reso += chaise

                else:
                    reso += yConversion(chaiseinv)

        else:

            if('JVO' in facejaune and 'JRV' in facejaune):

                if 'JBRb' in facejaune:
                    reso += yConversion(frere)

                else:
                    reso += yConversion(T)

            elif('JRV' in facejaune and 'JBR' in facejaune):

                if 'JBOo' in facejaune:
                    reso += frere

                else:
                    reso += T

            elif('JBR' in facejaune and 'JBO' in facejaune):

                if 'JVOv' in facejaune:
                    reso += ypConversion(frere)

                else:
                    reso += ypConversion(T)

            elif('JVO' in facejaune and 'JBO' in facejaune):

                if 'JRVr' in facejaune:
                    reso += y2Conversion(frere)

                else:
                    reso += y2Conversion(T)

            elif('JVO' in facejaune and 'JBR' in facejaune):

                if 'JBOb' in facejaune:
                    reso += L

                else:
                    reso += y2Conversion(L)
            
            elif('JBO' in facejaune and 'JRV' in facejaune):

                if 'JBRb' in facejaune:
                    reso += ypConversion(L)

                else:
                    reso += yConversion(L)

    Resolution += reso
    print(reso)
    cube = applyMove(cube, reso)

    reso = ''

    printCube(cube)

    JVO = Coin(cube[0], cube[11], cube[18])
    JRV = Coin(cube[2], cube[38], cube[9])
    JBR = Coin(cube[8], cube[29], cube[36])
    JBO = Coin(cube[6], cube[27], cube[20])
    BOBl = Coin(cube[33], cube[26], cube[45])
    BRBl = Coin(cube[35], cube[42], cube[47])
    RVBl = Coin(cube[44], cube[15], cube[53])
    VOBl = Coin(cube[17], cube[24], cube[51])


    if(JBO.getCouleur(2) == JBR.getCouleur(2) and
       JBR.getCouleur(3) == JRV.getCouleur(2) and
       JRV.getCouleur(3) == JVO.getCouleur(2) and
       JVO.getCouleur(3) == JBO.getCouleur(3)):
        jaunef = True

    if(BOBl.getCouleur(1) == BRBl.getCouleur(1) and
       BRBl.getCouleur(2) == RVBl.getCouleur(1) and
       RVBl.getCouleur(2) == VOBl.getCouleur(1) and
       VOBl.getCouleur(2) == BOBl.getCouleur(2)):
        blancf = True

    if(colorOpposed(JRV.getCouleur(3), JVO.getCouleur(2)) and
       JBR.getCouleur(2) == JBO.getCouleur(2)):
        jauneplltB = True
    elif(colorOpposed(JBR.getCouleur(3), JRV.getCouleur(2)) and
         JBO.getCouleur(3) == JVO.getCouleur(3)):
        jauneplltR = True
    elif(colorOpposed(JBO.getCouleur(2), JBR.getCouleur(2)) and
         JVO.getCouleur(2) == JRV.getCouleur(3)):
        jauneplltF = True
    elif(colorOpposed(JVO.getCouleur(3), JBO.getCouleur(3)) and
         JRV.getCouleur(2) == JBR.getCouleur(3)):
        jauneplltL = True
    if(colorOpposed(RVBl.getCouleur(2), VOBl.getCouleur(1)) and
         BRBl.getCouleur(1) == BOBl.getCouleur(1)):
        blancplltB = True
    elif(colorOpposed(BRBl.getCouleur(2), RVBl.getCouleur(1)) and
         BOBl.getCouleur(2) == VOBl.getCouleur(2)):
        blancplltR = True
    elif(colorOpposed(BRBl.getCouleur(1), BOBl.getCouleur(1)) and
         VOBl.getCouleur(1) == RVBl.getCouleur(2)):
        blancplltF = True
    elif(colorOpposed(VOBl.getCouleur(2), BOBl.getCouleur(2)) and
         BRBl.getCouleur(2) == RVBl.getCouleur(1)):
        blancplltL = True

    if(colorOpposed(JRV.getCouleur(3), JVO.getCouleur(2)) and
       colorOpposed(JBR.getCouleur(2), JBO.getCouleur(2))):

        if JBR.getCouleur(2) == BLEU:
            jaunediagF = True

        jaunediag = True

    if(colorOpposed(RVBl.getCouleur(2), VOBl.getCouleur(1)) and
       colorOpposed(BRBl.getCouleur(1), BOBl.getCouleur(1))):

        if BOBl.getCouleur(1) == BLEU:
            blancdiagF = True

        blancdiag = True

    if(blancdiag and jaunediag):
        reso += doublediag

    elif(blancdiag and (jauneplltF or jauneplltR or jauneplltB or jauneplltL)):

        if jauneplltF:
            reso += y2Conversion(pllTdiag)
        elif jauneplltR:
            reso += ypConversion(pllTdiag)
        elif jauneplltB:
            reso += pllTdiag
        elif jauneplltL:
            reso += yConversion(pllTdiag)

    elif(jaunediag and (blancplltF or blancplltR or blancplltL or blancplltB)):

        if blancplltF:
            reso += y2Conversion(xConversion(pllTdiag))
        elif blancplltR:
            reso += ypConversion(xConversion(pllTdiag))
        elif blancplltB:
            reso += xConversion(pllTdiag)
        elif blancplltL:
            reso += yConversion(xConversion(pllTdiag))

    elif((jauneplltF or jauneplltR or jauneplltB or jauneplltL) and
          (blancplltF or blancplltR or blancplltB or blancplltL)):

        if jauneplltF:

            if blancplltF:
                reso += inv

            elif blancplltR:
                reso += ("D'" + inv)

            elif blancplltB:
                reso += ("D2" + inv)

            elif blancplltL:
                reso += ("D" + inv)

        elif jauneplltR:

            if blancplltF:
                reso += ("D" + yConversion(inv))

            elif blancplltR:
                reso += yConversion(inv)

            elif blancplltB:
                reso += ("D'" + yConversion(inv))

            elif blancplltL:
                reso += ("D2" + yConversion(inv))

        elif jauneplltB:

            if blancplltF:
                reso += ("D2" + y2Conversion(inv))

            elif blancplltR:
                reso += ("D" + y2Conversion(inv))

            elif blancplltB:
                reso += y2Conversion(inv)

            elif blancplltL:
                reso += ("D'" + y2Conversion(inv))

        elif jauneplltL:

            if blancplltF:
                reso += ("D'" + ypConversion(inv))

            elif blancplltR:
                reso += ("D2" + ypConversion(inv))

            elif blancplltB:
                reso += ("D" + ypConversion(inv))

            elif blancplltL:
                reso += ypConversion(inv)

    elif(blancf and (jauneplltF or jauneplltR or jauneplltB or jauneplltL)):

        if jauneplltF:
            reso += pllT

        elif jauneplltR:
            reso += yConversion(pllT)

        elif jauneplltB:
            reso += y2Conversion(pllT)

        elif jauneplltL:
            reso += ypConversion(pllT)

    elif(jaunef and (blancplltF or blancplltR or blancplltB or blancplltL)):

        if blancplltF:
            reso += xConversion(pllT)

        elif blancplltR:
            reso += yConversion(xConversion(pllT))

        elif blancplltB:
            reso += y2Conversion(xConversion(pllT))

        elif blancplltL:
            reso += ypConversion(xConversion(pllT))

    elif jaunediag:

        if jaudiagF:
            reso += ("U2" + diag)

        else:
            reso += diag

    elif blancdiag:

        if blancdiagF:
            reso += ("D2" + xConversion(diag))

        else:
            reso += xConversion(diag)

    '''print(jaunef,
    jauneplltF,
    jauneplltR,
    jauneplltB,
    jauneplltL,
    jaunediag,
    jaunediagF,
    jaunediagR,
    blancf,
    blancplltF,
    blancplltR,
    blancplltB,
    blancplltL,
    blancdiag,
    blancdiagR,
    blancdiagF)'''
    print(reso)
    Resolution += (reso + ' ')
    cube = applyMove(cube, reso)

    reso = ''

    if cube[27] == ROUGE:
        reso += "U'"

    if cube[27] == VERT:
        reso += "U2"

    if cube[27] == ORANGE:
        reso += "U"

    if cube[35] == ROUGE:
        reso += "D"

    if cube[35] == VERT:
        reso += "D2"

    if cube[35] == ORANGE:
        reso += "D'"

    Resolution += reso
    applyMove(cube, reso)
    print(reso)
    print(Resolution)
    printCube(cube)
    return cube
    
