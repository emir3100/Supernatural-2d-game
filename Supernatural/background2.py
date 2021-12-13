import sys, pygame, random
import sprites

#The background2 screen
class Background2():

    def __init__(self): # Initialiazion
        self.load_content()
   
    def load_content(self) -> None: # Load once
        self.adjust = 2 # the adjustment
        self.imgWidth = (sprites.img_1background1.get_width())-self.adjust # the image widht with adjustment
        self.images = [sprites.img_1background1, sprites.img_1background2,
                      sprites.img_1background3, sprites.img_1background4,
                     sprites.img_1background5] # all the sprites in a list 

        self.xPos = 0 #starting position
        self.background1_img = self.randomImg() # loading in a random number
        self.background2_img = self.randomImg() # loading in a random number
        self.background3_img = self.randomImg() # loading in a random number


    def update(self, delta_time) -> None: # Update every frame
        #speed of the moving img
        speed = 2 # the image moving speed
        self.xPos -= speed # subtracting the speed each frame from the x pos

        if self.xPos <= -self.imgWidth: # if xpos is less or equals to than the width of the images
            self.background1_img = self.background2_img
            self.background2_img = self.background3_img
            self.background3_img = self.randomImg()
            self.xPos = 0

        
    def draw(self, screen) -> None: # Update every frame
        #draws the images
        screen.blit(self.background1_img, (self.xPos, 0))
        screen.blit(self.background2_img, ((self.xPos + self.imgWidth), 0))
        screen.blit(self.background3_img, ((self.xPos + (self.imgWidth*2)), 0))


    def randomImg(self): # random number between 0 and len(self.images)
        index = random.randint(0, len(self.images) - 1)
        return self.images[index]