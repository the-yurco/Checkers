from webbrowser import get
import pygame
from checkers.constants import SIRKA , VYSKA 
from checkers.plocha import Plocha

pygame.init()

FPS = 60

PLOCHA = pygame.display.set_mode((SIRKA,VYSKA))
pygame.display.set_caption('DAMA')

def main():
    ideto = True
    cas = pygame.time.Clock()
    plocha = Plocha

    while ideto:
        cas.tick(FPS)
        
        for udalost in pygame.event.get():
            if udalost.type == pygame.QUIT:
                ideto = False
            if udalost.type == pygame.MOUSEBUTTONDOWN:
                pass

        pygame.stvorceky(PLOCHA)
        pygame.display.update()

    pygame.quit()

main()