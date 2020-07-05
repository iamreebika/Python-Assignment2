"""
9. Write a binary search function. It should take a sorted sequence and
the item it is looking for. It should return the index of the item if found.
It should return -1 if the item is not found.
"""
sequence = [i for i in range(1, 13)]
sequence.sort()
search_item = 10


def search(seq, item):
    try:
        a = seq.index(item)
    except ValueError:
        return -1
    return a


print(search(sequence, search_item))
