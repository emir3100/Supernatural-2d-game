import sys, pygame, config, random
import sprites, audio

#The demon class
class Demon():

    def __init__(self): # Initialiazion
        self.load_content()
   
    def load_content(self) -> None: # Load once
        self.setDemonPos(1000,config.SCREEN_HEIGHT-125) #x,y
        self.anim(0,0,10) #sets the start frame and timer to 0, and animationFPS to default 5
        self.demon = [sprites.anim_demon0, sprites.anim_demon1, sprites.anim_demon2,
                     sprites.anim_demon3, sprites.anim_demon4, sprites.anim_demon5,
                    sprites.anim_demon6, sprites.anim_demon7, sprites.anim_demon8,
                   sprites.anim_demon9, sprites.anim_demon10, sprites.anim_demon11,
                  sprites.anim_demon12] # all the sprites in a list
        self.collidedLastFrame = False


    def update(self, delta_time) -> None: # Update every frame
        self.animUpdate(delta_time) # calling the animUpdate fucntion
        self.x -= 8 # makes the zombie move left 


    def draw(self, screen) -> None: # Update every frame
        config.screen.blit(pygame.transform.flip(self.demon[self.currentFrame], False, False), (self.x, self.y)) # draws the demon

    def setDemonPos(self, x, y):# the demon position
        self.x = x
        self.y = y

    def anim(self, currentFrame, timer, animationFPS): #animation function with the currentFrame, timer and animationdisplayspeed
        self.currentFrame = currentFrame
        self.timer = timer
        self.animationFPS = animationFPS

    def animUpdate(self, delta_time): # the animation update function
        #animation
        self.timer += delta_time #timer
        if self.timer >= 1000/self.animationFPS: # implement the animation fps together with the timer
            self.currentFrame += 1 # new frames
            self.timer = 0 # reset the timer

        if self.currentFrame == len(self.demon):  # it will go trough all the frames 
            self.currentFrame = 9 # when it went trough all the frames reset the fram to 0

