#written by Luci, aka Seamoss, using Python 3.10.4 and Pygame 2.1.2, in VSCode.
#I AM OZYMANDIAS, KING OF KINGS. LOOK UPON MY WORKS, YE MIGHTY, AND DESPAIR.
import pygame
import random as r





#If you are reading this then I have made the mistake of publishing this code. 
#There is enough spaghetti here to change someone's DNA to forcibly make them italian. You have been warned.
#I will attempt to label things properly but do not expect full documentation or even a bare modicum of professionalism.


#all of this is just setting up stuff my lazy ass can use elsewhere
#like size of the window, which is used to calculate how to center the text in each button
WIDTH = 600
HEIGHT = 800

#this is just pygame boilerplate
pygame.display.init()
pygame.font.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 0, 0, 0)
pygame.display.set_caption("Dice Utility")
Font = pygame.font.SysFont(None, 50)
#sets the mouse position in how it keeps track of it to the top right corner
mousePos = (0, 0)
#random variables that will help me not lose my mind over python errors that it seemingly throughs at me because it feels like it
resultLabel = "Result: "
result = ""
resultEMPTY = Font.render(resultLabel, 1, (255, 255, 255))
roll = 0


#neat cool welcome to my vlog, glad we got the boring shit out of the way
#this is the big lad that all the buttons use
#he's got all the bells and whistles, and knows how to draw each button based on the parameters we give himb
class Button:
    def __init__(self, x, y, width, height, label, color, aa):
        #position of button from top left corner of button
        self.x = x 
        self.y = y
        #size of button from top left corner of button
        self.width = width
        self.height = height
        #what the text on the button says
        self.label = label
        #color of the button
        self.color = color
        #whether or not the text has antialiasing
        self.aa = aa
        #more pygame boilerplate
        self.text = Font.render(self.label, self.aa, (0, 0, 0))
        self.background = pygame.Rect(self.x, self.y, self.width, self.height)
        #now we get to the cool part
        #labelsize calculates how much space each text label takes up
        self.labelSize = Font.size(self.label)
        #and the math here centers the text within the button
        self.labelX = ((self.width/2) - (self.labelSize[0]/2)) + self.x
        self.labelY = ((self.height/2) - (self.labelSize[1]/2)) + self.y

        #this little centering trick took like 20 minutes to figure out and i'm proud of it ok
    
    #helper function that is called in the main render function to draw the button
    def render(self, screen):
        pygame.draw.rect(screen, self.color, self.background)
        screen.blit(self.text, (self.labelX, self.labelY))
        

#list of all buttons, you can see the power of the class in action
d20 = Button(50, 50, 150, 100, "d20", (0, 255, 255), 1)
d6 = Button(50, 200, 150, 100, "d6", (255, 255, 0), 1)
d10 = Button(50, 350, 150, 100, "d10", (255, 0, 255), 1)
d8 = Button(400, 50, 150, 100, "d8", (0, 255, 255), 1 )
d2 = Button(400, 200, 150, 100, "d2", (255, 255, 0), 1)
d4 = Button(400, 350, 150, 100, "d4", (255, 0, 255), 1)


#position of the label displaying the results
resultPos = (200, 600)


#list of all the buttons for use in determining which one has been clicked
buttonList = (d20.background, d6.background, d10.background, d8.background, d2.background, d4.background)



#time for the meat and po-ta-tos
#boil'em, mash'em, put them in your ears
def logic():
    #global variables because i can't be assed to write a program correctly and this method works
    global mousePos
    global resultLabel
    global result
    global roll
    #updates mousePos with current mouse position within window, doesn't update when mouse is outside window
    mousePos = pygame.mouse.get_pos()
    #moves a tiny rectangle to the mouse's position, this is used for clicking
    mouseRect = pygame.Rect(mousePos[0], mousePos[1], 1, 1)
    
    #determining what got clicked
    if pygame.mouse.get_pressed(3)[0] == True:
        #d20
        if pygame.Rect.collidelist(mouseRect, buttonList) == 0:
            roll = r.randint(1,20)
        #d6
        elif pygame.Rect.collidelist(mouseRect, buttonList) == 1:
            roll = r.randint(1, 6)
        #d10
        elif pygame.Rect.collidelist(mouseRect, buttonList) == 2:
            roll = r.randint(1, 10)
        #d8
        elif pygame.Rect.collidelist(mouseRect, buttonList) == 3:
            roll = r.randint(1, 8)
        #d2, also known as a coin
        elif pygame.Rect.collidelist(mouseRect, buttonList) == 4:
            roll = r.randint(1, 2)
        #d4
        elif pygame.Rect.collidelist(mouseRect, buttonList) == 5:
            roll = r.randint(1,4)

    #pygame stuff for setting up the result display
    result = Font.render(resultLabel + str(roll), 1, (255, 255, 255))
    
            

#now to the render function, which has very little logic
def render():
    #clears the previous frame
    screen.fill((0, 0, 0))
    #draws all the buttons according to their helper functions
    d20.render(screen)
    d6.render(screen)
    d10.render(screen)
    d8.render(screen)
    d2.render(screen)
    d4.render(screen)
    
    #"anti-cheat" logic that makes it so you only see the roll after you are done pressing the button so you can't guess at it and try to force it to be high
    if pygame.mouse.get_pressed(3)[0] == False:
        screen.blit(result, resultPos)
        pygame.display.flip()
    else:
        screen.blit(resultEMPTY, resultPos)
        pygame.display.flip()



#main function that controls everything
#aka giant rat that makes all of da rulez
def main():
    global running
    running = True
    pygame.time.Clock()
    while running:
        pygame.time.Clock().tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        #runs the processes in the right order
        logic()
        render()
    pygame.display.quit()



#just makes sure you're running the right thing
if __name__ == "__main__":
    main() #ayyyyyyyyyyyyyy line 169 nice