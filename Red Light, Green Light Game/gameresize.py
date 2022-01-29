#Ghost icon attributed to 'Freepik' via 'flaticon.com'

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

#Player 1 function
def player1(x,y):
    screen.blit(player1Img, (x, y))

#Player 2 function
def player2(x,y):
    screen.blit(player2Img, (x, y))


#Loop allowing the game to run without closing down
running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #Background colour
        screen.fill((0,0,0))

        #Drawing game board
        borderHorizontal = pygame.draw.rect(screen, (255, 255, 255),(0, 49, 400, 2))
        borderVertical = pygame.draw.rect(screen, (255, 255, 255),(199, 50, 2, 450))

        #Drawing traffic lights
        orangeLight = pygame.draw.circle(screen, (255,165,0), (200,25), 15)
        redLight = pygame.draw.circle(screen, (255, 0, 0), (160, 25), 15)
        greenLight = pygame.draw.circle(screen, (0, 255, 0), (240, 25), 15)


        # Recognising player 1 key presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player1X_change = -0.05
            if event.key == pygame.K_d:
                player1X_change = 0.05
            if event.key == pygame.K_w:
                player1Y_change = -0.05
            if event.key == pygame.K_s:
                player1Y_change = 0.05
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d or event.key == pygame.K_w or event.key == pygame.K_s:
                player1X_change = 0
                player1Y_change = 0

        # Recognising player 2 key presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player2X_change = -0.05
            if event.key == pygame.K_RIGHT:
                player2X_change = 0.05
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
    player2Y += player2Y_change
    if player2Y >= winHeight - playerHeight:
        player2Y = winHeight - playerHeight

    pygame.display.update()
