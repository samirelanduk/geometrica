"""Contains functions for manipulating Cartesian coordinates."""

from math import radians, sin, cos
from matrices.checks import are_numeric, is_numeric
from matrices import create_vertex, Matrix

def translate(points, x, y, z):
    """Takes a set of coordinates and translates them in three dimensional
    space.

    The points must be a list (or tuple, or any collection really) of
    coordinates in the form ``(x, y, z)``.

    An example would be ``translate([(1, 1, 1), (2, 2, 2)], 5, 5, 5)``.

    :param points: A collection of (x, y, z) coordinates.
    :param number x: The distance to move the points in the x direction.
    :param number y: The distance to move the points in the y direction.
    :param number z: The distance to move the points in the z direction.
    :returns: The translated coordinates."""

    if not are_numeric(x, y, z):
        raise TypeError("Translation parameters must be numeric, not '%s'" % (
         str((x, y, z))
        ))
    return tuple([tuple([px + x, py + y, pz + z]) for px, py, pz in points])


def rotate(points, axis, angle):
    """Takes a set of coordinates and rotates them around one of the axes by a
    specified angle. The rotation performed is right-handed.

    The points must be a list (or tuple, or any collection really) of
    coordinates in the form ``(x, y, z)``.

    An example would be ``rotate([(1, 1, 1), (2, 2, 2)], "x", 45)``.

    :param points: A collection of (x, y, z) coordinates.
    :param str axis: The axis to rotate around. Accepted values are `"x"`,\
    `"y"` or `"z"`.
    :param number angle: The angle in degrees to rotate by.
    :returns: The rotated coordinates."""

    if not is_numeric:
        raise TypeError("angle must be numeric, not '%s'" % str(angle))
    angle = radians(angle)
    points = [create_vertex(*point) for point in points]
    matrix = None
    if axis == "x":
        matrix = Matrix(
         (1, 0, 0),
         (0, cos(angle), -sin(angle)),
         (0, sin(angle),  cos(angle))
        )
    elif axis == "y":
        matrix = Matrix(
         (cos(angle), 0, sin(angle)),
         (0, 1, 0),
         (-sin(angle), 0, cos(angle))
        )
    elif axis == "z":
        matrix = Matrix(
         (cos(angle), -sin(angle), 0),
         (sin(angle), cos(angle), 0),
         (0, 0, 1)
        )
    else:
        raise ValueError("axis can only be 'x', 'y' or 'z', not %s" % axis)
    new_points = [matrix * point for point in points]
    return tuple([point.columns()[0] for point in new_points])
