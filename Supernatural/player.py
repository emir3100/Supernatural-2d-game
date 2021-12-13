import sys, pygame, config, time
import sprites, audio
from heart import Heart

#The player class
class Player():
    
    def __init__(self): # Initialiazion of content
        self.load_content()
        

    def load_content(self) -> None: # Loades once 
        self.setPlayerPos(100, config.SCREEN_HEIGHT-80) # player position
        self.crouchReduce = 0 # default value to subtract of player pos y when crouch
        self.gameoverX = 700 # gameoversprite Y axis position
        self.instructionsX = 1000 # instructions when gameover Y axis position
        self.speed = 10 # player speed
        self.isJump = False # if player is jumping
        self.moving = False # if player is moving
        self.crouch = False # if player is crouching 
        self.dead = False # if player is dead
        self.health = 5 # player health
        self.maxHealth = self.health # player max health = to health
        print("your health =",self.health) # print start health
        self.oncollision_has_been_called = False # collision with enemy is false

        #---------------Animation---------------#
        self.anim(0,0,5) #sets the start frame and timer to 0, and animationFPS to default 5
        self.player = [sprites.anim_player0, sprites.anim_player1, sprites.anim_player2, 
                       sprites.anim_player3, sprites.anim_player4, sprites.anim_player5, 
                       sprites.anim_player6, sprites.anim_player7, sprites.anim_player8, 
                       sprites.anim_player9, sprites.anim_player10, sprites.anim_player11, 
                       sprites.anim_player12] # all player sprites put into a list
        
        self.heart = sprites.img_heart # load the heart sprite
        self.dead_heart = sprites.img_dead_heart # load the dead heart sprite

    
    def update(self, delta_time, zombies, demons, hearts, lightnings, hellhounds) -> None: # Updates every frame
        self.handleInput() # calls the handleInput function
        self.playerGravity() # calls the playerGravity function
        self.constrainPlayer() # calls the constrainPlayer function
        self.animUpdate(delta_time) # calls the animUpdate function
        self.detectionZombie(zombies) # calls the detectionZombie function
        self.detectionDemon(demons) # calls the detectionDemon function
        self.detectionHeart(hearts) # calls the detectionHeart function
        self.detectionLightning(lightnings) # calls the detectionLightning function
        self.detectionHellhound(hellhounds) # calls the detectionHellhound function

        #change speed of animation when moving and when not moving
        if self.moving == True:
            #animation speed if player is walking
            self.animationFPS = 12
        elif self.moving == False and not self.dead:
            #decrease animation speed if player is crouching and not dead
            self.animationFPS = 5
        else:
            #increase animation speed if player dies
            self.animationFPS = 16

        if self.dead: # if player is dead
            self.moving = False # moving is false
            #the gameover sprites move up on the screen
            if self.gameoverX >= 100:
                self.gameoverX -= 5
            #the gameover instructions move up on the screen
            if self.instructionsX >= 400:
                self.instructionsX -=5
            #player frame is set to 12 (last frame)
            if self.currentFrame == 12:
                #player moves left to creat a illusion
                self.x -= 2


    def draw(self, screen) -> None: # Update every frame
        #draws the player
        config.screen.blit(self.player[self.currentFrame], (self.x, self.y))
        self.heartsSprite() # calls the heartsSprite function
        self.gameOver()# calls the gameOver function

    def gameOver(self): # the gameover function
        if self.dead: # if player is dead
            # display these sprites belove
            config.screen.blit(sprites.img_gameover, ((config.SCREEN_WIDTH-sprites.img_gameover.get_width())*0.5, self.gameoverX))
            config.screen.blit(sprites.img_instructions, ((config.SCREEN_WIDTH-sprites.img_instructions.get_width())*0.5, self.instructionsX))
        
    def heartsSprite (self): # the heart sprite fucntion
        self.dhx = 30 # the first x value of the first heart
        for i in range(self.maxHealth): # deadhealth is loaded once to not get updated once health has been subtracted 
            self.dhx += 45 # the distance between each heart
            config.screen.blit(self.dead_heart, (self.dhx,30)) # displays the dead hearts by amount of health

        self.hx = 30 # the first x value of the first heart
        for i in range(self.health): # loops the code by the lenght of health
            self.hx += 45 # the distance between each heart
            config.screen.blit(self.heart, (self.hx,30)) # displays the hearts over the dead hearts by amount of health

    def detectionLightning(self, lightnings): # the lightning detection fucntion
        self.hitboxAdjustment = 20 # int value to create smaller hit boxes
        self.hitboxAdjustment1 = 200 # int value to create smaller hit boxes

        #player rectangle
        playerrectangle = (self.x+15, self.y+self.crouchReduce, sprites.anim_player0.get_width()-self.hitboxAdjustment-10, sprites.anim_player0.get_height()-self.hitboxAdjustment)

        #check every ligtning in lightnings 
        for lightning in lightnings:

            #ligtning rectangle
            lightningrectangle = (lightning.x+100, lightning.y, sprites.anim_lightning2.get_width()-self.hitboxAdjustment1, sprites.anim_lightning2.get_height())
            pygame.draw.rect(config.screen,(0,255,255), lightningrectangle) # draws the ligtning hitbox
            #checks if player and lightning is colliding 
            if (playerrectangle[0] < lightningrectangle[0] + lightningrectangle[2] and
            playerrectangle[0] + playerrectangle[2] > lightningrectangle[0] and
            playerrectangle[1] < lightningrectangle[1] + lightningrectangle[3] and
            playerrectangle[1] + playerrectangle[3] > lightningrectangle[1]):
                if not lightning.collidedLastFrame: # if lightning collidedLastFrame boolean is false
                    self.oncollision() # call the oncollision function
                    lightning.collidedLastFrame = True # set the collidedLastFrame boolean to true
            else: #otherwise if player did not collide 
                lightning.collidedLastFrame = False # set the collidedLastFrame boolean to false

    def detectionHellhound(self, hellhounds): #the hellhound detection function
        self.hitboxAdjustment = 20 # int value to create smaller hit boxes

        #player rectangle
        playerrectangle = (self.x+15, self.y+self.crouchReduce, sprites.anim_player0.get_width()-self.hitboxAdjustment-10, sprites.anim_player0.get_height()-self.hitboxAdjustment)

        #check every hellhound in hellhounds 
        for hellhound in hellhounds:
            #zombie rectangle
            hellhoundrectangle = (hellhound.x, hellhound.y, sprites.anim_hellhound0.get_width()-self.hitboxAdjustment, sprites.anim_hellhound0.get_height()-self.hitboxAdjustment)
            pygame.draw.rect(config.screen,(0,0,255), hellhoundrectangle)  # draws the hellhound hitbox
            #checks if player and lightning is colliding 
            if (playerrectangle[0] < hellhoundrectangle[0] + hellhoundrectangle[2] and
            playerrectangle[0] + playerrectangle[2] > hellhoundrectangle[0] and
            playerrectangle[1] < hellhoundrectangle[1] + hellhoundrectangle[3] and
            playerrectangle[1] + playerrectangle[3] > hellhoundrectangle[1]):
                if not hellhound.collidedLastFrame: # if hellhound collidedLastFrame boolean is false
                    self.oncollision() # call the oncollision function
                    hellhound.collidedLastFrame = True # set the collidedLastFrame boolean to true
            else: #otherwise if player did not collide 
                hellhound.collidedLastFrame = False # set the collidedLastFrame boolean to false

    def detectionZombie(self, zombies): #the zombie detection function
        self.hitboxAdjustment = 20 # int value to create smaller hit boxes

        #player rectangle
        playerrectangle = (self.x+15, self.y+self.crouchReduce, sprites.anim_player0.get_width()-self.hitboxAdjustment-10, sprites.anim_player0.get_height()-self.hitboxAdjustment)

        #check every zombie in zombies 
        for zombie in zombies:
            #zombie rectangle
            zombierectangle = (zombie.x, zombie.y, sprites.anim_zombie0.get_width()-self.hitboxAdjustment, sprites.anim_zombie0.get_height()-self.hitboxAdjustment)
            pygame.draw.rect(config.screen,(0,0,255), zombierectangle) # draws the zombie hitbox
            #checks if player and lightning is colliding 
            if (playerrectangle[0] < zombierectangle[0] + zombierectangle[2] and 
            playerrectangle[0] + playerrectangle[2] > zombierectangle[0] and
            playerrectangle[1] < zombierectangle[1] + zombierectangle[3] and
            playerrectangle[1] + playerrectangle[3] > zombierectangle[1]):
                if not zombie.collidedLastFrame: # if zombie collidedLastFrame boolean is false
                    self.oncollision() # call the oncollision function
                    zombie.collidedLastFrame = True # set the collidedLastFrame boolean to true
            else: #otherwise if player did not collide 
                zombie.collidedLastFrame = False # set the collidedLastFrame boolean to false

    def detectionDemon(self, demons): #the demon detection function
        self.hitboxAdjustment = 20 # int value to create smaller hit boxes

        #player rectangle
        playerrectangle = (self.x+15, self.y+self.crouchReduce, sprites.anim_player0.get_width()-self.hitboxAdjustment-10, sprites.anim_player0.get_height()-self.hitboxAdjustment)

        # draw player hitbox
        pygame.draw.rect(config.screen,(0,255,0), playerrectangle)

        #check every demon in demons
        for demon in demons:
            #demon rectangle
            demonrectangle = (demon.x, demon.y, sprites.anim_demon0.get_width()-self.hitboxAdjustment-40, sprites.anim_demon0.get_height()-self.hitboxAdjustment)
            # draw hitbox
            pygame.draw.rect(config.screen,(255,0,0), demonrectangle)
            #checks if player and demon is colliding 
            if (playerrectangle[0] < demonrectangle[0] + demonrectangle[2] and
            playerrectangle[0] + playerrectangle[2] > demonrectangle[0] and
            playerrectangle[1] < demonrectangle[1] + demonrectangle[3] and
            playerrectangle[1] + playerrectangle[3] > demonrectangle[1]):
                if not demon.collidedLastFrame: # if demon collidedLastFrame boolean is false
                    self.oncollision() # call the oncollision function
                    demon.collidedLastFrame = True # set the collidedLastFrame boolean to true
            else: #otherwise if player did not collide 
                demon.collidedLastFrame = False # set the collidedLastFrame boolean to false

    def detectionHeart(self, hearts): # the heart detection function
        self.hitboxAdjustment = 20 # int value to create smaller hit boxes

        #player rectangle
        playerrectangle = (self.x+15, self.y+self.crouchReduce, sprites.anim_player0.get_width()-self.hitboxAdjustment-10, sprites.anim_player0.get_height()-self.hitboxAdjustment)
        #check every heart in hearts 
        for heart in hearts:
            #heart rectangle
            heartrectangle = (heart.x, heart.y, sprites.anim_heart0.get_width()-self.hitboxAdjustment, sprites.anim_heart0.get_height()-self.hitboxAdjustment)
            pygame.draw.rect(config.screen,(0,0,255), heartrectangle) # draw heart hitbox
            if (playerrectangle[0] < heartrectangle[0] + heartrectangle[2] and
            playerrectangle[0] + playerrectangle[2] > heartrectangle[0] and
            playerrectangle[1] < heartrectangle[1] + heartrectangle[3] and
            playerrectangle[1] + playerrectangle[3] > heartrectangle[1]):
                if not heart.collidedLastFrame: # if heart collidedLastFrame boolean is false
                    self.oncollisionHeart() # call the oncollisionHeart function
                    heart.collidedLastFrame = True # set the collidedLastFrame boolean to true
                    heart.destroy = True # destroy heart if player collided
            else: #otherwise if player did not collide 
                heart.collidedLastFrame = False # set the collidedLastFrame boolean to false
    
    
    def oncollision(self): # if player collided function
        print("Collision!!")
        self.oncollision_has_been_called = True
        if self.health > 0: # if health is greater than 0 it can decrease health by 1
            self.health -= 1
            self.showBlooad = True # show blood
            print("your health =",self.health)
            if config.sound_effect_on: # if sound is on in the settings
                audio.play_effect(audio.effect_hurt) #play sound

        if self.health <= 0: # if health is less than or = 0 then player is dead
            print("you are dead")
            self.dead = True

            

    def oncollisionHeart(self): # the heart collision function
        print("Collision!!")
        
        if self.health < self.maxHealth and not self.dead: # if player health is less than max health and player is not dead, player can recive health
            self.health += 1
            if config.sound_effect_on: #if sound is on in the settings
                audio.play_effect(audio.effect_health) #play sound

            print("your health =",self.health)


    def anim(self, currentFrame, timer, animationFPS): #animation function with the currentFrame, timer and animationdisplayspeed
        self.currentFrame = currentFrame
        self.timer = timer
        self.animationFPS = animationFPS


    def animUpdate(self, delta_time): # the animation update function
        #animation
        self.timer += delta_time  #timer
        if self.timer >= 1000/self.animationFPS: # implement the animation fps together with the timer
            self.currentFrame += 1 # new frames
            self.timer = 0 # reset the timer

        if not self.crouch and not self.dead: # if player is not crouching and not dead
            #standing sprites
            if self.currentFrame >= 3:
                self.currentFrame = 0
        elif self.crouch:
            #crouching sprites
            if self.currentFrame >= 6:
                self.currentFrame = 4
        else: #last sprite to show after player is dead
            if self.currentFrame >= 12:
                self.currentFrame = 12

        #6 and 4 = crouch, 3 and 0 = standing, 7 and 12 = dead
        

    def setPlayerPos(self, x, y): #player position
        self.x = x
        self.y = y


    def jump(self, velocity, acceleration): #the player jumping function
        self.velocity = velocity # the new y velocity of the player
        self.acceleration = acceleration # the jump acceleration
        self.isJump = True # if function is called set this boolean to true


    def playerGravity(self): # player gravity
        if self.isJump:# if player is jumping
            self.y += self.velocity; 
            self.velocity += self.acceleration; 

        #the ground
        if self.y >= config.SCREEN_HEIGHT-80:
            self.y = config.SCREEN_HEIGHT-80
            self.isJump = False


    def constrainPlayer(self):# limits the player to not go passed the screen unless player is dead
        if not self.dead:
            if self.x < 0:
                self.x = 0
            if self.x + sprites.anim_player0.get_width() >  config.SCREEN_WIDTH:
                self.x = config.SCREEN_WIDTH - sprites.anim_player0.get_width()


    def handleInput(self):
        #all the inputs
        self.keys = pygame.key.get_pressed()

        if self.keys[pygame.K_ESCAPE] and self.dead: # if player is dead he can press escape to get back to main menu
            pygame.mixer.music.stop()
            config.current_screen = config.menuScreen
            pygame.mixer.music.set_volume(0.1)
            audio.play_song(audio.song_menu)  
        #check if player is moving if alive
        if self.keys[pygame.K_LEFT] and not self.dead or self.keys[pygame.K_RIGHT] and not self.dead or self.keys[pygame.K_d] and not self.dead or self.keys[pygame.K_a] and not self.dead:
            self.moving = True
        else:
            self.moving = False

        #the inputs for moving left and right and up and down using the arrow keys and the A and D and W and S keys
        if self.keys[pygame.K_LEFT] and not self.dead or self.keys[pygame.K_a] and not self.dead:
            self.x -= self.speed

        if self.keys[pygame.K_RIGHT] and not self.dead or self.keys[pygame.K_d] and not self.dead:
            self.x += self.speed
       
        if self.keys[pygame.K_UP] and not self.dead or self.keys[pygame.K_w] and not self.dead or self.keys[pygame.K_SPACE] and not self.dead:
            #check if player is on the ground
            if not self.isJump:
                self.jump(-15, 1.5)

        if self.keys[pygame.K_DOWN] and not self.isJump and not self.dead or self.keys[pygame.K_s] and not self.isJump and not self.dead:
            self.crouchReduce = 10 #if player is crouching make hitbox go down by 10
            if not self.crouch:
                self.currentFrame = 4
                self.crouch = True
        else: #else if playe is not crouching return crouch to default value
            self.crouchReduce = 0
            if self.crouch:
                self.currentFrame = 0
                self.crouch = False