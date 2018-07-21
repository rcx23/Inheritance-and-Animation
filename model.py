import controller, sys
import model   #strange, but we need a reference to this module to pass this module to update

from ball      import Ball
from floater   import Floater
from blackhole import Black_Hole
from pulsator  import Pulsator
from hunter    import Hunter
from special import Special

import random
import math

# Global variables: declare them global in functions that assign to them: e.g., ... = or +=
cycles = 0
running = False
select = None
simultons = set()

#return a 2-tuple of the width and height of the canvas (defined in the controller)
def world():
    return (controller.the_canvas.winfo_width(),controller.the_canvas.winfo_height())

#reset all module variables to represent an empty/stopped simulation
def reset ():
    global running
    running = False
    
    global simultons
    simultons = set()
    
    global cycles
    cycles = 0

#start running the simulation
def start ():
    global running
    running = True

#stop running the simulation (freezing it)
def stop ():
    global running
    running = False

#tep just one update in the simulation
def step ():
    global simultons
    for each in simultons.copy():
        each.update()
    
    global cycles
    cycles += 1
    
    global running
    running = False

#remember the kind of object to add to the simulation when an (x,y) coordinate in the canvas
#  is clicked next (or remember to remove an object by such a click)   
def select_object(kind):
    global select
    select = kind


#add the kind of remembered object to the simulation (or remove all objects that contain the
#  clicked (x,y) coordinate
def mouse_click(x,y):
    global select
    global simultons
    
    if select == "Remove":
        for each in find(lambda temp: temp.contains((x,y))):
            remove(each)
    else:
        if select == "Ball" or select == "Floater" or select == "Hunter" or select == "Special":
            random_angle = random.random()*math.pi*2
            add(eval(select + '(x,y,'+str(random_angle) + ')' ))
        elif select == "Black_Hole" or select == "Pulsator":
            add(eval(select + '(x,y)'))


#add simulton s to the simulation
def add(s):
    global simultons
    simultons.add(s)
    
# remove simulton s from the simulation    
def remove(s):
    global simultons
    simultons.remove(s)
    

#find/return a set of simultons that each satisfy predicate p    
def find(p):
    global simultons
    temp = set()
    dump = set()
    for each in simultons:
        temp.add(each) if p(each) else dump.add(each)
    
    return temp
    


#call update for every simulton in the simulation
def update_all():
    global cycles
    global simultons
    
    copy = simultons.copy()
    if running == True:
        cycles = cycles + 1
        for each in copy:
            each.update()


#delete every simulton being simulated from the canvas; then call display for every
#  simulton being simulated to add it back to the canvas, possibly in a new location, to
#  animate it; also, update the progress label defined in the controller
def display_all():
    for each in controller.the_canvas.find_all():
        controller.the_canvas.delete(each)
    
    for each in simultons:
        each.display(controller.the_canvas)
        
    temp = str(cycles) + " cycles / " + str(len(simultons)) + " simultons"  
    controller.the_progress.config(text = temp)
        
        
