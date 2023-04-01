#sum two numbers
from xml.sax.handler import property_interning_dict


print("print to screen",5)
print("Print Sum 1+2=",1+2)
#subtraction
print("5-2:",5-2)
#multiplication
print("multiplicarion",5*5)
#Divition
print("Divition 10/2",10/2)
#expontiation (rise to power)
print("exponentiation 10**2",10**2)
# floor divition (integer result)
print("floor Divition 5/2",5//2)
#divition Reminder(Modulo)
print( "Reminder divition 5%3",5%3)

'''Precednece Operation
1- ()
2- **
3- * / //
4- + -

'''
#string Operation
#Object attribute ( feature and function)
course_name="Python foundation"
print(course_name.upper())
print(course_name.lower())
print(course_name.capitalize())
print(course_name.count("Y")) # counting substring (case sensitive)
print(course_name.startswith("P")) #return true or false ( is it start with ??)
print(course_name.endswith("v")) # is it end with ??

#checking is a number ??
print(course_name.isnumeric())
print(course_name.isdigit())

#striung concatination
print("this course name is " + course_name + " by Twiaq Academy")

#string Interpltation ( formating )
print(f"course name is {course_name}")

# BMI Calculator    
name = input("please Enter your name : ")
weight = input("please Enter your weight :")
height = input("please Enter your height : ")
bmi = float(weight)/(float(height)**2)
print(f" BMI : {bmi}")

