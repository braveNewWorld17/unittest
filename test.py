import unittest
import avg

class averageTestCase(unittest.TestCase):

    def test_average1(self):
        answer = avg.compute_average([1, 2, 3, 4, 5])
        self.assertEqual(answer, 3.0)

    def test_average2(self):
        answer = avg.compute_average([2, 3, 4, 5, 6])
        self.assertEqual(answer, 4.0)
    
    def test_average3(self):
        answer = avg.compute_average(['w', 3, 4, 5, 6])
        self.assertRaisesRegex(ValueError, 'number')

    def test_empty_input_average(self):
        answer = avg.compute_average([])
        self.assertEqual(answer, 0)

if __name__ == "__main__":
    unittest.main()

