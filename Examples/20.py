"""
20. Write a Python class to find the three elements that sum to zero
from a list of n real numbers.
Input array : [-25, -10, -7, -3, 2, 4, 8, 10]
Output : [[-10, 2, 8], [-7, -3, 10]]
"""


class FindElements:

    def __init__(self, inp_arr=None):
        if inp_arr is None:
            inp_arr = []
        self.inp_arr = inp_arr

    def get_three_items_sums_to_zero(self):
        result_lst = []
        iter_dur = len(self.inp_arr)
        for fst_index in range(iter_dur):
            for sec_index in range(iter_dur):
                if sec_index != fst_index:
                    for third_index in range(iter_dur):
                        if (third_index != sec_index
                                and third_index != sec_index):
                            if (self.inp_arr[fst_index]
                                    + self.inp_arr[sec_index]
                                    + self.inp_arr[third_index] == 0):
                                result_lst.append([self.inp_arr[fst_index],
                                                   self.inp_arr[sec_index],
                                                   self.inp_arr[third_index]])
        for item in result_lst:
            item.sort()
        no_duplicates = set(tuple(x) for x in result_lst)
        result_lst = [list(lst) for lst in no_duplicates]
        return result_lst


find_el = FindElements([-25, -10, -7, -3, 2, 4, 8, 10, 17])
print(find_el.get_three_items_sums_to_zero())
