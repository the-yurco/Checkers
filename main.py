import pygame
from checkers.konstanty import SIRKA, VYSKA
from checkers.plocha import Plocha

FPS = 60

OKNO = pygame.display.set_mode((SIRKA, VYSKA))
pygame.display.set_caption('DAMA')

def main():
    ideto = True
    cas = pygame.time.Clock()
    plocha = Plocha()

    while ideto:
        cas.tick(FPS)

        for udalost in pygame.event.get():
            if udalost.type == pygame.QUIT:
                ideto = False

            if udalost.type == pygame.MOUSEBUTTONDOWN:
                pass

        plocha.vykreslovanie_stvorcekov(OKNO)
        pygame.display.update()

    pygame.quit()

main()
