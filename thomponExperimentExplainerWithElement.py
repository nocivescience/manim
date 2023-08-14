from manim import *
class WithGraphics(ZoomedScene):
    def __init__(self,**kwargs):
        ZoomedScene.__init__(
            self,
            zoomed_display_height=2,
            zoomed_display_width=4,
            image_frame_stroke_width=5,
            zoomed_camera_config={
                'default_frame_stroke_width':2
            },
            **kwargs
        )
    def construct(self):
        myAxes=Axes(x_range=[0,10,2]).add_coordinates()
        self.play(Create(myAxes))
        myForm1= lambda x: (.04*x)**2
        myForm2= lambda x: (.16*x)**2
        myFunc1=myAxes.get_graph(myForm1,x_range=[0,10],color=BLUE)
        myFunc2=myAxes.get_graph(myForm2,x_range=[0,10],color=BLUE)
        self.wait()
        point0_1=myAxes.c2p(4,myForm1(4))
        point0_2=myAxes.c2p(4,myForm2(4))
        point1_1=myAxes.c2p(8,myForm1(8))
        point2_1=myAxes.c2p(8,myForm2(8))
        dot0_1=Dot(point0_1).set_z_index(1)
        dot0_2=Dot(point0_2).set_z_index(1)
        dot1=Dot().move_to(point1_1).set_z_index(1)
        dot2=Dot().move_to(point2_1).set_z_index(1)
        self.play(Create(dot1),Create(dot0_1))
        self.wait()
        self.play(Create(myFunc1))
        self.wait()
        self.play(myFunc1.animate.become(myFunc2),dot1
            .animate.become(dot2),dot0_1
            .animate.become(dot0_2))
        texto=Text('La curvatura se pronuncia al acercar un campo magnético '
            'lo que demuestra que los electrones son afectados '
            'por la presencia de dichos campos'
        ).set_stroke(BLACK,width=1).set_width(config['frame_width'])
        self.wait()
        self.wait()
        time=0
        while time<15:
            myTime=.5
            time+=myTime
            self.play(ShowPassingFlash(myFunc2.copy().set_stroke(YELLOW,width=7),run_time=myTime,width_time=.3))
        self.wait()
        trajectory=Text('Trayectoria de electrón expuesto a un campo eléctrico o magnético').to_edge(UP).set_width(config['frame_width']-.5)
        self.play(TransformFromCopy(myFunc2,trajectory))
        self.wait(4)
        trajectory2=Text('La curvatura dependerá de la intensidad y de la proximidad del (o los) campo(s)').to_edge(UP).set_width(config['frame_width']-.5)
        self.play(ReplacementTransform(trajectory,trajectory2))
        self.wait(4)