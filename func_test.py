import unittest
import function
from unittest.mock import patch

class MyTestCase(unittest.TestCase):

    def test_add_multiply(self):
        x = 3
        y = 5
        addition, multiple = function.add_and_multiply(x, y)
        self.assertEqual(8, addition)
        self.assertEqual(15, multiple)

    @patch("function.multiply")
    def test_add_multiply2(self, mock_multiply):
        x = 3
        y = 5
        mock_multiply.return_value = 15
        addition, multiple = function.add_and_multiply(x, y)
        mock_multiply.assert_called_once_with(3, 5)

        self.assertEqual(8, addition)
        self.assertEqual(15, multiple)

if __name__=='__main__':
    unittest.main()