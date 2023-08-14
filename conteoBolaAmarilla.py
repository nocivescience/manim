from manim import *
import operator as op
class MyPRoject(Scene):
    conf={
        'n_balls':2,
        'color_a':YELLOW,
        'color_b':RED
    }
    def construct(self):
        balls=self.get_balls()
        dot=self.get_ball(balls)
        self.add(dot)
        self.play(Create(balls))
        self.wait(4)
    def get_balls(self):
        balls=VGroup()
        for _ in range(self.conf['n_balls']):
            ball=Dot(radius=0.4)
            ball.set_color(self.conf['color_a'])
            balls.add(ball)
        balls.arrange(RIGHT,buff=4)
        return balls
    def get_ball(self,balls):
        dot=Dot().move_to(ORIGIN)
        def dot_update(mob,dt):
            mob.get_center()[0]+=dt*4
            mob.move_to(mob.get_center())
        dot.add_updater(dot_update)
        return dot