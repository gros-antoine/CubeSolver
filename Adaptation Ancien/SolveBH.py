from Arete import *
from outils import *
import ast
import random
import time
import Solve2x2

f = open('BH.txt', 'r')

bh = ast.literal_eval(f.readline())

JAUNE = 0
BLEU = 1
ROUGE = 2
VERT = 3
ORANGE = 4
BLANC = 5

JV = Arete(0, 0)
JR = Arete(0, 0)
JB = Arete(0, 0)
JO = Arete(0, 0)
VO = Arete(0, 0)
RV = Arete(0, 0)
BR = Arete(0, 0)
BO = Arete(0, 0)
BBl = Arete(0, 0)
RBl = Arete(0, 0)
VBl = Arete(0, 0)
OBl = Arete(0, 0)

Aretes = ['JV', 'JO', 'JB', 'BO', 'BR', 'BBl', 'RV', 'RBl', 'VO', 'OBl', 'VBl']

buf = False

resoInter = ''

Resolution = ''
reso = ''

def setCouleur(face, couleur):
    

def randomCube(c):

    '''for i in [3,8,3,1,12,11,12,8,12,1,13,10,14,3,11,4,11,11,5,17,6,7,5,14]:
        numberMove(i, c)'''
    
    mel = ""
    
    for i in range(24):

        r = random.randint(0, 17)
        mel += str(r) + " "
        numberMove(r, c)

    return mel

def bufProcessing1():

    global reso
    global Aretes
    global bh
    global JV
    global JR
    global JB
    global JO
    global VO
    global RV
    global BR
    global BO
    global BBl
    global RBl
    global VBl
    global OBl
    
    if 'JV' in Aretes:
        
        c1 = JV.getCouleur(1)
        c2 = JV.getCouleur(2)
        reso += bh[3*100 + c1*10 + c2]

    elif 'JO' in Aretes:

        c1 = JO.getCouleur(1)
        c2 = JO.getCouleur(2)
        reso += bh[4*100 + c1*10 + c2]

    elif 'JB' in Aretes:

        c1 = JB.getCouleur(1)
        c2 = JB.getCouleur(2)
        reso += bh[1*100 + c1*10 + c2]

    elif 'BO' in Aretes:

        c1 = BO.getCouleur(1)
        c2 = BO.getCouleur(2)
        reso += bh[14*100 + c1*10 + c2]

    elif 'BR' in Aretes:

        c1 = BR.getCouleur(1)
        c2 = BR.getCouleur(2)
        reso += bh[12*100 + c1*10 + c2]

    elif 'BBl' in Aretes:

        c1 = BBl.getCouleur(1)
        c2 = BBl.getCouleur(2)
        reso += bh[15*100 + c1*10 + c2]

    elif 'RV' in Aretes:

        c1 = RV.getCouleur(1)
        c2 = RV.getCouleur(2)
        reso += bh[23*100 + c1*10 + c2]

    elif 'RBl' in Aretes:

        c1 = RBl.getCouleur(1)
        c2 = RBl.getCouleur(2)
        reso += bh[25*100 + c1*10 + c2]

    elif 'VO' in Aretes:

        c1 = VO.getCouleur(1)
        c2 = VO.getCouleur(2)
        reso += bh[34*100 + c1*10 + c2]

    elif 'OBl' in Aretes:

        c1 = OBl.getCouleur(1)
        c2 = OBl.getCouleur(2)
        reso += bh[45*100 + c1*10 + c2]

    elif 'VBl' in Aretes:

        c1 = VBl.getCouleur(1)
        c2 = VBl.getCouleur(2)
        reso += bh[35*100 + c1*10 + c2]

    if((c1 == JAUNE or c1 == VERT) and (c2 == JAUNE or c2 == VERT)):
        Aretes.remove('JV')
    elif((c1 == JAUNE or c1 == ROUGE) and (c2 == JAUNE or c2 == ROUGE)):
        Aretes.remove('JR')
    elif((c1 == JAUNE or c1 == BLEU) and (c2 == JAUNE or c2 == BLEU)):
        Aretes.remove('JB')
    elif((c1 == JAUNE or c1 == ORANGE) and (c2 == JAUNE or c2 == ORANGE)):
        Aretes.remove('JO')
    elif((c1 == VERT or c1 == ORANGE) and (c2 == VERT or c2 == ORANGE)):
        Aretes.remove('VO')
    elif((c1 == ROUGE or c1 == VERT) and (c2 == ROUGE or c2 == VERT)):
        Aretes.remove('RV')
    elif((c1 == BLEU or c1 == ROUGE) and (c2 == BLEU or c2 == ROUGE)):
        Aretes.remove('BR')
    elif((c1 == BLEU or c1 == ORANGE) and (c2 == BLEU or c2 == ORANGE)):
        Aretes.remove('BO')
    elif((c1 == BLEU or c1 == BLANC) and (c2 == BLEU or c2 == BLANC)):
        Aretes.remove('BBl')
    elif((c1 == ROUGE or c1 == BLANC) and (c2 == ROUGE or c2 == BLANC)):
        Aretes.remove('RBl')
    elif((c1 == VERT or c1 == BLANC) and (c2 == VERT or c2 == BLANC)):
        Aretes.remove('VBl')
    elif((c1 == ORANGE or c1 == BLANC) and (c2 == ORANGE or c2 == BLANC)):
        Aretes.remove('OBl')

def bufProcessing2():

    global reso
    global buf
    global Aretes
    global bh
    global JV
    global JR
    global JB
    global JO
    global VO
    global RV
    global BR
    global BO
    global BBl
    global RBl
    global VBl
    global OBl

    ALibre = 0
    
    buf = False

    c1 = JR.getCouleur(1)
    c2 = JR.getCouleur(2)

    if((c1 == JAUNE or c1 == VERT) and (c2 == JAUNE or c2 == VERT)):

        Aretes.remove('JV')
        ALibre = c1*10 + c2

    elif((c1 == JAUNE or c1 == ORANGE) and (c2 == JAUNE or c2 == ORANGE)):

        Aretes.remove('JO')
        ALibre = c1*10 + c2
    
    elif((c1 == JAUNE or c1 == BLEU) and (c2 == JAUNE or c2 == BLEU)):

        Aretes.remove('JB')
        ALibre = c1*10 + c2

    elif((c1 == BLEU or c1 == ORANGE) and (c2 == BLEU or c2 == ORANGE)):

        Aretes.remove('BO')
        ALibre = c1*10 + c2

    elif((c1 == BLEU or c1 == ROUGE) and (c2 == BLEU or c2 == ROUGE)):

        Aretes.remove('BR')
        ALibre = c1*10 + c2

    elif((c1 == BLEU or c1 == BLANC) and (c2 == BLEU or c2 == BLANC)):

        Aretes.remove('BBl')
        ALibre = c1*10 + c2

    elif((c1 == ROUGE or c1 == VERT) and (c2 == ROUGE or c2 == VERT)):

        Aretes.remove('RV')
        ALibre = c1*10 + c2

    elif((c1 == ROUGE or c1 == BLANC) and (c2 == ROUGE or c2 == BLANC)):

        Aretes.remove('RBl')
        ALibre = c1*10 + c2

    elif((c1 == VERT or c1 == ORANGE) and (c2 == VERT or c2 == ORANGE)):

        Aretes.remove('VO')
        ALibre = c1*10 + c2

    elif((c1 == ORANGE or c1 == BLANC) and (c2 == ORANGE or c2 == BLANC)):

        Aretes.remove('OBl')
        ALibre = c1*10 + c2

    elif((c1 == VERT or c1 == BLANC) and (c2 == VERT or c2 == BLANC)):

        Aretes.remove('VBl')
        ALibre = c1*10 + c2

    if 'JV' in Aretes and ALibre is not 3 and ALibre is not 30:
        reso += bh[ALibre*100 + 3]
    elif 'JO' in Aretes and ALibre is not 4 and ALibre is not 40:
        reso += bh[ALibre*100 + 4]
    elif 'JB' in Aretes and ALibre is not 1 and ALibre is not 10:
        reso += bh[ALibre*100 + 1]
    elif 'BO' in Aretes and ALibre is not 14 and ALibre is not 41:
        reso += bh[ALibre*100 + 14]
    elif 'BR' in Aretes and ALibre is not 12 and ALibre is not 21:
        reso += bh[ALibre*100 + 12]
    elif 'BBl' in Aretes and ALibre is not 15 and ALibre is not 51:
        reso += bh[ALibre*100 + 15]
    elif 'RV' in Aretes and ALibre is not 23 and ALibre is not 32:
        reso += bh[ALibre*100 + 23]
    elif 'RBl' in Aretes and ALibre is not 25 and ALibre is not 52:
        reso += bh[ALibre*100 + 25]
    elif 'VO' in Aretes and ALibre is not 34 and ALibre is not 43:
        reso += bh[ALibre*100 + 34]
    elif 'OBl' in Aretes and ALibre is not 45 and ALibre is not 54:
        reso += bh[ALibre*100 + 45]
    elif 'VBl' in Aretes and ALibre is not 35 and ALibre is not 53:
        reso += bh[ALibre*100 + 35]


'''B U' B D F U' L B D' R D' L B R2 F' U' R2 F L' B U' R' U' R' D' '''

JVLibre = True
JOLibre = True
JBLibre = True
JRLibre = True

resoInter = ''

Resolution = ''
reso = ''

buf = False

cube = [0,0,0,0,0,0,0,0,0,
        3,3,3,3,3,3,3,3,3,
        4,4,4,4,4,4,4,4,4,
        1,1,1,1,1,1,1,1,1,
        2,2,2,2,2,2,2,2,2,
        5,5,5,5,5,5,5,5,5]

melange = randomCube(cube)
print(melange)

cube = Solve2x2.solve(cube)

printCube(cube)

Aretes = ['JV', 'JO', 'JB', 'BO', 'BR', 'BBl', 'RV', 'RBl', 'VO', 'OBl', 'VBl']
AretesDesor = []

JV = Arete(cube[1], cube[10])
JR = Arete(cube[5], cube[37])
JB = Arete(cube[7], cube[28])
JO = Arete(cube[3], cube[19])
VO = Arete(cube[14], cube[21])
RV = Arete(cube[41], cube[12])
BR = Arete(cube[32], cube[39])
BO = Arete(cube[30], cube[23])
BBl = Arete(cube[34], cube[46])
RBl = Arete(cube[43], cube[50])
VBl = Arete(cube[16], cube[52])
OBl = Arete(cube[25], cube[48])

if JV.contient(JAUNE, VERT):

    Aretes.remove('JV')

    if JV.getCouleur(1) == VERT:

        AretesDesor.append('JV')
        JVLibre = False

if JO.contient(JAUNE, ORANGE):

    Aretes.remove('JO')

    if JO.getCouleur(1) == ORANGE:

        AretesDesor.append('JO')
        JOLibre = False

if JB.contient(JAUNE, BLEU):

    Aretes.remove('JB')

    if JB.getCouleur(1) == BLEU:

        AretesDesor.append('JB')
        JBLibre = False

if BO.contient(BLEU, ORANGE):

    Aretes.remove('BO')

    if BO.getCouleur(1) == ORANGE:
        AretesDesor.append('BO')

if BR.contient(BLEU, ROUGE):

    Aretes.remove('BR')

    if BR.getCouleur(1) == ROUGE:
        AretesDesor.append('BR')

if BBl.contient(BLEU, BLANC):

    Aretes.remove('BBl')

    if BBl.getCouleur(1) == BLANC:
        AretesDesor.append('BBl')

if RV.contient(ROUGE, VERT):

    Aretes.remove('RV')

    if RV.getCouleur(1) == VERT:
        AretesDesor.append('RV')

if RBl.contient(ROUGE, BLANC):

    Aretes.remove('RBl')

    if RBl.getCouleur(1) == BLANC:
        AretesDesor.append('RBl')

if VO.contient(VERT, ORANGE):

    Aretes.remove('VO')

    if VO.getCouleur(1) == ORANGE:
        AretesDesor.append('VO')

if OBl.contient(ORANGE, BLANC):

    Aretes.remove('OBl')

    if OBl.getCouleur(1) == BLANC:
        AretesDesor.append('OBl')

if VBl.contient(VERT, BLANC):

    Aretes.remove('VBl')

    if VBl.getCouleur(1) == BLANC:
        AretesDesor.append('VBl')

printCube(cube)

while Aretes:
    
    reso = ""
    c1, c2, c3, c4 = None, None, None, None
    
    JV = Arete(cube[1], cube[10])
    JR = Arete(cube[5], cube[37])
    JB = Arete(cube[7], cube[28])
    JO = Arete(cube[3], cube[19])
    VO = Arete(cube[14], cube[21])
    RV = Arete(cube[41], cube[12])
    BR = Arete(cube[32], cube[39])
    BO = Arete(cube[30], cube[23])
    BBl = Arete(cube[34], cube[46])
    RBl = Arete(cube[43], cube[50])
    VBl = Arete(cube[16], cube[52])
    OBl = Arete(cube[25], cube[48])

    c1 = JR.getCouleur(1)
    c2 = JR.getCouleur(2)

    if((c1 == JAUNE or c1 == VERT) and (c2 == JAUNE or c2 == VERT)):

        Aretes.remove('JV')
        c3 = JV.getCouleur(1)
        c4 = JV.getCouleur(2)

        if((c3 == JAUNE or c3 == ROUGE) and (c4 == JAUNE or c4 == ROUGE)):

            buf = True
            Aretes.append('JV')

    elif((c1 == JAUNE or c1 == BLEU) and (c2 == JAUNE or c2 == BLEU)):

        Aretes.remove('JB')
        c3 = JB.getCouleur(1)
        c4 = JB.getCouleur(2)

        if((c3 == JAUNE or c3 == ROUGE) and (c4 == JAUNE or c4 == ROUGE)):

            buf = True
            Aretes.append('JB')

    elif((c1 == JAUNE or c1 == ORANGE) and (c2 == JAUNE or c2 == ORANGE)):

        Aretes.remove('JO')
        c3 = JO.getCouleur(1)
        c4 = JO.getCouleur(2)

        if((c3 == JAUNE or c3 == ROUGE) and (c4 == JAUNE or c4 == ROUGE)):

            buf = True
            Aretes.append('JO')

    elif((c1 == VERT or c1 == ORANGE) and (c2 == VERT or c2 == ORANGE)):

        Aretes.remove('VO')
        c3 = VO.getCouleur(1)
        c4 = VO.getCouleur(2)

        if((c3 == JAUNE or c3 == ROUGE) and (c4 == JAUNE or c4 == ROUGE)):

            buf = True
            Aretes.append('VO')

    elif((c1 == ROUGE or c1 == VERT) and (c2 == ROUGE or c2 == VERT)):

        Aretes.remove('RV')
        c3 = RV.getCouleur(1)
        c4 = RV.getCouleur(2)

        if((c3 == JAUNE or c3 == ROUGE) and (c4 == JAUNE or c4 == ROUGE)):

            buf = True
            Aretes.append('RV')

    elif((c1 == BLEU or c1 == ROUGE) and (c2 == BLEU or c2 == ROUGE)):

        Aretes.remove('BR')
        c3 = BR.getCouleur(1)
        c4 = BR.getCouleur(2)

        if((c3 == JAUNE or c3 == ROUGE) and (c4 == JAUNE or c4 == ROUGE)):

            buf = True
            Aretes.append('BR')

    elif((c1 == BLEU or c1 == ORANGE) and (c2 == BLEU or c2 == ORANGE)):

        Aretes.remove('BO')
        c3 = BO.getCouleur(1)
        c4 = BO.getCouleur(2)

        if((c3 == JAUNE or c3 == ROUGE) and (c4 == JAUNE or c4 == ROUGE)):

            buf = True
            Aretes.append('BO')

    elif((c1 == BLEU or c1 == BLANC) and (c2 == BLEU or c2 == BLANC)):

        Aretes.remove('BBl')
        c3 = BBl.getCouleur(1)
        c4 = BBl.getCouleur(2)

        if((c3 == JAUNE or c3 == ROUGE) and (c4 == JAUNE or c4 == ROUGE)):

            buf = True
            Aretes.append('BBl')

    elif((c1 == ROUGE or c1 == BLANC) and (c2 == ROUGE or c2 == BLANC)):

        Aretes.remove('RBl')
        c3 = RBl.getCouleur(1)
        c4 = RBl.getCouleur(2)

        if((c3 == JAUNE or c3 == ROUGE) and (c4 == JAUNE or c4 == ROUGE)):

            buf = True
            Aretes.append('RBl')

    elif((c1 == VERT or c1 == BLANC) and (c2 == VERT or c2 == BLANC)):

        Aretes.remove('VBl')
        c3 = VBl.getCouleur(1)
        c4 = VBl.getCouleur(2)

        if((c3 == JAUNE or c3 == ROUGE) and (c4 == JAUNE or c4 == ROUGE)):

            buf = True
            Aretes.append('VBl')

    elif((c1 == ORANGE or c1 == BLANC) and (c2 == ORANGE or c2 == BLANC)):

        Aretes.remove('OBl')
        c3 = OBl.getCouleur(1)
        c4 = OBl.getCouleur(2)

        if((c3 == JAUNE or c3 == ROUGE) and (c4 == JAUNE or c4 == ROUGE)):

            buf = True
            Aretes.append('OBl')

    elif not buf:
        bufProcessing1()

    if buf:
        bufProcessing2()
        
    if((c3 == JAUNE or c3 == VERT) and (c4 == JAUNE or c4 == VERT)):
        Aretes.remove('JV')
    elif((c3 == JAUNE or c3 == BLEU) and (c4 == JAUNE or c4 == BLEU)):
        Aretes.remove('JB')
    elif((c3 == JAUNE or c3 == ORANGE) and (c4 == JAUNE or c4 == ORANGE)):
        Aretes.remove('JO')
    elif((c3 == VERT or c3 == ORANGE) and (c4 == VERT or c4 == ORANGE)):
        Aretes.remove('VO')
    elif((c3 == ROUGE or c3 == VERT) and (c4 == ROUGE or c4 == VERT)):
        Aretes.remove('RV')
    elif((c3 == BLEU or c3 == ROUGE) and (c4 == BLEU or c4 == ROUGE)):
        Aretes.remove('BR')
    elif((c3 == BLEU or c3 == ORANGE) and (c4 == BLEU or c4 == ORANGE)):
        Aretes.remove('BO')
    elif((c3 == BLEU or c3 == BLANC) and (c4 == BLEU or c4 == BLANC)):
        Aretes.remove('BBl')
    elif((c3 == ROUGE or c3 == BLANC) and (c4 == ROUGE or c4 == BLANC)):
        Aretes.remove('RBl')
    elif((c3 == VERT or c3 == BLANC) and (c4 == VERT or c4 == BLANC)):
        Aretes.remove('VBl')
    elif((c3 == ORANGE or c3 == BLANC) and (c4 == ORANGE or c4 == BLANC)):
        Aretes.remove('OBl')
        
    try:
        c = c1 * 10**3 + c2 * 10**2 + c3 * 10 + c4
        reso = bh[c]
    except:
        pass
    
    print(reso)
    cube = applyMove(cube, reso)
    Resolution += reso

reso = ''

JV = Arete(cube[1], cube[10])
JR = Arete(cube[5], cube[37])
JB = Arete(cube[7], cube[28])
JO = Arete(cube[3], cube[19])
VO = Arete(cube[14], cube[21])
RV = Arete(cube[41], cube[12])
BR = Arete(cube[32], cube[39])
BO = Arete(cube[30], cube[23])
BBl = Arete(cube[34], cube[46])
RBl = Arete(cube[43], cube[50])
VBl = Arete(cube[16], cube[52])
OBl = Arete(cube[25], cube[48])

print(AretesDesor)

if(JR.getCouleur(1) == ROUGE and JR.getCouleur(2) == JAUNE and 'JR' not in AretesDesor):

    AretesDesor.append('JR')
    JRLibre = False

if(JV.getCouleur(1) == VERT and JV.getCouleur(2) == JAUNE and 'JV' not in AretesDesor):

    AretesDesor.append('JV')
    JVLibre = False

if(JO.getCouleur(1) == ORANGE and JO.getCouleur(2) == JAUNE and 'JO' not in AretesDesor):

    AretesDesor.append('JO')
    JOLibre = False
    
if(JB.getCouleur(1) == BLEU and JB.getCouleur(2) == JAUNE and 'JB' not in AretesDesor):

    AretesDesor.append('JB')
    JBLibre = False

if(BO.getCouleur(1) == ORANGE and BO.getCouleur(2) == BLEU and 'BO' not in AretesDesor):
    AretesDesor.append('BO')

if(BR.getCouleur(1) == ROUGE and BR.getCouleur(2) == BLEU and 'BR' not in AretesDesor):
    AretesDesor.append('BR')

if(BBl.getCouleur(1) == BLANC and BBl.getCouleur(2) == BLEU and 'BBl' not in AretesDesor):
    AretesDesor.append('BBl')

if(RV.getCouleur(1) == VERT and RV.getCouleur(2) == ROUGE and 'RV' not in AretesDesor):
    AretesDesor.append('RV')

if(RBl.getCouleur(1) == BLANC and RBl.getCouleur(2) == ROUGE and 'RBl' not in AretesDesor):
    AretesDesor.append('RBl')

if(VO.getCouleur(1) == ORANGE and VO.getCouleur(2) == VERT and 'VO' not in AretesDesor):
    AretesDesor.append('VO')

if(OBl.getCouleur(1) == BLANC and OBl.getCouleur(2) == ORANGE and 'OBl' not in AretesDesor):
    AretesDesor.append('OBl')

if(VBl.getCouleur(1) == BLANC and VBl.getCouleur(2) == VERT and 'VBl' not in AretesDesor):
    AretesDesor.append('VBl')

print(AretesDesor)

if('JB' in AretesDesor and 'JV' in AretesDesor):

    reso += "M'UM'UM'U2MUMUMU2"
    AretesDesor.remove('JB')
    AretesDesor.remove('JV')
    JBLibre = True
    JVlibre = True

if('JR' in AretesDesor and 'JO' in AretesDesor):

    reso += "S'US'US'U2SUSUSU2"
    AretesDesor.remove('JR')
    AretesDesor.remove('JO')
    JRLibre = True
    JOlibre = True

if('JB' in AretesDesor and 'BBl' in AretesDesor):

    reso += "M'FM'FM'F2MFMFMF2"
    AretesDesor.remove('JB')
    AretesDesor.remove('BBl')
    JBLibre = True

if('BO' in AretesDesor and 'BR' in AretesDesor):

    reso += "EFEFMEF2E'FE'FE'F2"
    AretesDesor.remove('BO')
    AretesDesor.remove('BR')

if('JR' in AretesDesor and 'RBl' in AretesDesor):

    reso += "SRSRSR2S'RS'RS'R2"
    AretesDesor.remove('JR')
    AretesDesor.remove('RBl')
    JRLibre = True

if('BR' in AretesDesor and 'RV' in AretesDesor):

    reso += "ERERER2E'RE'RE'R2"
    AretesDesor.remove('BR')
    AretesDesor.remove('RV')


if('JV' in AretesDesor and 'VBl' in AretesDesor):

    reso += "M'BM'BM'B2MBMBMB2"
    AretesDesor.remove('JV')
    AretesDesor.remove('VBl')
    JVLibre = True

if('RV' in AretesDesor and 'VO' in AretesDesor):

    reso += "EBEBEB2E'BE'BE'B2"
    AretesDesor.remove('RV')
    AretesDesor.remove('VO')

if('JO' in AretesDesor and 'OBl' in AretesDesor):

    reso += "SLSLSL2S'LS'LS'L2"
    AretesDesor.remove('JO')
    AretesDesor.remove('OBl')
    JOLibre = True

if('VO' in AretesDesor and 'BO' in AretesDesor):

    reso += "ELELEL2E'LE'LE'L2"
    AretesDesor.remove('VO')
    AretesDesor.remove('BO')

if('BBl' in AretesDesor and 'VBl' in AretesDesor):

    reso += "MDMDMD2M'DM'DM'D2"
    AretesDesor.remove('BBl')
    AretesDesor.remove('VBl')

if('OBl' in AretesDesor and 'RBl' in AretesDesor):

    reso += "SDSDSD2S'DS'DS'D2"
    AretesDesor.remove('OBl')
    AretesDesor.remove('RBl')


if('JB' in AretesDesor and 'JR' in AretesDesor):

    reso += "RBMUMUMU2M'UM'UM'U2B'R'"
    AretesDesor.remove('JB')
    AretesDesor.remove('JR')
    JBLibre = True
    JRLibre = True

if('JB' in AretesDesor and 'JO' in AretesDesor):

    reso += "L'B'MUMUMU2M'UM'UM'U2BL"
    AretesDesor.remove('JB')
    AretesDesor.remove('JO')
    JBLibre = True
    JOLibre = True

if('JV' in AretesDesor and 'JR' in AretesDesor):

    reso += "R'F'MUMUMU2M'UM'UM'U2FR"
    AretesDesor.remove('JV')
    AretesDesor.remove('JR')
    JVLibre = True
    JRLibre = True

if('JV' in AretesDesor and 'JO' in AretesDesor):

    reso += "LFMUMUMU2M'UM'UM'U2F'L'"
    AretesDesor.remove('JV')
    AretesDesor.remove('JO')
    JVLibre = True
    JOLibre = True

if('BBl' in AretesDesor and 'BR' in AretesDesor):

    reso += "RUMFMFMF2M'FM'FM'F2U'R'"
    AretesDesor.remove('BBl')
    AretesDesor.remove('BR')

if('BBl' in AretesDesor and 'BO' in AretesDesor):

    reso += "L'U'MFMFMF2M'FM'FM'F2UL"
    AretesDesor.remove('BBl')
    AretesDesor.remove('BO')

if('JB' in AretesDesor and 'BR' in AretesDesor):

    reso += "R'D'MFMFMF2M'FM'FM'F2DR"
    AretesDesor.remove('JB')
    AretesDesor.remove('BR')
    JBLibre = True

if('JB' in AretesDesor and 'BO' in AretesDesor):

    reso += "LDMFMFMF2M'FM'FM'F2D'L'"
    AretesDesor.remove('JB')
    AretesDesor.remove('BO')
    JBLibre = True

if('RBl' in AretesDesor and 'RV' in AretesDesor):

    reso += "BUSRSRSR2S'RS'RS'R2U'B'"
    AretesDesor.remove('RBl')
    AretesDesor.remove('RV')

if('RBl' in AretesDesor and 'BR' in AretesDesor):

    reso += "F'U'SRSRSR2S'RS'RS'R2UF"
    AretesDesor.remove('RBl')
    AretesDesor.remove('BR')

if('JR' in AretesDesor and 'RV' in AretesDesor):

    reso += "B'D'SRSRSR2S'RS'RS'R2DB"
    AretesDesor.remove('JR')
    AretesDesor.remove('RV')
    JRLibre = True

if('JR' in AretesDesor and 'BR' in AretesDesor):

    reso += "FDSRSRSR2S'RS'RS'R2D'F'"
    AretesDesor.remove('JR')
    AretesDesor.remove('RBR')
    JRLibre = True

if('VBl' in AretesDesor and 'VO' in AretesDesor):

    reso += "LUMBMBMB2M'BM'BM'B2U'L'"
    AretesDesor.remove('VBl')
    AretesDesor.remove('VO')

if('VBl' in AretesDesor and 'RV' in AretesDesor):

    reso += "R'U'MBMBMB2M'BM'BM'B2UR"
    AretesDesor.remove('VBl')
    AretesDesor.remove('RV')

if('JV' in AretesDesor and 'VO' in AretesDesor):

    reso += "L'D'MBMBMB2M'BM'BM'B2DL"
    AretesDesor.remove('JV')
    AretesDesor.remove('VO')
    JVLibre = True

if('JV' in AretesDesor and 'RV' in AretesDesor):

    reso += "RDMBMBMB2M'BM'BM'B2D'R'"
    AretesDesor.remove('JV')
    AretesDesor.remove('RV')
    JVLibre = True

if('OBl' in AretesDesor and 'BO' in AretesDesor):

    reso += "FUSLSLSL2S'LS'LS'L2U'F'"
    AretesDesor.remove('OBl')
    AretesDesor.remove('BO')

if('OBl' in AretesDesor and 'VO' in AretesDesor):

    reso += "B'U'SLSLSL2S'LS'LS'L2UB"
    AretesDesor.remove('OBl')
    AretesDesor.remove('VO')

if('JO' in AretesDesor and 'BO' in AretesDesor):

    reso += "F'D'SLSLSL2S'LS'LS'L2DF"
    AretesDesor.remove('JO')
    AretesDesor.remove('BO')
    JOLibre = True

if('JO' in AretesDesor and 'VO' in AretesDesor):

    reso += "BDSLSLSL2S'LS'LS'L2D'B'"
    AretesDesor.remove('JO')
    AretesDesor.remove('VO')
    JOLibre = True

if('VBl' in AretesDesor and 'RBl' in AretesDesor):

    reso += "RFMDMDMD2M'DM'DM'D2F'R'"
    AretesDesor.remove('VBl')
    AretesDesor.remove('RBl')

if('VBl' in AretesDesor and 'oBl' in AretesDesor):

    reso += "L'F'MDMDMD2M'DM'DM'D2FL"
    AretesDesor.remove('VBl')
    AretesDesor.remove('OBl')

if('VBl' in AretesDesor and 'OBl' in AretesDesor):

    reso += "L'F'MDMDMD2M'DM'DM'D2FL"
    AretesDesor.remove('VBl')
    AretesDesor.remove('OBl')

if('BBl' in AretesDesor and 'RBl' in AretesDesor):

    reso += "R'B'MDMDMD2M'DM'DM'D2BR"
    AretesDesor.remove('BBl')
    AretesDesor.remove('RBl')

if('BBl' in AretesDesor and 'OBl' in AretesDesor):

    reso += "LBMDMDMD2M'DM'DM'D2B'L'"
    AretesDesor.remove('BBl')
    AretesDesor.remove('OBl')

if 'BR' in AretesDesor:

    if not JOLibre:

        reso += resoInter + "RSUSUSU2S'US'US'U2R'" + invMove(resoInter)
        AretesDesor.remove('JO')
        AretesDesor.remove('BR')
        JOLibre = True
        resoInter = ''

    elif not JVLibre:

        reso += resoInter + "F'MUMUMU2M'UM'UM'U2F" + invMove(resoInter)
        AretesDesor.remove('JV')
        AretesDesor.remove('BR')
        JOLibre = True
        resoInter = ''

    else:

        resoInter += "R"
        AretesDesor.remove('BR')
        JRLibre = False

if 'RV' in AretesDesor:

    if not JBLibre:

        reso += resoInter + "BMUMUMU2M'UM'UM'U2B'" + invMove(resoInter)
        AretesDesor.remove('JB')
        AretesDesor.remove('RV')
        JBLibre = True
        resoInter = ''

    elif not JOLibre:

        reso += resoInter + "R'SUSUSU2S'US'US'U2R" + invMove(resoInter)
        AretesDesor.remove('JO')
        AretesDesor.remove('RV')
        JOLibre = True
        resoInter = ''

    else:

        resoInter += "R'"
        AretesDesor.remove('RV')
        JRLibre = False

if 'VO' in AretesDesor:

    if not JBLibre:

        reso += resoInter + "B'MUMUMU2M'UM'UM'U2B" + invMove(resoInter)
        AretesDesor.remove('JB')
        AretesDesor.remove('VO')
        JBLibre = True
        resoInter = ''

    elif not JBLibre:

        reso += resoInter + "LSUSUSU2S'US'US'U2L'" + invMove(resoInter)
        AretesDesor.remove('JR')
        AretesDesor.remove('VO')
        JRLibre = True
        resoInter = ''

    else:

        resoInter += "L"
        AretesDesor.remove('VO')
        JOLibre = False

if 'BO' in AretesDesor:

    if not JVLibre:

        reso += resoInter + "FMUMUMU2M'UM'UM'U2F'" + invMove(resoInter)
        AretesDesor.remove('JV')
        AretesDesor.remove('VO')
        JVLibre = True
        resoInter = ''

    elif not JRLibre:

        reso += resoInter + "L'SUSUSU2S'US'US'U2L" + invMove(resoInter)
        AretesDesor.remove('JR')
        AretesDesor.remove('VO')
        JRLibre = True
        resoInter = ''

    else:

        resoInter += "L'"
        AretesDesor.remove('BO')
        JOLibre = False

if 'BBl' in AretesDesor:

    if not JVLibre:

        reso += resoInter + "F2MUMUMU2M'UM'UM'U2F2" + invMove(resoInter)
        AretesDesor.remove('JV')
        AretesDesor.remove('BBl')
        JVLibre = True
        resoInter = ''

    elif not JRLibre:

        reso += resoInter + "D'L2SUSUSU2S'US'US'U2L2D" + invMove(resoInter)
        AretesDesor.remove('JR')
        AretesDesor.remove('BBl')
        JRLibre = True
        resoInter = ''

    elif not JOLibre:

        reso += resoInter + "DR2SUSUSU2S'US'US'U2R2D'" + invMove(resoInter)
        AretesDesor.remove('JO')
        AretesDesor.remove('BBl')
        JRLibre = True
        resoInter = ''

    else:

        resoInter += "F2"
        AretesDesor.remove('BBl')
        JBLibre = False

if 'RBl' in AretesDesor:

    if not JOLibre:

        reso += resoInter + "R2SUSUSU2S'US'US'U2R2" + invMove(resoInter)
        AretesDesor.remove('JO')
        AretesDesor.remove('RBl')
        JOLibre = True
        resoInter = ''

    elif not JVLibre:

        reso += resoInter + "D'F2MUMUMU2M'UM'UM'U2F2D" + invMove(resoInter)
        AretesDesor.remove('JV')
        AretesDesor.remove('RBl')
        JVLibre = True
        resoInter = ''

    elif not JBLibre:

        reso += resoInter + "DB2MUMUMU2M'UM'UM'U2B2D'" + invMove(resoInter)
        AretesDesor.remove('JB')
        AretesDesor.remove('RBl')
        JBLibre = True
        resoInter = ''

    else:

        resoInter += "R2"
        AretesDesor.remove('RBl')
        JRLibre = False

if 'VBl' in AretesDesor:

    if not JBLibre:

        reso += resoInter + "B2MUMUMU2M'UM'UM'U2B2" + invMove(resoInter)
        AretesDesor.remove('JB')
        AretesDesor.remove('VBl')
        JBLibre = True
        resoInter = ''

    elif not JRLibre:

        reso += resoInter + "DL2SUSUSU2S'US'US'U2L2D'" + invMove(resoInter)
        AretesDesor.remove('JR')
        AretesDesor.remove('VBl')
        JRLibre = True
        resoInter = ''

    elif not JOLibre:

        reso += resoInter + "DB2MUMUMU2M'UM'UM'U2B2D'" + invMove(resoInter)
        AretesDesor.remove('JO')
        AretesDesor.remove('VBl')
        JOLibre = True
        resoInter = ''

    else:

        resoInter += "B2"
        AretesDesor.remove('VBl')
        JVLibre = False

if 'OBl' in AretesDesor:

    if not JRLibre:

        reso += resoInter + "L2SUSUSU2S'US'US'U2L2" + invMove(resoInter)
        AretesDesor.remove('JR')
        AretesDesor.remove('OBl')
        JRLibre = True
        resoInter = ''

    elif not JBLibre:

        reso += resoInter + "D'B2MUMUMU2M'UM'UM'U2B2D" + invMove(resoInter)
        AretesDesor.remove('JB')
        AretesDesor.remove('OBl')
        JBLibre = True
        resoInter = ''

    elif not JVLibre:

        reso += resoInter + "DF2MUMUSMU2M'UM'UM'U2F2D'" + invMove(resoInter)
        AretesDesor.remove('JV')
        AretesDesor.remove('OBl')
        JVLibre = True
        resoInter = ''

Resolution += reso
cube = applyMove(cube, reso)
print(Resolution)
printCube(cube)
        
