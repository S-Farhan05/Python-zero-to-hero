import unittest
import file

class Test_cap(unittest.TestCase):

    def test_one(self):

        word = 'python'
        result = file.cap(word)
        self.assertEqual(result,'Python')

    def test_multiple_words(self):

        word = 'hello world'
        result = file.cap(word)
        self.assertEqual(result,"Hello World") # must have world small , Title or else

if __name__ == "__main__":
    unittest.main()