from __future__ import annotations
from manimlib import *  # type: ignore
import numpy as np


class TwoBodyProblem(InteractiveScene):
    # Theme
    dot_fill_color: ManimColor = BLACK
    dot_stroke_color: ManimColor = "#53697c"
    circle_fill_color: ManimColor = "#9bb0d2"
    circle_stroke_color: ManimColor = "#40546c"
    vector1_fill_color: ManimColor = "#5d4e76"
    vector2_fill_color: ManimColor = "#4e5b2a"

    # Phiysical properties
    origin_position = np.array([0.0, 0.0, 0.0])
    body1_relative_position: Vect3 = np.array([-3.0, 0.5, 0.0])
    body2_relative_position: Vect3 = np.array([0.2, 1.5, 0.0])
    body1_position: Vect3 = origin_position + body1_relative_position
    body2_position: Vect3 = origin_position + body2_relative_position
    body1_velocity: Vect3 = np.array([3.0, -1.5, 0.0])
    body2_velocity: Vect3 = np.array([-0.5, -3.0, 0.0])
    body1_mass: float = 1.0
    body2_mass: float = 1.0

    # Formulas
    sum_of_masses: float = body1_mass + body2_mass  # M variable
    distance_between_bodies: float = float(np.linalg.norm(body1_position - body2_position))  # r variable

    # Bodies
    body1_circle: Circle
    body2_circle: Circle
    body1_dot: Circle
    body2_dot: Circle
    position_vector1: Arrow
    position_vector2: Arrow
    vector_beetween_bodies: Arrow
    origin_dot: Circle
    origin_text: Text
    baricenter_dot: Circle
    baricenter_vector: Arrow
    baricenter_text: Text

    def construct(self):
        self.camera.background_rgba = list(color_to_rgba(RED, 1))

        # Bodies
        self.body1_circle = Circle(
            radius=0.25,
            fill_color=self.circle_fill_color,
            fill_opacity=1,
            stroke_color=self.circle_stroke_color,
            stroke_opacity=0,
        ).move_to(self.body1_position)

        self.body2_circle = Circle(
            radius=0.25,
            fill_color=self.circle_fill_color,
            fill_opacity=1,
            stroke_color=self.circle_stroke_color,
            stroke_opacity=0,
        ).move_to(self.body2_position)

        self.body1_dot = Circle(
            radius=0.08,
            fill_color=self.dot_fill_color,
            fill_opacity=1,
            stroke_color=self.dot_stroke_color,
            stroke_opacity=0,
        ).move_to(self.body1_position)

        self.body2_dot = Circle(
            radius=0.08,
            fill_color=self.dot_fill_color,
            fill_opacity=1,
            stroke_color=self.dot_stroke_color,
            stroke_opacity=0,
        ).move_to(self.body2_position)

        self.position_vector1 = Arrow(
            start=self.origin_position,
            end=self.body1_position,
            fill_color=self.vector2_fill_color,
            buff=0,
            max_tip_length_to_length_ratio=1,
            max_width_to_length_ratio=1,
        )

        self.position_vector2 = Arrow(
            start=self.origin_position,
            end=self.body2_position,
            fill_color=self.vector2_fill_color,
            buff=0,
            max_tip_length_to_length_ratio=1,
            max_width_to_length_ratio=1,
        )

        self.vector_beetween_bodies = Arrow(
            start=self.body2_position,
            end=self.body1_position,
            fill_color=self.vector1_fill_color,
            buff=0,
            max_tip_length_to_length_ratio=1,
            max_width_to_length_ratio=1,
        )

        # Origin
        self.origin_dot = Circle(
            radius=0.1,
            fill_color=self.vector1_fill_color,
            fill_opacity=1,
            stroke_color=self.dot_stroke_color,
            stroke_opacity=0,
        ).move_to(self.origin_position)
        self.origin_text = Text("O", font_size=36).next_to(self.origin_dot, np.array([0.2, -0.2, 0.0]))

        # Baricenter
        self.baricenter_dot = Circle(
            radius=0.1,
            fill_color=WHITE,
            fill_opacity=0.5,
            stroke_color=self.vector1_fill_color,
            stroke_opacity=1,
            stroke_width=2,
        ).move_to(self.calculate_barycenter())

        self.baricenter_vector = Arrow(
            start=self.origin_position,
            end=self.calculate_barycenter(),
            fill_color=self.vector1_fill_color,
            buff=0,
            max_tip_length_to_length_ratio=1,
            max_width_to_length_ratio=1,
        )

        self.baricenter_text = Text("R", font_size=36).next_to(self.baricenter_vector.get_end(), np.array([0.0, -0.8, 0.0]))

        # Add to scene
        self.add(
            self.body1_circle,
            self.body2_circle,
            self.body1_dot,
            self.body2_dot,
            self.position_vector1,
            self.position_vector2,
            self.vector_beetween_bodies,
            self.origin_dot,
            self.origin_text,
            self.baricenter_dot,
            self.baricenter_vector,
            self.baricenter_text,
        )

    def calculate_barycenter(self) -> Vect3:
        """Calculate the barycenter (center of mass) of the two-body system."""
        total_mass = self.body1_mass + self.body2_mass
        return (self.body1_mass * self.body1_position + self.body2_mass * self.body2_position) / total_mass
