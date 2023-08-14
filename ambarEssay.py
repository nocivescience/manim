from manim import *
class Evaporacion(Scene):
    conf={
        'colors':[RED,GREEN,BLUE]
    }
    def construct(self):
        rectangle=Rectangle(width=6,height=4).set_color(TEAL).set_opacity(opacity=1)
        self.play(FadeIn(rectangle))
        dot=self.get_atoms(rectangle)
        self.wait()
        self.play(rectangle.animate.set_opacity(opacity=0.3),run_time=15)
    def get_atoms(self,rectangle):
        number=10
        positions=np.array([[np.random.uniform(-rectangle.width/2+0.4,rectangle.width/2-0.4),
            np.random.uniform(-rectangle.height/2+0.4,rectangle.height/2+0.4),0] for _ in range(number)])
        dots=VGroup(*[Dot().move_to(pos) for pos in positions])

        for dot,position in zip(dots,positions):
            texto=Tex('-')
            texto.move_to(dot.get_center())
            texto.set_width(dot.get_width()-0.05)
            texto.set_color(BLACK)
            dot.position=position
            dot.add(texto)
        def get_update(mobs,dt):
            for mob in mobs:
                mob.position[1]+=2*dt
                if mob.get_center()[1]>rectangle.height/2:
                    mob.set_opacity(1-1000/(dt+0.01))
                if mob.get_center()[1]>rectangle.height/2+1:
                    mob.position[0]=np.random.uniform(-rectangle.width/2+0.4,rectangle.width/2-0.4)
                    mob.position[1]=-rectangle.height/2+0.4
                    mob.set_opacity(1)
                mob.move_to(mob.position)
                mob.rotate(TAU*np.random.uniform(-.1,.1))
                mob.shift(np.random.uniform(-.1,.1)*RIGHT)
        dots.add_updater(get_update)
        self.add(dots)
        self.wait()
