# Imports
import pygame 
from pygame.locals import *
import math
import random
from time import sleep
import sys
from math import floor


# player variabels 
left = False # checks if the player is facing left
right = True # checking if the player is facing right
vel = 8 # speed of the player
walkcount = 0 # for the running animation
standingcount = 0 # for the idle standing animation
isPlayerRunning = False # Checking if the character is idel, not moving
isJump = False # player jumping state
jumpcount = 10 # value for the jump
jumpAnim = 0 # jump value for animastion
life = 3 # total lifes given to the player ## you cant change because of how the animation is set up ## note to self: making this able to change(Status: no hearts yet)
gameExit = False # variable for "game over screen"
playerx = 1700 # the x and y for the player, the player is placed here at the start of the game 
groundy =900 # making a vaiable for the ground 
playery = 900



# Making the class for the main menu

class main_menu:

    def setup(): # main function for the main menu
        #setting up the window
        pygame.init()
        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) # the default is fullscreen

        ## background img
        pathbg = r'pixelart\background\main_menu\background_main_menu_v1.png' #path variable for future change
        bgr = pygame.image.load(pathbg)
        screen.blit(bgr,(0,0))



        # the exit button 
        bt = pygame.image.load(r'pixelart\background\main_menu\icons8-close-window-48.png')
        exit_x = 1920 - 48 # All the way to the left minus the width of the button
        exit_y = 0
        screen.blit(bt, (exit_x, exit_y))
        exrec = Rect((exit_x, exit_y), (48,48)) # creating a rectangle that holds the same cords as button
        

        

        # creating the title 
        titl = pygame.image.load(r'pixelart\background\main_menu\titledesign.png') # loading the img
        titl_x = floor(1920/2) - 375 # x and y cords are difined in these lines
        titl_y = 100
        screen.blit(titl, (titl_x, titl_y))

        # play button
        playbt = pygame.image.load(r'pixelart\background\main_menu\playbt.png')
        playbt_x = 810 # defining x and y cords for the play btn
        playbt_y = 450
        screen.blit(playbt, (playbt_x, playbt_y))
        plyrec = Rect((playbt_x, playbt_y), (350, 62))  # the value of the ply btn stored in a rect value
       
        


        # options bottun
        optsbt = pygame.image.load(r'pixelart\background\main_menu\options.png') 
        opts_x = playbt_x  # all the buttons on the main menu has the same x values, so that they are lined up
        ops_Y = 550
        screen.blit(optsbt, (opts_x, ops_Y))


        # "Created by" label
        crtby = pygame.image.load(r'pixelart\background\main_menu\Created-by-Kjetil-Indreh.png')
        crtby_x = 1600 # the text should be in the bottom left corner
        crtby_y = 1000
        screen.blit(crtby, (crtby_x, crtby_y))


        running = True # menu 
        run1 = True # the variable that allows the main menu logic to run 
        # main menu loop 
        loopind = 0 # loopindex

        #clock = pygame.time.Clock() # offical time counter in frames

        while running:

            # loop index 
            if loopind + 1 >= 30:
                loopind == 0
            

            # check for all events 
            for event in pygame.event.get():
                #exit button pressed
                if game.isRun(run1) == True: # checking if the game has been opened and if it has, then it stops it
                    # the logic for the main menu works 
                    if exrec.collidepoint(pygame.mouse.get_pos()):  # test if the curser is over the exit rectangle from above 
                        if event.type == pygame.MOUSEBUTTONUP:
                            # print("i pressed quit") ## test line
                            pygame.QUIT
                            sys.exit()
                    if plyrec.collidepoint(pygame.mouse.get_pos()):
                        if event.type == pygame.MOUSEBUTTONUP:
                            game.setupgame(screen, left, right, playerx, walkcount, standingcount, isJump, jumpcount, playery, jumpAnim)
                            run1 = False # the game is now running

            main_menu.drawAnimationMainMenu(loopind, screen, run1)


            pygame.display.update()

    def drawAnimationMainMenu(loopind, screen, run1):
        
        # selfnote: not working and not sure why 
        
        if run1 == True: # checking if the game has been opened already 
            # bgr, bt, exit_x, exit_y, titl, titl_x, titl_y, playbt, playbt_x, playbt_y, optsbt, opts_x, ops_Y,
            """
            # redrawing all
            screen.blit(bgr,(0,0)) # bg
            screen.blit(bt, (exit_x, exit_y)) # exit
            exrec = Rect((exit_x, exit_y), (48,48)) # creating a rectangle that holds the same cords as button
            screen.blit(titl, (titl_x, titl_y)) # title
            screen.blit(playbt, (playbt_x, playbt_y)) # play 
            plyrec = Rect((playbt_x, playbt_y), (350, 62))  # the value of the ply btn stored in a rect value
            screen.blit(optsbt, (opts_x, ops_Y))  #created by
            """


            # radio animation in the bottom right corner
            radio = [
                pygame.image.load(r'pixelart\background\radio\frames\radio1.png'),
                pygame.image.load(r'pixelart\background\radio\frames\radio2.png'), 
                pygame.image.load(r'pixelart\background\radio\frames\radio3.png'), 
                pygame.image.load(r'pixelart\background\radio\frames\radio4.png'), 
                pygame.image.load(r'pixelart\background\radio\frames\radio5.png'), 
                pygame.image.load(r'pixelart\background\radio\frames\radio6.png'), 
                pygame.image.load(r'pixelart\background\radio\frames\radio7.png'), 
                pygame.image.load(r'pixelart\background\radio\frames\radio8.png'), 
                pygame.image.load(r'pixelart\background\radio\frames\radio9.png') 
            ]
            radio_x = 50
            radio_y = 950

            screen.blit(radio[loopind//3], (radio_x, radio_y))
            loopind += 1
        else:
            pass
        
            
        pygame.display.update()
    


# still in thought of how to fix

class options:
    class audio:
        def set_volume():
            pass
    
    class gamepopup:
        def pausegame():
            pass


      


class game :
    def isRun(run1): # removing/stopping the while loop from objects 
        return run1


    def setupgame(screen, left, right, playerx, walkcount, standingcount, isJump, jumpcount, playery, jumpAnim):
        # clearing the screen and making it ready with the background 
        screen.fill((0,0,0)) # clearing the screen
        #pl1.kill() # removing the the Rect values from the screen
        #ex1.kill()
        run = True

        backgr = pygame.image.load(r'pixelart\background\game\background\game_arena1.png')
        screen.blit(backgr, (0,0))
        

       

        rungame = True # running variable for the game loop 

        while rungame: # gameloop

            for event in pygame.event.get():
                pygame.time.delay(100) # note to self: adjust this for better peformance//fps. making the game smoother?

            # standing still is the standard
            
          


            keys = pygame.key.get_pressed()
            isPlayerRunning = False


            # holding the key
            if keys[pygame.K_LEFT] and playerx > vel: # checks if he is pressing left and setting a limitaion for moving out of screen
                isPlayerRunning = True
                left = True # Turning the player to the left and moving with the change of vel
                right = False
                playerx -= vel
                walkcount += 1
                
                
            if keys[pygame.K_RIGHT] and playerx < 1920 - vel - 27:# checks if he is pressing left and setting a limitaion for moving out of screen, wich is the width minus the player witdh and the vel
                isPlayerRunning = True
                left = False # Turning the player to the right and moving with the change of vel
                right = True
                playerx += vel
                walkcount += 1
                isPlayerRunning = True

            if not isJump:

                if keys[pygame.K_SPACE]:
                    isJump = True
                    jumpAnim += 1
            else:
                if jumpcount >= -10:
                    playery -= (jumpcount * abs(jumpcount)* 0.5)
                    jumpcount -= 1
                    jumpAnim += 1
                else:
                    jumpcount = 10
                    isJump = False
                    jumpAnim += 1

            

            
            
            standingcount += 1

            # Resets
            if walkcount + 1 >= 27: # resets the walkcount so the frames can recicle 
                walkcount = 0   
            
            if standingcount + 1 >= 27: # resetting the standing count, so the standing animation can recicle 
                standingcount = 0   

            if jumpAnim +1 >= 27:
                jumpAnim = 0
            
            
            game.redrawGame(screen, left, right, walkcount, backgr, playerx, playery, standingcount, isPlayerRunning) # redraws the game with all the elements

            

            



    def redrawGame(screen, left, right, walkcount, backgr, playerx, playery, standingcount, isPlayerRunning):
        
        # player data
        standingRight = [   # facing right, standing still .png
            pygame.image.load(r'pixelart\background\game\player\standing still\v2\Right\radiomanv2R1.png'),
            pygame.image.load(r'pixelart\background\game\player\standing still\v2\Right\radiomanv2R2.png'),
            pygame.image.load(r'pixelart\background\game\player\standing still\v2\Right\radiomanv2R3.png'),
            pygame.image.load(r'pixelart\background\game\player\standing still\v2\Right\radiomanv2R4.png'),
            pygame.image.load(r'pixelart\background\game\player\standing still\v2\Right\radiomanv2R5.png'),
            pygame.image.load(r'pixelart\background\game\player\standing still\v2\Right\radiomanv2R6.png'),
            pygame.image.load(r'pixelart\background\game\player\standing still\v2\Right\radiomanv2R7.png'),
            pygame.image.load(r'pixelart\background\game\player\standing still\v2\Right\radiomanv2R8.png'),
            pygame.image.load(r'pixelart\background\game\player\standing still\v2\Right\radiomanv2R9.png')
            
            ]

        standingLeft = [  # facing left, standing still .png
            pygame.image.load(r'pixelart\background\game\player\standing still\v2\Left\radiomanv2L1.png'),
            pygame.image.load(r'pixelart\background\game\player\standing still\v2\Left\radiomanv2L2.png'),
            pygame.image.load(r'pixelart\background\game\player\standing still\v2\Left\radiomanv2L3.png'),
            pygame.image.load(r'pixelart\background\game\player\standing still\v2\Left\radiomanv2L4.png'),
            pygame.image.load(r'pixelart\background\game\player\standing still\v2\Left\radiomanv2L5.png'),
            pygame.image.load(r'pixelart\background\game\player\standing still\v2\Left\radiomanv2L6.png'),
            pygame.image.load(r'pixelart\background\game\player\standing still\v2\Left\radiomanv2L7.png'),
            pygame.image.load(r'pixelart\background\game\player\standing still\v2\Left\radiomanv2L8.png'),
            pygame.image.load(r'pixelart\background\game\player\standing still\v2\Left\radiomanv2L9.png')
            
        ]

        #running animation where player is facing right
        runningRight =[
            pygame.image.load(r'pixelart\background\game\player\running\v1\right\runningR1.png'),
            pygame.image.load(r'pixelart\background\game\player\running\v1\right\runningR2.png'),
            pygame.image.load(r'pixelart\background\game\player\running\v1\right\runningR3.png'),
            pygame.image.load(r'pixelart\background\game\player\running\v1\right\runningR4.png'),
            pygame.image.load(r'pixelart\background\game\player\running\v1\right\runningR5.png'),
            pygame.image.load(r'pixelart\background\game\player\running\v1\right\runningR6.png'),
            pygame.image.load(r'pixelart\background\game\player\running\v1\right\runningR7.png'),
            pygame.image.load(r'pixelart\background\game\player\running\v1\right\runningR8.png'),
            pygame.image.load(r'pixelart\background\game\player\running\v1\right\runningR9.png')
        ]

        runningLeft =[
            pygame.image.load(r'pixelart\background\game\player\running\v1\left\runningL1.png'),
            pygame.image.load(r'pixelart\background\game\player\running\v1\left\runningL2.png'),
            pygame.image.load(r'pixelart\background\game\player\running\v1\left\runningL3.png'),
            pygame.image.load(r'pixelart\background\game\player\running\v1\left\runningL4.png'),
            pygame.image.load(r'pixelart\background\game\player\running\v1\left\runningL5.png'),
            pygame.image.load(r'pixelart\background\game\player\running\v1\left\runningL6.png'),
            pygame.image.load(r'pixelart\background\game\player\running\v1\left\runningL7.png'),
            pygame.image.load(r'pixelart\background\game\player\running\v1\left\runningL8.png'),
            pygame.image.load(r'pixelart\background\game\player\running\v1\left\runningL9.png'),
        ]

        jumpingLeft = [ # jumping animation when the player is facing left
            pygame.image.load(r'pixelart\background\game\player\jumping\v1\left\jumpingL1.png'),
            pygame.image.load(r'pixelart\background\game\player\jumping\v1\left\jumpingL2.png'),
            pygame.image.load(r'pixelart\background\game\player\jumping\v1\left\jumpingL3.png'),
            pygame.image.load(r'pixelart\background\game\player\jumping\v1\left\jumpingL4.png'),
            pygame.image.load(r'pixelart\background\game\player\jumping\v1\left\jumpingL5.png'),
            pygame.image.load(r'pixelart\background\game\player\jumping\v1\left\jumpingL6.png'),
            pygame.image.load(r'pixelart\background\game\player\jumping\v1\left\jumpingL7.png'),
            pygame.image.load(r'pixelart\background\game\player\jumping\v1\left\jumpingL8.png'),
            pygame.image.load(r'pixelart\background\game\player\jumping\v1\left\jumpingL9.png')
        ]


        jumpingRight = [ # jumping animation when the player is facing right
            pygame.image.load(r'pixelart\background\game\player\jumping\v1\right\jumpingR1.png'),
            pygame.image.load(r'pixelart\background\game\player\jumping\v1\right\jumpingR2.png'),
            pygame.image.load(r'pixelart\background\game\player\jumping\v1\right\jumpingR3.png'),
            pygame.image.load(r'pixelart\background\game\player\jumping\v1\right\jumpingR4.png'),
            pygame.image.load(r'pixelart\background\game\player\jumping\v1\right\jumpingR5.png'),
            pygame.image.load(r'pixelart\background\game\player\jumping\v1\right\jumpingR6.png'),
            pygame.image.load(r'pixelart\background\game\player\jumping\v1\right\jumpingR7.png'),
            pygame.image.load(r'pixelart\background\game\player\jumping\v1\right\jumpingR8.png'),
            pygame.image.load(r'pixelart\background\game\player\jumping\v1\right\jumpingR9.png')
        ]


        screen.blit(backgr, (0,0)) # draws the background again

        # checking the state of the player and drawing the player in the state
        if left and isPlayerRunning and not(isJump): # checking if the player is facing left and running for the animation 
            screen.blit(runningLeft[walkcount//3], (playerx, playery))
            walkcount += 1
            standingcount = 0
        elif right and isPlayerRunning and not(isJump): # checking if the player is facing right and running for the animation
            screen.blit(runningRight[walkcount//3], (playerx, playery))
            walkcount += 1
            standingcount = 0
        elif not isPlayerRunning and not(isJump): # checking if the player is not moving 
            # checking the direction of the player for the idle animation
            if left:
                screen.blit(standingLeft[standingcount//3], (playerx, playery))
                standingcount += 1
            elif right:
                screen.blit(standingRight[standingcount//3], (playerx, playery))
                standingcount += 1
        elif isJump:
           
            if left:
               screen.blit(jumpingLeft[jumpAnim//3], (playerx, playery))
               jumpAnim += 1
            
            if right:
               screen.blit(jumpingRight[jumpcount//3], (playerx, playery))
               jumpAnim += 1






        pygame.display.update()






# startuploop

if __name__ == "__main__":
    main_menu.setup()
