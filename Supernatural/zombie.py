import sys, pygame, config, random
import sprites

#The zombie class
class Zombie():

    def __init__(self): # Initialiazion
        self.load_content()
   
    def load_content(self) -> None: # Load once
        self.setZombiePos(config.SCREEN_WIDTH,config.SCREEN_HEIGHT-80) #x,y
        self.anim(0,0,10) #sets the start frame and timer to 0, and animationFPS to default 5
        self.zombie = [sprites.anim_zombie0, sprites.anim_zombie1, sprites.anim_zombie2,
                      sprites.anim_zombie3, sprites.anim_zombie4, sprites.anim_zombie5,
                     sprites.anim_zombie6, sprites.anim_zombie7] # all the sprites in a list 
        self.collidedLastFrame = False

    def update(self, delta_time) -> None: # Update every frame
        self.animUpdate(delta_time) # calling the animUpdate fucntion
        self.x -= 5 # makes the zombie move left 

        
    def draw(self, screen) -> None: # Update every frame
        config.screen.blit(pygame.transform.flip(self.zombie[self.currentFrame], True, False), (self.x, self.y)) # draws the zombie

    def setZombiePos(self, x, y): # the zombie position
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

        if self.currentFrame == len(self.zombie): # it will go trough all the frames 
            self.currentFrame = 0 # when it went trough all the frames reset the fram to 0
