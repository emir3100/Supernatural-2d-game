import sys, pygame, config, random
import sprites

#The game screen
class Heart():

    def __init__(self): # Initialiazion
        self.load_content()
   
    def load_content(self) -> None: # Load once
        self.setHeartPos(config.SCREEN_WIDTH,config.SCREEN_HEIGHT-55) #x,y
        self.anim(0,0,10) #sets the start frame and timer to 0, and animationFPS to default 5
        self.heart = [sprites.anim_heart0, sprites.anim_heart1, sprites.anim_heart2,
                     sprites.anim_heart3, sprites.anim_heart4] # all the sprites in a list 
        self.collidedLastFrame = False
        self.destroy = False

    def update(self, delta_time) -> None: # Update every frame
        self.animUpdate(delta_time) # calling the animUpdate fucntion
        self.x -= 5 # makes the heart move left 

        
    def draw(self, screen) -> None: # Update every frame
        config.screen.blit(pygame.transform.flip(self.heart[self.currentFrame], False, False), (self.x, self.y)) # draws the heart

    def setHeartPos(self, x, y): # the heart position
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
            self.timer = 0  # reset the timer

        if self.currentFrame == len(self.heart): # it will go trough all the frames 
            self.currentFrame = 0 # when it went trough all the frames it will destory the lightning

