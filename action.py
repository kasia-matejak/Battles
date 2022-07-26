import pygame
from pygame.locals import *

pygame.init()
window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Battles")

run = True
background = pygame.image.load("background.jpg")
height = 50
width = 50
w_position_x=220
w_position_y=1
k_position_x=250
k_position_y=450

#wizzard_image = pygame.image.load("wizzard.png")
#knight_image = pygame.image.load("knight.png")
#wizzard_location = wizzard_image.get_rect()
#wizzard_location = w_position_x, w_position_y
wizzard = pygame.Rect(w_position_x, w_position_y, width, height)
knight = pygame.Rect(k_position_x, k_position_y, width, height)

while run:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           run = False
        elif event.type == KEYDOWN:
            if event.key == K_SPACE:
                print("Fight WIZZARD")
            elif event.key == K_RETURN:
                print("Fight KNIGHT!")

    window.blit(background, (0,0))
    #window.blit(wizzard_image, wizzard_location)
    pygame.draw.rect(window, (153, 204, 255), wizzard)
    pygame.draw.rect(window, (102, 0, 51), knight)
    
    #poruszanie się czarodzieja
    if pygame.key.get_pressed() [pygame.K_w]:
        wizzard.y -= 1
    if pygame.key.get_pressed() [pygame.K_a]:
        wizzard.x -= 1
    if pygame.key.get_pressed() [pygame.K_s]:
        wizzard.y += 1
    if pygame.key.get_pressed() [pygame.K_d]:
        wizzard.x += 1

    #poruszanie się rycerza
    if pygame.key.get_pressed() [pygame.K_UP]:
        knight.y -= 1
    if pygame.key.get_pressed() [pygame.K_LEFT]:
        knight.x -= 1
    if pygame.key.get_pressed() [pygame.K_DOWN]:
        knight.y += 1
    if pygame.key.get_pressed() [pygame.K_RIGHT]:
        knight.x += 1
        
    pygame.display.update()
