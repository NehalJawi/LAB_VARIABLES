'''
Create a function that takes 1 parameter of type int , 
then it prints out the result formatted like 
the following patter (if we give it 5 for example):
'''
''''
number = int(input("Enter number:1"))
while  number <= 5:
    print(number)
    '''
rows = int(input("Enter number of rows:"))
for i in range(0, rows + 1):  
    # inner loop for decrement in i values  
    for j in range(rows - i, 0, -1):  
        print(j, end=' ')  
    print("\n")