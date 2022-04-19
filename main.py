'''
1. cele spustenie hry + menu
2. hlavne rozmery + nadpis
3. fps
4. vyuzivanie mysky
'''

import pygame                                                 #kniznica na tvorenie hry
from tkinter import *                                         #kniznica na tvorenie menucka
from checkers.konstanty import CIERNA, SIRKA, STVORCEK, VYSKA #importoval som konstanty aby som mohol s nimi pracovat
from checkers.hra import Hra

FPS = 60

OKNO = pygame.display.set_mode((SIRKA, VYSKA))  #rozmery na plochu hry
pygame.display.set_caption('DAMA')              #nadpis okna

def pohybovanie_s_myskou(pozicia):  #funkcia na pohyb s myskou
    x, y = pozicia
    riadok = y // STVORCEK
    stlpec = x // STVORCEK
    return riadok, stlpec

def main():                         #hlavna funkcia
    ideto = True                    #runnuje to
    cas = pygame.time.Clock()       #fpska
    hra = Hra(OKNO)                 #hra sa spusti


    while ideto:
        cas.tick(FPS)               #fpska

        if hra.vyhra() != None:     #ked niekto vyhra skonci sa hra
            print (hra.vyhra())
            ideto = False

        for udalost in pygame.event.get(): #vypne nam okno
            if udalost.type == pygame.QUIT:
                ideto = False
 
            if udalost.type == pygame.MOUSEBUTTONDOWN: #pohyb panacikov s pouzitim mysky
                pozicia = pygame.mouse.get_pos()
                riadok, stlpec = pohybovanie_s_myskou(pozicia)
                hra.zadat(riadok,stlpec)

        hra.update()

    pygame.quit()

main()
