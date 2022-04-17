import pygame
from .konstanty import CIERNA, BIELA, STVORCEK, SIVA

class Panacik:
    VYPLN = 10
    OBRYS = 2

    def __init__(self, riadok, stlpec, farba): #ked vytvorime noveho panacika musime mu urcit tieto veci !!!
        self.riadok = riadok
        self.stlpec = stlpec
        self.farba = farba
        self.kral = False
        

        if self.farba == CIERNA:
            self.smer = -1
        else:
            self.smer = 1

        self.x = 0
        self.y = 0

    def kalkulovanie_pozicie(self): #vykalkuluje nam nasu x,y poziciu zalozenu na riadku a stlpeci v ktorom su
        self.x = STVORCEK * self.riadok + STVORCEK // 2 #vyjadruje nam ze bude nas panacik v strede policka
        self.y = STVORCEK * self.stlpec + STVORCEK // 2

    def premenenie_na_krala(self):
        self.kral = True

    def vykreslenie_panacika(self, okno): #definuje nam ako bude panacik vyzerat
        polomer = STVORCEK // 2 - self.VYPLN
        pygame.draw.circle(okno, SIVA, (self.x, self.y,), polomer + self.OBRYS) #obrys   
        pygame.draw.circle(okno, self.farba, (self.x, self.y,), polomer)        #panacik

    def __repr__(self):
        return str(self.farba)