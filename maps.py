import pygame 
import setup as set


class Button():

    def __init__(self, x, y, w, h, rotation, image, mask, function, cursor):
        self.image = pygame.transform.scale(image, (w*set.SCALE_X, h*set.SCALE_Y))
        self.image = pygame.transform.rotate(self.image, rotation)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = mask  
        self.cursor = cursor
        self.selected = False
        self.function = function

    def draw(self):
        if self.mask == True:
            self.image.set_colorkey((255,255,255))
        set.screen.blit(self.image, self.rect)
        if self.selected == True:
            self.cursor.draw(self)

class Cursor():

    def __init__(self,image, mask):
        
        self.image = image
        self.rect = self.image.get_rect()
        self.width = self.rect.width
        self.height = self.rect.height
        self.placement = "left"
        self.rotation = 0
        self.mask = mask

    def draw(self, button):

        cursor_placement = button.cursor[0]
        width = button.cursor[1]
        height = button.cursor[2]
        rotation = button.cursor[3]

        if width != self.width or height != self.height:
            self.width = width
            self.height = height
            self.image = pygame.transform.scale(self.image, (self.width*set.SCALE_X, self.height*set.SCALE_Y))
            self.rect = self.image.get_rect()
        if rotation != self.rotation:
            self.image = pygame.transform.rotate(self.image, (360-self.rotation+rotation))
            self.rotation = rotation
        
        x=0; y=0

        #EI OTA HUOMIOON MUUTTUVAA CURSORIN PITUUTTA KÄÄNNÖSSÄ

        if self.mask == True:
            self.image.set_colorkey((255,255,255))
        if cursor_placement == "left":
            x = button.rect.left - self.rect.width
            y = button.rect.centery - self.rect.height/2
        if cursor_placement == "right":
            x = button.rect.right
            y = button.rect.centery - self.rect.height/2
        if cursor_placement == "bottom":
            x = button.rect.centerx - self.rect.width/2 
            y = button.rect.bottom
        if cursor_placement == "top":
            x = button.rect.centerx - self.rect.width/2 
            y = button.rect.top - self.rect.height/2
        set.screen.blit(self.image, (x,y))



character_choosing = {"TYPE": "MENU"}
menu = {"TYPE": "MENU"}

menu["BUTTONS"] = [Button(400,475,500,200, 0, image=set.new_game, mask=True, function=character_choosing, cursor=["left",150,150,270]),
                   Button(400,725,500,200, 0, image=set.quit, mask=True, function="QUIT", cursor=["left",150,150,270])]
menu["CURSOR"] = Cursor(image=set.menu_cursor, mask=False)
menu["BACKGROUND"] = set.menu_background
menu["THEME"] = ["120 The Dragon Spreads it's Wings.mp3"]

character_choosing["BUTTONS"] = [Button(200, 50, 200, 200, 0, cursor=["top",100,100,180], image=set.dwarvish_fighter, mask=False, function="QUIT"),
                                Button(500, 50, 200, 200, 0, cursor=["top",100,100,180], image=set.dwarvish_scout, mask=False, function="QUIT"),
                                Button(800, 50, 200, 200, 0, cursor=["top",100,100,180], image=set.dwarvish_guard, mask=False, function="QUIT"),
                                Button(200, 250, 200, 200, 0, cursor=["top",100,100,180], image=set.thug, mask=False, function="QUIT"),
                                Button(500, 250, 200, 200, 0, cursor=["top",100,100,180], image=set.footbad, mask=False, function="QUIT"),
                                Button(800, 250, 200, 200, 0, cursor=["top",100,100,180], image=set.thief, mask=False, function="QUIT"),
                                Button(200, 450, 200, 200, 0, cursor=["top",100,100,180], image=set.elvish_fighter, mask=False, function="QUIT"),
                                Button(500, 450, 200, 200, 0, cursor=["top",100,100,180], image=set.elvish_archer, mask=False, function="QUIT"),
                                Button(800, 450, 200, 200, 0, cursor=["top",100,100,180], image=set.elvish_shaman, mask=False, function="QUIT"),
                                Button(200,725,400,200, 0, cursor=["left",100,100,270], image=set.back, mask=True, function=menu),                         
                                Button(700,725,400,200, 0, cursor=["left",100,100,270], image=set.back, mask=True, function=menu)]                           
character_choosing["CURSOR"] = Cursor(image=set.menu_cursor, mask=False)

character_choosing["BACKGROUND"] = set.menu_background
character_choosing["THEME"] = ["120 The Dragon Spreads it's Wings.mp3"]



