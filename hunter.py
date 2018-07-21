# Hunter is derived from the Mobile_Simulton/Pulsator classes: it updates
#   like a Pulsator, but it also moves (either in a straight line
#   or in pursuit of Prey), and displays as a Pulsator.


from prey import Prey
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from math import atan2
import model


class Hunter(Pulsator,Mobile_Simulton):
    max_distance = 200
    def __init__(self,x,y,random_angle):
        Mobile_Simulton.__init__(self,x,y,self.radius*2,self.radius*2,random_angle,5)
        self.count = 0
        
    def update(self):
        possible_prey = model.find(lambda temp: isinstance(temp,Prey))
        chosen_target = None
        
        if possible_prey:
            chosen_target = min(possible_prey, key = lambda temp: self.distance(temp.get_location()) <= Hunter.max_distance)

        if chosen_target != None:
            self.set_angle(atan2(chosen_target.get_location()[1]-self.get_location()[1], chosen_target.get_location()[0]-self.get_location()[0]))
        
        self.move()
        self.wall_bounce()

        return Pulsator.update(self)
