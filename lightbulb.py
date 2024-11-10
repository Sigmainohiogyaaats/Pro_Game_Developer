import pygame 
WIDTH = 600 
HEIGHT = 500 
pygame.init() 
pygame.font.init() 
screen = pygame.display.set_mode((WIDTH,HEIGHT)) 
pygame.display.set_caption('click to light, go off the bulb to unlight') 
lit = pygame.image.load(r'C:\Users\aruni\OneDrive\Documents\Game Dev 2\lesson 4\Lit.png') 
unlit = pygame.image.load(r'C:\Users\aruni\OneDrive\Documents\Game Dev 2\lesson 4\unlit.png')
 
while True: 
    for event in pygame.event.get() :
        if event.type == pygame.QUIT: 
            pygame.quit() 
        screen.blit()