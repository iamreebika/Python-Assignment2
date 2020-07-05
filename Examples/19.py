"""
19. Write a Python class to find validity of a string of parentheses, '(',
')', '{', '}', '[' and ']. These brackets must be close in the correct order,
for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid
"""


class ParenthesesValidation:
    paragraph = ''
    open_parentheses = tuple('[{(')
    closed_parentheses = tuple(']})')
    parentheses_map = dict(zip(open_parentheses, closed_parentheses))

    def __init__(self, para=''):
        self.paragraph = para

    def check_if_valid(self):
        """
        :return: returns the string valid or invalid
        """
        stack = []
        letters_list = list(self.paragraph)
        for letter in letters_list:
            if letter in self.open_parentheses:
                stack.append(letter)
            elif letter in self.closed_parentheses:
                if len(stack) > 0:
                    open_pr = stack.pop()
                    if self.parentheses_map[open_pr] == letter:
                        pass
                    else:
                        return 'Parentheses are not valid!'
                else:
                    stack.append(letter)
                    break
        if len(stack) == 0:
            return 'Parentheses are valid!'
        else:
            return 'Parentheses are not valid!'


# check_para = ParenthesesValidation('hello my name is {anja[{()}]l} bam()')
check_para = ParenthesesValidation()
check_para.paragraph = 'hello my name[] is {anja[{()}]l} bam()'
print(check_para.check_if_valid())
