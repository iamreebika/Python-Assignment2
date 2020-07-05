"""
17. Write a program that serves as a basic calculator. It asks for two
numbers, then it asks for an operator. Gracefully deal with input that
doesn't cleanly convert to numbers. Deal with division by zero errors.
"""


def add_nums(num1, num2):
    """
    :returns the sum of two numbers
    """
    return num1 + num2


def sub_nums(num1, num2):
    """
    :returns the difference of two numbers
    """
    return num1 - num2


def mul_nums(num1, num2):
    """
    :returns the product of two numbers
    """
    return num1 * num2


def div_nums(num1, num2):
    """
    :return: the quotient of numbers
    """
    try:
        result = num1 / num2
    except ZeroDivisionError:
        return '\nError:\nThe second operand should not be zero.\n'

    return result


def start():
    stop = False
    while not stop:
        prompt_num1 = int(input('Enter the first number: '))
        prompt_num2 = int(input('Enter the second number: '))

        choice_text = """
    What operation would you like to perform?
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
"""
        print(choice_text)
        choice = int(input('Please enter your choice (1/2/3/4): '))
        if choice == 1:
            print(add_nums(prompt_num1, prompt_num2))
        elif choice == 2:
            print(sub_nums(prompt_num1, prompt_num2))
        elif choice == 3:
            print(mul_nums(prompt_num1, prompt_num2))
        elif choice == 4:
            print(div_nums(prompt_num1, prompt_num2))
        else:
            print('Please re enter the values and choose the right option!')

        continue_choice = input('Do you have more calculations? (y/n): ')
        if continue_choice == 'Y' or 'y' or '1':
            stop = False
        elif continue_choice == 'N' or 'n' or 0:
            stop = True
        else:
            stop = False


start()
