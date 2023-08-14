from manim import *
class ThomsomExperiment(ZoomedScene):
    def __init__(self,**kwargs):
        ZoomedScene.__init__(
            self,
            zoom_factor=0.1,
            zoomed_display_width=7,
            zoomed_display_height=2,
            image_frame_stroke_width=1,
            zoomed_camera_config={
                'default_frame_stroke_width':1
            },
            **kwargs
        )
    def construct(self):
        radio=Line(ORIGIN,2*DOWN,stroke_width=2)
        circle=Circle(radius=radio.get_length(),stroke_width=2).set_stroke(opacity=0.3,width=1)
        point1=circle.point_from_proportion(.75)
        point2=circle.point_from_proportion(.79)
        dot1=Dot(radius=.03).move_to(point1)
        dot2=Dot(radius=.03).move_to(point2)
        self.play(Create(circle),Create(VGroup(dot1,dot2)))
        self.activate_zooming(animate=True)
        self.wait()
        self.play(self.zoomed_camera.frame.animate.shift(1.92*DOWN+.2*RIGHT))
        self.wait()
        myRay=VMobject()
        self.add(myRay)
        circleCopy=circle.copy().set_color(YELLOW)
        time=0
        for time_width in [0.2,0.5,1,2]:
            while time<20:
                myTime=0.7
                time+=myTime
                self.play(ShowPassingFlash(circleCopy.copy()
                .set_stroke(opacity=1).set_color(YELLOW),run_time=myTime,time_width=time_width))
        self.wait()