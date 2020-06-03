
#Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
#For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
#Follow-up: what if you can't use division?

listA=[3,2,1,1,1]
def productArray(lst):
    product_of_all_lst=[1]*(len(lst))
    print(product_of_all_lst)
    n=1
    while n<len(lst):
      for i in range(0,len(lst)):
          product_of_all_lst[i]*=lst[i-n]
      n+=1

    return product_of_all_lst

print(productArray(listA))

