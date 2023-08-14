from random import triangular
from manim import *

def get_path_pending(path,proportion,dx=0.001):
    if proportion<1:
        coord_i=path.point_from_proportion(proportion)
        coord_f=path.point_from_proportion(proportion+dx)
    else:
        coord_i=path.point_from_proportion(proportion-dx)
        coord_f=path.point_from_proportion(proportion)
    line=Line(coord_i,coord_f)
    angle=line.get_angle()
    return angle
class ElectronWithVelocity(Scene):
    def construct(self):
        myArc=Arc(
            start_angle=1.5*PI,
            angle=PI/5,
            radius=10
        ).center()
        myArc.set_stroke(width=1,opacity=0.6)
        self.play(Create(myArc))
        dot=Dot()
        arrow=Arrow()
        startAngle=get_path_pending(myArc,0)
        dot.move_to(myArc.points[0])
        dot.rotate(0)
        dot.save_state()
        dot.rotate(
            startAngle,about_point=dot.get_center()
        )
        arrow.move_to(myArc.points[0])
        arrow.rotate(0)
        arrow.save_state()
        arrow.rotate(
            startAngle,about_point=arrow.get_center()
        )
        def updateRotateMove(mob,alpha):
            dot.restore()
            angle=get_path_pending(myArc,alpha)
            dot.move_to(myArc.point_from_proportion(alpha))
            dot.rotate(
                angle,about_point=dot.get_center()
            )
        def updateRotateMove2(mob,alpha):
            arrow.restore()
            angle=get_path_pending(myArc,alpha)
            arrow.move_to(dot.get_center() )
            arrow.rotate(
                angle,about_point=arrow.get_center()
            )
        self.play(Create(dot),Create(arrow))
        self.wait()
        time=0
        while time<20:
            myTime=3
            time+=myTime
            self.play(UpdateFromAlphaFunc(dot,updateRotateMove),UpdateFromAlphaFunc(arrow,updateRotateMove2),run_time=myTime,rate_func=linear)
        self.wait()