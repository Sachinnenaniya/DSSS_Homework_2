import unittest
from math_quiz import generate_random_integer, generate_random_operator, calculate_result


class TestMathQuizFunctions(unittest.TestCase):

    def test_generate_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_value = 1
        max_value = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_random_integer(min_value, max_value)
            self.assertTrue(min_value <= rand_num <= max_value)

    def test_generate_random_operator(self):
        # Test if the generated operator is one of the valid options
        valid_operators = ['+', '-', '*']
        for _ in range(1000):  # Test a large number of random values
            operator = generate_random_operator()
            self.assertIn(operator, valid_operators)

    def test_calculate_result(self):
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (10, 3, '-', '10 - 3', 7),
            (4, 6, '*', '4 * 6', 24),
            # Add more test cases here
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = calculate_result(num1, num2, operator)
            self.assertEqual(problem, expected_problem)
            self.assertEqual(answer, expected_answer)


if __name__ == "__main__":
    unittest.main()
    
