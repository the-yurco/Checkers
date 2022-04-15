import pygame  #kniznica potrebna na vytvorenie hry
from checkers.konstanty import VYSKA, SIRKA #importujem z ineho filu
from checkers.plocha import Plocha

FPS = 60

OKNO = pygame.display.set_mode((VYSKA, SIRKA)) #plocha 
pygame.display.set_caption('DAMA') #nadpis hry

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

    plocha.vykreslenie_stvorcekov(OKNO)
    pygame.display.update()
    
    pygame.quit()

main()