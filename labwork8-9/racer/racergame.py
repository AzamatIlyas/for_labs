#Imports
import pygame, sys
from pygame.locals import *
import random, time

#Initialzing 
pygame.init()

#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()

#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
monyespeed = 5
SCORE = 0
money = 0
count = 0
dddd = 0

#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# background phon
background = pygame.image.load("labwork8-9/racer/AnimatedStreet.png")

# backgraund music
pygame.mixer.music.load('labwork8-9/racer/background.wav')
pygame.mixer.music.play(-1)

#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

# class for enemies
class Enemy(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__() 
            self.image = pygame.image.load("labwork8-9/racer/Enemy.png")
            self.rect = self.image.get_rect()
            self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)

        def move(self):
            global SCORE
            global dddd
            self.rect.move_ip(0,SPEED)
            if (self.rect.bottom > 600):
                SCORE += 1
                dddd += 1
                self.rect.top = 0
                self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# class for our player
class Player(pygame.sprite.Sprite):
    # function to generate players car
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("labwork8-9/racer/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
       
    # function for moving
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

# first coin 
class Money5(pygame.sprite.Sprite):
        # first coin
        def __init__(self):
            super().__init__() 
            orig_im = pygame.image.load("labwork8-9/racer/5tenge.png")
            self.image = pygame.transform.scale(orig_im,(20,20))
            self.rect = self.image.get_rect()
            self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)
        # generate first coin randomly
        def move(self):
            global money
            self.rect.move_ip(0,monyespeed)
            if (self.rect.bottom > 600):
                self.rect.top = 0
                self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
                  
# second coin
class Money10(pygame.sprite.Sprite):
        # second coin 
        def __init__(self):
            super().__init__() 
            orig_im = pygame.image.load("labwork8-9/racer/20tenge.png")
            self.image = pygame.transform.scale(orig_im,(30,30))
            self.rect = self.image.get_rect()
            self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)
        # generate second coin randomly
        def move(self):
            global money
            self.rect.move_ip(0,monyespeed)
            if (self.rect.bottom > 600):
                self.rect.top = 0
                self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

#Setting up Sprites        
P1 = Player()
E1 = Enemy()
M1 = Money5()
M2 = Money10()

money1 = pygame.sprite.Group()
money1.add(M1)
money2 = pygame.sprite.Group()
money2.add(M2)

#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(M1)
all_sprites.add(M2)

#Adding a new User event 
# INC_SPEED = pygame.USEREVENT + 1
# pygame.time.set_timer(INC_SPEED, 1000)

running = True

#Game Loop
while running:
      
    #Cycles through all events occuring  
    for event in pygame.event.get():
        # if event.type == INC_SPEED:
        #       SPEED += 0.2      
        if event.type == QUIT:
            pygame.mixer.music.stop()
            running = False

    # score and quantity of coin
    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))
    moneyscore = font_small.render(str(money), True, RED)
    DISPLAYSURF.blit(moneyscore, (360,10))

    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)

    # taking first coin
    if pygame.sprite.spritecollideany(P1, money1):
        pygame.mixer.Sound('labwork8-9/racer/tdn.wav').play()
        # money +=5
        # M1.kill()
        # M2 = Money()
        # moneys.add(M2)
        money += 5
        count += 5
        M1.rect.y = -100 
        M1.rect.x = random.randint(40, SCREEN_WIDTH - 40)
        # money1.empty()
        # money1.add(M2)

    # taking second coin
    if pygame.sprite.spritecollideany(P1, money2):
        pygame.mixer.Sound('labwork8-9/racer/moneytake.wav').play()
        # money +=5
        # M1.kill()
        # M2 = Money()
        # moneys.add(M2)
        money += 10
        count += 10
        M2.rect.y = -100 
        M2.rect.x = random.randint(40, SCREEN_WIDTH - 40)
        # money2.empty()
        # money2.add(M1)

    # increase speed
    if count % 15 >= 0 and count > 14 :
        SPEED += 5
        count = count - 15

    if dddd % 3 == 0 and dddd > 2:
        dddd = 0
        cong = font_small.render("CONGRATULATION", True, RED)
        DISPLAYSURF.blit(cong, (150,150))
        

        

    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound('labwork8-9/racer/crash.wav').play()
          time.sleep(1)
                   
          DISPLAYSURF.fill(RED)
          DISPLAYSURF.blit(game_over, (30,250))
          
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          running = False       
    
    pygame.display.update()
    FramePerSec.tick(FPS)
