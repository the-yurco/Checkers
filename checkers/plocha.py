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
                                                                                    # [CIERNY,0,CIERNY,0,BIELY]]
        self.cierny_vlavo = self.biely_vlavo = 12 #pocet panacikov
        self.cierny_krali = self.biely_krali = 0  #pocet kralov
        self.vytvorenie_plochy()

    def vykreslovanie_stvorcekov(self, okno):     #vykresli nam nase stvorceky na ploche [okno]
        okno.fill(HNEDA)
        for riadok in range(RIADKY):                     
            for stlpec in range(riadok % 2, STLPCE, 2):  #ak je hneda 0 tak 0 % 2 je 0 takze nam vykresli hnede policko potom 2,4,6....
                pygame.draw.rect(okno, KREMOVA, (riadok * STVORCEK, stlpec * STVORCEK, STVORCEK, STVORCEK))

    def pohyb(self, panacik, riadok, stlpec):
        self.plocha[panacik.riadok][panacik.stlpec], self.plocha[riadok][stlpec] = self.plocha[riadok][stlpec], self.plocha[panacik.riadok][panacik.stlpec]
        panacik.pohyb(riadok, stlpec)

        if riadok == RIADKY -1 or riadok == 0:
            panacik.premenenie_na_krala()
            if panacik.farba == BIELA:
                self.biely_krali += 1
            else:
                self.cierny_krali

    def dostat_panacika(self, riadok, stlpec):
        return self.plocha[riadok][stlpec]

    def vytvorenie_plochy(self): #toto bude reprezentovat nasu 'self.plocha = []' a budeme pridavat panacikov do listu
        for riadok in range (RIADKY):
            self.plocha.append([]) #prazdny list
            for stlpec in range (STLPCE):
                if stlpec % 2 == ((riadok + 1) % 2): # 
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
                    panacik.vykreslenie(okno)

    def odstranit(self, panacikovia):
        for panacik in panacikovia:
            self.plocha[panacik.riadok][panacik.stlpec] = 0
            if panacik != 0:
                if panacik.farba == CIERNA:
                    self.cierny_vlavo -= 1
                else:
                    self.biely_vlavo -= 1

    def vyhra(self):
        if self.cierny_vlavo <= 0:
            return BIELA
        elif self.biely_vlavo <= 0:
            return CIERNA

        return None

    def dostat_platne_pohyby(self, panacik):
        pohyby = {}
        dolava = panacik.stlpec - 1
        doprava = panacik.stlpec + 1
        riadok = panacik.riadok

        if panacik.farba == CIERNA or panacik.kral:
            pohyby.update(self._priecne_dolava(riadok -1, max(riadok -3, -1), -1, panacik.farba, dolava))
            pohyby.update(self._priecne_doprava(riadok -1, max(riadok -3, -1), -1, panacik.farba, doprava))
        if panacik.farba == BIELA or panacik.kral:
            pohyby.update(self._priecne_dolava(riadok +1, min(riadok +3, RIADKY), 1, panacik.farba, dolava))
            pohyby.update(self._priecne_doprava(riadok +1, min(riadok +3, RIADKY), 1, panacik.farba, doprava))

        return pohyby

    def _priecne_dolava(self, start, stop, krok, farba, dolava, preskoceny = []): #diagonalne pohyby dolava
        pohyby = {}
        posledny = []
        for r in range(start, stop, krok):
            if dolava < 0:
                break

            aktualny = self.plocha[r][dolava]
            if aktualny == 0:
                if preskoceny and not posledny:
                    break
                elif preskoceny:
                    pohyby[(r, dolava)] = posledny + preskoceny
                else:
                    pohyby[(r, dolava)] = posledny

                if posledny:
                    if krok == -1:
                        riadok = max(r -3, 0)
                    else:
                        riadok = min(r +r, RIADKY)

                    pohyby.update(self._priecne_dolava(r + krok, riadok, krok, farba, dolava -1, preskoceny = posledny))
                    pohyby.update(self._priecne_doprava(r + krok, riadok, krok, farba, dolava +1, preskoceny = posledny))
                    break 

            elif aktualny.farba == farba:
                break
            else:
                posledny = [aktualny]
            dolava -= 1

        return pohyby

    def _priecne_doprava(self, start, stop, krok, farba, doprava, preskoceny = []): #diagonalne pohyby doprava
        pohyby = {}
        posledny = []
        for r in range(start, stop, krok):
            if doprava >= STLPCE:
                break

            aktualny = self.plocha[r][doprava]
            if aktualny == 0:
                if preskoceny and not posledny:
                    break
                elif preskoceny:
                    pohyby[(r, doprava)] = posledny + preskoceny
                else:
                    pohyby[(r, doprava)] = posledny

                if posledny:
                    if krok == -1:
                        riadok = max(r -3, 0)
                    else:
                        riadok = min(r +r, RIADKY)

                    pohyby.update(self._priecne_dolava(r + krok, riadok, krok, farba, doprava -1, preskoceny = posledny))
                    pohyby.update(self._priecne_doprava(r + krok, riadok, krok, farba, doprava +1, preskoceny = posledny))
                    break 

            elif aktualny.farba == farba:
                break
            else:
                posledny = [aktualny]
            doprava += 1

        return pohyby