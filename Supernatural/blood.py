import sys, pygame, config, random
import sprites

#The blood class
class Blood():

    def __init__(self): # Initialiazion
        self.load_content()
   
    def load_content(self) -> None: # Load once
        self.setBloodPos(300, 300) #x,y
        self.anim(0,0,20) #sets the start frame and timer to 0, and animationFPS to default 5
        self.blood = [sprites.anim_blood0, sprites.anim_blood1, sprites.anim_blood2,
                     sprites.anim_blood3, sprites.anim_blood4, sprites.anim_blood5,
                    sprites.anim_blood6, sprites.anim_blood7] # all the sprites in a list 
        self.collidedLastFrame = False
        self.bloodOn = False
    def update(self, delta_time) -> None: # Update every frame
        self.animUpdate(delta_time)  # calling the animUpdate fucntion
        
        
    def draw(self, screen) -> None: # Update every frame
        if self.bloodOn:
            config.screen.blit(pygame.transform.flip(self.blood[self.currentFrame], False, False), (self.x, self.y)) # draws the blood

    def setBloodPos(self, x, y): # the blood position
        self.x = x
        self.y = y

    def anim(self, currentFrame, timer, animationFPS): #animation function with the currentFrame, timer and animationdisplayspeed
        self.currentFrame = currentFrame
        self.timer = timer
        self.animationFPS = animationFPS

    def animUpdate(self, delta_time): # the animation update function
        #animation
        self.timer += delta_time  #timer
        if self.timer >= 1000/self.animationFPS:  # implement the animation fps together with the timer
            self.currentFrame += 1  # new frames
            self.timer = 0 # reset the timer

        if self.currentFrame == len(self.blood): # it will go trough all the frames 
            self.currentFrame = 0 # when it went trough all the frames reset the fram to 0

