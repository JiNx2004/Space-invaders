import pygame
import random
import math
pygame.init()

#Screen_size
screen=pygame.display.set_mode((800, 600))                           

#Title+Icon
pygame.display.set_caption("Space Invaders")                         
pygame.display.set_icon(pygame.image.load("ufo.png"))

 #Player
playerX=370
playerY=480                                                                  
changeX=0

#Enemy
enemyX=random.randint(0, 735)
enemyY=random.randint(50,150)                                                 
echangeX=-0.3
echangeY=40
    


#Projectile
projX=0
projY=480                                             
pchangeX=0
pchangeY=0.6
pstate="ready"


#Score
score = 0
textX=10
textY=10
font = pygame.font.SysFont(None, 55)


def show_score(x,y):
    score_value = font.render("SCORE:"+str(score), True, (255,255,255))
    screen.blit(score_value,(x,y))
    
    
def proj(x,y):
    global pstate
    pstate = "fire"
    screen.blit(pygame.image.load("bullet.png"),(x,y-10))

def enemy(x,y):
    screen.blit(pygame.image.load("alien.png"),(x,y))

def player(x,y):
    screen.blit(pygame.image.load("spaceship.png") ,(x,y))       
 
#Collision
def iscollision(enemyX,enemyY,projX,projY) :
    distance = math.sqrt(math.pow(enemyX-projX,2) + math.pow(enemyY-projY,2))
    if distance<27:
        return True
    else:
        return False



gexit=True
while gexit:
 
    #Background colour
    screen.fill((0,0,0))                           
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gexit=False
            
        #Player Movement    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                changeX-=0.5
            if event.key == pygame.K_RIGHT:
                changeX+=0.5
            #Projectile Shooting
            if event.key == pygame.K_SPACE and pstate == "ready":
                projX=playerX
                proj(projX,projY)
                
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                changeX=0
            
                

    playerX+=changeX
    if playerX <= 0:
        playerX=0
    if playerX >=736:
        playerX=736
    
    #Enemy Movement
    enemyX+=echangeX
    if enemyX <= 0:
        echangeX=0.3
        enemyY+=echangeY
    if enemyX >=736:
        echangeX=-0.3
        enemyY+=echangeY
        
    #Projectile Movement
    if projY <= 0:
        pstate="ready"
        projY=480
    if pstate == "fire" :
        proj(projX,projY)
        projY-=pchangeY


    #Collision
    collision = iscollision(enemyX, enemyY, projX, projY)
    if collision:
         projY=480
         pstate="ready"
         score+=50
         enemyX=random.randint(0, 735)
         enemyY=random.randint(50,150) 
         

        

    enemy(enemyX,enemyY)    
    player(playerX,playerY)
    show_score(textX,textY)
    pygame.display.update()