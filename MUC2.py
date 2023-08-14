from manim import *
conf={
    'RADIO':2
}
def get_pending(path,proportion,dx=0.001):
    if proportion<1:
        coord_i=path.point_from_proportion(proportion)
        coord_f=path.point_from_proportion(proportion+dx)
    else:
        coord_i=path.point_from_proportion(proportion-dx)
        coord_f=path.point_from_proportion(proportion)
    line=Line(coord_i,coord_f)
    angle=line.get_angle()
    return angle
class MCU(Scene):
    def construct(self):
        self.get_circle()
    def get_circle(self):
        orbital=Circle(radius=conf['RADIO'])
        orbital.set_color(TEAL)
        square=Square(side_length=.5).move_to(orbital.points[0])
        square.save_state()
        def updateRotate(square,alpha):
            square.restore()
            angle=get_pending(orbital,alpha)
            square.move_to(orbital.point_from_proportion(alpha))
            square.rotate(angle,about_point=square.get_center())
        self.play(Create(square))
        self.play(Create(orbital))
        decoratives=self.get_decoratives(orbital)
        self.play(Create(decoratives[0]),Create(decoratives[1]))
        time=0
        anims=[UpdateFromAlphaFunc(square,updateRotate)]
        while time<40:
            myTime=1
            time+=myTime
            if time>10:
                myTime=.7
                anims.append(Indicate(decoratives[1]))
            if time>20:
                myTime=.4
                anims.append(Wiggle(decoratives[1]))
            if time>30:
                myTime=.2
                anims.append(Flash(decoratives[1],flash_radius=square.get_width()))
            self.play(*anims,run_time=myTime)
        self.wait(4)
    def get_decoratives(self,circle):
        square=Square()
        square.move_to(circle.center())
        texto=Text('+ -')
        texto.move_to(square.get_center())
        return [square,texto]