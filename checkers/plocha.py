import pygame

from .konstanty import HNEDA, KREMOVA, RIADKY, STVORCEK

class Plocha:
    def __init__(self):
        self.plocha = []                            #2-dimenzionalny list pre stvorceky
        self.oznaceny_panacik = None                #hovori nam ci sme oznacili alebo nie panacika
        self.cierne_vlavo = self.biele_vlavo = 12   #pocet panacikov
        self.cierny_krali = self.biely_krali = 0    #pocet kralov

    def vykreslenie_stvorcekov(self, okno):
        okno.fill (HNEDA)                                                                            #-|
                                                                                                     # |
        for riadok in range(RIADKY):                                                                 # = toto nam vytvara patern nasej plochy 
            for stlpec in range(riadok % 2, RIADKY , 2): #vykresli nam aky svorcek bude akej farny   # |
                pygame.draw.rect(okno, KREMOVA, (riadok * STVORCEK, stlpec * STVORCEK , STVORCEK , STVORCEK))          #
                                                               