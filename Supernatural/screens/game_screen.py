import sys, pygame
import sprites, audio, config
import random

from background import Background
from background2 import Background2
from background3 import Background3
from player import Player
from zombie import Zombie
from demon import Demon
from heart import Heart
from lightning import Lightning
from blood import Blood
from hellhound import Hellhound


#The game screen
class gameScreen():

    def __init__(self): # Initialiazion
        self.load_content()

   
    def load_content(self) -> None: # Load once
        self.totalThunders = 0 # counting the total thunders
        #background classes
        self.background = Background() 
        self.background2 = Background2()
        self.background3 = Background3()
        #player class
        self.player = Player()
        #enemies in a list 
        self.hellhounds = []
        self.zombies = []
        self.demons = []
        self.lightnings = []
        #heart list
        self.hearts = []
        #blood class
        self.blood = Blood()
        #timers
        self.timer = self.getRandomTime()
        self.timerH = self.getTime()
        self.timerL = self.getThunderTime()
        self.timerR = self.resetBoolean()
        self.score = 0 # start score 
        self.Supernatural_Knight = 'content/Supernatural_Knight.ttf' #font
        self.font = pygame.font.Font(self.Supernatural_Knight, 25) 

        #play music
        pygame.mixer.music.set_volume(0.1)
        audio.play_song(audio.song_background)

        #colors
        self.black = (0,0,0)
        self.red = (255,0,0)
        self.color = (0,0,0) # default
        #score text
        self.text = self.font.render("Score: " + str(self.score), True, self.color)

    def getRandomTime(self) -> int: # timer for all enemies except for lightning
        # random time between 2000ms - 10000ms
        return random.randint(2000, 10000)

    def getTime(self) -> int: # timer for heart spawn
        # time 30000 ms
        return 30000

    def getThunderTime(self) -> int:    #start return value is 30000, each time it return it decreases by the amount of totalthunders times 5000
        # time 30000 ms
        time = 30000 - self.totalThunders * 5000
        if time <= 3000: #minimum is 3000 ms
            time = 3000

        self.totalThunders += 1
        return time

    def resetBoolean(self) -> int: # resets the boolean for blood
        return 1000

    def update(self, delta_time) -> None: # Update every frame
        #updates the score text
        self.text = self.font.render("Score: " + str(self.score), True, self.color)

        #blood (x,y) set to player
        self.blood.setBloodPos(self.player.x, self.player.y)

        if self.player.oncollision_has_been_called == True: # if boolean is true blood on is true
            self.blood.bloodOn = True
            self.blood.currentFrame = 3 # start frame of blood
        else:
            self.blood.bloodOn = False

        self.timerR -= delta_time #timer for the blood
        if self.timerR <= 0: 
            self.player.oncollision_has_been_called = False

        # spawn zombies if timer reaches 0
        self.timer -= delta_time
        if self.timer <= 0:
          self.zombies.append(Zombie())
          self.timer = self.getRandomTime()

        #spawn zombies, demon and hellhound if timer reaches 0
        self.timer -= delta_time
        if self.timer <= 0:
            self.zombies.append(Zombie())
            self.timer = self.getRandomTime()
            self.demons.append(Demon()) 
            self.hellhounds.append(Hellhound())

        self.timerH -= delta_time #if timer reaches 0, spawn heart
        if self.timerH <= 0:
            self.hearts.append(Heart())
            self.timerH = self.getTime()
            
        self.timerL -= delta_time
        if self.timerL <= 0:
            self.lightnings.append(Lightning()) #if timer reaches 0, spawn lightning
            self.timerL = self.getThunderTime()
            print(self.timerL)
        
        #updates all the classes
        self.blood.update(delta_time)
        self.background.update(delta_time)
        self.background2.update(delta_time)
        self.background3.update(delta_time)
        self.player.update(delta_time, self.zombies, self.demons, self.hearts, self.lightnings, self.hellhounds)

        for demon in self.demons:
            demon.update(delta_time)
            #removes demon for optimazation
            if demon.x <= 0-sprites.anim_demon0.get_width():
                self.demons.remove(demon)
                if self.player.health > 0:
                    self.score += 1 # gives score after enemy is deleted and player health is greater than 0

        for zombie in self.zombies:
            zombie.update(delta_time)
            #removes zombie for optimazation
            if zombie.x <= 0-sprites.anim_zombie0.get_width():
                self.zombies.remove(zombie)
                if self.player.health > 0:
                    self.score += 1 # gives score after enemy is deleted and player health is greater than 0

        for hellhound in self.hellhounds:
            hellhound.update(delta_time)
            #removes hellhound for optimazation
            if hellhound.x <= 0-sprites.anim_hellhound0.get_width():
                self.hellhounds.remove(hellhound)
                if self.player.health > 0:
                    self.score += 1 # gives score after enemy is deleted and player health is greater than 0
            
        for heart in self.hearts:
            heart.update(delta_time)
            #removes heart for optimazation
            if heart.x <= 0-sprites.anim_heart0.get_width() or heart.destroy and not self.player.dead:
                self.hearts.remove(heart)

        for lightning in self.lightnings:
            lightning.update(delta_time)
            #removes lightning for optimazation
            if lightning.destroy:
                self.lightnings.remove(lightning)

    def draw(self, screen) -> None: # Update every frame
        self.currentMap(screen) #calls the currentMap fucntion
        config.screen.blit(self.text, (100,100)) 
        self.player.draw(screen) # draws the player

        if not self.player.dead: #if player is alive draw blood
            self.blood.draw(screen)


        #draws every enemy and heart
        for demon in self.demons:
            demon.draw(screen)

        for zombie in self.zombies:
            zombie.draw(screen)

        for hellhound in self.hellhounds:
            hellhound.draw(screen)
          
        for heart in self.hearts:
            heart.draw(screen)

        for lightning in self.lightnings:
            lightning.draw(screen)
    
    def currentMap(self, screen): # the current map function
        if config.map1: # based on the configuration settings diffrent background will be drawn.
            self.background.draw(screen)
            self.color = self.black
            self.showScore = True
        elif config.map2:
            self.background2.draw(screen)
            self.color = self.red
            self.showScore = True
        elif config.map3:
            self.background3.draw(screen)
            self.color = self.red
            self.showScore = True


