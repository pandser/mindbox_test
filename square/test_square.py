from unittest import main, TestCase 

from square import Circle, Triangle


class TestCircle(TestCase):

        def test_square(self):
            self.assertEqual(Circle(5).square(), 78.54)


class TestTriangle(TestCase):
     
    def setUp(self):
         self.triangle_1 = Triangle(3, 4, 5)
         self.triangle_2 = Triangle(12, 14, 17)
    
    def test_square(self):
        self.assertEqual(self.triangle_1.square(), 6.0)
        self.assertEqual(self.triangle_2.square(), 83.0267276243018)

    def test_rectangle(self):
        self.assertTrue(self.triangle_1.rectangular())
        self.assertFalse(self.triangle_2.rectangular())


if __name__ == '__main__':
    main()
