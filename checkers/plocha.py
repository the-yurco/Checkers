import pygame

from checkers.kruzok import Kruzok
from .constants import CIERNA, HNEDA , RIADKY , KREMOVA, STLPCE , STVORCEK , BIELA
from .kruzok import Kruzok

class Plocha:
    def __init__(self):
        self.plocha = []
        self.zadany_objekt = None
        self.cervene = self.biele = 12
        self.cerveny_kral = self.biely_kral = 0
        self.vytvaranie_plochy() 
    
    def vykreslit_stvorceky(self , plocha):
        plocha.fill(HNEDA)
        for riadok in range(RIADKY):
            for stlpec in range(riadok % 2, RIADKY, 2):
                pygame.draw.rect(plocha, KREMOVA , (riadok * STVORCEK , stlpec * STVORCEK , STVORCEK , STVORCEK))

    def vytvaranie_plochy(self):
        for riadok in range(RIADKY):
            self.plocha.append([])
            for stlpec in range(STLPCE):
                if stlpec % 2 == ((riadok + 1) % 2):
                    self.plocha[riadok].append(Kruzok(riadok, stlpec, BIELA))
                elif riadok > 4:
                    self.plocha[riadok].append(Kruzok(riadok, stlpec, CIERNA))
                else:
                    self.plocha[riadok].append(0)
            else:
                self.plocha[riadok].append(0)
    
    #VYKRESLOVANIE VSETKYCH KRUZKOV A STVORCEKOV
    def vykreslovanie(self, plocha):
        self.vykreslit_stvorceky(plocha)
        for riadok in range(RIADKY):
            for stlpec in range(STLPCE):
                kruzok = self.plocha[riadok],[stlpec]
                if kruzok != 0:
                    kruzok.vykreslovanie(plocha)