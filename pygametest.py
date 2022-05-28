import sys, pygame

pygame.init()

width, height = 320, 240
size = (width, height)
black = (0, 0, 0)

InterMoveWaitTime = 20
TotalWaitSinceLastMove = 0.0

screen = pygame.display.set_mode(size)

ballgif = pygame.image.load("ball.gif")
ballrect = ballgif.get_rect()
Clock = pygame.time.Clock()
direction = [1, 1]

while 1:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()

    TotalWaitSinceLastMove = TotalWaitSinceLastMove + Clock.get_time()
    if TotalWaitSinceLastMove <= InterMoveWaitTime:
        Clock.tick()
        continue

    TotalWaitSinceLastMove = 0

    ballrect = ballrect.move(direction)
    if ballrect.left < 0 or ballrect.right > width:
        direction[0] = -direction[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        direction[1] = -direction[1]

    screen.fill(black)
    screen.blit(ballgif, ballrect)
    pygame.display.flip()

    Clock.tick()

pygame.quit()