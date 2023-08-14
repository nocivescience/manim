from os import waitpid
from typing_extensions import runtime
from manim import *
import operator as op
class MyFaradayWithElectrones(Scene):
    def construct(self):
        my_dots=self.getttingParticles(30)
        my_dots.add_updater(self.getUpdateElectron)  
        self.add(my_dots)      
        self.gettingMyPool()
        self.wait(12)
        textoExplicativo=(
            'esto ocurre como consecuencia de la decomposición de '
            'la solución al ser expuesta a flujos de electrones '
            'decubrimiento realizado por Faraday'
        )
        MiTextoElaborado=MarkupText(textoExplicativo,justify=True).set_width(config['frame_width'])
        MiTextoElaborado.set_stroke(width=0.5,color=BLACK)
        self.play(Write(MiTextoElaborado,reverse=True),run_time=6)
        self.wait(7)
    def getttingParticles(self,n_particles):
        my_parts=np.array([
            [np.random.uniform(-config['frame_width']/2,config['frame_width']/2),np.random.uniform(-config['frame_height']/4,config['frame_height']/4),0]
            for _ in range(n_particles)
        ])
        colors=[RED,GREEN,YELLOW,BLUE]
        my_dots=VGroup()
        for part in my_parts:
            dot=Dot(radius=.1,color=YELLOW)
            dot.center=part
            dot.move_to(dot.center)
            dot.velocity=6
            dot.set_color(colors[np.random.randint(0,len(colors))])
            texto=MathTex('-').set_color(BLACK)
            texto.match_width(dot)
            texto.move_to(dot.get_center())
            dot.texto=texto
            dot.add(texto)
            my_dots.add(dot)
        my_dots.colors=colors
        return my_dots
    def getUpdateElectron(self,electrons,dt):
        for electron in electrons:
            electron.center[0]+=dt*electron.velocity
            if electron.center[0]+electron.radius>config['frame_width']/2:
                electron.center[0]=-config['frame_width']/2
                electron.set_color(electrons.colors[np.random.randint(0,len(electrons.colors))])
                electron.texto.set_color(BLACK)
                electron.texto.match_width(electron)
        for electron in electrons:
            electron.move_to(electron.center)
        return electrons
    def gettingMyPool(self):
        myRectangle=Rectangle(width=6,height=4)
        myRectangle.set_fill(color=ORANGE,opacity=1)
        myRectangle.set_stroke(width=2,color=ORANGE)
        self.play(Create(myRectangle))
        self.play(myRectangle.animate.set_opacity(0.2),run_time=10)
        self.wait(5)
        textoSolucionNaCL=Text('Solución de Cloruro de Sodio que se descompone por el flujo de electrones')
        textoSolucionNaCL.to_edge(UP,buff=0.4)
        textoSolucionNaCL.set_width(config['frame_width'])
        self.play(TransformFromCopy(myRectangle,textoSolucionNaCL))
        self.wait(5)