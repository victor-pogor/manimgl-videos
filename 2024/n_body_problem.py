from __future__ import annotations
from manimlib import *
import numpy as np


class TwoBodyProblem(InteractiveScene):
    # Theme
    dot_fill_color: ManimColor = BLACK
    dot_stroke_color: ManimColor = "#53697c"
    circle_fill_color: ManimColor = "#9bb0d2"
    circle_stroke_color: ManimColor = "#40546c"
    vector1_fill_color: ManimColor = "#5d4e76"
    vector2_fill_color: ManimColor = "#4e5b2a"

    # Constants
    dot_radius: float = 0.06
    circle_radius: float = 0.25

    # Phiysical properties
    origin = np.array([0.0, 0.0, 0.0])
    body1_relative_position: Vect3 = np.array([-3.0, 0.5, 0.0])
    body2_relative_position: Vect3 = np.array([0.5, 1.5, 0.0])
    body1_position: Vect3 = origin + body1_relative_position
    body2_position: Vect3 = origin + body2_relative_position
    body1_velocity: Vect3 = np.array([3.0, -1.5, 0.0])
    body2_velocity: Vect3 = np.array([-0.5, -3.0, 0.0])

    def construct(self):
        self.camera.background_rgba = list(color_to_rgba(RED, 1))

        # Plane
        # axes = Axes(x_range=(-100, 100, 10), y_range=(-100, 100, 10))
        # axes.add_coordinate_labels(font_size=48)

        # plane = NumberPlane(
        #     x_range=(-100, 100, 10), y_range=(-100, 100, 10), faded_line_ratio=0
        # )
        # self.add(plane, axes)

        # Bodies
        body1_circle = self.__create_body_circle().move_to(self.body1_position)
        body2_circle = self.__create_body_circle().move_to(self.body2_position)
        self.add(body2_circle, body1_circle)

        body1_dot = self.__create_body_dot().move_to(self.body1_position)
        body2_dot = self.__create_body_dot().move_to(self.body2_position)
        self.add(body1_dot, body2_dot)

        # Vectors
        # r_vector = Arrow(
        #     start=self.body1_position, end=self.body2_position, buff=0
        # )  # body1 <----- body2
        # self.add(r_vector)

        position_vector1 = Arrow(
            start=self.origin,
            end=self.body1_position,
            fill_color=self.vector2_fill_color,
            buff=0,
            max_tip_length_to_length_ratio=1,
            max_width_to_length_ratio=1,
        )

        position_vector2 = Arrow(
            start=self.origin,
            end=self.body2_position,
            fill_color=self.vector2_fill_color,
            buff=0,
            max_tip_length_to_length_ratio=1,
            max_width_to_length_ratio=1,
        )

        vector_beetween_bodies = Arrow(
            start=self.body2_position,
            end=self.body1_position,
            fill_color=self.vector1_fill_color,
            buff=0,
            max_tip_length_to_length_ratio=1,
            max_width_to_length_ratio=1,
        )

        self.add(position_vector1, position_vector2, vector_beetween_bodies)

    # Create bodies
    def __create_body_dot(
        self,
        radius=dot_radius,
        fill_color: ManimColor = dot_fill_color,
        stroke_color: ManimColor = dot_stroke_color,
    ) -> Circle:
        return Circle(
            radius=radius,
            fill_color=fill_color,
            fill_opacity=1,
            stroke_color=stroke_color,
            stroke_opacity=0,
        )

    def __create_body_circle(
        self,
        radius=circle_radius,
        fill_color: ManimColor = circle_fill_color,
        stroke_color: ManimColor = circle_stroke_color,
    ) -> Circle:
        return Circle(
            radius=radius,
            fill_color=fill_color,
            fill_opacity=1,
            stroke_color=stroke_color,
            stroke_opacity=0,
        )
