import unittest
import avg

class averageTestCase(unittest.TestCase):

    def test_average(self):
        answer = avg.compute_average([1, 2, 3, 4, 5])
        self.assertEqual(answer, 3.0)
    
    def test_empty_input_average(self):
        answer = avg.compute_average([])
        self.assertEqual(answer, 0)

if __name__ == "__main__":
    unittest.main()

