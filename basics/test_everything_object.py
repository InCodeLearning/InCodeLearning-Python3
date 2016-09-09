import unittest
# to use both python test.py and python -m unittest
try:
    from . import everything_object
except:
    import everything_object


class TestEverythingObject(unittest.TestCase):
    """
    Testing everything_object.py first class everything in python.
    """

    def setUp(self):
        self.fun_object = everything_object.i_am_an_object

    def test_assign_to_var(self):
        self.assertEqual(self.fun_object, everything_object.i_am_an_object,
                         'function not equal to assigned variable')
        self.assertEqual(self.fun_object(1), 1, 'function should return'
                         'argument directly')

    def test_higher_order(self):
        self.assertEqual(everything_object.cubic(everything_object.square,
                         2), 8, "cubic of 2 should be 8")

    def test_higher_oder_sort(self):
        zepp = [('Guitar', 'Jimmy'), ('Vocals', 'Robert'), ('Bass',
                'John Paul'), ('Drums', 'John')]
        self.assertEqual(sorted(zepp, key=everything_object.second_element),
                         [('Guitar', 'Jimmy'), ('Drums', 'John'), ('Bass',
                          'John Paul'), ('Vocals', 'Robert')],
                         "should sort with second tuple element as key")

    def tearDown(self):
        self.fun_object = None

if __name__ == '__main__':
    unittest.main()
