#  Q1. Write a python script to take input for two numbers calculate and print their sum?
'''a = int(input("Enter your number "))
b = int(input("Enter your number "))
c = a+b

print("First no. a = ",a)
print("Second no. b = ",b)
print("Sum = ",c)'''

# Q2. Write a python script to take input for a number calculate and print its square?
"""a = int(input("Enter your number "))
b = a*a
print("number :" ,a)
print("square : ",b) """

#  Q3 Write a python script to take input for a number calculate and print its cube?
'''a = int(input("Enter your number "))
b = a*a*a
print("Number : ",b)
print("Cube : ",b)'''

# Q4  Write a python script to take input for two numbers to calculate and print their difference?
'''a = int(input("Enter your number "))
b = int(input("Enter your number "))
c = a-b
print("First Number a = ",a)
print("Second number b = ",b)
print("difference = ",c)'''

# Q5 Write a python script to take input for three numbers calculate and print their product?
'''a = int(input("Enter your 1st number "))
b = int(input("Enter your 2nd number "))
c = int(input("Enter your 3rd number "))
p = a*b*c
print("1st no. ",a)
print("2nd no. ",b)
print("3rd no. ",c)
print("Product ",p) '''

# Q6 Write a python script to take input for two numbers calculate and print their sum, product, difference, and average?
''' a = int(input("Enter your 1st number "))
b = int(input("Enter your 2nd number "))
s = a+b
d = a-b
p= a*b
av = (a+b)/2

print("First no. ",a)
print("Second no. ",b)
print("sum = ",s)
print("difference = ",d)
print("product = ",p)
print("average = ",av) '''

# Q7  Write a python script to take input for a number calculate and print its square and cube?
'''a = int(input("Enter your  number "))
b = a*a
c = a*a*a
print("Number = ",a)
print("Square = ",b)
print("Cube = ",c) '''

# imp questions
# Q8 Write a python script to calculate and print the area and perimeter of the square?
''' s = int(input("Enter side of Squre "))
a = s*s
p = 4/s

print("Number : ",s)
print("Area : ",a)
print("Square : ",p) '''

# Q9 Write a python script to calculate and print area and perimeter of rectangle?
'''l=int(input("Enter length of rectangle "))
w=int(input("Enter widthof rectangle "))
a=l*w
p=2*(l+w)
print("Area = ",a)
print("Perimeter = ",p)   '''

# Q10 Write a python script to calculate and print area and circumference of the circle?
'''r=float(input("Enter radius of circle "))
a=3.1415*r*r
c=2*3.1415*r
print("Area = ",a)
print("Circumference = ",c)  '''

# 11 Write a python script to calculate and print Simple Interest?
''' p = float(input("Enter Principle : "))
r = float(input("Enter Rate : "))
t = float(input("Enter Time : "))

si = (p*r*t)/100

print("SI" , si)  '''

# 12 Write a python script to take input for two numbers and interchange them (swap them)? (Method :1)(using third variable)
a=int(input("Enter 1st no "))
b=int(input("Enter 2nd no "))
print("1st value ",a," 2nd value ",b)
t=a
a=b
b=t
print("1st value ",a," 2nd value ",b)

# 13 Write a python script to take input for two numbers and interchange them (swap them)? (Method :2)(without using third variable)
a=int(input("Enter 1st no "))
b=int(input("Enter 2nd no "))
print("1st value ",a," 2nd value ",b)
a=a+b
b=a-b
a=a-b
print("1st value ",a," 2nd value ",b)

# 14 Write a python script to take input for two numbers and interchange them (swap them)? (Method :3)(Only Python can do it)
a=int(input("Enter 1st no "))
b=int(input("Enter 2nd no "))
print("1st value ",a," 2nd value ",b)
a,b=b,a
print("1st value ",a," 2nd value ",b)