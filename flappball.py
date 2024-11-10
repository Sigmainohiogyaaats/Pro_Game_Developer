#import libraries  
# game constants 
#ball class -> properties and funtions 
#draw functio to render items on the screen  
#functionalities of the ball--> physics properties 
#key event  



import pgzrun 

from random import randint  
GRAVITY = 2000.0
TITLE =  'Flappyball'
WIDTH = 500 
HEIGHT = 600  


r = randint(0,255)
g = randint(0,255)
b = randint(0,255)  
clr  = r,g,b
class Ball():  


    def __init__(self):  
        self.x = randint(0,300) 
        self.y = randint(0,300) 
        self.vx = randint(100,200) 
        self.vy = 0
        self.radius = 40
         
    def draw(self): 
        pos = (self.x, self.y)  
        screen.draw.filled_circle(pos, self.radius, clr)   
ball = Ball()
def draw(): 
    screen.clear() 
    ball.draw() 


def update(dt): # inbuilt function, loops automatically 
    #uy stands for initial velocity  
    uy = ball.vy 
    #apply gravity 
    ball.vy += GRAVITY * dt 
    ball.y = ball.y +(uy+ball.vy) * 0.5 * dt
    #bounce 
    if ball.y > HEIGHT- ball.radius: 
        ball.y = HEIGHT - ball.radius 
        ball.vy = - ball.vy*0.9 
    #x velocity 
    ball.x = ball.x + ball.vx * dt 
    if ball.x > WIDTH - ball.radius or ball.x < ball.radius: 
        ball.vx = - ball.vx*0.9


def on_key_down(key): 
    if key == keys.SPACE: 
        ball.vy = -500 



pgzrun.go() 










