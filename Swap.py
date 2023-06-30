# to swap two number without using third variable
a = int(input("please give first number a: "))   #2
b = int(input("please give second number b: "))  #5
a=a-b
b=a+b
a=b-a
print("After swapping")
print("value of a is : ", a);    #5
print("value of b is : ", b);    #2

"""
After swapping
value of a is :  5
value of b is :  2"""

#using third variable

a = int(input("please give first number a: "))
b = int(input("please give second number b: "))
tempvar=a
a=b
b=tempvar
print("After swapping")
print("value of a is : ", a);
print("value of b is : ", b);
