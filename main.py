from maps import grille, position
from fonctions import *
import pickle, os

if 'save' in os.listdir():
    with open('save', 'rb') as monFichier:
        monDepickler = pickle.Unpickler(monFichier)
        game = monDepickler.load()
else:
    game = Robot(position, grille)
print(game)

while game.old != 'U':
    ask = input('>>> ')
    if len(ask) >=  2:
        nb = int(ask[1:])
    else:
        nb = 1
    for i in range(nb):
        if ask[0] == 'n':
            game.nord()
        elif ask[0] == 's':
            game.sud()
        elif ask[0] == 'o':
            game.ouest()
        elif ask[0] == 'e':
            game.est()
        if game.old == 'U':
            break
        elif game.old == '.':
            game.old = ' '
    with open('save', 'wb') as monFichier:
        monPickler = pickle.Pickler(monFichier)
        monPickler.dump(game)

os.remove('save')
print('GAGNER')