import pygame
from sys import exit

def counter(count):
    text = font.render("Count: "+str(count), True, 'Black')
    screen.blit(text, [85,40])

count = 0
pygame.init()
screen = pygame.display.set_mode((250,200))
icon = pygame.image.load('counter_icon.png')
pygame.display.set_caption("Counter")
pygame.display.set_icon(icon)
font = pygame.font.SysFont('Poppins', 24, bold= True)
increment = font.render("Increment", True, 'White')
Reset = font.render("Reset", True, 'White')
button1 = pygame.Rect(70,80,110,25)
button2 = pygame.Rect(70,115,110,25)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button1.collidepoint(event.pos):
                count += 1
                counter(count)
            if button2.collidepoint(event.pos):
                count = 0
                counter(count)
            

    screen.fill('White')
    counter(count)
    pygame.draw.rect(screen, 'Grey', button1)
    screen.blit(increment, [80,85])
    pygame.draw.rect(screen, 'Grey', button2)
    screen.blit(Reset, [100,120])

    pygame.display.update()