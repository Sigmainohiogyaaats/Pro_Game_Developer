import pygame 

pygame.init()
HEIGHT = 700
WIDTH = 600
screen = pygame.display.set_mode((WIDTH,HEIGHT)) 
pygame.display.set_caption('rocket_game')
sprites = pygame.sprite.Group() 

class Player(pygame.sprite.Sprite): 
    def __init__(self): 
        super().__init__()
        self.image = pygame.image.load(r'C:\Users\aruni\OneDrive\Documents\Game Dev 2\lesson 8\baloon.png').convert_alpha()
        self.image = pygame.transform.scale(self.image,(100,100))
        self.rect = self.image.get_rect()

    def update(self,pressed_key):
        if pressed_key[pygame.K_UP]:
            self.rect.move_ip(0,-15) 
        
        elif pressed_key[pygame.K_DOWN]: 
            self.rect.move_ip(0,15)

        elif pressed_key[pygame.K_RIGHT]: 
            self.rect.move_ip(5,0) 

        elif pressed_key[pygame.K_LEFT]: 
            self.rect.move_ip(-5,0)  
rocket = Player()   
sprites.add(rocket)
  

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
        
    pressed_key = pygame.key.get_pressed()
    screen.fill('turquoise') 
    sprites.draw(screen)
    rocket.update(pressed_key) 
    
    

    pygame.display.update()
