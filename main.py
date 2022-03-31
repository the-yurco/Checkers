import pygame

from checkers.constants import VYSKA, SIRKA

FPS = 60

PLOCHA = pygame.display.set_mode((SIRKA, VYSKA))
pygame.display.set_caption('SPS IT DAMA PROJEKT')

def main():
    ideto = True
    clock = pygame.time.Clock()

    while ideto:
        clock.tick(FPS)
        
        for udalost in pygame.event.get():
            if udalost.type == pygame.QUIT:
                ideto = False
            if udalost.typr == pygame.MOUSEBUTTONDOWN:
                pass
            
    pygame.quit()
main()