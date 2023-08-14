from manim import *
import itertools as it
class Ambar(Scene):
    conf={
        'n_part':50,
        'colors':[YELLOW,BLUE,TEAL,GREEN,RED]
    }
    def construct(self):
        square=Square(side_length=2)
        self.play(Create(square))
        dots=self.get_dots(square)
        self.get_anim(dots)
    def get_dots(self,square):
        positions=np.array([
            [-square.side_length/2*np.random.uniform(-.8,.8),square.side_length/2*np.random.uniform(-.8,.8),0]
            for _ in range(self.conf['n_part'])
        ])
        signatures=np.random.choice(['+','-'],size=len(positions))
        dots=VGroup()
        myColors=it.cycle(self.conf['colors'])
        for pos,sign in zip(positions,signatures):
            dot=Dot().move_to(pos).set_color(next(myColors))

            if sign=='-':
                texto=Tex(sign).move_to(dot.get_center()).set_width(dot.get_width()-0.05).set_color(BLACK)
            else:
                texto=Tex(sign).move_to(dot.get_center()).match_width(dot).set_color(BLACK)
            dot.add(texto)
            dots.add(dot)
        return dots
    def get_anim(self,dots):
        time=0
        while time<100:
            positions=[]
            for particle in dots:
                posicion=rotate_vector(0.08*RIGHT,2*np.pi*np.random.random())+particle.get_center()+0.01*RIGHT
                if posicion[0]>1:
                    posicion[0]=-1
                if posicion[0]<-1:
                    posicion[0]=1
                if posicion[1]>1:
                    posicion[1]=-1
                if posicion[1]<-1:
                    posicion[1]=1
                positions.append(posicion)
            myTime=.5
            time+=myTime
            self.play(*it.chain(*[
                    (particle.animate.rotate(TAU*.2*np.random.random())
                    .move_to(pos)
                    ,)
                    for particle, pos in zip(dots, positions)
                ]), run_time=myTime
            )
        self.wait()