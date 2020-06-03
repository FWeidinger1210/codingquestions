# Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
# You can modify the input array in-place.


listA = [0, 1, 7, 2, 4, 1, 9, 1, 5, 8, 6, -2]

def findLowestPositiveInt(lst):
    lowest_positive_index_in_lst = 0
    highest_positive_index_in_lst = 0
    for x in range(0, len(lst)):
        if lst[x] > lst[x - 1]:
            highest_positive_index_in_lst = lst[x]
    for x in range(0, len(lst)):
        if lst[x] > 0 and lst[x] < lst[x - 1]:
            lowest_positive_index_in_lst = lst[x]
    # print(lowest_positive_index_in_lst,highest_positive_index_in_lst)
    if lst[lowest_positive_index_in_lst] - 1 in lst:
        return lst[highest_positive_index_in_lst] + 1
    else:
        return lst[lowest_positive_index_in_lst] - 1


print("The lowest positive Integer in this list would resolve to: ", findLowestPositiveInt(listA))
