from unittest import TestCase
from geometrica.transform import translate, rotate

class TransformationTest(TestCase):

    def setUp(self):
        self.points = [(1, 1, 1), (2, 1, 1), (3, 1, 1), (4, 1, 1), (5, 1, 1)]


    def assertPointsAlmostEqual(self, points1, points2):
        self.assertEqual(len(points1), len(points2))
        for index, point1 in enumerate(points1):
            point2 = points2[index]
            self.assertEqual(len(point1), len(point2), 3)
            self.assertAlmostEqual(point1[0], point2[0], delta=0.0005)
            self.assertAlmostEqual(point1[1], point2[1], delta=0.0005)
            self.assertAlmostEqual(point1[2], point2[2], delta=0.0005)



class TranslationTests(TransformationTest):

    def test_can_translate(self):
        self.assertEqual(
         translate(self.points, 3, -2, 8),
         ((4, -1, 9), (5, -1, 9), (6, -1, 9), (7, -1, 9), (8, -1, 9))
        )


    def translation_directions_must_be_numeric(self):
        with self.assertRaises(TypeError):
            translate(self.points, "3", -2, 8)
        with self.assertRaises(TypeError):
            translate(self.points, 3, "-2", 8)
        with self.assertRaises(TypeError):
            translate(self.points, 3, -2, "8")



class RotationTests(TransformationTest):

    def test_can_rotate_around_x_axis_180(self):
        self.assertPointsAlmostEqual(
         rotate(self.points, "x", 180),
         ((1, -1, -1), (2, -1, -1), (3, -1, -1), (4, -1, -1), (5, -1, -1))
        )


    def test_can_rotate_around_x_axis_90(self):
        self.assertPointsAlmostEqual(
         rotate(self.points, "x", 90),
         ((1, -1, 1), (2, -1, 1), (3, -1, 1), (4, -1, 1), (5, -1, 1))
        )


    def test_can_rotate_around_y_axis_180(self):
        self.assertPointsAlmostEqual(
         rotate(self.points, "y", 180),
         ((-1, 1, -1), (-2, 1, -1), (-3, 1, -1), (-4, 1, -1), (-5, 1, -1))
        )


    def test_can_rotate_around_y_axis_90(self):
        self.assertPointsAlmostEqual(
         rotate(self.points, "y", 90),
         ((1, 1, -1), (1, 1, -2), (1, 1, -3), (1, 1, -4), (1, 1, -5))
        )


    def test_can_rotate_around_z_axis_180(self):
        self.assertPointsAlmostEqual(
         rotate(self.points, "z", 180),
         ((-1, -1, 1), (-2, -1, 1), (-3, -1, 1), (-4, -1, 1), (-5, -1, 1))
        )


    def test_can_rotate_around_z_axis_90(self):
        self.assertPointsAlmostEqual(
         rotate(self.points, "z", 90),
         ((-1, 1, 1), (-1, 2, 1), (-1, 3, 1), (-1, 4, 1), (-1, 5, 1))
        )


    def test_can_switch_handedness(self):
        self.assertPointsAlmostEqual(
         rotate(self.points, "x", 90, hand="left"),
         ((1, 1, -1), (2, 1, -1), (3, 1, -1), (4, 1, -1), (5, 1, -1))
        )


    def test_axis_must_be_x_or_y_or_z(self):
        with self.assertRaises(ValueError):
            rotate(self.points, "a", 90)


    def test_angle_must_be_numeric(self):
        with self.assertRaises(TypeError):
            rotate(self.points, "x", "90")


    def test_hand_must_be_str(self):
        with self.assertRaises(TypeError):
            rotate(self.points, "x", 90, hand=100)


    def test_hand_must_be_valid(self):
        with self.assertRaises(ValueError):
            rotate(self.points, "x", 90, hand="wrong")
