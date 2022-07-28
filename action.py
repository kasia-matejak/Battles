import pygame
from pygame.locals import *
from characters import Wizzard, Knight

# tworzę postaci
knight = Knight()
wizzard = Wizzard()

pygame.init()
window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Battles")

run = True
background = pygame.image.load("background.jpg")
height = 50
width = 50

while run:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif wizzard.check_if_alive() == False:
            print("Knight has killed wizzard. Long live the king!")
            run = False
        elif knight.check_if_alive() == False:
            print("Wizzard has killed the knight. Let there be anarchy")
            run = False
        elif event.type == KEYDOWN:
            if event.key == K_SPACE:
                wizzard.attack(knight)
            elif event.key == K_RETURN:
                knight.attack(wizzard)

    wizzard_icon = pygame.Rect(wizzard.position_x, wizzard.position_y, width, height)
    knight_icon = pygame.Rect(knight.position_x, knight.position_y, width, height)

    window.blit(background, (0, 0))
    pygame.draw.rect(window, (51, 102, 0), wizzard_icon)
    pygame.draw.rect(window, (102, 0, 51), knight_icon)

    # poruszanie się czarodzieja - wasd, spacja
    if pygame.key.get_pressed()[pygame.K_w]:
        wizzard.move_up()
    if pygame.key.get_pressed()[pygame.K_a]:
        wizzard.move_left()
    if pygame.key.get_pressed()[pygame.K_s]:
        wizzard.move_down()
    if pygame.key.get_pressed()[pygame.K_d]:
        wizzard.move_right()

    # poruszanie się rycerza - strzałki, enter
    if pygame.key.get_pressed()[pygame.K_UP]:
        knight.move_up()
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        knight.move_left()
    if pygame.key.get_pressed()[pygame.K_DOWN]:
        knight.move_down()
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        knight.move_right()

    pygame.display.update()
