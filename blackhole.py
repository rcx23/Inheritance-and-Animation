# Black_Hole is derived from Simulton only: it updates by finding/removing
#   any Prey whose center is contained within its radius
#  (returning a set of all eaten simultons), and
#   displays as a black circle with a radius of 10
#   (width/height 20).
# Calling get_dimension for the width/height (for
#   containment and displaying) will facilitate
#   inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey
import model

class Black_Hole(Simulton):
    radius = 10
    def __init__(self,x,y):
        Simulton.__init__(self,x,y,Black_Hole.radius*2,Black_Hole.radius*2)

    def update(self):
        blackhole_can_eat = model.find(lambda temp: isinstance(temp,Prey) and temp.contains((self._x,self._y)))
        
        for each in blackhole_can_eat:
                model.remove(each)
        
        return blackhole_can_eat
            
    def display(self, canvas):
        top_x = self._x - (self.get_dimension()[0]/2)
        top_y = self._y - (self.get_dimension()[0]/2)
        bottom_x = self._x + (self.get_dimension()[0]/2)
        bottom_y = self._y + (self.get_dimension()[0]/2)
        canvas.create_oval(top_x,top_y,bottom_x,bottom_y,fill = "black")


    def contains(self, xy):
        if self.distance(xy) < Black_Hole.radius:
            return True
        else:
            return False