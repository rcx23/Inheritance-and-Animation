# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage


#from PIL.ImageTk import PhotoImage
from prey import Prey
from random import random


class Floater(Prey):
    radius = 5
    def __init__(self,x,y,random_angle):
        Prey.__init__(self,x,y,Floater.radius*2,Floater.radius*2,random_angle,5)
    
    def update(self):
        if random() > .3:
            self.move()
            self.wall_bounce()
        else:
            random_minus = random() - .5
            random_plus = random() + .5
            random_choose = random_minus

            if self.get_speed() > 3 and self.get_speed() < 7:
                if random() > .5:
                    random_choose = random_minus
                else:
                    random_choose = random_plus
                self.set_speed(self.get_speed() + random_choose)
                
            self.set_angle(self.get_angle() + random_choose)
            
            self.move()
            self.wall_bounce()
                
    
    def display(self,canvas):
        top_x = self._x - Floater.radius
        top_y = self._y - Floater.radius
        bottom_x = self._x + Floater.radius
        bottom_y = self._y + Floater.radius
        canvas.create_oval(top_x,top_y,bottom_x,bottom_y,fill = "#FF0000")