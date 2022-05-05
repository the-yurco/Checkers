"""
1. POHYB PANACIKOV
2. MAZANIE PANACIKOV
3. VYKRESLENIE PLOCHY
4. VYTVORENIE CELKOVEJ PLOCHY
5. PRIECNE POHYBY
"""
import pygame                                                                   #kniznica na vytvaranie hry
from .konstanty import BIELA, CIERNA, HNEDA, KREMOVA, RIADKY, STLPCE, STVORCEK  #importoval som potrebne konstanty
from .panacik import Panacik                                                    #importoval som klasu Panacik

class Plocha:
    def __init__(self):
        self.plocha = []                                 #list ktory reprezentuje vsetky nase pnaciky
        self.cierny_vlavo = self.biely_vlavo = 12        #pocet panacikov
        self.cierny_krali = self.biely_krali = 0         #pocet kralov
        self.vytvorenie_plochy()

    def vykreslovanie_stvorcekov(self, okno):            #vykresli nam nase stvorceky na ploche [okno]
        okno.fill(HNEDA)
        for riadok in range(RIADKY):                     
            for stlpec in range(riadok % 2, STLPCE, 2):  #ak je hneda 0 tak 0 % 2 je 0 takze nam vykresli hnede policko potom 2,4,6....
                pygame.draw.rect(okno, KREMOVA, (riadok * STVORCEK, stlpec * STVORCEK, STVORCEK, STVORCEK))

    def pohyb(self, panacik, riadok, stlpec):            #toto je na zmazanie panacika ktoreho chceme vyhodit a dat tam svojho
        self.plocha[panacik.riadok][panacik.stlpec], self.plocha[riadok][stlpec] = self.plocha[riadok][stlpec], self.plocha[panacik.riadok][panacik.stlpec]  #panacik ktory je na pozicii a chceme ho potiahnut na miesto inde, jednoducho swapneme hodnoty
        panacik.pohyb(riadok, stlpec)                    #ked potiahneme panacika na urcite misto tak sa tam premiestni v urcitom 'riadok' a 'stlpec'

        #toto je nato aby ked pride enemy panacik na posledny/prvy riadok tak sa stane kralom
        if riadok == RIADKY -1 or riadok == 0:           #ak sa pohneme na poziciu 0 alebo 7 'riadok' znamena to ze sme na konci/zaciatku plochy
            panacik.premenenie_na_krala()                #no a panacik sa premeni na krala
            if panacik.farba == BIELA:                   #toto bude len kontrolvat kedy ma akeho krala spravit z akeho panacika 'farba'
                self.biely_krali += 1
            else:
                self.cierny_krali += 1

    def dostat_panacika(self, riadok, stlpec):          #ty zadas tomuto 'Plocha' objektu presny riadok + stlpec = 'mozna pozicia' a da ti tam panacika
        return self.plocha[riadok][stlpec]

    def vytvorenie_plochy(self):                        #toto bude reprezentovat nasu 'self.plocha = []' a budeme pridavat panacikov do listu
        for riadok in range (RIADKY):           
            self.plocha.append([])                      #prazdny list
            for stlpec in range (STLPCE):
                if stlpec % 2 == ((riadok + 1) % 2):    #ak je aktualny stlpec % 2 == akykolvek riadok + 1 a % 2 nam vykresli panacika  
                    if riadok < 3:                      #davame toto preto lebo chceme vykreslit nasich panacikov do prvych 3 riadkov
                        self.plocha[riadok].append(Panacik(riadok, stlpec, BIELA))
                    elif riadok > 4 :                   #davame toto preto lebo chceme vykreslit nasich panacikov do prvych 3 riadokv na druhej strane
                        self.plocha[riadok].append(Panacik(riadok, stlpec, CIERNA))
                    else:                            
                        self.plocha[riadok].append(0)   #else nam dodava to ze tam kde nemame zadaneho panaka nam vykresli (NIC)
                else:
                    self.plocha[riadok].append(0)

    def vykreslenie(self, okno):                        #vykresli nam vsetkych panacikov a stvorceky
        self.vykreslovanie_stvorcekov(okno)             #vykresli nam panacikov v okne
        for riadok in range(RIADKY):                    
            for stlpec in range(STLPCE):
                panacik = self.plocha[riadok][stlpec]   #definovany panacik v liste riadku a stlpca
                if panacik != 0:
                    panacik.vykreslenie(okno)

    def odstranit(self, panacikovia):                        #definicia pre vymazanie panaka
        for panacik in panacikovia:
            self.plocha[panacik.riadok][panacik.stlpec] = 0
            if panacik != 0:
                if panacik.farba == CIERNA:
                    self.cierny_vlavo -= 1
                else:
                    self.biely_vlavo -= 1

    def font_pixel(velkost):
        return pygame.font.Font("font.ttf", velkost)

    def vyhra(self):                    #definicia pre vyhru
        if self.cierny_vlavo <= 0:
            return BIELA
        elif self.biely_vlavo <= 0:
            return CIERNA

        return None
    
    

    #funkcia pre vsetky mozne a platne pohyby
    def dostat_platne_pohyby(self, panacik):
        pohyby = {}                     #tu budeme ukladat mozne pohyby, ze kde sa mozme potencionalne pohybovat
        dolava = panacik.stlpec - 1     #zadali sme co znamena ist dolava (v stlpcoch)
        doprava = panacik.stlpec + 1    #zadali sme co znamena ist doprava (v stlpcoch)
        riadok = panacik.riadok         #zadali sme co znamena samotny riadok

        if panacik.farba == CIERNA or panacik.kral:   #mozne pohyby pre krala

            #chcem updatovat akekolvek pohyby z tych zatvoriek 
            #v zatvorkach zacinam tym ze prechadzam priecne vlavo, potom prechadzam riadok -1 (ak sme cierny tak sa pohybujeme hore)Takže musíme skontrolovať smerom nahor, aby sme zistili, či je tam nieco platne
            #takze musime zacat v rade nad sucastnym riadokm, v ktorom sa nachadzame
            #potom tam mame ze 'max' to znamena kolko riadkov do hora sa budem pozerat
            #budem sa pozerat na riadok(-3, alebo -1) maximmum z toho, cize -1 to zastavi a znamena to potom aby sa pozrel len o 2 hore
            #panacik.farba - znamena farbu panaka, dolava - znamena ze je to miesto kde zacneme pre nas stlpec a co budeme odpocitat, ked sa budeme pohybovat nahor
            pohyby.update(self._priecne_dolava(riadok -1, max(riadok -3, -1), -1, panacik.farba, dolava))       
            pohyby.update(self._priecne_doprava(riadok -1, max(riadok -3, -1), -1, panacik.farba, doprava))

        if panacik.farba == BIELA or panacik.kral:    #mozne pohyby pre krala
            pohyby.update(self._priecne_dolava(riadok +1, min(riadok +3, RIADKY), 1, panacik.farba, dolava))
            pohyby.update(self._priecne_doprava(riadok +1, min(riadok +3, RIADKY), 1, panacik.farba, doprava))

        return pohyby

    #funkcia urcujuca kde budeme zacinat, kde budeme stat, kolkokrat sa mozeme pohnut, aka je farba, dolava (strana), a preskoceny
    def _priecne_dolava(self, start, stop, krok, farba, dolava, preskoceny = []): #diagonalne pohyby dolava
        pohyby = {}                                                 
        posledny = []

        #premenná, ktorá pre nás sleduje ľavú stranu, ktorú len zvyšujeme, keď sa pohybujeme v radoch, to nás opäť posunie ako diagonálny vzor, čo je to, čo sa snažíme hľadať
        for r in range(start, stop, krok):                          #tento cyklus nam hovori ze v ktorom riadku (startujeme, stopujeme a kde budeme chodit)
            if dolava < 0:                                      
                break

            aktualny = self.plocha[r][dolava]                       

            #tuto sa jedna o mozne dosledky ktore sa mozu stat kde sa mozme/nemozme pohnut, kde mozme/nemozme skocit, spojene z farbou ktorou hybeme panaka
            #stale sa opakuje a hlada mozny 'tah' ak to mozem tak nazvat
            if aktualny == 0:                                       #1. najdeme platneho panaka
                if preskoceny and not posledny:                     
                    break
                elif preskoceny:                                    #preskocime cez nejakeho
                    pohyby[(r, dolava)] = posledny + preskoceny     #vieme ci mozme preskocit 1 alebo 2 a ktory potrebujeme odstranit
                else:
                    pohyby[(r, dolava)] = posledny

                if posledny:                                        #2. preskocime cez nejaky / rozhodneme sa ci mozme nahodou dat double alebo triple
                    if krok == -1:
                        riadok = max(r -3, 0)
                    else:
                        riadok = min(r +3, RIADKY)

                    #3. toto by to malo zopakovat rekurzivne (urobit to este raz) a vidiet ci mozme dat vlastne ten double alebo triple
                    pohyby.update(self._priecne_dolava(r + krok, riadok, krok, farba, dolava -1, preskoceny = posledny))
                    pohyby.update(self._priecne_doprava(r + krok, riadok, krok, farba, dolava +1, preskoceny = posledny))
                break 

            elif aktualny.farba == farba:
                break
            else:
                posledny = [aktualny]
            dolava -= 1

        return pohyby

    #funkcia urcujuca kde budeme zacianat, kde budeme stat, kolkokrat sa mozeme pohnut, aka je farba, dolava (strana), a preskoceny
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
                        riadok = min(r +3, RIADKY)

                    pohyby.update(self._priecne_dolava(r + krok, riadok, krok, farba, doprava -1, preskoceny = posledny))
                    pohyby.update(self._priecne_doprava(r + krok, riadok, krok, farba, doprava +1, preskoceny = posledny))
                break 

            elif aktualny.farba == farba:
                break
            else:
                posledny = [aktualny]
            doprava += 1

        return pohyby