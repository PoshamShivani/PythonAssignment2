import collections


def max_repeated(num_list):
    count_element = collections.Counter(num_list)
    return count_element.most_common()[0][0]


print(max_repeated([10, 10, 20, 30, 30, 40, 10, 20, 10]))
