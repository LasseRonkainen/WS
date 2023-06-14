import pygame
import ctypes
import os

user32 = ctypes.windll.user32
dir_path = os.getcwd()

SCREEN_WIDTH = user32.GetSystemMetrics(0)
SCREEN_HEIGHT = user32.GetSystemMetrics(1)
SCALE_X = SCREEN_WIDTH/1280
SCALE_Y = SCREEN_HEIGHT/1080

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)

path = dir_path + r"\images\ "
path = path.strip()


#Kuvat voi ladata tobytes/tostring vähentämään tilaa!


#BACKGROUNDS
path_background = path + r"background\ "
path_background = path_background.strip()

menu_background = pygame.image.load(path_background + "menu_background.jpg")

#BUTTONS
path_buttons = path + r"\buttons\ "
path_buttons = path_buttons.strip()

new_game = pygame.image.load(path_buttons + "new_game.png")
quit = pygame.image.load(path_buttons + "quit.png")
back = pygame.image.load(path_buttons + "back.png")

#MISC
path_misc = path + r"\misc\ "
path_misc = path_misc.strip()

menu_cursor = pygame.image.load(path_misc + "menu_cursor.png")

#UNITS
path_dwarves = path + r"units\dwarves\ "
path_dwarves = path_dwarves.strip() 

dwarvish_fighter = pygame.image.load(path_dwarves + "fighter.png")
dwarvish_scout = pygame.image.load(path_dwarves + "scout.png")
dwarvish_guard = pygame.image.load(path_dwarves + "guard.png")

path_outlaws = path + r"units\human-outlaws\ "
path_outlaws = path_outlaws.strip()

footbad = pygame.image.load(path_outlaws + "footpad.png")
thug = pygame.image.load(path_outlaws + "thug.png")
poacher = pygame.image.load(path_outlaws + "poacher.png")
thief = pygame.image.load(path_outlaws + "thief.png")

path_elves = path + r"units\elves-wood\ "
path_elves = path_elves.strip()

elvish_archer = pygame.image.load(path_elves + "archer.png")
elvish_fighter = pygame.image.load(path_elves + "fighter.png")
elvish_shaman = pygame.image.load(path_elves + "shaman.png")
