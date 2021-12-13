import sys, pygame
import sprites, audio
import random
import config
from screens.game_screen import gameScreen
from screens.menu_settings import menu_settingsScreen
from screens.choose_map_screen import chooseMapScreen

#The menu screen
class menuScreen():

    def __init__(self): # Initialiazion
        self.load_content()
        
   
    def load_content(self) -> None: # Load once
        self.x = 240 # the arrow start value
        self.selected_start = True
        self.selected_settings = False
        self.selcted_quit = False
        self.value = 0 # the value start value

        self.playMusic() # calls the playMusic fucntion

    def update(self, delta_time) -> None: # Update every frame
        self.handleInput() # calls the handleInput fucntion
        if self.value == 0: # if the value is 0 set the arrow to position 240
            self.selected_start = True
            self.x = 240

        elif self.value == 1: # if the value is 1 set the arrow to position 290
            self.selected_settings = True
            self.x = 290

        elif self.value == 2: # if the value is 2 set the arrow to position 340
            self.selcted_quit = True
            self.x = 340

        #limits the value to be max 2 and min 0
        if self.value > 2:
            self.value = 2
        elif self.value < 0:
            self.value = 0

    def draw(self, screen) -> None: # Update every frame    
        screen.blit(sprites.img_menu_screen, (0, 0)) # draws the menu screen
        screen.blit(sprites.img_arrow, (((config.SCREEN_WIDTH-sprites.img_arrow.get_width())*0.5)-100, self.x)) #draws the arrow
        screen.blit(sprites.img_s_start, ((config.SCREEN_WIDTH-sprites.img_s_start.get_width())*0.5, 230)) # draws the start button
        screen.blit(sprites.img_s_settings, ((config.SCREEN_WIDTH-sprites.img_s_settings.get_width())*0.5, 280)) # draws the settings button
        screen.blit(sprites.img_s_quit, ((config.SCREEN_WIDTH-sprites.img_s_quit.get_width())*0.5, 330)) # draws the quit button

    def playMusic(self): # the play music function
        pygame.mixer.music.set_volume(0.1) # sets the volume to 0.1
        audio.play_song(audio.song_menu) # plays the song 

    def handleInput(self):
        #all the inputs for the menu
        
        for event in config.events:        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP: # if key up is pressed
                    print("up")
                    self.value -=1 # value gets -1

                if event.key == pygame.K_DOWN: #if key down is pressed
                    print("down")
                    self.value +=1 # value gets +1

                if event.key == pygame.K_RETURN and self.value == 0: # if value is 0 and enter is pressed
                    print("enter, start")
                    config.current_screen = chooseMapScreen() # change the screen to chooseMapScreen

                if event.key == pygame.K_RETURN and self.value == 1: # if value is 1 and enter is pressed
                    print("enter, settings")
                    config.current_screen = menu_settingsScreen() # change the screen to menu_settingsScreen

                if event.key == pygame.K_RETURN and self.value == 2: # if value is 1 and enter is pressed
                    print("enter, quit")
                    config.quit_game = True # quit the game