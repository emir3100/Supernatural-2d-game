import pygame
import sprites, audio
import config
from screens.game_screen import gameScreen

#The menu screen
class chooseMapScreen():

    def __init__(self): # Initialiazion
        self.load_content()
        
   
    def load_content(self) -> None: # Load once
        self.x = 355  # the arrow start value
        self.selected_start = True
        self.selected_settings = False
        self.selcted_quit = False
        self.value = 0 # the value start value


    def update(self, delta_time) -> None: # Update every frame
        self.handleInput() # calls the handleInput fucntion
        if self.value == 0: # if the value is 0 set the arrow to position 355
            self.selected_start = True
            self.x = 355

        elif self.value == 1: # if the value is 1 set the arrow to position 550
            self.selected_settings = True
            self.x = 550

        elif self.value == 2: # if the value is 2 set the arrow to position 725
            self.selected_settings = True
            self.x = 725


        #limits the value to be max 2 and min 0
        if self.value > 2:
            self.value = 2
        elif self.value < 0:
            self.value = 0

    def draw(self, screen) -> None: # Update every frame    
        screen.blit(sprites.img_choose_map_screen, (0, 0)) # draws the choos map screen
        screen.blit(pygame.transform.rotate(sprites.img_arrow, 90), (self.x,380)) # draws the arrow

  

    def handleInput(self):
        #all the inputs for the menu
        
        for event in config.events:        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:  # if key left is pressed
                    print("up")
                    self.value -=1 # value gets -1

                if event.key == pygame.K_RIGHT: # if key right is pressed
                    print("down")
                    self.value +=1 # value gets +1

                if event.key == pygame.K_RETURN and self.value == 0: # if value is 0 and enter is pressed
                    print("enter, MAP1") # map 1 is selected
                    config.map1 = True
                    config.map2 = False
                    config.map3 = False 
                    config.current_screen = gameScreen() #change screen to game screen

                if event.key == pygame.K_RETURN and self.value == 1: # if value is 1 and enter is pressed
                    print("enter, MAP3") # map 3 is selected
                    config.map1 = False
                    config.map2 = False
                    config.map3 = True
                    config.current_screen = gameScreen() #change screen to game screen

                if event.key == pygame.K_RETURN and self.value == 2: # if value is 2 and enter is pressed
                    print("enter, MAP2") # map 2 is selected
                    config.map1 = False
                    config.map2 = True
                    config.map3 = False
                    config.current_screen = gameScreen() #change screen to game screen

                if event.key == pygame.K_ESCAPE: # if key esc is pressed change screen to menu screen
                    print("escape, menu")
                    config.current_screen = config.menuScreen

