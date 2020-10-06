import unittest
from chooser import Chooser

class TestMe(unittest.TestCase):

    def test_emptyChooser_returnsNothing(self):
        generator = Chooser(names=[], honorifics=[])
        self.assertEqual("", generator.next())
        
    def test_single_name_returns(self):
        generator = Chooser(names=['x'], honorifics=[])
        self.assertIn('x', generator.next())
        self.assertIn('x', generator.next())

    def test_alternatesMultipleNames(self):
        generator = Chooser(names=['a','b'], honorifics=[])
        (a_entry,b_entry) = sorted([generator.next(), generator.next()])
        self.assertIn('a', a_entry)
        self.assertIn('b', b_entry)
        
    def test_returnsSingleHonorificEveryTime(self):
        honor = 'hero'
        generator = Chooser(names=['a','b','c'], honorifics=[honor])
        self.assertIn(honor, generator.next())
        self.assertIn(honor, generator.next())
        self.assertIn(honor, generator.next())
    
    def test_some_shuffling(self):
        honors = ['1', '2', '3','4']
        names = ['a','b','c']
        initial = Chooser(names,honors).next()
        first_calls = [ Chooser(names,honors).next() for i in range(20) ]
        self.assertFalse( all(x == initial for x in first_calls),
                f"Should shuffle, but always starts with'{initial}'")

        

