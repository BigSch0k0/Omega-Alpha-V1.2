
scenes:list = []
sceneCurrent:int = 0
sceneProperty:list = []


def initSceneSystem(fileContent) -> None: #To Do
    pass


def addSceneProperty(entity:list) -> None:

    sceneProperty.add(entity)


def deleteSceneEntity(entityID:str) -> None:

    for entity in sceneProperty:
        if entity[-1] == entityID:
            sceneProperty.remove(entity)


def loadScene(sceneID:int) -> None:

    sceneCurrent = sceneID
    sceneProperty.append(scenes[sceneID])

