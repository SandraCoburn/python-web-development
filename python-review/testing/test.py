import unittest
import main
import testing_random_func

#To run test in command line:
# python3 test.py
# or:
# python3 -m unittest
# or
# python3 -m unittest -v
class TestMain(unittest.TestCase):
    def setUp(self) -> None:
        ''' Allow us to run a piece of code before each test'''
        print('about to test a function')
    def test_do_stuff(self):
        ''' You can add some comments here! '''
        test_param = 10
        result = main.testing_func(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param = "shslkdl"
        result = main.testing_func(test_param)
        self.assertTrue(isinstance(result, ValueError))

    def test_params(self):
        test_param = None
        result = main.testing_func(test_param)
        self.assertEqual(result, "please enter number")

    def test_for_params(self):
        test_param = ''
        result = main.testing_func(test_param)
        self.assertEqual(result, "please enter number")

    def tearDown(self):
        print("cleaning up")

class TestGame(unittest.TestCase):
    def test_input(self):
        answer = 5
        guess = 5
        result = testing_random_func.guess_game(guess,answer)
        self.assertTrue(result)

    def test_input_wrong_guess(self):
        result = testing_random_func.guess_game(5,11)
        self.assertFalse(result)

    def test_input_wrong_number(self):
        result = testing_random_func.guess_game(5,0)
        self.assertFalse(result)

    def test_input_wrong_type(self):
        result = testing_random_func.guess_game(5, '10')
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()