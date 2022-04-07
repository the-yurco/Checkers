import pygame
from .constants import BIELA , CIERNA , STVORCEK , SIVA

class Kruzok:
    VYPCHAVKA = 10
    OBRYS = 2

    def __init__(self, riadok , stlpec , farba):
        self.riadok = riadok
        self.stlpec = stlpec
        self.farba = farba
        self.kral = False
        self.smer = 1

        if self.farba == BIELA:
            self.smer = -1
        else:
            self.smer = 1

        self.x = 0
        self.y = 0
        self.pozicia_kruzkov()

    def pozicia_kruzkov(self):
        self.x = STVORCEK * self.stlpec + STVORCEK // 2
        self.y = STVORCEK * self.riadok + STVORCEK // 2

    def kral(self):
        self.kral = True

    def vykreslenie_kruzkov(self , plocha):
        radius = STVORCEK // 2 - self.VYPCHAVKA
        pygame.draw.circle(plocha, SIVA, (self.x, self.y), radius)
        pygame.draw.circle(plocha, self.farba, (self.x, self.y), radius + self.OBRYS)

    def __repr__(self):
        return str(self.farba)
