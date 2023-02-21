import random

#initialisation des variables
colonnes, lignes = 2, 2
nbCell = 0

#génère un tableau de 10 * 10
tableau = [[random.randint(0,1) for i in range(colonnes)] for j in range(lignes)]
tableauTemp =[]

#afficher le tableau
def affichTab(nbColones,nbLigne):
    for i in range(colonnes):
        for j in range(lignes):
            if (tableau[i][j] == 0):
                print(' ',end='')
            else :
                print('1',end='')    
        print()

#vérifie les voisins d'une cellule 
for x in range(colonnes):
    for y in range(lignes):
        for i in range(-1,2,1):
            for j in range(-1,2,1):
                if(i != 0 and j != 0):
                    if (( x + i >= 0) and ( x + i < lignes) and (y + j >= 0) and ( y + j < colonnes)):
                        if (tableau[x + i][y + j] == 1 ):
                            nbCell += 1
        print(nbCell)
        nbCell = 0

tableauTemp = tableau

