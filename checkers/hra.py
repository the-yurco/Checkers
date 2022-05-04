'''
1. KTO JE NA RADE?
2. KONTROLA CI SME SELEKTLI NASHO PANAKA
3. KONTROLA CI HO MOZME POHNUT TAM, TAM, SEM...
'''
import pygame                                           #kniznica na robenie hry
from .konstanty import CIERNA, BIELA, MODRA, STVORCEK   #imporoval som konstanty ktore som potreboval
from checkers.plocha import Plocha                      #importoval som klasu 'Plocha' ktoru som potreboval

class Hra:                                              #nasa klasa 'Hra'
    def __init__(self, okno):                           
        self._init()
        self.okno = okno

    def update(self):                                   #updatovanie plochy
        self.plocha.vykreslenie(self.okno)
        self.vykreslit_platne_pohyby(self.platne_pohyby)
        pygame.display.update()

    def _init(self):
        self.oznaceny_panacik = None                    #ziaden oznaceny panak
        self.plocha = Plocha()
        self.narade = CIERNA                            #urcuje nam kto ide prvy
        self.platne_pohyby = {}                         #obsah pre platne pohyby

    def vyhra(self):                                    #definicia pre vyvolanie vyhry
        return self.plocha.vyhra()

    def reset(self):                                    #resetovanie hry
        self._init()

    #akykolvek input co robime na mape nam vyvolava tuto funkciu
    def zadat(self, riadok, stlpec):                    #zadavanie riadku a stlpca + ak som urcite zadal panacika tak sa moze pohnut ale nemusim a mozem kliknut na druheho
        if self.oznaceny_panacik:                       #ak sme oznacili urciteho panacika
            vysledok = self._pohyb(riadok, stlpec)      #tak ho mozme posunut ako vidime v urcitom (riadok, stlpec)
            if not vysledok:                            #ale ak chceme pojnut ineho panaka tak znaci ze 'vysledok = false'
                self.oznaceny_panacik = None            #tu to znaci zmeneneho panaka
                self.zadat(riadok,stlpec)               #tu to znaci zmenene miesto pohybu (+ to vyvola tu funkciu este raz a potom vyhodnoti podla kodu nizsie)

        #toto hovori pouzivatelovi ze HEJ! tento vyber bol platny tak vratim ti TRUE ale ak to platne nebolo tak ti vratim FALSE
        panacik = self.plocha.dostat_panacika(riadok, stlpec)               
        if panacik != 0 and panacik.farba == self.narade:
            self.oznaceny_panacik = panacik
            self.platne_pohyby = self.plocha.dostat_platne_pohyby(panacik)
            return True
        
        return False

    #funkcia pohybu
    def _pohyb(self, riadok, stlpec):
        panacik = self.plocha.dostat_panacika(riadok, stlpec)                                   #panacik ktoreho chceme pohnut na urcitom riadku a stlpci
        if self.oznaceny_panacik and panacik == 0 and (riadok, stlpec) in self.platne_pohyby:   #ak zadame panaka, a ak zadany panak je 0 takze tam nestoji dalsi panak tak sa moze pohnut na 'platne pohyby'
            self.plocha.pohyb(self.oznaceny_panacik, riadok, stlpec)                            #mozme pohnut panaka na urcity riadok a stlpec
            preskoceny = self.platne_pohyby[(riadok, stlpec)]                                   #
            if preskoceny:
                self.plocha.odstranit(preskoceny)
            self.zmenit_narade()
        else:
            return False

        return True

    #funkcia ktora nam urcuje tie modre bodky pre znazornenie moznych pohybov
    def vykreslit_platne_pohyby(self, pohyby):
        for pohyb in pohyby:                    #cyklus pre pohyby
            riadok, stlpec = pohyb              #miesta rovnajuce sa platnemu pohybu
            pygame.draw.circle(self.okno, MODRA, (stlpec * STVORCEK + STVORCEK // 2 , riadok * STVORCEK + STVORCEK // 2 ), 15) #vykreslenie a znazornenie bodiek

    #toto je jednoducha funkcia na to aby sa islo po rade, kto ma ist teraz, kto teraz atd...
    def zmenit_narade(self):
        self.platne_pohyby = {}
        if self.narade == CIERNA:
            self.narade = BIELA
        else:
            self.narade = CIERNA