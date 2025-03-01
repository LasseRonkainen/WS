import pygame
import maps
import units
import enemies

def input_handler(event, map):

    run = True

    if event.key == pygame.K_ESCAPE:
        run = False

    if map.select:
        i = map.buttons.index(map.select)

    if map.target:        
        i = enemies.enemy_characters.index(map.target)

    if map.type == "MENU" and map.select:

        if event.key == pygame.K_RETURN:
            run, map = menu_handler(map, i)

        if (event.key == pygame.K_DOWN or event.key == pygame.K_RIGHT 
            or event.key == pygame.K_UP or event.key == pygame.K_LEFT):

            map.select = menu_cursor(event, map, i)

    if map.type == "BATTLE":

        if map.current_state == map.states[0]:

            if event.key == pygame.K_RETURN:
                run, map = menu_handler(map, i)
        
            if (event.key == pygame.K_DOWN or event.key == pygame.K_RIGHT 
                or event.key == pygame.K_UP or event.key == pygame.K_LEFT):

                map.select = menu_cursor(event, map, i)

        elif map.current_state == map.states[1]:

            if (event.key == pygame.K_DOWN or event.key == pygame.K_RIGHT 
                or event.key == pygame.K_UP or event.key == pygame.K_LEFT):

                map.target = battle_cursor(event, map, i)

                for e in enemies.enemy_characters:
                    e.target = False
                map.target.target = True

            if event.key == pygame.K_RETURN:
                run, map = battle_handler(map)

            
    return run, map



def menu_handler(map, i):

    function = map.select.function

    #keyword = f[0]
    #object = f[1]

    for f in function:

        if f == "QUIT":
            return False, map

        if f[0] == "MAP":
            map = maps.Display(f[1])

        if f[0] == "CHOOSE_CHARACTER":
            choose_character(map, f[1], i)
            map.select.access = not map.select.access

        if f[0] == "RESET_CHARACTER_CHOISES":       #for loops flipped fidnt work???
            for i,b in enumerate(map.buttons[:9]):
                for u in units.player_characters:
                    if b.function[0][1] == u:
                        choose_character(map,u,i)
                        b.access = not b.access

        if f[0] == "TEAMUP":
            f[1] = units.teamup(f[1])

        if f == "ATTACK" and map.battle_turn:

            map.current_state = maps.state_handler(map.states[1])
            map.battle_turn.action = "attack"
            
            for e in enemies.enemy_characters:
                if e.alive and not map.target:
                    map.target = e
                    map.target.target = True

    return True, map



def menu_cursor(event, map, i):

    select = map.select

    if i < 0 or i > len(map.buttons):
        return select

    if event.key == pygame.K_DOWN or event.key == pygame.K_RIGHT:

        if i < (len(map.buttons)-1):
            select = map.buttons[i+1]

            if not select.access:
                select = menu_cursor(event,map,i+1)

    if event.key == pygame.K_UP or event.key == pygame.K_LEFT:

        if i > 0:
            select = map.buttons[i-1]

            if not select.access:
                select = menu_cursor(event,map,i-1)

    return select


def choose_character(map, character, i):

    if units.player_characters.count(character):
        units.player_characters.remove(character)
    else:
        units.player_characters.append(character)

    if len(units.player_characters) == 3:
        map.current_state = maps.state_handler(map.states[1])
    else:
        map.current_state = maps.state_handler(map.states[0])
                
    for count, b in enumerate(map.buttons):
        
        if i < 3 and count < 3:
            b.access = not b.access
        if i > 2 and count > 2 and i < 6 and count < 6:
            b.access = not b.access
        if i > 5 and count > 5 and count < 9:
            b.access = not b.access

def battle_handler(map):

    if map.battle_turn.action == "attack":
        attack(map)

    return True, map



def battle_cursor(event, map, i):

    select = enemies.enemy_characters[i]

    if i < 0 or i > len(enemies.enemy_characters):
        return select

    elif event.key == pygame.K_DOWN or event.key == pygame.K_RIGHT:

        if i < (len(enemies.enemy_characters)-1):
            select = enemies.enemy_characters[i+1]

            if not select.alive:
                select = battle_cursor(event,map,i+1)        

    elif event.key == pygame.K_UP or event.key == pygame.K_LEFT:

        if i > 0:
            select = enemies.enemy_characters[i-1]

            if not select.alive:
                select = battle_cursor(event,map,i-1)

    return select

def attack(map):
    
    if units.player_characters.count(map.battle_turn):
        pass