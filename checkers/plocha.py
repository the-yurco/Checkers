"""
1. panacikovia ako sa hybu
2. pohyb panacikov
3. mazanie panacikov
"""
import pygame
from .konstanty import BIELA, CIERNA, HNEDA, KREMOVA, RIADKY, STLPCE, STVORCEK
from .panacik import Panacik

class Plocha:
    def __init__(self):
        self.plocha = [] #ukladanie panacikov v 2-dimenzionalnom liste v tejto clase [[BIELY,0,BIELY,0,BIELY],
        self.oznaceny_panacik = None                                                # [CIERNY,0,CIERNY,0,BIELY]]
        self.cierny_vlavo = self.biely_vlavo = 12 #pocet panacikov
        self.cierny_krali = self.biely_krali = 0  #pocet kralov
        self.vytvorenie_plochy()

    def vykreslovanie_stvorcekov(self, okno):     #vykresli nam nase stvorceky na ploche [okno]
        okno.fill(HNEDA)
        for riadok in range(RIADKY):                     
            for stlpec in range(riadok % 2, STLPCE, 2):  #ak je hneda 0 tak 0 % 2 je 0 takze nam vykresli hnede policko potom 2,4,6....
                pygame.draw.rect(okno, KREMOVA, (riadok * STVORCEK, stlpec * STVORCEK, STVORCEK, STVORCEK))

    def vytvorenie_plochy(self): #toto bude reprezentovat nasu 'self.plocha = []' a budeme pridavat panacikov do listu
        for riadok in range (RIADKY):
            self.plocha.append([]) #prazdny list
            for stlpec in range (STLPCE):
                if stlpec % 2 == ((riadok + 1) % 2):
                    if riadok < 3:
                        self.plocha[riadok].append(Panacik(riadok, stlpec, BIELA))
                    elif riadok > 4 :
                        self.plocha[riadok].append(Panacik(riadok, stlpec, CIERNA))
                    else:
                        self.plocha[riadok].append(0)
                else:
                    self.plocha[riadok].append(0)

    def vykreslenie(self, okno):
        self.vykreslovanie_stvorcekov(okno)
        for riadok in range(RIADKY):
            for stlpec in range(STLPCE):
                panacik = self.plocha[riadok][stlpec]
                if panacik != 0:
                    panacik.draw(okno)