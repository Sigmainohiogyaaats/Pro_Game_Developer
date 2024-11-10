import pygame
import sys 

pygame.init() 
red_bullets = [] 
blue_bullets = []  
blue_hit = pygame.USEREVENT + 1 
red_hit = pygame.USEREVENT + 2 


def handle_bullets(blue_bullets, red_bullets, red, blue): 
    for bullet in blue_bullets:
        bullet.x += 5 
        if red.colliderect(bullet): 
            pygame.event.post(pygame.event.Event(red_hit))
            blue_bullets.remove(bullet)
        elif bullet.x > WIDTH: 
            blue_bullets.remove(bullet) 
    for bullet in red_bullets: 
        bullet.x -= 5 
        if blue.colliderect(bullet):  
            pygame.event.post(pygame.event.Event(blue_hit)) 
            red_bullets.remove(bullet) 
        elif bullet.x < 0: 
            red_bullets.remove(bullet) 

WIDTH = 1000
HEIGHT = 750
BORDER = pygame.Rect(WIDTH // 2 - 5, 0, 10, HEIGHT)
screen = pygame.display.set_mode((WIDTH, HEIGHT)) 


# Load and scale images
blueship = pygame.image.load(r'C:\Users\aruni\OneDrive\Documents\Game Dev 2\lesson 6\PLAYER_SHIP.png')
redship = pygame.image.load(r'C:\Users\aruni\OneDrive\Documents\Game Dev 2\lesson 6\SMALL_ENEMY.png')
bluescale = pygame.transform.scale(blueship, (50, 50))
redscale = pygame.transform.scale(redship, (50, 50))
bluer = pygame.transform.rotate(bluescale, 270)
redr = pygame.transform.rotate(redscale, 90)   

def handle_blue_movement(keys_pressed, blue):
    if keys_pressed[pygame.K_a] and blue.x > 0:
        blue.x -= 5
    if keys_pressed[pygame.K_d] and blue.x < BORDER.x - blue.width:
        blue.x += 5
    if keys_pressed[pygame.K_w] and blue.y > 0:
        blue.y -= 5
    if keys_pressed[pygame.K_s] and blue.y < HEIGHT - blue.height:
        blue.y += 5 

def handle_red_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x > BORDER.x + BORDER.width:
        red.x -= 5
    if keys_pressed[pygame.K_RIGHT] and red.x < WIDTH - red.width:
        red.x += 5
    if keys_pressed[pygame.K_UP] and red.y > 0:
        red.y -= 5
    if keys_pressed[pygame.K_DOWN] and red.y < HEIGHT - red.height:
        red.y += 5 

blue = pygame.Rect(200, 200, 50, 50)
red = pygame.Rect(800, 200, 50, 50) 

health_text = pygame.font.SysFont('Comic Sans',40)  
red_health = 10

blue_health = 10

def draw_winner(text):  
    winner_font = pygame.font.SysFont('Georgia',70) 
    draw_text = winner_font.render(text,1,'white')
    screen.blit(draw_text, (WIDTH/2 , HEIGHT/2))


while True:     
    screen.fill((0, 0, 0))  
    blue_health_text = health_text.render('Health: '+str(blue_health),1,'white') 
    screen.blit(blue_health_text,(10,10))
    red_health_text = health_text.render('Health: '+str(red_health),1,'white') 
    screen.blit(red_health_text,(800,10))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() 
        if event.type == pygame.KEYDOWN:  
            if event.key == pygame.K_q: 
                bullet = pygame.Rect(blue.x, blue.y, 10, 5) 
                blue_bullets.append(bullet) 
            if event.key == pygame.K_RSHIFT:
                bullet = pygame.Rect(red.x, red.y, 10, 5) 
                red_bullets.append(bullet)   
        if event.type == red_hit: 
            red_health -= 1 
        if event.type == blue_hit: 
            blue_health -= 1 
    winner_text = '' 
    if red_health <= 0:  
        winner_text = 'Blue Wins!' 
        screen.fill('Blue') 
    if blue_health <= 0: 
        winner_text = 'Red Wins!'  
        screen.fill('Red')
    if winner_text != '': 
        draw_winner(winner_text) 
        


    screen.blit(bluer, (blue.x, blue.y))
    screen.blit(redr, (red.x, red.y)) 
    pygame.draw.rect(screen, 'yellow', BORDER)  
    
    keys_pressed = pygame.key.get_pressed() 
    handle_blue_movement(keys_pressed, blue)
    handle_red_movement(keys_pressed, red)  
    handle_bullets(blue_bullets, red_bullets, red, blue)

    for bullet in blue_bullets: 
        pygame.draw.rect(screen, 'blue', bullet)
    for bullet in red_bullets: 
        pygame.draw.rect(screen, 'red', bullet)

    pygame.display.update()


