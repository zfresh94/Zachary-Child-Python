from graphics import *
import random
count = 1

window = GraphWin("Visualisation", 600, 600)
# Read in and print out the data in the data file
datafile = open("data.txt",'r') #Opens the data file 



for line in datafile:
    integer = float(line) stores the data in the line 
    #print(line)
    #while (count < 250):
    line1 = Line(Point(0,0),Point(600,600)) 
    line1.setFill(color_rgb(0,0,0))
    time.sleep(0.5)
    line1.setWidth(integer) #Uses data to adjust the width of the line 
    
    line2 = Line(Point(0,600),Point(600,0))
    line2.setFill(color_rgb(0,0,0))
    time.sleep(0.5)
    line2.setWidth(integer) #Uses data to adjust the width of the line 
    
    
    
    count = count + 1
    
    line1.draw(window)
    line2.draw(window)
    
    
    

window.getMouse()