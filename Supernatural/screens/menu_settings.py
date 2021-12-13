import sys, pygame
import sprites, audio
import random
import config

#The menu settings screen
class menu_settingsScreen():

    def __init__(self): # Initialiazion
        self.load_content()
        

   
    def load_content(self) -> None: # Load once
        self.x = 240 # the arrow start position
        self.selected_start = True
        self.selected_settings = False
        self.selcted_quit = False
        self.value = 0 # value start value
        self.showM = False
        self.showSE = False


    def update(self, delta_time) -> None: # Update every frame
        self.handleInput() # calls the handleInput fucntion

        if self.value == 0: # if the value is 0 set the arrow to position 240
            self.selected_start = True
            self.x = 240

        elif self.value == 1: # if the value is ´1 set the arrow to position 290
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

        #change the text based on if it is selected or deselected
        if config.sound_song_on:
            self.showM = False
        else:
            self.showM = True

        if config.sound_effect_on:
            self.showSE = False
        else:
            self.showSE = True

    def draw(self, screen) -> None: # Update every frame    
        screen.blit(sprites.img_menu_screen, (0, 0)) # draws the menu screen
        screen.blit(sprites.img_arrow, (((config.SCREEN_WIDTH-sprites.img_arrow.get_width())*0.5)-135, self.x)) #draws the arrow

        screen.blit(sprites.img_s_music, ((config.SCREEN_WIDTH-sprites.img_s_music.get_width())*0.5, 230)) # draws the music button
        screen.blit(sprites.img_s_sound_effects, ((config.SCREEN_WIDTH-sprites.img_s_sound_effects.get_width())*0.5, 280)) # draws the sound effects button
        #after selected
        if self.showM:
            screen.blit(sprites.img_ns_music, ((config.SCREEN_WIDTH-sprites.img_s_music.get_width())*0.5, 230)) # draws the music button after selected 
        if self.showSE:
            screen.blit(sprites.img_ns_sound_effects, ((config.SCREEN_WIDTH-sprites.img_s_sound_effects.get_width())*0.5, 280)) # draws the sound effects button after selected
        screen.blit(sprites.img_s_main_menu, ((config.SCREEN_WIDTH-sprites.img_s_main_menu.get_width())*0.5, 330))# draws the main menu button

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
                    print("enter, music")
                    self.showM = True # show music selected button
                    self.soundOn() # soundOn function is called 

                if event.key == pygame.K_RETURN and self.value == 1: # if value is 1 and enter is pressed
                    print("enter, sound effects")
                    self.showSE = True  # show sound effects selected button
                    self.soundEffectOn() # soundEffectOn function is called
                    
                if event.key == pygame.K_RETURN and self.value == 2:  # if value is 2 and enter is pressed
                    print("enter, menu")
                    config.current_screen = config.menuScreen #change the screen to menu screen

                if event.key == pygame.K_ESCAPE: # if you press esc button
                    print("escape, menu")
                    config.current_screen = config.menuScreen #change the screen to menu screen
                    
    def soundOn(self): # the sound on fucntion, changes the boolean if sound_song_on in the config.py 
        if config.sound_song_on:
            config.sound_song_on = False
            pygame.mixer.music.pause()
        else:
            self.showM = False
            config.sound_song_on = True
            pygame.mixer.music.set_volume(0.1) # sets the volume to 0.1
            audio.play_song(audio.song_menu) # plays the song 


    def soundEffectOn(self): # the sound effects on function, changes the boolean if sound_effect_on in the config.py 
        if config.sound_effect_on:
            config.sound_effect_on = False
        else:
            self.showSE = False
            config.sound_effect_on = True