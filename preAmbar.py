from manim import *
import itertools as it
class Budin(Scene):
    CONFIG={
        "circle_style":{
            "radius":2,
            "stroke_color":BLUE,
            "stroke_width":0.7
        },
        "charge_style":{
            "radius":0.06,
            "color":WHITE
        },
        "n_points":20
    }
    
    def construct(self):
        my_circle=Circle(**self.CONFIG['circle_style'])
        self.play(Create(my_circle))
        my_charges=self.my_charges(self.CONFIG['n_points'])
        self.my_movement(20,my_charges)

    def my_charges(self,n_points):
        points=np.array([
            rotate_vector(RIGHT*np.random.uniform(0,1.5),np.random.uniform(0,10*np.pi))
            for _ in range(n_points)
        ])
        
        dots=VGroup(*[
            Dot().move_to(point) for point in points
        ])
        for t in range(n_points):
            texto=Tex("-").set_color(BLACK).set_stroke(width=0)
            texto.match_width(dots[t])
            texto.shift(dots[t].get_center())
            dots[t].add(texto)
        self.play(LaggedStartMap(FadeIn,dots),run_time=3)
        return dots

    def my_movement(self,my_time,particles=None):
        if particles is not None:
            time=0
            while time<my_time:
                part_time=np.random.random()*0.2
                time+=part_time
                location=rotate_vector(0.03*RIGHT,2*np.pi)
                self.play(*it.chain(*[
                    (particle.animate.rotate(TAU*.1*m).move_to(rotate_vector(0.03*RIGHT,2*np.pi*m)+particle.get_center()),)
                    for particle, m in zip(particles, np.random.uniform(-1,1,self.CONFIG['n_points']))
                ]),
                run_time=part_time)