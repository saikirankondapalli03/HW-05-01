from Triangle import classify_triangle
import unittest
class TestCases(unittest.TestCase):
    """This is a testing class for the classify_triangles method"""

    def test_equilateral_triangle(self):
        assert classify_triangle(1, 1, 1) == 'Equilateral triangle'
        assert classify_triangle(100, 100, 100) == 'Equilateral triangle'
        assert classify_triangle(0, 0, 0) != 'Equilateral triangle'

    def test_right_angled_triangle(self):
        """Test that right triangles are identified"""
        assert classify_triangle(15, 17, 8) == 'Right angled triangle'
        assert classify_triangle(28, 45, 53) == 'Right angled triangle'
        assert classify_triangle(12, 5, 13) == 'Right angled triangle'

    def test_isoceles_triangle(self):
        assert classify_triangle(10, 10, 10) != 'Isoceles triangle'
        assert classify_triangle(5, 5, 3) == 'Isoceles triangle'

    def test_Scalene_triangle(self):
        assert classify_triangle(13, 9, 14) == 'Scalene triangle'
        assert classify_triangle(7.7, 5, 9) == 'Scalene triangle'

    def test_invalid_triangle(self):
        assert classify_triangle(-1, -1, -9) == 'invalid input'
        assert classify_triangle(0, 0, 0) == 'invalid input'


if __name__ == '__main__':
    # note: there is no main(). Only test cases here
    unittest.main(exit=False, verbosity=2)
