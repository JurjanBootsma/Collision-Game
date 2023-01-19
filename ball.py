#Class Assignment 3

#This class contains all the information and the functions for the balls
#in the game. There is always an X, with what the player can move
#and there are other balls as well.
#Last edit: January 11 2021
#Interpreter: Python 3.7.6
#Operating system: MacOS Catalina
class Ball():
    
    #The input for the Ball class:
    #x: The x coordinate on the map.
    #y: The y coordinate on the map.
    #board: The map that is chosen.
    #name: Name of the ball, which has to be a letter (so a string)
    def __init__(self,x,y,board,name):
        self.x = x
        self.y = y
        self.board = board
        self.name = name
    
    #This functions determines if the ball is still on the map.
    #If the x- or y-coordinates get too big or small, the ball falls off.
    #For the x-ball this means the game will be over.
    #For another ball it means points.   

    #Input:
    #rollingball: That is the ball that is moving (usually X,
    #but if X hit another ball it could be another.)       
    #allballs: The list of ball classes in the game.
    #ballpoints: The amount of balls kicked of the board.
        
    #Output:
    #ballpoints: The amount of balls kicked of the board.
    #stop: determines if something is kicked of.
    #allballs: The list of ball classes in the game.
    def faloff(self, rollingball, allballs, ballpoints):
        if self.name == "X":    #If X is the ball rolling.
            #If it gets smaller than 0 (minimum) or bigger than the maximum.
            if (self.x < 0 or self.y < 0 or self.x > (len(self.board[0])-1) 
                or self.y > (len(self.board)-1)):
                print("The ball X fell off")
                return 0.5,0.5, allballs
        q = 0
        #Checks for every ball any ball can hit.
        while q < len(allballs):
            if self.name == (allballs[q]).name:
                if (self.x < 0 or self.y < 0 or self.x > (len(self.board[0])-1) 
                    or self.y > (len(self.board)-1)):
                    print("Ball",rollingball.name,"fell off")
                    del allballs[q] #Cuts the ball that fell off the map of the list
                    return ballpoints + 1, 1, allballs
            q=q+1
        else:
            return ballpoints,0,allballs
    
    #This functions determines a change in direction of the ball.
    #This will only change if a ball hits a wall (a 1).
        
    #Input and output:
    #q: Determines how many actions the ball still has to do.
    #change: Determines the direction the ball is rolling.
    #points: How many points the user still has.
    def changedirection(self,q,change,points):
        if (self.board[self.y])[self.x] == "1": #If it hit the wall.
            change = change * -1    #Changed direction
            #q has to be done minus 2, because the game now thinks the ball
            #is in the wall, so it first has to go back to the first position.
            q = q-1
            points = points+100
            print("Ball", self.name, "is changed in direction")
            
        return change,q,points







