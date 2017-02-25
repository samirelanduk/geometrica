"""Contains functions for using trigonometry equations."""

from math import radians, degrees, sin, asin, cos, acos, sqrt
from matrices.checks import is_numeric

def sine_law(side1=None, angle1=None, side2=None, angle2=None, obtuse=False):
    """The sine law states concerns the fixed ratio between each angle and its
    opposing side, and is given by:

    .. math::
        \\frac{\\sin A}{a}=\\frac{\\sin B}{b}=\\frac{\\sin C}{c}

    It is particularly useful for determining either an unknown side or an
    unknown angle in a triangle, providing the opposite element is known and one
    other angle-side pair.

    You must provide three arguments - if you give two angles and a side, a side
    length will be returned, and if you give two sides and an angle, an angle
    will be returned.

    :param Number side1: A triangle side length.
    :param Number angle1: A triangle angle in degrees.
    :param Number side2: A triangle side length.
    :param Number angle2: A triangle angle in degrees.
    :param bool obtuse: This is relevant if you are trying to determine an\
    angle - the sine law will return an angle less than 90° unless you set this\
    to ``True``. Look up "sine law ambiguous case" for more information.
    :raises TypeError: if you supply all four arguments instead of just three.
    :rtype: ``float``"""

    if side1 is not None and not is_numeric(side1):
        raise TypeError("side1 must be a number, not '%s'" % str(side1))
    if side2 is not None and not is_numeric(side2):
        raise TypeError("side2 must be a number, not '%s'" % str(side2))
    if angle1 is not None and not is_numeric(angle1):
        raise TypeError("angle1 must be a number, not '%s'" % str(angle1))
    if angle2 is not None and not is_numeric(angle2):
        raise TypeError("angle2 must be a number, not '%s'" % str(angle2))
    if [side1, angle1, side2, angle2].count(None) != 1:
        raise TypeError("You must supply exactly three arguments to sine_law()")

    angle = None
    if side1 is None:
        return (side2 * sin(radians(angle1))) / sin(radians(angle2))
    elif side2 is None:
        return (side1 * sin(radians(angle2))) / sin(radians(angle1))
    elif angle1 is None:
        angle = degrees(asin((side1 * sin(radians(angle2))) / side2))
    elif angle2 is None:
        angle = degrees(asin((side2 * sin(radians(angle1))) / side1))
    if (obtuse and angle < 90) or (not obtuse and angle > 90):
        return 180 - angle
    else:
        return angle


def cosine_law(side1, side2, side3=None, angle=None):
    """The cosine law is as follows:

    .. math::
        c^2 = a^2 + b^2 + 2ab {\\cos C}

    It is useful in working out an angle or a side, provided you know the
    opposite element and two other sides.

    :param Number side1: A triangle side length.
    :param Number side2: A trinagle side length.
    :param Number side3: The triangle side length of interest.
    :param Number angle: The angle of interest.
    :raises TypeError: if you supply all four arguments instead of just three.
    :rtype: ``float``"""

    if not is_numeric(side1):
        raise TypeError("side1 must be a number, not '%s'" % str(side1))
    if not is_numeric(side2):
        raise TypeError("side2 must be a number, not '%s'" % str(side2))
    if side3 is not None and not is_numeric(side3):
        raise TypeError("side3 must be a number, not '%s'" % str(side3))
    if angle is not None and not is_numeric(angle):
        raise TypeError("angle must be a number, not '%s'" % str(angle))
    if side3 is not None and angle is not None:
        raise TypeError("side3 and angle both supplied")
    if side3 is None and angle is None:
        raise TypeError("You must supply either an angle or a side3")

    if side3 is None:
        return sqrt(
         ((side1 ** 2) + (side2 ** 2)) - (2 * side1 * side2 * cos(radians(angle)))
        )
    elif angle is None:
        return degrees(acos(
         ((side3 ** 2) - ((side1 ** 2) + (side2 ** 2))) / (-2 * side1 * side2)
        ))
