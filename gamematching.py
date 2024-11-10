import pygame
pygame.init() 
WIDTH = 600 
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH,HEIGHT)) 
bg = pygame.image.load(r'C:\Users\aruni\OneDrive\Documents\Game Dev 2\Lesson 7\bg.png')
candy_crush = pygame.image.load(r'C:\Users\aruni\OneDrive\Documents\Game Dev 2\Lesson 7\candy_crush.jpg') 
ludo = pygame.image.load(r'C:\Users\aruni\OneDrive\Documents\Game Dev 2\Lesson 7\ludo.png') 
subway= pygame.image.load(r'C:\Users\aruni\OneDrive\Documents\Game Dev 2\Lesson 7\subway.png') 
temple_run = pygame.image.load(r'C:\Users\aruni\OneDrive\Documents\Game Dev 2\Lesson 7\temple_run.png')
bs = pygame.image.load(r'C:\Users\aruni\OneDrive\Documents\Game Dev 2\Lesson 7\bs.jpg') 

screen.blit(ludo,(150,0)) 
screen.blit(subway,(150,100))
screen.blit(temple_run,(150,200)) 
screen.blit(candy_crush,(150,300))   
screen.blit(bs,(150,350))



font=pygame.font.SysFont('Times New Roman',36)

text=font.render('ludo',True,(255,1,1)) 
text1=font.render('candy_crush',True,(255,1,1)) 
text2=font.render('subway',True,(255,1,1)) 
text3=font.render('temple_run',True,(255,1,1))
text4=font.render('bs' ,True,(255,1,1))

screen.blit(text,(350,100)) 
screen.blit(text1,(350,0))
screen.blit(text2,(350,300))
screen.blit(text3,(350,200))
screen.blit(text4,(350,350))
pygame.display.update() 

while 1: 
    event = pygame.event.poll()

    if event.type == pygame.MOUSEBUTTONDOWN: 
        pos = pygame.mouse.get_pos()
        pygame.draw.circle(screen, (0,0,0), (pos), 20, 0)
    elif event.type ==pygame.MOUSEBUTTONUP: 
        pos1 = pygame.mouse.get_pos()
        pygame.draw.line(screen,(0,0,0),(pos),(pos1),5)
        pygame.draw.circle(screen, (0,0,0), (pos1), 20, 0)



    pygame.display.update()
