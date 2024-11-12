from manimlib import *

class TwoBodyProblem(InteractiveScene):
    def construct(self):
        # Add some simple geometry
        circle = Circle(radius=1, color=BLUE)
        square = Square(side_length=2, color=RED)
        self.add(circle)
        self.add(square)
        self.embed()