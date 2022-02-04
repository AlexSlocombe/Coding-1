#Ghost icon attributed to 'Freepik' via 'flaticon.com'

from contextlib import redirect_stderr
import random
import time
import math
import pygame
pygame.init()

#Creating game screen
winWidth = 400
winHeight = 500
screen = pygame.display.set_mode((winWidth, winHeight))

# Title and Icon
pygame.display.set_caption("Red Light, Green Light")
icon = pygame.image.load('traffic lights.png')
pygame.display.set_icon(icon)

playerWidth = 10
playerHeight = 10

#Player 1 image
player1Img = pygame.image.load('cyan square.png')
player1Img = pygame.transform.scale(player1Img, (playerWidth, playerHeight))
player1X = winWidth/4 - playerWidth/2
player1Y = winHeight - 50
player1X_change = 0
player1Y_change = 0

#Player 2 image
player2Img = pygame.image.load('redsquare.jpg')
player2Img = pygame.transform.scale(player2Img, (playerWidth, playerHeight))
player2X = winWidth*0.75 - playerWidth/2
player2Y = winHeight - 50
player2X_change = 0
player2Y_change = 0

enemyWidth = 35
enemyHeight = 35

#Enemy 1 image
enemy1Img = pygame.image.load('ghost.png')
enemy1Img = pygame.transform.scale(enemy1Img, (enemyWidth, enemyHeight))
enemy1X = random.randint(0, 164)
enemy1Y = random.randint(100, 200)
enemy1X_change = 0.07

#Enemy 2 image
enemy2Img = pygame.image.load('ghost.png')
enemy2Img = pygame.transform.scale(enemy2Img, (enemyWidth, enemyHeight))
enemy2X = random.randint(200, 365)
enemy2Y = random.randint(100, 200)
enemy2X_change = 0.07

#Enemy 3 image
enemy3Img = pygame.image.load('ghost.png')
enemy3Img = pygame.transform.scale(enemy2Img, (enemyWidth, enemyHeight))
enemy3X = random.randint(0, 164)
enemy3Y = random.randint(250, 350)
enemy3X_change = 0.07

#Enemy 4 image
enemy4Img = pygame.image.load('ghost.png')
enemy4Img = pygame.transform.scale(enemy2Img, (enemyWidth, enemyHeight))
enemy4X = random.randint(200, 365)
enemy4Y = random.randint(250, 350)
enemy4X_change = 0.07

#Enemy 1 function
def enemy1(x,y):
    screen.blit(enemy1Img, (x,y))

#Enemy 2 function
def enemy2(x,y):
    screen.blit(enemy2Img, (x,y))

#Enemy 3 function
def enemy3(x,y):
    screen.blit(enemy3Img, (x,y))

#Enemy 4 function
def enemy4(x,y):
    screen.blit(enemy4Img, (x,y))

#Player 1 function
def player1(x,y):
    screen.blit(player1Img, (x, y))

#Player 2 function
def player2(x,y):
    screen.blit(player2Img, (x, y))

#Collision detection (Player 1)
def isCollision1(enemy1X, enemy1Y, player1X, player1Y):
    distance = math.sqrt((math.pow((enemy1X + 17.5) - (player1X + 5), 2)) + (math.pow((enemy1Y + 17.5) - (player1Y + 5), 2)))
    if distance < (35*math.sqrt(2))/2:
        return True
    else:
        return False
def isCollision3(enemy3X, enemy3Y, player1X, player1Y):
    distance = math.sqrt((math.pow((enemy3X + 17.5) - (player1X + 5), 2)) + (math.pow((enemy3Y + 17.5) - (player1Y + 5), 2)))
    if distance < (35*math.sqrt(2))/2:
        return True
    else:
        return False

#Collision detection (Player 2)
def isCollision2(enemy2X, enemy2Y, player2X, player2Y):
    distance = math.sqrt((math.pow((enemy2X + 17.5) - (player2X + 5), 2)) + (math.pow((enemy2Y + 17.5) - (player2Y + 5), 2)))
    if distance < (35*math.sqrt(2))/2:
        return True
    else:
        return False
def isCollision4(enemy4X, enemy4Y, player2X, player2Y):
    distance = math.sqrt((math.pow((enemy4X + 17.5) - (player2X + 5), 2)) + (math.pow((enemy4Y + 17.5) - (player2Y + 5), 2)))
    if distance < (35*math.sqrt(2))/2:
        return True
    else:
        return False

#Score
player1Score = 0
player2Score = 0  

#Loop allowing the game to run without closing down
running = True
while running:
    #Background colour
    screen.fill((0,0,0))

    #Drawing game board
    borderHorizontal = pygame.draw.rect(screen, (255, 255, 255),(0, 49, 400, 2))
    borderVertical = pygame.draw.rect(screen, (255, 255, 255),(199, 50, 2, 450))


    #Traffic light colours
    orangeR = 0
    orangeG = 0
    orangeB = 0

    redR = 0
    redG = 0
    redB = 0

    greenR = 0
    greenG = 0
    greenB = 0

    # #Changing traffic light colour loop
    # while True:
    #     greenR = 0
    #     greenG = 255
    #     greenB = 0
    #     time.sleep(3)

    #Drawing traffic lights
    orangeLight = pygame.draw.circle(screen, (255, 165, 0), (200,25), 15)
    redLight = pygame.draw.circle(screen, (255, 0, 0), (160, 25), 15)
    greenLight = pygame.draw.circle(screen, (0, 255, 0), (240, 25), 15)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Recognising player 1 key presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player1X_change = -0.025
            if event.key == pygame.K_d:
                player1X_change = 0.025
            if event.key == pygame.K_w:
                player1Y_change = -0.025
            if event.key == pygame.K_s:
                player1Y_change = 0.025
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d or event.key == pygame.K_w or event.key == pygame.K_s:
                player1X_change = 0
                player1Y_change = 0

        # Recognising player 2 key presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player2X_change = -0.025
            if event.key == pygame.K_RIGHT:
                player2X_change = 0.025
            if event.key == pygame.K_UP:
                player2Y_change = -0.025
            if event.key == pygame.K_DOWN:
                player2Y_change = 0.025
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player2X_change = 0
                player2Y_change = 0
    
    #Player1 movement
    player1X += player1X_change
    player1Y += player1Y_change
    player1(player1X, player1Y)

    #Player 1 boundaries
    if player1X <= 0:
        player1X = 0
    elif player1X >= winWidth/2 - playerWidth -1:
        player1X = winWidth/2 - playerWidth -1
    if player1Y >= winHeight - playerHeight:
        player1Y = winHeight - playerHeight
 
    #Player 2 movement
    player2X += player2X_change
    player2Y += player2Y_change
    player2(player2X, player2Y)

    #Player 2 boundaries
    if player2X <= winWidth/2 + 1:
        player2X = winWidth/2 + 1
    elif player2X >= winWidth - playerWidth:
        player2X = winWidth - playerWidth
    if player2Y >= winHeight - playerHeight:
        player2Y = winHeight - playerHeight

    #Enemy 1 movement
    enemy1X += enemy1X_change
    enemy1(enemy1X, enemy1Y)

    #Enemy 1 boundaries
    if enemy1X <= 0:
        enemy1X_change = -enemy1X_change
    elif enemy1X >= winWidth/2 - enemyWidth -1:
        enemy1X_change = -enemy1X_change

    #Enemy 2 movement
    enemy2X += enemy2X_change
    enemy2(enemy2X, enemy2Y)

    #Enemy 2 boundaries
    if enemy2X <= winWidth/2 + 1:
        enemy2X_change = -enemy2X_change
    elif enemy2X >= winWidth - enemyWidth:
        enemy2X_change = -enemy2X_change

    #Enemy 3 movement
    enemy3X += enemy3X_change
    enemy3(enemy3X, enemy3Y)

    #Enemy 3 boundaries
    if enemy3X <= 0:
        enemy3X_change = -enemy3X_change
    elif enemy3X >= winWidth/2 - enemyWidth -1:
        enemy3X_change = -enemy3X_change

    #Enemy 4 movement
    enemy4X += enemy4X_change
    enemy4(enemy4X, enemy4Y)

    #Enemy 4 boundaries
    if enemy4X <= winWidth/2 + 1:
        enemy4X_change = -enemy4X_change
    elif enemy4X >= winWidth - enemyWidth:
        enemy4X_change = -enemy4X_change

    #Player 1 Collision
    collision1 = isCollision1(enemy1X, enemy1Y, player1X, player1Y)
    if collision1:
        player1X = winWidth/4 - playerWidth/2
        player1Y = winHeight - 50
    collision3 = isCollision3(enemy3X, enemy3Y, player1X, player1Y)
    if collision3:
        player1X = winWidth/4 - playerWidth/2
        player1Y = winHeight - 50
    
    #Player 2 Collision
    collision2 = isCollision2(enemy2X, enemy2Y, player2X, player2Y)
    if collision2:
        player2X = winWidth*0.75 - playerWidth/2
        player2Y = winHeight - 50
    collision4 = isCollision4(enemy4X, enemy4Y, player2X, player2Y)
    if collision4:
        player2X = winWidth*0.75 - playerWidth/2
        player2Y = winHeight - 50

    #Finish line
    if player1Y < 50:
        player1X = winWidth/4 - playerWidth/2
        player1Y = winHeight - 50
        player1Score += 1
    if player2Y < 50:
        player2X = winWidth*0.75 - playerWidth/2
        player2Y = winHeight - 50
        player2Score += 1
        print(player2Score)

    pygame.display.update()
