import pygame  
pygame.init() 
WIDTH = 500  
HEIGHT = 600  
screen = pygame.display.set_mode((WIDTH,HEIGHT)) 
goku = pygame.image.load('goku.png')  
gokuscale = pygame.transform.scale(goku, (200,200))
glacier = pygame.image.load(r'C:\Users\aruni\OneDrive\Documents\Game Dev 2\lesson 5\glacier.jpg') 
keys = [False,False,False,False] #state of the arrow keys are stored in the form of a list

goku_x = 100 
goku_y = 100
while True: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.blit(glacier,(0,0))
    screen.blit(gokuscale,(goku_x,goku_y))
    pygame.display.update()  
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            pygame.quit() 
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP: 
                keys[0] = True 
            elif event.key == pygame.K_LEFT: 
                keys[1] = True 
            elif event.key == pygame.K_DOWN: 
                keys[2] = True 
            elif event.key == pygame.K_RIGHT: 
                keys[3] = True 


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP: 
                keys[0] = False
            elif event.key == pygame.K_LEFT: 
                keys[1] = False
            elif event.key == pygame.K_DOWN: 
                keys[2] = False
            elif event.key == pygame.K_RIGHT: 
                keys[3] = False 

    if keys[0] == True: 
        if goku_y >0:
            goku_y -= 7 
    elif keys[1] == True:  
        if goku_x >0:
            goku_x -= 7 
    elif keys[2] == True:  
            goku_y += 7 
    elif keys[3] == True: 
        if goku_x <400:
            goku_x += 7 




pygame.display.update()
    
