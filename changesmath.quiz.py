import random


def generate_random_integer(min_value, max_value):
    """
    Generates a random integer within the specified range.

    Args:
        min_value (int): Minimum value of the range.
        max_value (int): Maximum value of the range.

    Returns:
        int: Random integer within the specified range.
    """
    return random.randint(min_value, max_value)


def generate_random_operator():
    """
    Generates a random arithmetic operator.

    Returns:
        str: Random arithmetic operator (+, -, or *).
    """
    return random.choice(['+', '-', '*'])


def calculate_result(num1, num2, operator):
    """
    Calculates the result of the arithmetic operation.

    Args:
        num1 (int): First operand.
        num2 (int): Second operand.
        operator (str): Arithmetic operator.

    Returns:
        tuple: A tuple containing the arithmetic expression and its result.
    """
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    else:
        result = num1 * num2

    expression = f"{num1} {operator} {num2}"
    return expression, result


def math_quiz():
    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        num1 = generate_random_integer(1, 10)
        num2 = generate_random_integer(1, 5)
        operator = generate_random_operator()

        problem, answer = calculate_result(num1, num2, operator)
        print(f"\nQuestion: {problem}")
        user_answer = int(input("Your answer: "))

        if user_answer == answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")


if __name__ == "__main__":
    math_quiz()