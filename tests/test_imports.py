from unittest import TestCase
import geometrica

class TrigFunctionsImportTests(TestCase):

    def test_sine_law_imported(self):
        from geometrica.trig import sine_law
        self.assertIs(sine_law, geometrica.sine_law)


    def test_cosine_law_imported(self):
        from geometrica.trig import cosine_law
        self.assertIs(cosine_law, geometrica.cosine_law)



class TransformationImportTests(TestCase):

    def test_translate_imported(self):
        from geometrica.transform import translate
        self.assertIs(translate, geometrica.translate)


    def test_rotate_imported(self):
        from geometrica.transform import rotate
        self.assertIs(rotate, geometrica.rotate)
