import pygame
from color import *
from Renderer import *
from Buttonfunc import *
from Editorhandle import *
from TKInter import *
from Scenehandle import sceneProperty

global running 
running = True

gameComponents:list = []
clock = pygame.time.Clock()


def initData() -> None:
    pass


def runtime(screen:pygame.display, gameMode:str = "") -> int:
    global running
    if gameMode == "ENGINE":

        initEngine()
        running = True

        while running:
            gameloop(screen)

    if gameMode == "RELEASE":
        pass
    return 0


#------------------------------------------------------------------------------------------------
#Entry Point
#------------------------------------------------------------------------------------------------

def gameloop(screen:pygame.display) -> None:

    
    global running
    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False
        
    mouse_state:bool = pygame.mouse.get_pressed()[0]
    print(sceneProperty)
    if len(windowData) == 0 :buttonFunction(mouse_state)
    render_EngineDisplay(screen)
    runEditor(screen, mouse_state)
    pygame.display.update()
    clock.tick(144)

#------------------------------------------------------------------------------------------------
#
#------------------------------------------------------------------------------------------------