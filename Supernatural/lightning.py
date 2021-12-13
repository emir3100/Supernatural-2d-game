import sys, pygame, config, random
import sprites,audio

#The game screen
class Lightning():

    def __init__(self): # Initialiazion
        self.load_content()
   
    def load_content(self) -> None: # Load once
        self.setLightningPos(500,0) #x,y
        self.anim(0,0,10) #sets the start frame and timer to 0, and animationFPS to default 5
        self.lightning = [sprites.anim_lightning0, sprites.anim_lightning1, sprites.anim_lightning2,
                         sprites.anim_lightning3, sprites.anim_lightning4, sprites.anim_lightning5,
                        sprites.anim_lightning6, sprites.anim_lightning7, sprites.anim_lightning8,
                       sprites.anim_lightning9, sprites.anim_lightning10] # all the sprites in a list 
        self.collidedLastFrame = False
        self.destroy = False

        if config.sound_effect_on: # playing the sound
            audio.play_effect(audio.effect_lightning)

    def update(self, delta_time) -> None: # Update every frame
        self.animUpdate(delta_time) # calling the animUpdate fucntion
        
    def draw(self, screen) -> None: # Update every frame
        config.screen.blit(pygame.transform.flip(self.lightning[self.currentFrame], False, False), (self.x, self.y)) # draws the lightning



    def setLightningPos(self, x, y): # the ligthning position
        self.x = random.randint(150, config.SCREEN_WIDTH-150)# random lightning position -150 from each side
        self.y = y
        
    def anim(self, currentFrame, timer, animationFPS): #animation function with the currentFrame, timer and animationdisplayspeed
        self.currentFrame = currentFrame
        self.timer = timer
        self.animationFPS = animationFPS

    def animUpdate(self, delta_time):  # the animation update function
        #animation 
        self.timer += delta_time #timer
        if self.timer >= 1000/self.animationFPS: # implement the animation fps together with the timer
            self.currentFrame += 1 # new frames
            self.timer = 0 # reset the timer

        if self.currentFrame == len(self.lightning): # it will go trough all the frames 
            self.destroy = True # when it went trough all the frames it will destory the lightning


