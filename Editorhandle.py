import pygame
from color import*
from Entity import *
import time
from Renderer import *
from TKInter import windowData
from Scenehandle import sceneProperty


global selected
selected:bool = False

global selectedEntity_ID
selectedEntity_ID:list = []


def runEditor(screen:pygame.display, mouse_clicked:bool) -> None:
    global selected
    global selectedEntity_ID

    if mouse_clicked:
        pos = pygame.mouse.get_pos()
        if isInRange(pos, [400,200,1000,600], 0) and len(windowData) == 0:
            if(len(sceneProperty)) > 0:
                if not selected:
                    resetEngineButtonColor()
                    preRenderEntities.clear()
                    try:
                        initEditorSelect(pos)
                    except AttributeError:
                        updateSelected([], False)
                if selected:
                    updateEntityInfo(sceneProperty[selectedEntity_ID[1]])
                    setData(pos)
    else:
        updateSelected([], False)


def initEditorSelect(pos:list) -> None:
    for entity in sceneProperty:
        if isInRange(pos, entity, 0, True):
            getID(entity)
            updateEngineButton(entity)
            preRenderEntities.append(entity)
            updateSelected(entity, True)

    if(len(selectedEntity_ID)) > 0:
        if isInRange(pos, sceneProperty[selectedEntity_ID[1]], 10, True):
            updateEntityPos(pos)


def updateEngineButton(entity:list) -> None:
    for button in engineButtons:
        if button[-1] == entity[5]:
            button[5] = red


def updateSelected(entity:list, mode:bool = True) -> None:
    global selected
    global selectedEntity_ID

    selected = mode
    if mode:
        selectedEntity = entity
    else:
        selected = False 
        selectedEntity = []
        selectedEntity_ID.clear()


def updateEntityPos(pos:list) -> None:
    sceneProperty[selectedEntity_ID[1]] [entityIndex["xPos"]]  = (pos[0] - 400 - sceneProperty[ selectedEntity_ID[1]] [entityIndex["width"]] / 2)
    sceneProperty[selectedEntity_ID[1]] [entityIndex["yPos"]]  = (pos[1] - 200 - sceneProperty[ selectedEntity_ID[1]] [entityIndex["height"]] / 2)


def isInRange(mouse:list, obj:list, incr:int, editorEntity:bool = False) -> bool:
    x,y = 0,0
    if editorEntity:
        x,y = 400,200
    if mouse[0] <= obj[0] + x + obj[2] + incr and mouse[0] >= obj[0] + x - incr:
        if mouse[1] <= obj[1] + y + obj[3] + incr and mouse[1] >= obj[1] + y - incr:
            #print("here2")
            return True
    return False 


def setData(pos:list) -> None:
    global selectedEntity_ID
    if pygame.mouse.get_pressed()[0]:
        try:
            if isInRange(pos, sceneProperty[selectedEntity_ID[1]], 10, True):
                updateEntityPos(pos)
        except AttributeError:
                pass
    

def resetEngineButtonColor() -> None:
    for button in engineButtons:
        button[5] = darkgrey
        engineEntityInfo.clear()


def getID(entity:list) -> None:
    global selectedEntity_ID
    for i in range(len(sceneProperty)):
        if sceneProperty[i][-1] == entity[-1]: 
            selectedEntity_ID = [sceneProperty[i][-1], i]
        

# // TO DO :

def setFocus(focusPoint:list) -> None:
    pass