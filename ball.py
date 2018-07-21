# A Ball is Prey; it updates by moving in a straight
#   line and displays as blue circle with a radius
#   of 5 (width/height 10).


from prey import Prey


class Ball(Prey):
    radius = 5
    
    def __init__(self,x,y,random_angle):
        Prey.__init__(self,x,y,Ball.radius*2,Ball.radius*2,random_angle,5)
        
    def update(self):
        self.wall_bounce()
        self.move()
    
    def display(self,canvas):
        top_x = self._x - Ball.radius
        top_y = self._y - Ball.radius
        bottom_x = self._x + Ball.radius
        bottom_y = self._y + Ball.radius
        canvas.create_oval(top_x,top_y,bottom_x,bottom_y,fill = "#0000CD")
