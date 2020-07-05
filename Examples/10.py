"""
10. Write a function that takes camel-cased strings (i.e.
ThisIsCamelCased), and converts them to snake case (i.e.
this_is_camel_cased). Modify the function by adding an argument,
separator, so it will also convert to the kebab case
(i.e.this-is-camel-case) as well.
"""
sample_str = 'ThisIsCamelCased'


def camelcase_to_snakecase( string, separator='_' ):
    letters = list(string)
    final_letters_list = [string[0].lower(),]
    for i in range(1, len(string)):
        current_letter = letters[i]
        if current_letter.isupper():
            final_letters_list.append(separator)
            current_letter = current_letter.lower()
        final_letters_list.append(current_letter)
    return ''.join(final_letters_list)


print(camelcase_to_snakecase(sample_str, '-'))
