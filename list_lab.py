'''
Q1: Write a function that takes a list as a parameter,
and then returns the sum of all the items in that list.
'''
def list_sum(numbers):
    result:int=0
    for x in numbers:
        result=result+x
    return result


'''
Q2: Write a function that takes a list as a parameter,
and then returns the largest number from a list of numbers.
'''
def list_max(numbers):
    return max(numbers)


my_list=[1,2,3]
print("my List is :",my_list)
print("Q1: List summation Function's result :",list_sum(my_list),"\n")
print("Q2: The maximum Function's result :",list_max(my_list),"\n")

'''
Q3: Create an odd numbers list from the elements of a range from 1200 to 2000
with steps of 125, using [ list comprehension ].
'''
my_odd_list=[]
my_range= range(1200,2000,125)
for x in  my_range:
    #print(x)
    if x%2!=0:
      my_odd_list.append(x) 
print("Q3: Odd numbers list is:",my_odd_list,"\n") 

'''
Q4: use list slicing to get a new list from the previous list 
starting from the start to the 5th element in the list.
'''
list_2=[]
list_slicing=[]
for x in my_range:
    list_2.append(x)
for y in range(4,len(list_2)):
    list_slicing.append(list_2[y])

print("Q4: List Slising :",list_slicing,"\n")

