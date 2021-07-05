import collections
def maxRepeatedElement(num_list):
    count_element = collections.Counter(num_list)
    return count_element.most_common()[0][0]
max_element=maxRepeatedElement([10,10,20,30,30,40,10,20,10])
print(max_element)