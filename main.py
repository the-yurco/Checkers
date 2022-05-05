'''
1. CELA HRA 
2. ROZMERY OKNA + NADPIS
3. FPS-ka
4. VYUZIVANIE MYSKY
'''

import pygame
from pygame import *                                          #kniznica na tvorenie hry
from tkinter import *                                         #kniznica na tvorenie menucka
from checkers.konstanty import SIRKA,STVORCEK, VYSKA          #importoval som konstanty aby som mohol s nimi pracovat
from checkers.hra import Hra

FPS = 60

OKNO = pygame.display.set_mode((SIRKA, VYSKA))  #rozmery na plochu hry
pygame.display.set_caption('DAMA')              #nadpis okna

pygame.mixer.init()
pygame.init()

def pohybovanie_s_myskou(pozicia):  #funkcia na pohyb s myskou
    x, y = pozicia                  #zadali sme ze x,y osi su nasa urcena pozicia
    riadok = y // STVORCEK          #zadali sme co znamena nasa y-ova os  (ak je y = 700 to znamena ze je to riadok 7 atd...)
    stlpec = x // STVORCEK          #zadali sme co znamena nasa x-ova os
    return riadok, stlpec


def main():                         #hlavna funkcia

    mixer.music.load('assets\checkerssoundtrack.mp3')   #muzika
    mixer.music.play(-1)                                #to ze sa to bude opakovat

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

            if udalost.type == pygame.MOUSEBUTTONDOWN:          #pohyb panacikov s pouzitim mysky
                pozicia = pygame.mouse.get_pos()                #definujeme co je nasa urcena pozicia
                riadok, stlpec = pohybovanie_s_myskou(pozicia)  #jednoducho klikneme na nasho panacika a potom klikneme na moznu pozicku
                hra.zadat(riadok,stlpec)

        hra.update()

    pygame.quit()

main()
