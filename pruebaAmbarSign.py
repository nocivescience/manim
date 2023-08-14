import numpy as np
lista=np.random.choice(['+','-'],90)
print(lista)
conf={
    'n_part':40,
    'side_square':4
}
lista2=posiciones=np.array([
            [np.random.uniform(-conf['side_square']/2,conf['side_square']/2),
            np.random.uniform(-conf['side_square']/2,conf['side_square']/2),0]
            for _ in range(100)
        ])
print(lista2)
from manim import *
number3=rotate_vector(RIGHT,0,PI)
print(number3)