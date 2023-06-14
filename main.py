import pygame
import setup as set
import maps as maps


#PYGAME AND MIXER
pygame.init()
pygame.mixer.init()

path_music = set.dir_path + "\Music\ "
path_music = path_music.strip()


class Display():

    def __init__(self, map):
        
        self.event = ""
        self.type = map["TYPE"]
        self.background = pygame.transform.scale(map["BACKGROUND"], (set.SCREEN_WIDTH, set.SCREEN_HEIGHT))
        self.playlist = map["THEME"]
        set_theme(self.playlist)
        try:
            self.buttons = map["BUTTONS"]
            self.select = self.buttons[0]
        except KeyError:
            self.buttons = False  
            self.select = False 
        try:
            self.cursor = map["CURSOR"]
        except KeyError:
            self.cursor = False


    def draw(self):
        set.screen.blit(self.background, (0,0))
        if self.buttons != False:
            for button in self.buttons:
                button.draw()
        if self.cursor != False:
            map.cursor.draw(self.select)
        
    def play_theme(self, volume):
        pygame.mixer.music.set_volume(volume)
        if not pygame.mixer.music.get_busy():
            set_theme(self.playlist)
            pygame.mixer.music.play()

def set_theme(playlist):
    if pygame.mixer.music.get_busy():
        for theme in playlist:
            pygame.mixer.music.queue(path_music + theme)
    else:
        pygame.mixer.music.load(path_music + playlist[0])
        if len(playlist) > 1:
            for i in range(1, len(playlist)):
                pygame.mixer.music.queue(path_music + playlist[i])


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


volume = 0.5
map = Display(maps.menu)
run = True

while run:

    map.draw()
    map.play_theme(volume)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            run, map = input_handler(event, map)
                
    pygame.mouse.set_visible(False)
    pygame.display.update()

