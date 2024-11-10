import pygame
pygame.init()

screen = pygame.display.set_mode((500, 500))

class mycircle:
    # properties
    def __init__(self, color, pos, rad, width=0):
        self.color = color
        self.pos = pos
        self.rad = rad
        self.width = width
        self.surf = screen

    def draw(self):
        pygame.draw.circle(self.surf, self.color, self.pos, self.rad, self.width)

    def grow(self, r):
        self.rad += r
        pygame.draw.circle(self.surf, self.color, self.pos, self.rad, self.width)


bluecircle = mycircle('blue', (250, 250), 5) 

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:           
                bluecircle.draw()
        elif event.type == pygame.MOUSEBUTTONUP:             
                bluecircle.grow(10)  

    screen.fill((0, 0, 0)) 
    bluecircle.draw()  
    pygame.display.update()

pygame.quit()
 