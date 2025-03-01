import pygame
import setup
import misc

SCREEN = setup.SCREEN
SCALE_X = setup.SCALE_X
SCALE_Y = setup.SCALE_Y
SCREEN_WIDTH = setup.SCREEN_WIDTH
SCREEN_HEIGHT = setup.SCREEN_HEIGHT

Button = misc.Button
Cursor = misc.Cursor

font = setup.font

player_characters = []
player_positions = [(400*SCALE_X, 550*SCALE_Y), (400*SCALE_X, 700*SCALE_Y), (400*SCALE_X, 850*SCALE_Y), #front row up and down
                    (300*SCALE_X, 600*SCALE_Y), (300*SCALE_X, 800*SCALE_Y)] #back row up and down
unit_size = (75*2*SCALE_X, 100*2*SCALE_Y) #2x because shitty unit images lol
player_name_positions = [(200*SCALE_X, 10*SCALE_Y), (200*SCALE_X, 60*SCALE_Y), (200*SCALE_X, 110*SCALE_Y),
                         (200*SCALE_X, 160*SCALE_Y), (200*SCALE_X, 210*SCALE_Y)]
name_size = (80*SCALE_X, 30*SCALE_Y)
hp_bar_positions = [(300*SCALE_X, 10*SCALE_Y),(300*SCALE_X, 60*SCALE_Y), (300*SCALE_X, 110*SCALE_Y),
                    (300*SCALE_X, 160*SCALE_Y), (300*SCALE_X, 210*SCALE_Y)]
hp_bar_size = (200*SCALE_X, 30*SCALE_Y)


class Player_Character():

    def __init__(self, stats, i):
        self.stats = stats
        self.index = i

        self.image = self.stats["BASE_IMAGE"]
        self.rect = self.image.get_rect()
        self.hp = self.stats["HP"]
        self.name = self.stats["NAME"]

        self.name_display = font.render(self.name, True, (0,0,0))
        self.name_display = pygame.transform.scale(self.name_display, name_size)

        self.action = False
        self.access = False
        self.victim = False
        self.alive = True

        self.scale(0)

    def draw(self):

        SCREEN.blit(self.image, self.rect)
        SCREEN.blit(self.name_display, (player_name_positions[self.index], name_size))

        pygame.draw.rect(SCREEN, (200,0,0), (hp_bar_positions[self.index], hp_bar_size))
        pygame.draw.rect(SCREEN, (0,200,0), (hp_bar_positions[self.index], (hp_bar_size[0]*(self.hp/self.stats["HP"]), hp_bar_size[1])))

    def scale(self, rotation):
        self.image = pygame.transform.scale(self.image, unit_size)
        self.image = pygame.transform.rotate(self.image, rotation)
        self.rect = self.image.get_rect()
        self.rect.topleft = player_positions[self.index]


def teamup(characters):
    for i, c in enumerate(characters):
        characters[i] = Player_Character(c, i)

    return characters

def player_turn(character):
    print("pabas")



BATTLE_UI_BUTTONS = [Button(50*SCALE_X,20*SCALE_Y,120*SCALE_X,100*SCALE_Y, 0, image=setup.attack, mask=True, 
                        function=["ATTACK"], cursor=["left",40,40,270], type="FUNCTION"),
                    Button(50*SCALE_X,150*SCALE_Y,120*SCALE_X,100*SCALE_Y, 0, image=setup.special, mask=True, 
                        function=["QUIT"], cursor=["left",40,40,270], type="FUNCTION"),
                    Button(50*SCALE_X,280*SCALE_Y,120*SCALE_X,100*SCALE_Y, 0, image=setup.formation,mask=True,
                        function=["QUIT"], cursor=["left",40,40,270],type="FUNCTION")]

BATTLE_UI = [(pygame.Rect(0, 0, SCREEN_WIDTH, 250*SCALE_Y), (50,0,100)), (pygame.Rect(525*SCALE_X, 0, 225*SCALE_X, 250*SCALE_Y), (0,0,75))]
BATTLE_CURSOR = Cursor(image=setup.menu_cursor, mask=False)
BATTLE_STATES = [[["ACCESS", BATTLE_UI_BUTTONS[0]], ["ACCESS", BATTLE_UI_BUTTONS[1]], ["ACCESS", BATTLE_UI_BUTTONS[2]], ["VISIBLE", BATTLE_CURSOR]],
                 [["UNACCESS", BATTLE_UI_BUTTONS[0]], ["UNACCESS", BATTLE_UI_BUTTONS[1]], ["UNACCESS", BATTLE_UI_BUTTONS[2]], ["UNVISIBLE", BATTLE_CURSOR]]]


#UNITS

path = setup.path

path_dwarves = path + r"units\dwarves\ "
path_dwarves = path_dwarves.strip() 

fighter = {}
fighter["BASE_IMAGE"] = pygame.image.load(path_dwarves + "fighter.png")
fighter["NAME"] = "FIGHTER"
fighter["HP"] = 100
fighter["ATTACK"] = 10

sentry = {}
sentry["BASE_IMAGE"] = pygame.image.load(path_dwarves + "scout.png")
sentry["NAME"] = "SENTRY"
sentry["HP"] = 80
sentry["ATTACK"] = 5

vanguard = {}
vanguard["BASE_IMAGE"] = pygame.image.load(path_dwarves + "guard.png")
vanguard["NAME"] = "VANGUARD"
vanguard["HP"] = 120
vanguard["ATTACK"] = 8

path_outlaws = path + r"units\human-outlaws\ "
path_outlaws = path_outlaws.strip()

footbad = {}
footbad["BASE_IMAGE"] = pygame.image.load(path_outlaws + "footpad.png")
footbad["NAME"] = "FOOTBAD"
footbad["HP"] = 60
footbad["ATTACK"] = 1

ruffian = {}
ruffian["BASE_IMAGE"] = pygame.image.load(path_outlaws + "thug.png")
ruffian["NAME"] = "RUFFIAN"
ruffian["HP"] = 90
ruffian["ATTACK"] = 8

poacher = {}
poacher["BASE_IMAGE"] = pygame.image.load(path_outlaws + "poacher.png")
poacher["NAME"] = "POACHER"
poacher["HP"] = 70
poacher["ATTACK"] = 2

mugger = {}
mugger["BASE_IMAGE"] = pygame.image.load(path_outlaws + "thief.png")
mugger["NAME"] = "MUGGER"
mugger["HP"] = 50
mugger["ATTACK"] = 3

path_elves = path + r"units\elves-wood\ "
path_elves = path_elves.strip()

archer = {}
archer["BASE_IMAGE"] = pygame.image.load(path_elves + "archer.png")
archer["NAME"] = "ARCHER"
archer["HP"] = 50
archer["ATTACK"] = 3

warrior = {}
warrior["BASE_IMAGE"] = pygame.image.load(path_elves + "fighter.png")
warrior["NAME"] = "WARRIOR"
warrior["HP"] = 70
warrior["ATTACK"] = 7

shaman = {}
shaman["BASE_IMAGE"] = pygame.image.load(path_elves + "shaman.png")
shaman["NAME"] = "SHAMAN"
shaman["HP"] = 30
shaman["ATTACK"] = 1