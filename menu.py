#Main file with the menu
#This program is the menu for the collission game.
#The goal of this game is to kick other balls out of the map
#with your own ball.
#Last edit: January 11 2021
#Interpreter: Python 3.7.6
#Operating system: MacOS Catalina

import ball   #Own made module with class for balls
import gamefunctions as gf   #Own made module for general functions
import sys #To exit the game

print("COLLISION GAME")
print("Creators Jurjan Bootsma and Stefano Goeptar")
print("Years of arrival: 2019 and 2019")
print("Studies: Natuur- en sterrenkunde and natuurkunde")
print("Goal: This can be found in 'Rules'")
print()

#Here the loop of the menu starts.
#By making this loop infinite, the game can be played until the player
#wants to exit.
while True:
    #Choices in the menu.
    print("Type the number of map you want to play:")
    print()
    print("1. Tiny Map")
    print("2. Small Map")
    print("3. Medium Map")
    print("4. Large map")
    print("5. Rules")
    print("6. Exit game")
    
    #The maps that can be played.
    file1 = "map_tiny.txt"
    file2 = "map_small.txt"
    file3 = "map_medium.txt"
    file4 = "map_large.txt"
    
    #A list of those files
    filelist = [file1,file2,file3,file4]
    
    mapchoice = input("\n") #The user makes its choice through the menu
    print()
    options = ["1","2","3","4","5","6"] #Possible entries
    valid = gf.wronginput(options,mapchoice)    #Check if it is valid.
    if valid == 1:  #User has to choose again
        print("Choose again")
        print()
        continue
    
    if int(mapchoice) == 5: #The rules of the game have been chosen.
        print()
        gf.rules()
        continue 
    elif int(mapchoice) == 6:   #Players wants to exit game.
        sys.exit(1)
    
    #The map and all the positions of the balls get loaded for the chosen map.
    themap = gf.organize(filelist[int(mapchoice)-1]) 
    xball, allballs = gf.findballs(themap)
    
    points = gf.playing(xball, allballs)    #A level is played in 'playing'
    
    print()
    if points == 0: #Player is out of actions or fell off the map.
        print("You lost the game!")
    else:   #Player won the game.
        print("You won!")
        print("You scored", points, "points")
    print()






