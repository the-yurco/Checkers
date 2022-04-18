import pygame
from checkers.konstanty import CIERNA, SIRKA, STVORCEK, VYSKA
from checkers.hra import Hra

FPS = 60

OKNO = pygame.display.set_mode((SIRKA, VYSKA))
pygame.display.set_caption('DAMA')

def pohybovanie_s_myskou(pozicia):
    x, y = pozicia
    riadok = y // STVORCEK
    stlpec = x // STVORCEK
    return riadok, stlpec

def main():
    ideto = True
    cas = pygame.time.Clock()
    hra = Hra(OKNO)


    while ideto:
        cas.tick(FPS)

        if hra.vyhra() != None:
            print (hra.vyhra())
            ideto = False

        for udalost in pygame.event.get():
            if udalost.type == pygame.QUIT:
                ideto = False

            if udalost.type == pygame.MOUSEBUTTONDOWN:
                pozicia = pygame.mouse.get_pos()
                riadok, stlpec = pohybovanie_s_myskou(pozicia)
                hra.zadat(riadok,stlpec)

        hra.update()

    pygame.quit()

main()
