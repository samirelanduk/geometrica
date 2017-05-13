"""Contains functions for manipulating Cartesian coordinates."""

from math import radians, sin, cos
from matrices.checks import are_numeric, is_numeric
from matrices import create_vertex, Matrix

def accept_objects(func):
    """This decorator can be applied to functions whose first argument is a list
    of x, y, z points. It allows the function to also accept a list of objects
    which have x(), y() and z() methods instead."""

    def new_func(objects, *args, **kwargs):
        try:
            points = [(x, y, z) for x, y, z in objects]
        except TypeError:
            points = [(obj.x(), obj.y(), obj.z()) for obj in objects]
        return func(points, *args, **kwargs)
    new_func.__name__ = func.__name__
    new_func.__doc__ = func.__doc__
    return new_func


@accept_objects
def translate(points, x, y, z):
    """Takes a set of coordinates and translates them in three dimensional
    space.

    The points must be a list (or tuple, or any collection really) of
    coordinates in the form ``(x, y, z)``, *or* a list (etc.) of objects with
    x(), y() and z() methods.

    An example would be ``translate([(1, 1, 1), (2, 2, 2)], 5, 5, 5)``.

    :param points: A collection of (x, y, z) coordinates or appropriate objects.
    :param number x: The distance to move the points in the x direction.
    :param number y: The distance to move the points in the y direction.
    :param number z: The distance to move the points in the z direction.
    :returns: The translated coordinates."""

    if not are_numeric(x, y, z):
        raise TypeError("Translation parameters must be numeric, not '%s'" % (
         str((x, y, z))
        ))
    return tuple([tuple([px + x, py + y, pz + z]) for px, py, pz in points])


@accept_objects
def rotate(points, axis, angle, hand="right"):
    """Takes a set of coordinates and rotates them around one of the axes by a
    specified angle. The rotation performed is right-handed, unless specified
    otherwise.

    The points must be a list (or tuple, or any collection) of
    coordinates in the form ``(x, y, z)``, *or* a list (etc.) of objects with
    x(), y() and z() methods.

    An example would be ``rotate([(1, 1, 1), (2, 2, 2)], "x", 45)``.

    :param points: A collection of (x, y, z) coordinates or appropriate objects.
    :param str axis: The axis to rotate around. Accepted values are `"x"`,\
    `"y"` or `"z"`.
    :param number angle: The angle in degrees to rotate by.
    :param str hand: specifies whether the rotation should be right-handed or\
    left-handed. The deafult is 'right'.
    :returns: The rotated coordinates."""

    if not is_numeric:
        raise TypeError("angle must be numeric, not '%s'" % str(angle))
    if not isinstance(hand, str):
        raise TypeError("hand must be str, not '%s'" % str(hand))
    elif hand not in ("left", "right"):
        raise ValueError("hand must be 'left' or 'right', not %s" % hand)
    elif hand == "left":
        angle = -angle
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
