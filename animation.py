#import pygame 
#pygame.init() 
#pygame.display.set_mode((WIDTH,HEIGHT)) 
#pygame.display.set_caption('birthday sigma card') 
#pygame.image.load('backgroundone.jpg') 
#pygame.transform.scale(img,(WIDTH,HEIGHT)) 
#font = pygame.font.SysFont('Times New Roman',72)  
#font.render('happy',True,(0,0,0))  
#display_surface.blit(image,(0,0)) 
#pygame.display.update() 
#time.sleep(2)  

import pygame   
import time
WIDTH = 600 
HEIGHT = 500 

pygame.init()  
pygame.font.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT)) 
pygame.display.set_caption(('happy birthday'))  
cake = pygame.image.load(r'C:\Users\aruni\OneDrive\Documents\Game Dev 2\lesson 4\cake.jpg') 
confet = pygame.image.load(r'C:\Users\aruni\OneDrive\Documents\Game Dev 2\lesson 4\confet..jpg') 
smth = pygame.image.load(r'C:\Users\aruni\OneDrive\Documents\Game Dev 2\lesson 4\smth.jpg') 
font = pygame.font.SysFont('Comic Sans',72) 
  
while True:  
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()  
    text = font.render('happy',True,(0,0,0)) 
    screen.blit(smth,(0,0)) 
    screen.blit(text,(0,0)) 
    pygame.display.update()
    time.sleep(2)  
    screen.blit(cake,(0,0))   
    pygame.display.update()
    time.sleep(2)
    screen.blit(confet,(0,0))  
    pygame.display.update() 
    time.sleep(2)
