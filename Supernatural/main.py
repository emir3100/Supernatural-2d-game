import pygame, sys, config
import sprites
import audio
from screens.menu_settings import menu_settingsScreen
from screens.game_screen import gameScreen
from screens.menu_screen import menuScreen
from screens.choose_map_screen import chooseMapScreen

#Initialize pygame
pygame.init()
#load sprites
sprites.init()
#load audio
audio.init()

config.menu_settingsScreen = menu_settingsScreen()
config.gameScreen = gameScreen()
config.menuScreen = menuScreen()
config.chooseMapScreen = chooseMapScreen()

#frames per second
fpsClock = pygame.time.Clock()

#Display the screen
config.screen = pygame.display.set_mode(config.SCREEN_SIZE)

#Name on the window
pygame.display.set_caption('Supernatural')

#Icon
icon = pygame.image.load('content/sprites/icon.jpg')
pygame.display.set_icon(icon)

#Current screen being displayed
config.current_screen = menuScreen()




#Game loop, makes the screen on all the time unless running = false
while not config.quit_game:
    config.events = pygame.event.get()
    for event in config.events:
        #Quit
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    config.screen.fill((0, 0, 0))
    config.current_screen.update(fpsClock.get_time())
    config.current_screen.draw(config.screen)
    pygame.display.update()

    if config.sound_song_on == False:
        pygame.mixer.music.pause()

    fpsClock.tick(60) # set the FPS to 60
    #Name on the window with FPS
    pygame.display.set_caption(f'Supernatural - fps: {fpsClock.get_fps()}')