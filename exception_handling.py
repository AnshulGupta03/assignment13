#Q.1- Name and handle the exception occured in the following program: 

#a=3
#if a<4:
#    a=a/(a-3)
#    print(a)

try:
    a=3
    if a<4:
        a=a/(a-3)
        print(a)
except ZeroDivisionError as e:
    print("The exception occured in above code is ",e)

print("\n\n",10*"*")





#Q.2- Name and handle the exception occurred in the following program: 

#l=[1,2,3]
#print(l[3])

try:
    l=[1,2,3]
    print(l[3])

except IndexError as e:
    print("The exception occured in above code is ",e)

print("\n\n",10*"*")





#Q.3- What will be the output of the following code:

# Program to depict Raising Exception
 
#try:
#    raise NameError("Hi there")  # Raise Error
#except NameError:
#    print "An exception"
#    raise  # To determine whether the exception was raised or not


OUTPUT:
An exception
Traceback (most recent call last):
  File "C:\git\assignment13\exception_handling.py", line 45, in <module>
    raise NameError("Hi there")  # Raise Error
NameError: Hi there


print("\n\n",10*"*")







#Q.4- What will be the output of the following code:

 # Function which returns a/b
#def AbyB(a , b):
#	try:
#		c = ((a+b) / (a-b))
#	except ZeroDivisionError:
#		print "a/b result in 0"
#	else:
#		print c

# Driver program to test above function
#AbyB(2.0, 3.0)
#AbyB(3.0, 3.0)


OUTPUT:
-5.0
a/b result in 0


print("\n\n",10*"*")





#Q.5- Write a program to show and handle following exceptions: 
#1. Import Error
#2. Value Error
#3. Index Error

try:
    from time import currentTime   #import error

except ImportError:
    print("import error has occured because there is no class named as currentTime in time module")


try:
    x = 'age'
    int(x)                         #value error

except ValueError:
    print("value error has occured because string cannot be converted into int")


try:
    tup = (1,2,3)
    print(tup[3])                   # index error
    
except IndexError:
    print("index error has occured because length of tuple is 3 and index starts from 0")

print("\n\n",10*"*")





#Q.6- Create a user-defined exception AgeTooSmallError() that warns the user when they have entered age less than 18.
    #The code must keep taking input till the user enters the appropriate age number(less than 18).

class AgeTooSmallError(Exception):
    pass


while True:
    age = int(input("enter age :"))
    try:
        if(age < 18):
            raise AgeTooSmallError("Age is too small")
        else:
            print("adult")
            break
    
    except AgeTooSmallError as e:
        print(e)



print("\n\n",10*"*")
