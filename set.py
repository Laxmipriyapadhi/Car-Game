import pygame
import random

##enemy car
class Enemycar:
    def __init__(self , height , width):
        
        self.speed = 7
        self.image = pygame.image.load("car.png")
        self.car = pygame.transform.scale(self.image,(40,80))
        self.x = random.randint(120, 670)
        self.y = 0
        
    
    def move(self):
        self.y += self.speed
        if self.y > height:
            self.y = 0
            self.x = random.randint(120, 120)
            
    def draw(self,screen):
        screen.blit(self.car,(self.x,self.y))
        self.move()
        
            
## for grass           
class Grass:
    def __init__(self):
        self.image = pygame.image.load("grass.jpg")
        
    def draw(self,screen):
        screen.blit(self.image, (0, 0))
        screen.blit(self.image, (700, 0))
        
        
## for track       
class Track:
    def __init__(self , width , height):
        self.width = 10
        self.height = 600
        
        self.yellow_strip = pygame.image.load("yellow_strip.png")
        self.white_strip = pygame.image.load("white_strip.jpg")
        self.white = pygame.transform.scale(self.white_strip,(self.width , self.height))

        
        
        
    def draw(self,screen):
        for y in range(0,self.height,150):
            screen.blit(self.yellow_strip,(400,y))

        screen.blit(self.white, (100, 0))
        screen.blit(self.white, (700, 0))



if __name__=='__main__':
    pygame.init()

    width,height = 800,600
    screen = pygame.display.set_mode((width,height))

    pygame.display.set_caption("Car Game")

    enemycar = Enemycar(width , height)
    grass = Grass()
    track = Track(width , height)
    drawables = (enemycar , grass , track )
    

while True:        
    screen.fill((128,128,128))
    for drawable in drawables:
        drawable.draw(screen)
    
    pygame.display.update()
    pygame.time.Clock().tick(70)

