from webbrowser import get
import pygame
from checkers.constants import SIRKA , VYSKA 

FPS = 60

PLOCHA = pygame.display.set_mode((SIRKA,VYSKA))
pygame.display.set_caption('DAMA')

def main():
    ideto = True
    cas = pygame.time.Clock()

    while ideto:
        cas.tick(FPS)
        
        for udalost in pygame.event,get():
            if udalost.type == pygame.QUIT:
                ideto = False
            if udalost._type == pygame.MOUSEBUTTONDOWN:
                pass

    pygame.quit()

main()