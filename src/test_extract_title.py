from extract_title import extract_title
import unittest

class Test_Extract_Title(unittest.TestCase):

    def test_simple_hello(self):
        heading = extract_title('#Hello World')
        self.assertEqual(heading,'Hello World')
    
    def extra_spaces_test(self):
        heading = extract_title('#      Hello World       ')
        self.assertEqual(heading,'Hello World')

if __name__=="__main__":
    unittest.main()