"""
Functions for calculating the volume of certain shapes
"""
from math import pi


class Formulas(object):

    @staticmethod
    def cube_volume(side: int):
        """
        Calculate the volume of a cube V = S ^ 3
        :param side: Length of side of the cube
        :return: The volume of the cube
        """
        volume = side ** 3
        return volume

    @staticmethod
    def sphere_volume(radius: int):
        """
        Calculate the volume of a sphere V = 4/3(pi * radius ^ 3)
        :param radius: the radii of the sphere
        :return: the volume of the sphere
        """
        volume = 4/3 * (pi * (radius ** 3))
        return volume

    @staticmethod
    def right_square_pyramid(base_edge: int, height: int):
        """
        Calculate the volume of a Right Square Pyramid
        V = base_edge ^ 2 * (height / 3)
        :param base_edge: the length of one of the edges
        :param height: Height of the pyramid
        :return: volume of the pyramid
        """
        volume = (base_edge ** 2) * (height / 3)
        return volume


