import pygame
import time
import random

pygame.init()

#colours:
black=(0,0,0)
white=(255,255,255)
red=(225,0,0)
green=(0,255,0)
blue=(0,0,225)
road=(64,64,64)
sky=(135,206,250)
brown=(150,75,0)

#font
font1=pygame.font.Font('sources/Pacifico.ttf',30)
font2=pygame.font.Font('sources/PlayfairDisplay-Black.otf',20)

#dimentions
width=432
height=700

#window
gamedisplay=pygame.display.set_mode((width,height))
clock=pygame.time.Clock()

pygame.display.set_caption('Flappy Bird')
icon=pygame.image.load('sources/icon.png')
pygame.display.set_icon(icon)

#surface
bgimg=pygame.image.load('sources/background.png')
bg=lambda :gamedisplay.blit(bgimg,(0,0))

#floor
floorimg=pygame.image.load('sources/floor.png')
floor=lambda x:gamedisplay.blit(floorimg,(x,650))

#bird
birdimg=pygame.image.load('sources/bird.png')
bird=lambda y,v: gamedisplay.blit(pygame.transform.rotozoom(birdimg,-v*5,1),(70,y))

#pipes
pipe=[
    pygame.image.load('sources/pipup.png'),
    pygame.image.load('sources/pipdown.png')
]

def score(s):
    text=font2.render('Score: '+str(s),True,blue)
    gamedisplay.blit(text,(0,0))

def out(s):
    textface=font1.render(s,True,(225,0,0))
    textrect=textface.get_rect()
    textrect.center=((width/2,height/2))
    gamedisplay.blit(textface,textrect)
    pygame.display.update()
    time.sleep(2)
    game()

def game():
    groundx=0
    birdp=350
    birdv=0
    g=0.25

    points=0
    gamespeed=3
    
    temp1=random.randrange(50,400)
    temp2=random.randrange(50,400)
    pipes=[
        pipe[0].get_rect(midbottom=(width+36,temp1)),
        pipe[0].get_rect(midtop=(width+36,temp1+200)),
        pipe[0].get_rect(midbottom=(36+width*5//3,temp2)),
        pipe[0].get_rect(midtop=(36+width*5//3,temp2+200))
    ]
    
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                birdv=-6
        bg()
        score(points)

        bird(birdp,birdv)

        if pipes[0].x<=-72:
            temp=random.randrange(50,400)
            pipes.append(pipe[0].get_rect(midbottom=(width*4//3-36,temp)))
            pipes.append(pipe[1].get_rect(midtop=(width*4//3-36,temp+200)))
            pipes.pop(0)
            pipes.pop(0)
        for i in range(len(pipes)):
            gamedisplay.blit(pipe[i%2],pipes[i])
        
        floor(groundx)
        floor(groundx+width)
        if groundx<=-width:
            groundx=0
        groundx-=gamespeed

        birdrect=birdimg.get_rect()
        birdrect.x=70
        birdrect.y=birdp
        for p in pipes:
            if birdrect.colliderect(p):
                pygame.draw.rect(gamedisplay,brown,birdrect,2)
                pygame.draw.rect(gamedisplay,brown,p,2)
                out('Crashed into a pipe!!! Score: '+str(points))
            p.x-=gamespeed
        if birdp>=598:
            out('Ground hit!! Score: '+str(points))
        birdp+=birdv
        birdv+=g
        points+=1
        gamespeed+= points%100==0
        pygame.display.update()
        clock.tick(60)
game()
