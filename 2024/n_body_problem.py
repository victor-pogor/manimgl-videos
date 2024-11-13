from manimlib import *
import numpy as np

XYPoint = Tuple[float, float]


class TwoBodyProblem(InteractiveScene):
    def construct(self):
        # Constants
        body1_position: XYPoint = (5.0, 10.0)
