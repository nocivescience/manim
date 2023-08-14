from manim import *
class LaCargaElectrica(Scene):
    def construct(self):
        formula1=MathTex('e=1.6\\cdot 10^{-19}C').set_width(config['frame_width'])
        formula1.set_color_by_gradient(RED,YELLOW)
        self.play(Write(formula1),run_time=3)
        self.wait(5) 
        