import pygame
from .konstanty import CIERNA, BIELA, MODRA, STVORCEK
from checkers.plocha import Plocha 

class Hra:
    def __init__(self, okno):
        self._init()
        self.okno = okno

    def update(self):
        self.plocha.vykreslenie(self.okno)
        self.vykreslit_platne_pohyby(self.platne_pohyby)
        pygame.display.update()

    def _init(self):
        self.oznaceny_panacik = None
        self.plocha = Plocha()
        self.narade = CIERNA
        self.platne_pohyby = {}

    def vyhra(self):
        return self.plocha.vyhra()

    def reset(self):
        self._init()

    def zadat(self, riadok, stlpec):
        if self.oznaceny_panacik:
            vysledok = self._pohyb(riadok, stlpec)
            if not vysledok:
                self.oznaceny_panacik = None
                self.zadat(riadok,stlpec)

        panacik = self.plocha.dostat_panacika(riadok, stlpec)
        if panacik != 0 and self.panacik.farba == self.narade:
            self.oznaceny_panacik = panacik
            self.platne_pohyby = self.plocha.dostat_platne_pohyby(panacik)
            return True
        
        return False

    def _pohyb(self, riadok, stlpec):
        panacik = self.plocha.dostat_panacika(riadok, stlpec)
        if self.oznaceny_panacik and panacik == 0 and (riadok, stlpec) in self.platne_pohyby:
            self.plocha.pohyb(self.oznaceny_panacik, riadok, stlpec)
            preskoceny = self.platne_pohyby[(riadok, stlpec)]
            if preskoceny:
                self.plocha.odstranit(preskoceny)
            self.zmenit_narade()
        else:
            return False
        return True

    def vykreslit_platne_pohyby(self, pohyby):
        for pohyb in pohyby:
            riadok, stlpec = pohyb
            pygame.draw.circle(self.okno, MODRA, (stlpec * STVORCEK + STVORCEK // 2 , riadok * STVORCEK + STVORCEK // 2 ), 15)

    def zmenit_narade(self):
        self.platne_pohyby = {}
        if self.narade == CIERNA:
            self.narade = BIELA
        else:
            self.narade = CIERNA