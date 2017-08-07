"""
Functions for calculating the volume of certain shapes
"""
from math import pi, sqrt


def cube_volume(side: int):
    """
    Calculate the volume of a cube V = S ^ 3
    :param side: Length of side of the cube
    :return: The volume of the cube
    """
    if side <= 0:
        raise ValueError('Side length must be greater than 0')

    volume = side ** 3
    return round(volume, 2)


def sphere_volume(radius: int):
    """
    Calculate the volume of a sphere V = 4/3(pi * radius ^ 3)
    :param radius: the radii of the sphere
    :return: the volume of the sphere
    """
    if radius <= 0:
        raise Exception('Radius must be greater than 0')
    else:
        volume = 4/3 * (pi * (radius ** 3))
        return float('{0:.2f}'.format(volume))


def right_square_pyramid(base_edge: int, height: int):
    """
    Calculate the volume of a Right Square Pyramid
    V = base_edge ^ 2 * (height / 3)
    :param base_edge: the length of one of the edges
    :param height: Height of the pyramid
    :return: volume of the pyramid
    """
    if base_edge <= 0 or height <= 0:
        raise Exception('Base Edge and/or Height must be greater than 0')
    else:
        volume = (base_edge ** 2) * (height / 3)
        return float('{0:.2f}'.format(volume))


def cylinder_volume(radius: int, height: int):
    """
    Calculate the volume of a cylinder
    V = pi * (radius ** 2 * (height))
    :param radius: The radius of the cylinder
    :param height: The height of the cylinder
    :return: volume of the cylinder
    """
    if radius <= 0 or height <= 0:
        raise Exception('Radius and/or Height must be greater than 0')
    else:
        volume = pi * (radius ** 2 * height)
        return float('{0:.2f}'.format(volume))


def dodecahedron_volume(side: int):
    """
    Calculate the volume of a dodecahedron
    V = ((15 + 7) * sqrt5 / 4) * side ** 3
    :param side: length of one edge
    :return: volume of the dodecahedron
    """
    if side <= 0:
        raise Exception('Side length much be greater than 0')
    else:
        volume = ((15 + 7 * sqrt(5)) / 4) * side ** 3
        return float('{0:.2f}'.format(volume))


