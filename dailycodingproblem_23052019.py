
#Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
#Bonus: Can you do this in one pass?


listA=[10,15,3,7,5,90,15,8,9]
def findSolution(lst,k):
    for x in range(0,len(lst)):
        temp=k-lst[x]
        print(temp)
        if temp in lst:
            print("True")
            exit(0)

    else:
         print("False")
         exit(2)

findSolution(listA,17)

jodel_list=[5, 6, 7, 10]

