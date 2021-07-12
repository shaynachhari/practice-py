#  Int
'''Integer value can be any length such as integers 10, 2, 29, -20, -150 etc. Python has no restriction on the length of an integer.
Its value belongs to int.
Integers can be of any length, it is only limited by the memory available. '''
a = 5
print(" a = ",a)
print(a,"is of Type" , type(a))
print(a, "is int number ?", isinstance(a , int))
print(a, "is float number ?",isinstance(a , float))
print(a,"is Complex number ?", isinstance(a, complex))
print('\n')

''' Float
Float is used to store floating-point numbers like 1.9, 9.902, 15.2, etc. It is accurate upto 15 decimal points.
A floating point number is accurate up to 15 decimal places. Integer and floating points are separated by decimal 
points. 1 is integer, 1.0 is floating point number.

'''
a = 5.8
print("a = ",a)
print(a,"is of Type" ,type(a))
print(a,"is int Number ?", isinstance(a,int))
print(a,"is float Number ?", isinstance(a,float))
print(a,"is Complex Number ?", isinstance(a,complex))
print('\n')

'''
Complex
A complex number contains an ordered pair, i.e., x + iy where x and y denote the real and imaginary parts, respectively. 
The complex numbers like 2 + 14j, 2.0 + 2.3j, etc.
Complex numbers are written in the form, x + yj, where x is the real part and y is the imaginary part.
'''
a = 1+2j
print("a = ",a)
print(a,"is of Type" ,type(a))
print(a,"is int Number ?", isinstance(a,int))
print(a,"is float Number ?", isinstance(a,float))
print(a,"is Complex Number ?", isinstance(a,complex))

#We can convert between different data types by using different type conversion functions like int(), float(), str() etc.

# Integers:

x = int(20)      # x will be 10
y = int(4.8)     # y will be 4
z = int("3")     # z will be 3
print(x)
print(y)
print(z)
print('\n')

# float
x = float(20)
y = float(48)
z = float("3")
print(x)
print(y)
print(z)
print('\n')

# string
x = str("30")
y = str(33)
z = str(2.5)
print(x)
print(y)
print(z)
print('\n')

b = "Hello World!"
print(b)
print(type(b))
print(b[0])
print(b[1])
print(b[2 : 5])
print('\n')

c = " Shayna Is a Cute Girl! "
print(c.strip())
print(len(c))
print(c.upper())
print(c.lower())
print(c.replace("S" , "D"))
print(c.strip(","))




