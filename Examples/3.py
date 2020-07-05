"""
3. Write code that will print out the anagrams (words that use the same
letters) from a paragraph of text.
"""

paragraph = """ python is great language."""

# print(paragraph)
word_list = paragraph.split(' ')
print(word_list)

print('The words that are anagram in paragraph are:')
for i in range(len(word_list)):
    for j in range(i, len(word_list)-1):
        first_word_list = list(word_list[i])
        actual_word = ''.join(first_word_list)
        first_word_list.sort()
        second_word_list = list(word_list[j+1])
        second_word_list.sort()
        if first_word_list == second_word_list:
            print('->', actual_word)
