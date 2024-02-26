import numpy as np
from manim import *

FFMPEG_BIN = r'E:/PROGRAMS/ffmpeg-6.1.1-full_build/bin/ffmpeg.exe'

# as we know each vector can be represented as a sum of basis vectors (i, j)
# but we can transform our space (2d in tutorial). Today we'll do it linearly.
# linearly means: 1. all lines will save their shape (won't deform) 2. center of plane (0; 0) will not change position

# but why should we do it?
# 1. it's cool
# 2. we can get formula matrix vector multiplicatiion:

# for example we transformed our space linearly
# now i and j have the following coordinates (1; -2) (3; 0)
# noice

# now we can use i and j basis vectors (their new transformed versions) to implement some random vector

"""
in this case we get:
    [1 ]         [3]
x * |  |  +  y * | |    (where x and y - coordinates of original vector) 
    [-2]         [0]



if we had x = -1 and y = 2:

     [1 ]         [3]
-1 * |  |  +  2 * | |
     [-2]         [0]

getting:
        [  -1 * 1 + 2 * 3 ]
        |                 |
        [-1 * (-2) + 2 * 0]


result:
        [5]
        [2]


so here matricies are used to represent basis vectors coordinates
"""

# but enough comments: let's code!



from manim import *

class VectorExample(Scene):
    def construct(self):
        plane = NumberPlane()
        vector_i = Vector([1, 0], color=RED)
        vector_j = Vector([0, 1], color=BLUE)
        vector_1 = Vector([1, 2])
        self.add(plane, vector_i, vector_j, vector_1)
        self.play(ShowCreationThenFadeOut(plane))
        txt = Text("""Each vector can be represented
                    as sum of basis vectors""")
        self.play(Write(txt))

# lesson_3-matricies_linear_transformation
        
# python -m manim lesson_3-matricies_linear_transformation.py VectorExample