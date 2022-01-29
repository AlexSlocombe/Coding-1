#Ghost icon attributed to 'Freepik' via 'flaticon.com'

import pygame
pygame.init()

#Creating game screen
screen = pygame.display.set_mode((800, 1000))

# Title and Icon
pygame.display.set_caption("Red Light, Green Light")
icon = pygame.image.load('traffic lights.png')
pygame.display.set_icon(icon)

#Player 1 image
player1Img = pygame.image.load('cyan square.png')
player1Img = pygame.transform.scale(player1Img, (20,20))
player1X = 190
player1Y = 900
player1X_change = 0
player1Y_change = 0

#Player 2 image
player2Img = pygame.image.load('redsquare.jpg')
player2Img = pygame.transform.scale(player2Img, (20,20))
player2X = 590
player2Y = 900
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
        borderHorizontal = pygame.draw.rect(screen, (255, 255, 255),(0, 98, 800, 4))
        borderVertical = pygame.draw.rect(screen, (255, 255, 255),(398, 100, 4, 900))

        #Drawing traffic lights
        orangeLight = pygame.draw.circle(screen, (255,165,0), (400,50), 30)
        redLight = pygame.draw.circle(screen, (255, 0, 0), (320,50), 30)
        greenLight = pygame.draw.circle(screen, (0, 255, 0), (480, 50), 30)


        # Recognising player 1 key presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player1X_change = -0.1
            if event.key == pygame.K_d:
                player1X_change = 0.1
            if event.key == pygame.K_w:
                player1Y_change = -0.1
            if event.key == pygame.K_s:
                player1Y_change = 0.1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d or event.key == pygame.K_w or event.key == pygame.K_s:
                player1X_change = 0
                player1Y_change = 0

        # Recognising player 2 key presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player2X_change = -0.1
            if event.key == pygame.K_RIGHT:
                player2X_change = 0.1
            if event.key == pygame.K_UP:
                player2Y_change = -0.05
            if event.key == pygame.K_DOWN:
                player2Y_change = 0.05
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
    elif player1X >=378:
        player1X = 378
    if player1Y >= 980:
        player1Y = 980
 
    #Player 2 movement
    player2X += player2X_change
    player2Y += player2Y_change
    player2(player2X, player2Y)

    #Player 2 boundaries
    if player2X <= 402:
        player2X = 402
    elif player2X >= 780:
        player2X = 780
    player2Y += player2Y_change
    if player2Y >= 980:
        player2Y = 980

    pygame.display.update()
