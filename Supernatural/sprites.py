#This is for loading all the sprites

import pygame

img_background1 = None
img_background2 = None
img_background3 = None
img_background4 = None
img_background5 = None
img_moon = None
img_heart = None
img_dead_heart = None

img_1background1 = None
img_1background2 = None
img_1background3 = None
img_1background4 = None
img_1background5 = None

img_2background1 = None
img_2background2 = None
img_2background3 = None
img_2background4 = None
img_2background5 = None

img_instructions = None
img_gameover = None
img_menu_screen = None
img_choose_map_screen = None
img_arrow = None
img_s_start = None
img_s_settings = None
img_s_quit = None
img_s_sound_effects = None
img_s_music = None
img_s_main_menu = None

img_ns_music = None
img_ns_sound_effects = None

anim_player0 = None
anim_player1 = None
anim_player2 = None
anim_player3 = None
anim_player4 = None
anim_player5 = None
anim_player6 = None
anim_player7 = None
anim_player8 = None
anim_player9 = None
anim_player10 = None
anim_player11 = None
anim_player12 = None

anim_zombie0 = None
anim_zombie1 = None
anim_zombie2 = None
anim_zombie3 = None
anim_zombie4 = None
anim_zombie5 = None
anim_zombie6 = None
anim_zombie7 = None

anim_hellhound0 = None
anim_hellhound1 = None
anim_hellhound2 = None
anim_hellhound3 = None
anim_hellhound4 = None

anim_demon0 = None
anim_demon1 = None
anim_demon2 = None
anim_demon3 = None
anim_demon4 = None
anim_demon5 = None
anim_demon6 = None
anim_demon7 = None
anim_demon8 = None
#moving
anim_demon9 = None
anim_demon10 = None
anim_demon11 = None
anim_demon12 = None

anim_heart0 = None
anim_heart1 = None
anim_heart2 = None
anim_heart3 = None
anim_heart4 = None

anim_lightning0 = None
anim_lightning1 = None
anim_lightning2 = None
anim_lightning3 = None
anim_lightning4 = None
anim_lightning5 = None
anim_lightning6 = None
anim_lightning7 = None
anim_lightning8 = None
anim_lightning9 = None
anim_lightning10 = None

anim_blood0 = None
anim_blood1 = None
anim_blood2 = None
anim_blood3 = None
anim_blood4 = None
anim_blood5 = None
anim_blood6 = None
anim_blood7 = None



def init() -> None:
    #loads all the sprites

    global img_background1, img_background2, img_background3, img_background4, img_background5, img_moon, img_heart, img_dead_heart, img_menu_screen, img_arrow, img_choose_map_screen, img_ns_music, img_ns_sound_effects
    global img_1background1, img_1background2, img_1background3, img_1background4, img_1background5
    global img_2background1, img_2background2, img_2background3, img_2background4, img_2background5
    global anim_hellhound0, anim_hellhound1, anim_hellhound2, anim_hellhound3, anim_hellhound4, anim_hellhound5
    global img_s_start, img_s_settings, img_s_quit, img_s_sound_effects, img_s_music, img_s_main_menu, img_gameover, img_instructions
    global anim_player0, anim_player1, anim_player2, anim_player3, anim_player4, anim_player5, anim_player6, anim_player7, anim_player8, anim_player9, anim_player10, anim_player11, anim_player12
    global anim_zombie0, anim_zombie1, anim_zombie2, anim_zombie3, anim_zombie4, anim_zombie5, anim_zombie6, anim_zombie7
    global anim_heart0, anim_heart1, anim_heart2, anim_heart3, anim_heart4, anim_heart5
    global anim_demon0, anim_demon1, anim_demon2, anim_demon3, anim_demon4, anim_demon5, anim_demon6, anim_demon7,anim_demon8, anim_demon9, anim_demon10, anim_demon11, anim_demon12
    global anim_lightning0, anim_lightning1, anim_lightning2, anim_lightning3, anim_lightning4, anim_lightning5, anim_lightning6, anim_lightning7, anim_lightning8, anim_lightning9, anim_lightning10
    global anim_blood0, anim_blood1, anim_blood2, anim_blood3, anim_blood4, anim_blood5, anim_blood6, anim_blood7

    path = 'content/sprites/'

    img_1background1 = pygame.image.load(f'{path}background1/background1.png')
    img_1background2 = pygame.image.load(f'{path}background1/background2.png')
    img_1background3 = pygame.image.load(f'{path}background1/background3.png')
    img_1background4 = pygame.image.load(f'{path}background1/background4.png')
    img_1background5 = pygame.image.load(f'{path}background1/background5.png')

    img_2background1 = pygame.image.load(f'{path}background2/background1.png')
    img_2background2 = pygame.image.load(f'{path}background2/background2.png')
    img_2background3 = pygame.image.load(f'{path}background2/background3.png')
    img_2background4 = pygame.image.load(f'{path}background2/background4.png')
    img_2background5 = pygame.image.load(f'{path}background2/background5.png')

    img_background1 = pygame.image.load(f'{path}background/background1.png')
    img_background2 = pygame.image.load(f'{path}background/background2.png')
    img_background3 = pygame.image.load(f'{path}background/background3.png')
    img_background4 = pygame.image.load(f'{path}background/background4.png')
    img_background5 = pygame.image.load(f'{path}background/background5.png')
    img_moon = pygame.image.load(f'{path}background/moon.png')

    img_heart = pygame.image.load(f'{path}heart.png')
    img_dead_heart = pygame.image.load(f'{path}dead_heart.png')

    img_instructions = pygame.image.load(f'{path}instructions.png')
    img_gameover = pygame.image.load(f'{path}gameover.png')
    img_menu_screen = pygame.image.load(f'{path}menu_screen.png')
    img_arrow = pygame.image.load(f'{path}arrow.png')
    img_choose_map_screen = pygame.image.load(f'{path}choose_map_screen.png')
    img_s_start = pygame.image.load(f'{path}buttons/selected/s_start.png')
    img_s_settings = pygame.image.load(f'{path}buttons/selected/s_settings.png')    
    img_s_quit = pygame.image.load(f'{path}buttons/selected/s_quit.png') 
    img_s_sound_effects = pygame.image.load(f'{path}buttons/selected/s_sound_effects.png') 
    img_s_music = pygame.image.load(f'{path}buttons/selected/s_music.png') 
    img_s_main_menu = pygame.image.load(f'{path}buttons/selected/s_main_menu.png') 
    img_ns_music = pygame.image.load(f'{path}buttons/not_selected/ns_music.png') 
    img_ns_sound_effects = pygame.image.load(f'{path}buttons/not_selected/ns_sound_effects.png') 

    #Player walking
    anim_player0 = pygame.image.load(f'{path}dean/frame0.png')
    anim_player1 = pygame.image.load(f'{path}dean/frame1.png')
    anim_player2 = pygame.image.load(f'{path}dean/frame2.png')
    #Player crouch
    anim_player3 = pygame.image.load(f'{path}dean/frame3.png')
    anim_player4 = pygame.image.load(f'{path}dean/frame4.png')
    anim_player5 = pygame.image.load(f'{path}dean/frame5.png')
    #PLayer dies
    anim_player6 = pygame.image.load(f'{path}dean/frame6.png')
    anim_player7 = pygame.image.load(f'{path}dean/frame7.png')
    anim_player8 = pygame.image.load(f'{path}dean/frame8.png')
    anim_player9 = pygame.image.load(f'{path}dean/frame9.png')
    anim_player10 = pygame.image.load(f'{path}dean/frame10.png')
    anim_player11 = pygame.image.load(f'{path}dean/frame11.png')
    anim_player12 = pygame.image.load(f'{path}dean/frame11.png')

    anim_zombie0 = pygame.image.load(f'{path}zombie/frame0.png')
    anim_zombie1 = pygame.image.load(f'{path}zombie/frame1.png')
    anim_zombie2 = pygame.image.load(f'{path}zombie/frame2.png')
    anim_zombie3 = pygame.image.load(f'{path}zombie/frame3.png')
    anim_zombie4 = pygame.image.load(f'{path}zombie/frame4.png')
    anim_zombie5 = pygame.image.load(f'{path}zombie/frame5.png')
    anim_zombie6 = pygame.image.load(f'{path}zombie/frame6.png')
    anim_zombie7 = pygame.image.load(f'{path}zombie/frame7.png')

    anim_demon0 = pygame.image.load(f'{path}demon/frame0.png')
    anim_demon1 = pygame.image.load(f'{path}demon/frame1.png')
    anim_demon2 = pygame.image.load(f'{path}demon/frame2.png')
    anim_demon3 = pygame.image.load(f'{path}demon/frame3.png')
    anim_demon4 = pygame.image.load(f'{path}demon/frame4.png')
    anim_demon5 = pygame.image.load(f'{path}demon/frame5.png')
    anim_demon6 = pygame.image.load(f'{path}demon/frame6.png')
    anim_demon7 = pygame.image.load(f'{path}demon/frame7.png')
    anim_demon8 = pygame.image.load(f'{path}demon/frame8.png')
    anim_demon9 = pygame.image.load(f'{path}demon/frame9.png')
    anim_demon10 = pygame.image.load(f'{path}demon/frame10.png')
    anim_demon11 = pygame.image.load(f'{path}demon/frame11.png')
    anim_demon12 = pygame.image.load(f'{path}demon/frame12.png')

    anim_heart0 = pygame.image.load(f'{path}heart_spin/frame0.png')
    anim_heart1 = pygame.image.load(f'{path}heart_spin/frame1.png')
    anim_heart2 = pygame.image.load(f'{path}heart_spin/frame2.png')
    anim_heart3 = pygame.image.load(f'{path}heart_spin/frame3.png')
    anim_heart4 = pygame.image.load(f'{path}heart_spin/frame4.png')

    anim_lightning0 = pygame.image.load(f'{path}lightning/frame0.png')
    anim_lightning1 = pygame.image.load(f'{path}lightning/frame1.png')
    anim_lightning2 = pygame.image.load(f'{path}lightning/frame2.png')
    anim_lightning3 = pygame.image.load(f'{path}lightning/frame3.png')
    anim_lightning4 = pygame.image.load(f'{path}lightning/frame4.png')
    anim_lightning5 = pygame.image.load(f'{path}lightning/frame5.png')
    anim_lightning6 = pygame.image.load(f'{path}lightning/frame6.png')
    anim_lightning7 = pygame.image.load(f'{path}lightning/frame7.png')
    anim_lightning8 = pygame.image.load(f'{path}lightning/frame8.png')
    anim_lightning9 = pygame.image.load(f'{path}lightning/frame9.png')
    anim_lightning10 = pygame.image.load(f'{path}lightning/frame10.png')

    anim_blood0 = pygame.image.load(f'{path}blood/frame0.png')
    anim_blood1 = pygame.image.load(f'{path}blood/frame1.png')
    anim_blood2 = pygame.image.load(f'{path}blood/frame2.png')
    anim_blood3 = pygame.image.load(f'{path}blood/frame3.png')
    anim_blood4 = pygame.image.load(f'{path}blood/frame4.png')
    anim_blood5 = pygame.image.load(f'{path}blood/frame5.png')
    anim_blood6 = pygame.image.load(f'{path}blood/frame6.png')
    anim_blood7 = pygame.image.load(f'{path}blood/frame7.png')

    anim_hellhound0 = pygame.image.load(f'{path}hellhound/frame0.png')
    anim_hellhound1 = pygame.image.load(f'{path}hellhound/frame1.png')
    anim_hellhound2 = pygame.image.load(f'{path}hellhound/frame2.png')
    anim_hellhound3 = pygame.image.load(f'{path}hellhound/frame3.png')
    anim_hellhound4 = pygame.image.load(f'{path}hellhound/frame4.png')