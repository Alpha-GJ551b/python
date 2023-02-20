import random

#initialisation des variables
colonnes, lignes = 10, 10

#génère un tableau de 10 * 10
tableau = [[random.randint(0,1) for i in range(colonnes)] for j in range(lignes)]

#afficher le tableau
for i in range(colonnes):
    for j in range(lignes):
        if (tableau[i][j]== 0):
            print(' ',end='')
        else :
            print('1',end='')    
    print()
    
#vérifie les voisins d'une cellule 


#while true :
    

