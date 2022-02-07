#Ghost icon attributed to 'Freepik' via 'flaticon.com'
#8 Bit Music (loop) by Alexander Blu via 'orangefreesounds.com/8-bit-music-loop/'

from contextlib import redirect_stderr
import random
import math
import pygame
from pygame import mixer
pygame.init()

#Creating game screen
winWidth = 400
winHeight = 500
screen = pygame.display.set_mode((winWidth, winHeight))

#Loading music
mixer.music.load('8-bit-music-loop.mp3')
mixer.music.play(-1)

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
enemy1X = random.randint(5, 160)
enemy1Y = random.randint(100, 200)
enemy1X_change = 0.07

#Enemy 2 image
enemy2Img = pygame.image.load('ghost.png')
enemy2Img = pygame.transform.scale(enemy2Img, (enemyWidth, enemyHeight))
enemy2X = random.randint(205, 360)
enemy2Y = random.randint(100, 200)
enemy2X_change = 0.07

#Enemy 3 image
enemy3Img = pygame.image.load('ghost.png')
enemy3Img = pygame.transform.scale(enemy2Img, (enemyWidth, enemyHeight))
enemy3X = random.randint(5, 160)
enemy3Y = random.randint(250, 350)
enemy3X_change = 0.07

#Enemy 4 image
enemy4Img = pygame.image.load('ghost.png')
enemy4Img = pygame.transform.scale(enemy2Img, (enemyWidth, enemyHeight))
enemy4X = random.randint(205, 360)
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
player1Score_value = 0
player2Score_value = 0 
fontScore = pygame.font.Font('EightBitDragon-anqx.ttf', 26) 
fontWin = pygame.font.Font('EightBitDragon-anqx.ttf', 32) 
fontRestart = pygame.font.Font('EightBitDragon-anqx.ttf', 16) 

def show_player1Score(x, y):
    player1Score = fontScore.render(str(player1Score_value), True, (255, 255, 255))
    screen.blit(player1Score, (x, y))

def show_player2Score(x, y):
    player2Score = fontScore.render(str(player2Score_value), True, (255, 255, 255))
    screen.blit(player2Score, (x, y))

#Game over
def show_gameOver(x, y):
    gameOver = fontWin.render(str("GAME OVER"), True, (255, 255, 255))
    screen.blit(gameOver, (x, y))

def show_Restart(x, y):
    restart = fontRestart.render(str("PRESS R TO RESTART"), True, (255, 255, 255))
    screen.blit(restart, (x, y))

def show_player1Win(x, y):
    player1Win = fontWin.render(str("PLAYER 1 WINS!"), True, (255, 255, 255))
    screen.blit(player1Win, (x, y))

def show_player2Win(x, y):
    player2Win = fontWin.render(str("PLAYER 2 WINS!"), True, (255, 255, 255))
    screen.blit(player2Win, (x, y))

#Start screen

def show_RedLight(x, y):
    redLight = fontScore.render(str("RED LIGHT, "), True, (255, 0, 0))
    screen.blit(redLight, (x, y))

def show_GreenLight(x, y):
    greenLight = fontScore.render(str("GREEN LIGHT"), True, (0, 255, 0))
    screen.blit(greenLight, (x, y))

def show_instruction1(x, y):
    instruction1 = fontRestart.render(str("RACE TO THE TOP"), True, (255, 255, 255))
    screen.blit(instruction1, (x, y))

def show_instruction2(x, y):
    instruction2 = fontRestart.render(str("DON'T MOVE ON A RED  LIGHT"), True, (255, 255, 255))
    screen.blit(instruction2, (x, y))

def show_instruction3(x, y):
    instruction3 = fontRestart.render(str("DON'T TOUCH THE GUARDS"), True, (255, 255, 255))
    screen.blit(instruction3, (x, y))

def show_instruction4(x, y):
    instruction4 = fontRestart.render(str("PRESS SPACE TO BEGIN"), True, (255, 255, 255))
    screen.blit(instruction4, (x, y))

#Loading in key images
arrowKeysImg = pygame.image.load('ArrowKeys.png')
arrowKeysImg = pygame.transform.scale(arrowKeysImg, (120, 80))

def arrowKeys(x,y):
    screen.blit(arrowKeysImg, (x,y))

WASDKeysImg = pygame.image.load('WASDKeys.png')
WASDKeysImg = pygame.transform.scale(WASDKeysImg, (120, 80))

def WASDKeys(x,y):
    screen.blit(WASDKeysImg, (x,y))

#Traffic light colours
brightAmber = (255, 198, 0)
dimAmber = (85, 66, 0)
brightRed = (255, 0, 0)
dimRed = (85 , 0, 0)
brightGreen = (0, 255, 0)
dimGreen = (0, 85, 0)

count = 0

greenTime = random.randint(1, 6)
redTime = greenTime + 1 + random.randint(1, 6)

#Start-screen loop
start = True
while start:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                start = False
                running = True
    show_RedLight(40, 100)
    show_GreenLight(200, 100)
    show_instruction1(120, 200)
    show_instruction2(70, 240)
    show_instruction3(80, 280)
    show_instruction4(90, 320)
    arrowKeys(250, 400)
    WASDKeys(30, 400)

    pygame.display.update()

#Main game loop
while running:
    #Background colour
    screen.fill((0,0,0))

    #Drawing game board
    borderHorizontal = pygame.draw.rect(screen, (255, 255, 255),(0, 49, 400, 2))
    borderVertical = pygame.draw.rect(screen, (255, 255, 255),(199, 50, 2, 450))
    
    #Changing traffic light colours
    greenColor = brightGreen
    amberColor = dimAmber
    redColor = dimRed
    if count >= greenTime:
        greenColor = dimGreen
        amberColor = brightAmber
        redColor = dimRed
    if count >= greenTime + 1:
        greenColor = dimGreen
        amberColor = dimAmber
        redColor = brightRed
    if count >= redTime:
        count = 0
        greenTime = random.randint(1,6)
        redTime = greenTime + 1 + random.randint(1,6)
    count += 0.0006
    
    #Pausing and playing music
    if redColor == brightRed:
        pygame.mixer.music.set_volume(0.2)
    else:
        pygame.mixer.music.set_volume(1)

    #Drawing traffic lights
    amberLight = pygame.draw.circle(screen, amberColor, (200,25), 15)
    redLight = pygame.draw.circle(screen, redColor, (160, 25), 15)
    greenLight = pygame.draw.circle(screen, greenColor, (240, 25), 15)

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

    # Player 1 Collision
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

#Player red-light movement:
    if redColor == brightRed and player1X_change != 0:
        player1X = winWidth/4 - playerWidth/2
        player1Y = winHeight - 50
    if redColor == brightRed and player1Y_change != 0:
        player1X = winWidth/4 - playerWidth/2
        player1Y = winHeight - 50
    if redColor == brightRed and player2X_change != 0:
        player2X = winWidth*0.75 - playerWidth/2
        player2Y = winHeight - 50
    if redColor == brightRed and player2Y_change != 0:
        player2X = winWidth*0.75 - playerWidth/2
        player2Y = winHeight - 50

    #Finish line
    if player1Y < 50:
        player1X = winWidth/4 - playerWidth/2
        player1Y = winHeight - 50
        player2X = winWidth*0.75 - playerWidth/2
        player2Y = winHeight - 50
        player1Score_value += 1
        enemy1X = random.randint(1, 160)
        enemy1Y = random.randint(100, 200)
        enemy2X = random.randint(201, 360)
        enemy2Y = random.randint(100, 200)
        enemy3X = random.randint(1, 160)
        enemy3Y = random.randint(250, 350)
        enemy4X = random.randint(201, 360)
        enemy4Y = random.randint(250, 350)
    
    if player2Y < 50:
        player2X = winWidth*0.75 - playerWidth/2
        player2Y = winHeight - 50
        player1X = winWidth/4 - playerWidth/2
        player1Y = winHeight - 50
        player2Score_value += 1
        greenTime = random.randint(2,4)
        redTime = greenTime + 1 + random.randint(1,4)
        enemy1X = random.randint(1, 160)
        enemy1Y = random.randint(100, 200)
        enemy2X = random.randint(201, 360)
        enemy2Y = random.randint(100, 200)
        enemy3X = random.randint(1, 160)
        enemy3Y = random.randint(250, 350)
        enemy4X = random.randint(201, 360)
        enemy4Y = random.randint(250, 350)
        
    #Score
    show_player1Score(15, 15)
    show_player2Score(370, 15)

    #Game over
    if player1Score_value >= 3:
        show_gameOver(105, 200)
        show_player1Win(65, 260)
        show_Restart(110, 320)
        enemy1X= -35
        enemy2X= -35
        enemy3X = -35
        enemy4X = -35
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_r:
                player1Score_value = 0
                player2Score_value = 0
                enemy1X = random.randint(0, 164)
                enemy1Y = random.randint(100, 200)
                enemy1X_change = 0.07
                enemy2X = random.randint(200, 365)
                enemy2Y = random.randint(100, 200)
                enemy2X_change = 0.07
                enemy3X = random.randint(0, 164)
                enemy3Y = random.randint(250, 350)
                enemy3X_change = 0.07
                enemy4X = random.randint(200, 365)
                enemy4Y = random.randint(250, 350)
                enemy4X_change = 0.07

                
    if player2Score_value >= 3:
        show_gameOver(105, 200)
        show_player2Win(75, 260)
        show_Restart(110, 320)
        enemy1X= -35
        enemy2X= -35
        enemy3X = -35
        enemy4X = -35
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_r:
                player1Score_value = 0
                player2Score_value = 0
                enemy1X = random.randint(0, 164)
                enemy1Y = random.randint(100, 200)
                enemy1X_change = 0.07
                enemy2X = random.randint(200, 365)
                enemy2Y = random.randint(100, 200)
                enemy2X_change = 0.07
                enemy3X = random.randint(0, 164)
                enemy3Y = random.randint(250, 350)
                enemy3X_change = 0.07
                enemy4X = random.randint(200, 365)
                enemy4Y = random.randint(250, 350)
                enemy4X_change = 0.07
    
    pygame.display.update()
