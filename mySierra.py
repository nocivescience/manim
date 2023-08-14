from manim import *
class MiSierra(Scene):
    conf={
        'n_num':13
    }
    def construct(self):
        mi_sierra=Star(15,outer_radius=2,density=5)
        mi_sierra.add_updater(self.get_update)
        self.add(mi_sierra)
        dot=Dot().set_opacity(0)
        mi_sierra.add_updater(lambda t:t.move_to(dot.get_center()))
        time=0
        while time<self.conf['n_num']:
            position=rotate_vector(0.1*RIGHT,np.random.uniform(0,TAU))
            TIME=0.05
            time+=TIME
            self.play(dot.animate.move_to(position),run_time=TIME)
        self.wait()
    def get_update(self,mob,dt):
        mob.rotate(dt*2)
        mob.move_to(dt*rotate_vector(RIGHT*1,np.random.uniform(0,TAU)))
        return mob