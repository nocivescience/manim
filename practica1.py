from manim import *
def proving():
    color=YELLOW
    variable=Dot().set_color(color)
    variable.color=color
    if variable.color==GREEN:
        return str('pass')
    else:
        return str('no pass')
print(proving())