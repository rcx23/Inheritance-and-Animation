#Space ship that behaves like a ball

from prey import Prey
import model


class Special(Prey):
    radius = 5
    
    def __init__(self,x,y,random_angle):
        Prey.__init__(self,x,y,Special.radius*2,Special.radius*2,random_angle,5)

    def update(self):
        self.wall_bounce()
        self.move()

    def display(self,canvas):
        #wing top
        top_x_wt = self._x - Special.radius*.5
        top_y_wt = self._y - Special.radius*3
        bottom_x_wt = self._x + Special.radius*.5
        bottom_y_wt = self._y - Special.radius
        canvas.create_rectangle(top_x_wt,top_y_wt,bottom_x_wt,bottom_y_wt,fill = "yellow")
        
        #wing bottom
        top_x_wb = self._x - Special.radius*.5
        top_y_wb = self._y + Special.radius*3
        bottom_x_wb = self._x + Special.radius*.5
        bottom_y_wb = self._y - Special.radius
        canvas.create_rectangle(top_x_wb,top_y_wb,bottom_x_wb,bottom_y_wb,fill = "yellow")
        
        #back top
        top_x_bt = self._x + Special.radius*2
        top_y_bt = self._y - Special.radius*6.5
        bottom_x_bt = self._x + Special.radius*5
        bottom_y_bt = self._y - Special.radius*6
        canvas.create_rectangle(top_x_bt,top_y_bt,bottom_x_bt,bottom_y_bt,fill = "yellow")
        
        #back bottom
        top_x_bb = self._x + Special.radius*2
        top_y_bb = self._y + Special.radius*6
        bottom_x_bb = self._x + Special.radius*5
        bottom_y_bb = self._y + Special.radius*6.5
        canvas.create_rectangle(top_x_bb,top_y_bb,bottom_x_bb,bottom_y_bb,fill = "yellow")
        
        #back
        top_x_b = self._x + Special.radius*3
        top_y_b = self._y - Special.radius*6
        bottom_x_b = self._x + Special.radius*4
        bottom_y_b = self._y + Special.radius*6
        canvas.create_rectangle(top_x_b,top_y_b,bottom_x_b,bottom_y_b,fill = "yellow")
        
        #body
        top_x_r = self._x - Special.radius*4
        top_y_r = self._y - Special.radius*2
        bottom_x_r = self._x + Special.radius*4
        bottom_y_r = self._y + Special.radius*2
        canvas.create_rectangle(top_x_r,top_y_r,bottom_x_r,bottom_y_r,fill = "red")
        
        #cockpit
        top_x = self._x - Special.radius*2
        top_y = self._y - Special.radius
        bottom_x = self._x - Special.radius
        bottom_y = self._y + Special.radius
        canvas.create_oval(top_x,top_y,bottom_x,bottom_y,fill = "black")
        
        #fuel pipe
        top_x_fp = self._x + Special.radius*4
        top_y_fp = self._y - Special.radius*.5
        bottom_x_fp = self._x + Special.radius*6
        bottom_y_fp = self._y + Special.radius*.5
        canvas.create_rectangle(top_x_fp,top_y_fp,bottom_x_fp,bottom_y_fp,fill = "#696969")
        
    
