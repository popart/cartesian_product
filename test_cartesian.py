import unittest
from cartesian import *

class TestCartesian(unittest.TestCase):
    def test_split(self):
        self.assertEqual(split(''), [''])
        self.assertEqual(split('a,b,c'), ['a', 'b', 'c'])
        self.assertEqual(split('a,'), ['a', ''])
        self.assertEqual(split(',a'), ['', 'a'])
        self.assertEqual(split('a{b,c}'), ['a{b,c}'])
        self.assertEqual(split('a{{b,c}}'), ['a{{b,c}}'])
        self.assertEqual(split('}}{b,c},}'), ['}}{b,c}', '}'])

    def test_tokenize(self):
        self.assertEqual(tokenize(''), ([''], []))
        self.assertEqual(tokenize('abc{1,2,3}'),
                (['abc', ''], [['1', '2', '3']]))
        self.assertEqual(tokenize('{1,2,3}abc'),
                (['', 'abc'], [['1', '2', '3']]))
        self.assertEqual(tokenize('a{1,2}b{x,y}'),
                (['a', 'b', ''], [['1', '2'], ['x', 'y']]))
        self.assertEqual(tokenize('a{x{1,2}y}'),
                (['a', ''], [['x{1,2}y']]))
        with self.assertRaises(InputException):
            tokenize('}}{1,2}{{')

    def test_cartesian(self):
        self.assertEqual(cartesian(''), [''])
        self.assertEqual(cartesian('a{1,2}'), ['a1', 'a2'])
        self.assertEqual(cartesian('{1,2}{x,y}'), ['1x', '1y', '2x', '2y'])
        self.assertEqual(cartesian('{1,2}{x,y}{a,b}'),
                ['1xa', '1xb', '1ya', '1yb', '2xa', '2xb', '2ya', '2yb'])
        self.assertEqual(cartesian('{a,}z'), ['az', 'z'])
        self.assertEqual(cartesian('a{x,y{1,2}}'),
                ['ax', 'ay1', 'ay2'])
        with self.assertRaises(InputException):
            cartesian('}}{1,2}{{')
        with self.assertRaises(InputException):
            cartesian('a{1, 2}')

if __name__ == "__main__":
    unittest.main()
