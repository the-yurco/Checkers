import pygame                                  #kniznica na vytvorenie hry
from .konstanty import STVORCEK, SIVA, KORUNA  #importoval som potrebne konstanty

class Panacik:
    VYPLN = 13  #to co bude kolo panacika
    OBRYS = 2   #to co bude panacika obkreslovat

    def __init__(self, riadok, stlpec, farba): #ked vytvorime noveho panacika musime mu urcit tieto veci !!!
        self.riadok = riadok
        self.stlpec = stlpec
        self.farba = farba
        self.kral = False
        self.x = 0
        self.y = 0
        self.kalkulovanie_pozicie()

    def kalkulovanie_pozicie(self):                     #vykalkuluje nam nasu x,y poziciu zalozenu na riadku a stlpci v ktorom su panacikovia
        self.x = STVORCEK * self.stlpec + STVORCEK // 2 #vyjadruje nam ze bude nas panacik v strede policka na x-ovej osi
        self.y = STVORCEK * self.riadok + STVORCEK // 2 #vyjadruje nam ze bude nas panacik v strede policka na y-ovej osi

    def premenenie_na_krala(self): #funkcia na premenu krala ked panacik dojde na koniec plochy
        self.kral = True

    def vykreslenie(self, okno):   #definuje nam ako bude panacik vyzerat
        polomer = STVORCEK // 2 - self.VYPLN                                    #velkost panacika
        pygame.draw.circle(okno, SIVA, (self.x, self.y,), polomer + self.OBRYS) #vykreslenie obrysu pomocou pygamu
        pygame.draw.circle(okno, self.farba, (self.x, self.y,), polomer)        #vykreslenie pancika pomocou pygamu
        if self.kral:
            okno.blit(KORUNA, (self.x - KORUNA.get_width() // 2, self.y - KORUNA.get_height() // 2)) #vykreslenie obarzku do stredu panacika
            #blit znamena ze dame nejaky obrazok alebo fotku na dane misto na nasej ploche

    def pohyb(self, riadok, stlpec): #toto je to iste co v 'plocha.py' len definovane tu
        self.riadok = riadok
        self.stlpec = stlpec
        self.kalkulovanie_pozicie()

    def __repr__(self):           
        return str(self.farba)