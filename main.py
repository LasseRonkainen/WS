import pygame
import functions
import maps

pygame.init()
pygame.mixer.init()


volume = 0.1
map = maps.Display(maps.menu)
run = True
pygame.mouse.set_visible(False)


while run:

    map.draw()
    map.play_theme(volume)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == maps.MUSIC_END:
            maps.music_queue.pop(0)

        if event.type == pygame.KEYDOWN:
            run, map = functions.input_handler(event, map)
                
    pygame.display.update()

