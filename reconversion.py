from sys import path
from manim import *
import itertools as it
class MyComponents(Scene):
    conf={
        'width':6,
        'height':3,
        'colors':[GREEN,RED,YELLOW,BLUE,PURE_BLUE],
        'n_electrons':40,
    }
    def construct(self):
        self.get_animation()
    def get_animation(self):
        color_electron=it.cycle(self.conf['colors'])
        rectangle=Rectangle(width=self.conf['width'],height=self.conf['height'])
        dots=VGroup()
        positions=np.array([[np.random.uniform(-self.conf['width']/2+0.1,self.conf['width']/2)-0.1,
            np.random.uniform(-self.conf['height']/2+0.1,self.conf['height']/2)-0.1,0] for _ in range(self.conf['n_electrons'])])
        textos=np.random.choice(['a^+','b^-'],size=len(positions))
        for pos,texto in zip(positions,textos):
            dot=Dot().move_to(pos)
            dot.set_color(next(color_electron))
            text=MathTex(texto).set_width(dot.get_width()-0.01)
            text.move_to(dot.get_center())
            text.set_color(BLACK)
            dot.add(text)
            dot.pos=pos
            dots.add(dot)
        def electron_update(mobs,dt):
            for mob in mobs:
                mob.pos[1]+=dt*3
                if mob.pos[1]>rectangle.height/2:
                    mob.pos[1]=-rectangle.height/2
                mob.move_to(mob.pos)
        dots.add_updater(electron_update)
        self.add(dots,rectangle)
        self.wait(3)
        self.anodoCatodo(rectangle)
        self.wait(2)
    def anodoCatodo(self,rectangle):
        zinc=Tex('Zn').move_to(np.array([-rectangle.width/2,rectangle.height/2+0.5,0]))
        platino=Tex('Pt').move_to(np.array([rectangle.width/2,rectangle.height/2+0.5,0]))
        path=VGroup()
        path.set_points_smoothly([np.array([-rectangle.width/2,rectangle.height/2-.5,0]),ORIGIN+DOWN,np.array([rectangle.width/2,rectangle.height/2-.5,0])])
        self.play(Write(platino),Write(zinc))
        time=0
        while time<10:
            my_time=0.2
            time+=my_time
            self.play(ShowPassingFlash(path.set_color(TEAL_B)),run_time=my_time,time_width=0.2)
        self.wait()
        self.play(*[
            FadeOut(anim) for anim in [platino,zinc]
        ])
        