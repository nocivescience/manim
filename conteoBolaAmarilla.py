from manim import *
import operator as op
class MyPRoject(Scene):
    conf={
        'n_balls':2,
        'color_a':YELLOW,
        'color_b':RED,
        'radius_balls': .4,
        'radius_ball': .2,
    }
    def construct(self):
        balls=self.balls=self.get_balls()
        ball=self.ball_main().set_z_index(2)
        self.get_ball(ball)
        self.add(ball,balls)
        self.wait(6)
    def ball_main(self):
        radius=self.conf['radius_ball']
        ball=Dot(radius=radius,color=self.conf['color_b'])
        ball.center=ball.get_center()
        ball.radius=radius
        return ball
    def get_balls(self):
        balls=VGroup()
        positions=np.array([[-4,0,0],[4,0,0]])
        for _,pos in zip(range(self.conf['n_balls']),positions):
            radius=self.conf['radius_balls']
            ball=Dot(radius=radius)
            ball.radius=radius
            ball.set_color(self.conf['color_a'])
            ball.position=pos
            ball.move_to(pos)
            balls.add(ball)
        return balls
    def get_ball(self,ball):
        def dot_update(mob,dt):
            if mob.center[0]-mob.radius<self.balls[0].position[0]+self.balls[0].radius:
                mob.center[0]+=dt*4
            if mob.center[0]+mob.radius>self.balls[1].position[0]-self.balls[0].radius:
                mob.center[0]-=dt*4
            mob.move_to(mob.center)
        ball.add_updater(dot_update)
        return ball