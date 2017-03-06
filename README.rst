geometrica
==========

matrices is a pure-python library for handling geometry and trigonometry.

Example
-------

  >>> import geometrica
  >>> geometrica.translate([(1, 1, 1), (3, 4, -8)], 5, 5, 5)
  ((6, 6, 6), (8, 9, -3))
  >>> geometrica.rotate([(1, 1, 1), (3, 4, -8)], "x", 90)
  ((1, -1, 1), (3, 8, 4))



Installing
----------

pip
~~~

geometrica can be installed using pip:

``$ pip install geometrica``

geometrica is written for Python 3. If the above installation fails, it may be
that your system uses ``pip`` for the Python 2 version - if so, try:

``$ pip3 install geometrica``

Requirements
~~~~~~~~~~~~

geometrica requires the Python library
`matrices <https://matrices.samireland.com/>`_ - pip will install this
automatically when it installs geometrica.


Overview
--------

geometrica currently contains tools for using the trigonometric laws, and
processing coordinates.

Trigonometry
~~~~~~~~~~~~

The sine law and cosine law are both trigonometric equations that allow you to
determine some missing component of a triangle given a specific set of known
components.

The sine law, for example, allows you to determine a side if you know the
opposite angle, and another side-angle pair - or, alternatively, it can tell
you an angle if you know the opposing side and another side-angle pair. See the
documentation for ``sine_law`` for more details.

    >>> import geometrica
    >>> geometrica.sine_law(side1=7, angle1=35, angle2=105)
    11.788282006559363
    >>> geometrica.sine_law(side1=7, angle1=35, side2=11.8)
    75.21404844616559
    >>> geometrica.sine_law(side1=7, angle1=35, side2=11.8, obtuse=True)
    104.78595155383441

The cosine law (``cosine_law``) can be used to find any interior angle
of a triangle if you know all three sides, or a side if the opposing angle is
known as well as the other two sides. In each case, you need to know two sides,
and these are the first two arguments:

    >>> geometrica.cosine_law(5, 9, side3=8)
    62.181860715346076
    >>> geometrica.cosine_law(5, 9, angle=62.2)
    8.001574993050417

Coordinate Transformation
~~~~~~~~~~~~~~~~~~~~~~~~~

If you have a set of coordinates in three dimensional space, you can translate
them with the ``translate`` function. This will shift the set of
coordinates around but will retain their relative positions and orientation.

The coordinates are provided as a list/tuple/collection of (x, y, z) values,
along with the magnitude of the translation in the x, y, and z directions:

    >>> geometrica.translate([(1, 1, 1), (3, 4, -8)], 5, 5, 5)
    ((6, 6, 6), (8, 9, -3))

Here, two points were given - one at (1,1,1) and one at (3,4,-8) - and the two
points were translated by 5 in the positive x, y, and z directions. The
positions of the two points after the translation are returned.

You can also rotate coordinates around one of the three axes with the
``rotate`` function. The coordinates are supplied in the same way, but
you also need to provide the axis to rotate around as a one character string,
and the angle in degrees to rotate by (right-handed is the default):

    >>> geometrica.rotate([(1, 1, 1), (3, 4, -8)], "x", 90)
    ((1, -1, 1), (3, 8, 4))

Here, the two points were rotated around the x-axis by 90°.


Changelog
---------

Release 0.1.1
~~~~~~~~~~~~~

`6 March 2017`

* Added option to make coordinate rotation left-handed.

* Added required packages to setup.py


Release 0.1.0
~~~~~~~~~~~~~

`25 February 2017`

* Added trigonometry functions for using the sine and cosine laws.

* Added functions for translating and rotating coordinates.
