#Gaming functions
#This program contains functions for the Collission game.
#There are functions for actually playing the game
#and for loading the map.
#Last edit: January 11 2021
#Interpreter: Python 3.7.6
#Operating system: MacOS Catalina

import ball #Own made module

#This function makes from a txt file, a series of lists of letters as strings.
#Input: file: A txt file (one in the menu.)
#Output: gamelist: A series of lists with strings (of letters, 0's and 1's.)
def organize(file):
    w = 0
    gamelist = []
    lineslist = [line.rstrip() for line in open(file)]  #Reading the file.
    while w < len(lineslist):   #For every line.
        partlist = lineslist[w].split(" ")  #A letter or 0 or 1.
        gamelist.append(partlist)
        w=w+1
    
    return gamelist    

#This function is made to find all the balls in the map.
#Input: gamelist: A series of lists with strings which resembles the map.
#Output: classballx: The class Ball of X
#Output: ball_list: A list of classes of all the other balls (so not X)
def findballs(gamelist):
    ball_list = []
    r = 0
    vertical = len(gamelist) #y-dimension
    horizontal = len(gamelist[0])    #x-dimension
    #Two while loops to check in 2 dimensions where all the balls are.
    while r<vertical:
        q = 0
        while q<horizontal:
            #These are not balls, but empty areas and walls.
            if ((gamelist[r])[q] == "0" or (gamelist[r])[q] == "1"): 
                pass
            #This is where the X ball is located.
            elif ((gamelist[r])[q] == "X"):
                xposition = q
                yposition = r
                classballx = ball.Ball(xposition,yposition, gamelist, "X")
            #This is where all the other balls are located.
            else:
                xposition = q
                yposition = r
                name = (gamelist[r])[q] #The letter of the ball
                classball =  ball.Ball(xposition,yposition, gamelist, name)    
                ball_list.append(classball)
            q=q+1        
        r=r+1

    return classballx, ball_list   

#This function is to load the map.
#It properly makes horizontal and vertical axes and prints the whole map 
#for the user.
def loadmap(xball):
    vertical = len(xball.board) #y-dimension
    horizontal = len(xball.board[0])    #x-dimension
    
    q=0
    #prints all the lines, from left to right, then to under.
    while q<vertical:
        w=0
        while w <horizontal:
            print((xball.board[q])[w], sep=" ", end=" ", flush=True)
            w=w+1
        print()
        q=q+1

#This function checks wether an entry is valid or not.
#Input: validentries: The entries that will be accepted.
#Input: entered: The actual entered input.
#Output: valid: if 0, the input was correct, if 1 not.
def wronginput(validentries, entered):
    q=0
    while q < len(validentries):    #Check if it is valid
        if entered == validentries[q]:
            valid = 0   #valid entry.
            break
        else:
            valid = 1   #Not valid entry.
        q=q+1
    return valid

#This functions is for playing a map.
#The user is in this function as long as it has not won or lost.
        
#Input:
#xball: The Ball class of ball X
#allballs: All the ball classes without X as a list.
        
#Output: points: The number of points the user ends with.
def playing(xball, allballs):
    points = 2000  #Starting number of points.
    felloff = 0     #Number of balls kicked off.
    n = len(allballs)   #Total number of balls.
    #The following are all the possible entries
    #This is important to check if a valid entry is given.
    possiblenumbers = ["1","2","3","4","5","6","7","8","9","10","11","12","13"]
    Rpossibles = ["R" + s for s in possiblenumbers]
    Lpossibles = ["L" + s for s in possiblenumbers]
    Dpossibles = ["D" + s for s in possiblenumbers]
    Upossibles = ["U" + s for s in possiblenumbers]
    possibles = Rpossibles + Lpossibles + Dpossibles + Upossibles
    
    while points > 0:   #The game continues as long as the players has more
                        #Than 0 points or won.

        if felloff == 0.5 or felloff == n:
            break #End of the function, because of winning or losing.
        
        (xball.board[xball.y])[xball.x] = xball.name    #Position of X.
        i=0
        while i < len(allballs):   #Position of all other balls.
            (xball.board[allballs[i].y])[allballs[i].x] = allballs[i].name
            i=i+1
        
        print()
        loadmap(xball)  #See previous function.
        
        rollingball = xball     #Start of turn, so the user can only move X.
    
        (xball.board[xball.y])[xball.x] = 0 #X becomes 0 again, for when 
                                            #it moves.
    
        print()
        print("You still have",points,"points")
        print("What is your next move?")
        action = input("")  #Action of the user.
        print()
        #Seperate the letter from direction and number of actions.
        actions = list(action)
        valid = wronginput(possibles,action)
        if valid == 1:  #Input not valid, try again.
            print("Choose again")
            print()
            continue
    
        change = 1
        q=1
        direction = actions[0]  #Right, left, down or up.
        while q < int(actions[1])+1:
            if points == 0: #Check per move
                break
            
            if direction == "R":
                rollingball.x = rollingball.x + change #More in x direction
            elif direction == "L":
                rollingball.x = rollingball.x - change #Less in x direction
            elif direction == "U":
                rollingball.y = rollingball.y - change #Less in y direction
            elif direction == "D":
                rollingball.y = rollingball.y + change #More in y direction 
            
            felloff,stop,allballs = rollingball.faloff(rollingball,allballs,
                                                       felloff)
            
            #0.5 means the user lost the game, because X rolled off.
            if stop== 0.5:
                points = 0
                break
            #This means another ball than X rolled off.
            elif stop == 1:
                points = points + 1000 - 100 #-100 because of the action.
                break
            onecollission = 0   #This means there has been no collission
            change, q, points = rollingball.changedirection(q,change,points)
            
            #This part is for a collission with X
            if (xball.board[rollingball.y])[rollingball.x] == "X":
                (xball.board[rollingball.y])[rollingball.x] = rollingball.name
                print("Ball",rollingball.name,"collided with ball X")
                rollingball = xball #New ball with momentum
                #q=q-1
                #points=points+100    
                onecollission = 1   #Cannot collide in this turn again
            
            if onecollission == 1:
                continue
            
            #This is for a collision with any other ball.
            t=0
            while t<len(allballs):
                if ((xball.board[rollingball.y])[rollingball.x] == 
                    (allballs[t].name)):
                    (xball.board[rollingball.y])[rollingball.x] = rollingball.name
                    print("Ball",rollingball.name,"collided with ball",allballs[t].name)
                    rollingball = allballs[t]   #New moving ball
                    q=q-1
                    points=points+100
                    break
                t=t+1
            
            points=points-100   #Points subtracted per movement
            q=q+1
        
    return points

def rules():
    print("The goal of the game is to kick all the balls off the map.")
    print("Except for X.")
    print("All the 0's in the map are empty spaces.")
    print("The ones are walls and the letters are balls.")
    print("You can move the ball X by typing the direction")
    print("(R for right, L for left, U for up and D for down)")
    print("and the number of times the ball has to go in that direction.")
    print()
    print("If the ball hits a wall (a 1), it changes in direction.")
    print("If it hits another ball, all the momentum goes in that other ball.")
    print("The player starts with 1000 points. For every action 100 points get subtracted.")
    print("For every ball that is kicked off the map, the player gains 1000 points.")
    print("The player wins when all the balls are off the map.")
    print("The player loses if the ball X falls off the map or when he has 0 points.")

