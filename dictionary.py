'''
Q1:Build a phone book program that receives the phone number 
(Use Input to let the user provide the number), 
and returns the name of the owner.
'''
phone_book={"1": "Amal","2":"Mohammed"}
phone_number = input("Please Enter phone number :")
if phone_number in phone_book :
    print("Username : ",phone_book[phone_number])
elif len(phone_number)!=1:
    print("please Enter 10 digits only")
elif phone_number.isnumeric() == False:
    print("please enter numbers only")
else:
    print("user not exist")

'''
Q2:Write a function that receives a list containing the following numbers :
'''
def re_arrange(my_list:list):
    sorted_list = sorted(my_list)
    return sorted_list
print(re_arrange([5, 0, 34, 9, 0, 13, 8]))



