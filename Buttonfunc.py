from Renderer import updateEntityInfo
from Screenobject import *
from TKInter import *
import time
from Editorhandle import *
from Scenehandle import sceneProperty


selectedProperty = []
ID:int = -1

def buttonFunction(mouse_clicked:bool):
    global selected
    if mouse_clicked == True and not selected:
        #print("Im here")
        buttonID:str = collide()
        if buttonID == "s_Hyrarchie_NewByStats":
            resetButtons()
            updateSelected([], False)
            createWindow("ENTITY")
        elif buttonID == "New":
            pass
        else:
            for entity in engineButtons:
                if entity[-2] == "type_Entity":
                        if entity[ID] == buttonID:
                            resetButtons()
                            selectButton(entity)
                            time.sleep(0.12)


def selectButton(entity):
    if entity[ID] not in selectedProperty:
        selectedProperty.clear()
        selectedProperty.append(entity[ID])

        entity[5] = red
        for e in sceneProperty:
            if e[5] == entity[ID]:
                preRenderEntities.append(e)
                updateEntityInfo(e)
    else:
        selectedProperty.clear()


def resetButtons():
    engineEntityInfo.clear()
                
    for current in engineButtons:   
        if current[5] == red:
            current[5] = darkgrey
    updateSelected([], False)
    preRenderEntities.clear()
    engineEntityInfo.clear()


def getSelected() -> list:

    return selectedProperty

                

