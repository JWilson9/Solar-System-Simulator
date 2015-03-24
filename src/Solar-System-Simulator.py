"""By James Wilson
   DT211/2 Programming
   C12527253
"""

"""Solar-System Simulation : Where the planets rotate around the sun
   Two classes are defined: 1.Sun 2.Planets
   The sun class is how the planets class interact, by the distance from the sun
   actual distace is suns radius + planets radius + distance between the sun
   & planets.
   The new_pos  function moves the planets and plots them in a new position due to the
   force of gravity from the sun and the time factor. 
"""
from turtle import *
import math

'''Background color has been chaged to black to give the solarsystem like effect
   Screensize also changed so that you can view the movement of the planets without the planets going outside the screen
   Gravity force = 0.1
   and the time factor = 10
'''
bgcolor("black")
screensize(15000,10000)
G = 0.1
T = 10


class sun(Turtle):
    '''This is the Sun class
    '''
    
    def __init__(self, name, radius, mass, x,y, shape, color):
        '''Initalize the sun and its position
        Also initalise the Turtle, in order for the graphics of the sun to be seen by the user
        (using the turtle graphics)
        '''
        Turtle.__init__(self, shape=shape)
        self.name = name
        self.radius = radius
        self.mass = mass
        self.setpos(x,y)
        self.color(color)
        

class planets(Turtle):
    '''This is the planet class
    '''
    
    def __init__(self, name, radius, mass, color, distFromSun, xv, yv, shape, star):
        '''Initalize the planets and there position
        Also initalise the Turtle again, in order for the graphics of the planets to be seen by the user
        (using the turtle graphics)
        '''
        Turtle.__init__(self, shape=shape)
        self.penup()
        self.name = name
        self.radius = radius
        self.mass = mass
        self.color(color)
        self.dist = distFromSun
        self.xv = xv
        self.yv = yv
        
        #star.radius & star.mass are both inheritance from the Sun class
        self.sRad = star.radius
        self.s_mass = star.mass
        
        #Equation to get the actual distance from the sun and planet
        self.x =  self.sRad + self.radius + self.dist
        #Every starting position for each planet must by on the y-axis of a starting poin of 0 when plotting
        self.y = 0
        
        #Plot the initial postion of the planet on the x,y axis
        self.setpos((self.x), (self.y))
        self.pendown()  

    def new_pos(self):
        '''Update the new position of each of the planets using the new pos function,
        '''
        #Pythagorean theorem to get the distance from the sun
        self.dist = math.sqrt((self.x * self.x + self.y * self.y))
        
        #Acceleration in both x,y 
        x_acc = (G * self.s_mass * self.x) / self.dist**3
        y_acc = (G * self.s_mass *self.y) / self.dist**3
        
        #x,y velocities found by initial velocity + the time by the accleration
        self.xv = self.xv + (T * x_acc)
        self.yv = self.yv + (T * y_acc)
        
        #to get the distance of both x & y directions through the current x,y velocity and time
        distOf_x = self.xv * T
        distOf_y = self.yv * T

        #what positions the x,y values both have
        self.x = self.x - distOf_x
        self.y = self.y - distOf_y

        #plot the points on the x,y axis
        self.goto((self.x), (self.y))
        
    def __str__(self):
        return "{}: X position{}, Y position:{}".format(self.name, self.x, self.y)
        
def main():
    ''' ------------- Main Simulation ------------
    Creates the sun and the planets.
    Runs event loop (move in clock ticks) and plots the planets in their
    according x,y position.
    '''
    #Let turtle = s
    s = Turtle()
    #Hide the turtle
    s.ht()
    #Set move to be = 0
    move = 0
    #Number of times the planets will move determined by clock ticks
    CLOCK_TICKS = 1000000

    #Registering gif's to become new shapes
    s.screen.register_shape("sun.gif")  
    s.screen.register_shape("earth.gif")
    s.screen.register_shape("mars.gif")
    s.screen.register_shape("jupiter.gif")
    s.screen.register_shape("venus.gif")
    
    #Create the Sun
    star=sun("sun",500.0, 15000.0, 0,0, "sun.gif", "yellow")
    

    #Create the planets, star is being inherited into the planet class 
    p1 = planets('earth',19.5, 1000.0, "green",0.25,  0.0, 2.0, "earth.gif", star)
    p2 = planets('mars',47.5, 5000.0, "blue",  0.3, 0.0, 2.0, "mars.gif",  star)
    p3 = planets('jupiter',50.0, 9000.0, "red", 0.5, 0.0, 1.63, "jupiter.gif",  star)
    p4 = planets('venus',100.0, 49000.0, "purple", 0.7, 0.0, 1.0, "venus.gif",  star)
    
    
    #For every tick the planets will move through the new_pos function
    for move in range(CLOCK_TICKS):
        #Allow the planets to move to their new position
        p1.new_pos()
        print(p1)
        p2.new_pos()
        print(p2)
        p3.new_pos()
        print(p3)
        p4.new_pos()
        print(p4)
        
        move+=1

        
if __name__ == '__main__':
    main()

    
