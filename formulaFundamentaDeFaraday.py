from typing_extensions import runtime
from manim import *
class FormulaFundamentaFaraday(Scene):
    def construct(self):
        formula=MathTex('F=',"N_A",'\\cdot','e')
        formula.set_width(config['frame_width']-1)
        self.play(Write(formula))
        self.wait()
        time=0
        while time<6:
            part_time=1
            time+=part_time
            self.play(*[Indicate(form[-1],run_time=part_time) for form in [formula[1:2],formula[-1]]])
        self.wait(5)