import pygame 
import setup
import units
import enemies
import misc

SCREEN = setup.SCREEN
SCALE_X = setup.SCALE_X
SCALE_Y = setup.SCALE_Y
SCREEN_WIDTH = setup.SCREEN_WIDTH
SCREEN_HEIGHT = setup.SCREEN_HEIGHT

Button = misc.Button
Cursor = misc.Cursor

path_music = setup.dir_path + "\Music\ "
path_music = path_music.strip()

MUSIC_END = pygame.USEREVENT+1
music_queue = []

class Display():

    def __init__(self, map):

        self.type = map["TYPE"]
        self.background = pygame.transform.scale(map["BACKGROUND"], (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.playlist = map["THEME"]
        
        self.battle_turn = False
        self.target = False



        try:
            self.buttons = map["BUTTONS"]
            self.select = self.buttons[0]
            self.cursor = map["CURSOR"]

        except KeyError:
            if self.type == "BATTLE":
                self.buttons = units.BATTLE_UI_BUTTONS
                self.select = self.buttons[0]
                self.cursor = units.BATTLE_CURSOR

            else:
                self.buttons = False  
                self.select = False 
                self.cursor = False

        try:
            self.ui = map["UI"]

        except KeyError:
            if self.type == "BATTLE":
                self.ui = units.BATTLE_UI

            else:
                self.ui = False

        try:
            self.states = map["STATES"]
            state_handler(self.states[0])
            self.current_state = self.states[0]

        except KeyError:
            if self.type == "BATTLE":
                self.states = units.BATTLE_STATES
                state_handler(self.states[0])
                self.current_state = self.states[0]
                
            else:
                self.states = False
                self.current_state = False

        try:
            if self.playlist[0] != music_queue[0]:
                pygame.mixer.music.fadeout(300)

        except IndexError:
            pass


    def draw(self):
        SCREEN.blit(self.background, (0,0))

        if self.ui:
            for ui in self.ui:
                pygame.draw.rect(SCREEN, ui[1], ui[0])

        if self.buttons:
            for button in self.buttons:
                button.draw()
            self.cursor.draw(self.select)

        if self.type == "BATTLE":

            for u in units.player_characters:
                u.draw()
            for e in enemies.enemy_characters:
                e.draw()

            self.turn_handler()

    def turn_handler(self):

        for u in units.player_characters:
            if not u.action and not self.battle_turn:
                self.battle_turn = u

        for e in enemies.enemy_characters:
            if not e.action and not self.battle_turn:
                self.battle_turn = e

    def play_theme(self, volume):
        pygame.mixer.music.set_volume(volume)

        if not pygame.mixer.music.get_busy():
            set_theme(self.playlist)
            pygame.mixer.music.play()

def set_theme(playlist):

    if pygame.mixer.music.get_busy():
        for theme in playlist:
            pygame.mixer.music.queue(path_music + theme)
            music_queue.append(theme)
    else:
        pygame.mixer.music.load(path_music + playlist[0])
        music_queue.append(playlist[0])
        if len(playlist) > 1:
            for i in range(1, len(playlist)):
                pygame.mixer.music.queue(path_music + playlist[i])
                music_queue.append(playlist[i])
                
    pygame.mixer.music.set_endevent(MUSIC_END)


def state_handler(state):

    #keyword = state[0]
    #object = state[1]

    for s in state:

        if s[0] == "UNACCESS":
            s[1].access = False

        if s[0] == "ACCESS":
            s[1].access = True

        if s[0] == "UNVISIBLE":
            s[1].visible = False
        
        if s[0] == "VISIBLE":
            s[1].visible = True

    return state


character_choosing = {"TYPE": "MENU"}
menu = {"TYPE": "MENU"}
battle = {"TYPE": "BATTLE"}

menu["BUTTONS"] = [Button(400,475,500,200, 0, image=setup.new_game, mask=True, 
                          function=[["MAP", character_choosing]], cursor=["left",150,150,270], type="FUNCTION"),
                   Button(400,725,500,200, 0, image=setup.quit, mask=True, 
                          function=["QUIT"], cursor=["left",150,150,270], type="FUNCTION")]

menu["CURSOR"] = Cursor(image=setup.menu_cursor, mask=False)
menu["BACKGROUND"] = setup.menu_background
menu["THEME"] = ["The Dragon Spreads it's Wings.mp3"]

character_choosing["BUTTONS"] = [Button(200, 50, 200, 200, 0, cursor=["top",100,100,180], 
                                        image=units.fighter["BASE_IMAGE"], mask=False, 
                                        function=[["CHOOSE_CHARACTER", units.fighter]], type="CHOOSE_CHARACTER"),
                                Button(500, 50, 200, 200, 0, cursor=["top",100,100,180], 
                                       image=units.sentry["BASE_IMAGE"], mask=False, 
                                       function=[["CHOOSE_CHARACTER", units.sentry]], type="CHOOSE_CHARACTER"),
                                Button(800, 50, 200, 200, 0, cursor=["top",100,100,180], 
                                        image=units.vanguard["BASE_IMAGE"], mask=False, 
                                        function=[["CHOOSE_CHARACTER", units.vanguard]], type="CHOOSE_CHARACTER"),
                                Button(200, 250, 200, 200, 0, cursor=["top",100,100,180], 
                                       image=units.ruffian["BASE_IMAGE"], mask=False, 
                                       function=[["CHOOSE_CHARACTER", units.ruffian]], type="CHOOSE_CHARACTER"),
                                Button(500, 250, 200, 200, 0, cursor=["top",100,100,180], 
                                       image=units.footbad["BASE_IMAGE"], mask=False, 
                                       function=[["CHOOSE_CHARACTER", units.footbad]], type="CHOOSE_CHARACTER"),
                                Button(800, 250, 200, 200, 0, cursor=["top",100,100,180], 
                                       image=units.mugger["BASE_IMAGE"], mask=False, 
                                       function=[["CHOOSE_CHARACTER", units.mugger]], type="CHOOSE_CHARACTER"),
                                Button(200, 450, 200, 200, 0, cursor=["top",100,100,180], 
                                       image=units.warrior["BASE_IMAGE"], mask=False, 
                                       function=[["CHOOSE_CHARACTER", units.warrior]], type="CHOOSE_CHARACTER"),
                                Button(500, 450, 200, 200, 0, cursor=["top",100,100,180], 
                                       image=units.archer["BASE_IMAGE"], mask=False, 
                                       function=[["CHOOSE_CHARACTER", units.archer]], type="CHOOSE_CHARACTER"),
                                Button(800, 450, 200, 200, 0, cursor=["top",100,100,180], 
                                       image=units.shaman["BASE_IMAGE"], mask=False, 
                                       function=[["CHOOSE_CHARACTER", units.shaman]], type="CHOOSE_CHARACTER"),
                                Button(150,725,400,200, 0, cursor=["left",150,150,270], 
                                       image=setup.back, mask=True, type="FUNCTION",
                                       function=[["RESET_CHARACTER_CHOISES"], ["MAP", menu]]),                         
                                Button(750,725,400,200, 0, cursor=["left",150,150,270], 
                                       image=setup.start, mask=True, function=[["MAP", battle], ["TEAMUP", units.player_characters]], type="FUNCTION")]    
                       
character_choosing["CURSOR"] = Cursor(image=setup.menu_cursor, mask=False)
character_choosing["BACKGROUND"] = setup.menu_background
character_choosing["THEME"] = ["The Dragon Spreads it's Wings.mp3"]
character_choosing["STATES"] = [[["UNACCESS", character_choosing["BUTTONS"][10]]], 
                                [["ACCESS", character_choosing["BUTTONS"][10]]]]

battle["BACKGROUND"] = setup.summer_forest
battle["THEME"] = ["FF5 Battle.mp3", "FF4 Battle.mp3"]


