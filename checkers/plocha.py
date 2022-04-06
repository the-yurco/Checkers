import pygame
from .constants import CIERNA , RIADKY , FIALOVA , STVORCEK

class Plocha:
    def __init__(self):
        self.plocha = []
        self.zadany_objekt = None
        self.cervene = self.biele = 12
        self.cerveny_kral = self.biely_kral = 0
    
    def vykreslit_stvorceky(self , plocha):
        plocha.fill(CIERNA)
        for riadok in range(RIADKY):
            for stlpec in range(riadok % 2, RIADKY, 2):
                pygame.draw.rect(plocha, FIALOVA , (riadok * STVORCEK , stlpec * STVORCEK , STVORCEK , STVORCEK))
