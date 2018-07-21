# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions


from blackhole import Black_Hole
import model

class Pulsator(Black_Hole):
    disappear = 30
    def __init__(self,x,y):
        Black_Hole.__init__(self,x,y)
        self.count = 0
    
    def update(self):
        if self.radius-1 != 0:
            something_is_eaten = Black_Hole.update(self)
            if something_is_eaten:
                self.change_dimension(1,1)
                self.count = 0
            else:
                self.count += 1
                if self.count == Pulsator.disappear:
                    if self.radius - 1 == 0:
                        model.remove(self)
                        self.count == 0
                    else:
                        self.change_dimension(-1,-1)
                        self.count = 0
            return something_is_eaten
        else:
            model.remove(self)