import pygame

def event_handler(function, map):
    if type(function) is dict:
        map = Display(function)
    if function == "QUIT":
        return False, map
    return True, map

def input_handler(event, map):
    run = True

    if map.type == "MENU":
        
        i = map.buttons.index(map.select)

        if event.key == pygame.K_ESCAPE:
            run = False
        if event.key == pygame.K_RETURN and map.select != False: 
            run, map = event_handler(map.select.function, map)
        if event.key == pygame.K_DOWN or event.key == pygame.K_RIGHT:
            if i < (len(map.buttons)-1):
                map.select = map.buttons[i+1]
        if event.key == pygame.K_UP or event.key == pygame.K_LEFT:
            if i > 0:
                map.select = map.buttons[i-1]
            


    return run, map