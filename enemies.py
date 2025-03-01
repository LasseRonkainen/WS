import pygame
import setup

SCREEN = setup.SCREEN
SCALE_X = setup.SCALE_X
SCALE_Y = setup.SCALE_Y

path = setup.path
font = setup.font

enemy_characters = []
enemy_positions = [(700*SCALE_X, 550*SCALE_Y), (700*SCALE_X, 700*SCALE_Y), (700*SCALE_X, 850*SCALE_Y), #front row up and down
                    (800*SCALE_X, 600*SCALE_Y), (800*SCALE_X, 800*SCALE_Y)] #back row up and down
unit_size = (75*2*SCALE_X, 100*2*SCALE_Y) #2x because shitty unit images lol
enemy_name_positions = [(800*SCALE_X, 10*SCALE_Y), (800*SCALE_X, 60*SCALE_Y), (800*SCALE_X, 110*SCALE_Y),
                         (800*SCALE_X, 160*SCALE_Y), (800*SCALE_X, 210*SCALE_Y)]
name_size = (100*SCALE_X, 40*SCALE_Y)


class Enemy_Character():

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
        self.target = False
        self.alive = True

        self.scale(True)

    def draw(self):

        SCREEN.blit(self.image, self.rect)
        SCREEN.blit(self.name_display, (enemy_name_positions[self.index], name_size))

        if self.target:
            self.mark()

    def mark(self):
        pygame.draw.rect(SCREEN, (0,255,0), (self.rect.centerx, self.rect.top + 30, 25, 25))


    def scale(self, flip):
        self.image = pygame.transform.flip(self.image, flip, False)
        self.image = pygame.transform.scale(self.image, unit_size)
        self.rect = self.image.get_rect()
        self.rect.topleft = enemy_positions[self.index]

path_goblins = path + r"units\goblins\ "
path_goblins = path_goblins.strip() 

spear_goblin = {}
spear_goblin["BASE_IMAGE"] = pygame.image.load(path_goblins + "spearman.png")
spear_goblin["NAME"] = "SPEAR GOBLIN"
spear_goblin["HP"] = 30
spear_goblin["ATTACK"] = 3

enemy_characters.append(spear_goblin)
enemy_characters.append(spear_goblin)
enemy_characters.append(spear_goblin)
enemy_characters.append(spear_goblin)
enemy_characters.append(spear_goblin)

for i,e in enumerate(enemy_characters):
    enemy_characters[i] = Enemy_Character(e, i)