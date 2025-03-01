import pygame
import setup

SCREEN = setup.SCREEN
SCALE_X = setup.SCALE_X
SCALE_Y = setup.SCALE_Y
SCREEN_WIDTH = setup.SCREEN_WIDTH
SCREEN_HEIGHT = setup.SCREEN_HEIGHT

class Button():

    def __init__(self, x, y, w, h, rotation, image, mask, function, cursor, type):
        self.type = type
        self.image = pygame.transform.scale(image, (w*SCALE_X, h*SCALE_Y))
        self.image = pygame.transform.rotate(self.image, rotation)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x*SCALE_X, y*SCALE_Y)
        self.mask = mask  
        self.cursor = cursor
        self.function = function

        self.selected = False
        self.access = True

    def draw(self):

        if self.mask:
            self.image.set_colorkey((255,255,255))
        
        if self.access:
            SCREEN.blit(self.image, self.rect)

        if self.selected:
            self.cursor.draw(self)

class Cursor():

    def __init__(self,image, mask):       
        self.image = image
        self.rect = self.image.get_rect()
        self.width = self.rect.width
        self.height = self.rect.height
        self.rotation = 0
        self.placement = ""
        self.mask = mask
        self.visible = True

    def draw(self, button):
        
        try:
            cursor_placement = button.cursor[0]
            width = button.cursor[1]
            height = button.cursor[2]
            rotation = button.cursor[3]

        except AttributeError:
            cursor_placement = "top"
            width = 50
            height = 50
            rotation = 180


        #VERY IPMORTTANT TO FIRST ROTATE, FUQS UPP THE IMAGE IF NOT

        if rotation != self.rotation:
            self.image = pygame.transform.rotate(self.image, (360-self.rotation+rotation))
            self.rect = self.image.get_rect()
            self.rotation = rotation

        if width != self.width or height != self.height:
            self.width = width
            self.height = height
            self.image = pygame.transform.scale(self.image, (self.width*SCALE_X, self.height*SCALE_Y))
            self.rect = self.image.get_rect()

        
        x=0; y=0

        #EI OTA HUOMIOON MUUTTUVAA CURSORIN PITUUTTA KÄÄNNÖSSÄ

        if self.mask:
            self.image.set_colorkey((255,255,255))
        if cursor_placement != self.placement:
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

        if self.visible:
            SCREEN.blit(self.image, (x,y))

