from unittest import TestCase
from geometrica.trig import sine_law, cosine_law

class SineLawTests(TestCase):

    def test_can_get_side_from_other_side_and_two_angles(self):
        self.assertAlmostEqual(
         sine_law(side1=2, angle1=30, angle2=105),
         3.86,
         delta=0.005
        )
        self.assertAlmostEqual(
         sine_law(side2=2, angle2=30, angle1=105),
         3.86,
         delta=0.005
        )


    def test_can_get_angle_given_other_angle_and_two_sides(self):
        self.assertAlmostEqual(
         sine_law(angle1=40, side1=30, side2=40),
         58.99,
         delta=0.005
        )
        self.assertAlmostEqual(
         sine_law(angle2=40, side2=30, side1=40),
         58.99,
         delta=0.005
        )


    def test_can_specify_missing_angle_is_obtuse(self):
        self.assertAlmostEqual(
         sine_law(angle1=33, side1=6, side2=10),
         65.2,
         delta=0.05
        )
        self.assertAlmostEqual(
         sine_law(angle1=33, side1=6, side2=10, obtuse=True),
         114.8,
         delta=0.05
        )


    def test_all_arguments_must_be_numeric(self):
        with self.assertRaises(TypeError):
            sine_law(side1="2", angle1=30, angle2=105)
        sine_law(side1=2.5, angle1=30, angle2=105)
        with self.assertRaises(TypeError):
            sine_law(side1=2, angle1="30", angle2=105)
        sine_law(side1=2, angle1=30.5, angle2=105)
        with self.assertRaises(TypeError):
            sine_law(side1=2, angle1=30, angle2="105")
        sine_law(side1=2, angle1=30, angle2=105.5)
        with self.assertRaises(TypeError):
            sine_law(angle1=40, side1=30, side2="40")
        sine_law(angle1=40, side1=30, side2=40.5)


    def test_three_arguments_must_be_supplied(self):
        with self.assertRaises(TypeError):
            sine_law()
        with self.assertRaises(TypeError):
            sine_law(angle1=100)
        with self.assertRaises(TypeError):
            sine_law(angle1=100, angle2=90)
        with self.assertRaises(TypeError):
            sine_law(angle1=100, angle2=90, side1=20, side2=100)



class CosineLawTests(TestCase):

    def test_can_get_side_from_other_two_sides_and_their_angle(self):
        self.assertAlmostEqual(
         cosine_law(side1=12, side2=9, angle=87),
         14.6,
         delta=0.05
        )


    def test_can_get_angle_from_three_sides(self):
        self.assertAlmostEqual(
         cosine_law(side1=60, side2=50, side3=20),
         18.2,
         delta=0.05
        )


    def test_all_arguments_must_be_numeric(self):
        with self.assertRaises(TypeError):
            cosine_law(side1="12", side2=9, angle=87)
        cosine_law(side1=12.5, side2=9, angle=87)
        with self.assertRaises(TypeError):
            cosine_law(side1=12, side2="9", angle=87)
        cosine_law(side1=12, side2=9.5, angle=87)
        with self.assertRaises(TypeError):
            cosine_law(side1=12, side2=9, angle="87")
        cosine_law(side1=12, side2=9, angle=87.5)
        with self.assertRaises(TypeError):
            cosine_law(side1=60, side2=50, side3="20")
        cosine_law(side1=60, side2=50, side3=20.5)


    def test_cannot_supply_both_angle_and_side3(self):
        with self.assertRaises(TypeError):
            cosine_law(side1=60, side2=50, side3=20, angle=100)


    def test_need_to_supply_angle_or_side3(self):
        with self.assertRaises(TypeError):
            cosine_law(side1=60, side2=50)
