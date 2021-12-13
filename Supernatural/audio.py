#This is for loading all the audio

import pygame
import config

#effects
effect_lightning = None
effect_hurt = None
effect_health = None



#songs
song_background = None
song_menu = None

def init() -> None:

    #effects 
    global effect_lightning, effect_hurt, effect_health
    #songs
    global song_background, song_menu

    #path 
    path = 'content/audio/'

    #load_effects
    effect_lightning = pygame.mixer.Sound(f'{path}effect_lightning.ogg')
    effect_hurt = pygame.mixer.Sound(f'{path}effect_hurt.ogg')
    effect_health = pygame.mixer.Sound(f'{path}effect_health.ogg')

    #load_songs
    song_background = f'{path}song_background.mp3'
    song_menu =f'{path}song_menu.mp3'



def play_effect(effect) -> None: # function to check if boolean is true in config
    if config.sound_effect_on:
        effect.play() #play sound effect


def play_song(path): #function to play song and check if boolean is true in config
    pygame.mixer.music.load(path)

    if config.sound_song_on:
        pygame.mixer.music.play(-1) # play soong in loop


