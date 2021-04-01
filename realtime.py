import time
import pygame
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from pytz import timezone   
pygame.init()
yellow = 255,255,0
screen = pygame.display.set_mode((1250, 650))
myfont = pygame.font.SysFont("Arial", 40) 
myfont2 = pygame.font.SysFont("Arial", 22) 
clock = pygame.time.Clock()
clock.tick(100)
while True:
    screen.fill(yellow)
    from datetime import datetime
    # South Africa
    south_africa = timezone('Africa/Johannesburg')
    sa_time = datetime.now(south_africa)
    sa = sa_time.strftime("%H:%M:%S")
    # Paris
    paris = timezone("Europe/Paris")
    paris_time = datetime.now(paris)
    pt = paris_time.strftime("%H:%M:%S")
    # Perth
    perth = timezone("Australia/Perth")
    perth_time = datetime.now(perth)
    perth2 = perth_time.strftime("%H:%M:%S")
    # LA
    la = timezone("America/Los_Angeles")
    la_time = datetime.now(la)
    losangeles = la_time.strftime("%H:%M:%S")
    # London
    import datetime
    now = datetime.datetime.now()
    realtime = (now.strftime("%H:%M:%S"))
    textsurface1 = myfont.render(sa, True,(0,0,0))
    textsurface = myfont.render(realtime, True, (0, 0, 0))
    textsurface2 = myfont.render(pt,True,(0,0,0))
    textsurface3 = myfont.render(perth2,True,(0,0,0))
    textsurface4 = myfont.render(losangeles,True,(0,0,0))
    # Define labels
    label = myfont2.render("South Africa", True,(255,0,0))
    label2 = myfont2.render("Paris",True,(255,0,0))
    label3 = myfont2.render("London",True,(255,0,0))
    label4 = myfont2.render("Perth", True,(255,0,0))
    label5 = myfont2.render("Los Angeles",True,(255,0,0,))
    # Render labels
    screen.blit(label, (40,60))
    screen.blit(label2,(1125,60))
    screen.blit(label3,(590, 340))
    screen.blit(label4,(60,620))
    screen.blit(label5,(1100,620))
    # Render times
    screen.blit(textsurface1,(20,17)) # South Africa
    screen.blit(textsurface, (550,300)) # London
    screen.blit(textsurface2,(1070,20)) # Paris
    screen.blit(textsurface3,(20, 575)) # Perth
    screen.blit(textsurface4,(1070,575)) # LA 
    pygame.display.update()
    time.sleep(0.9988888888888)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()