import os
from random import randint

nmaps = list()
for nom_fichier in os.listdir("cartes"):
    if nom_fichier.endswith(".txt"):
        nmaps.append(nom_fichier)

params = nmaps[randint(0, len(nmaps)-1)], 'r'
maps_dir = str(os.getcwd() + "/cartes")
os.chdir(maps_dir)

monfichier = open(*params)
chaine = monfichier.read()
tableau = chaine.split('\n')

def listeDouble(hor, col):
    malist = []
    i1 = 0
    i2 = 0
    while i1 < hor:
        malist.append([])
        i1 += 1
    i1 = 0
    while i1 < hor:
        maPhrase = str(i1+1) + " - " + str(i2+1)
        malist[i1].append([maPhrase])
        i2 += 1
        if len(malist[i1]) == col:
            i1+=1
            i2 = 0
    return malist

grille = listeDouble(len(tableau[0]),len(tableau))
ligne = list()

for elt1 in range(len(tableau[0])):
    for elt in range(len(tableau)): 
        ligne.append(tableau[elt][elt1])
        if tableau[elt][elt1] == "X":
            position = elt1, elt
    grille[elt1] = ligne
    ligne = list()