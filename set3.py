'''
a = int(input("Enter first no  "))
b = int(input("Enter second no  "))
c = a+b
print("Sum ",c)
c= a-b
print("diff ",c)
c = a*b
print("multi ",c)
c = (a+b)/2
print("avr ",c)
print(10/3)
print(10//3)

print(10%3)
print(20%4)
print(a*a)
print(a**2)
print(a**3)   '''

#  Write a python script to take input for two numbers calculate and print their sum, product and difference?
# Sol:
'''a = int(input("Enter 1st Number "))
b = int(input("Enter 2nd Number "))
S = a+b
D = a-b
P = a*b
print("Sum = ",S)
print("Diff = ",D)
print("Prod = " , P) '''

# Write a python script to take input for three numbers calculate and print their average?
# Sol:
'''a = float(input("Enter 1st Number "))
b = float(input("Enter 2nd Number "))
c = float(input("Enter 3rd Number "))
av = (a+b+c)/3
print("Average = ",av) '''

# Write a python script to take input for total number of days and convert them into week and days? [ 1 week = 7 days]
# Sol:
'''d = int(input("Enter Total days "))
w = d//7
d = d%7
print(w ," WEEK" ,d ," DAYS") '''

# Write a python script to take input for total distance in inches, convert them into total feet and inches? [ 1 feet = 12 inches ]
# Sol:

'''inh = int(input("Enter Total inches "))
f = inh//12
inh = inh%12
print(f,"Feet",inh,"Inches")  '''

# Write a python script to take input for total distance in meters, convert them into km and m? [ 1 km = 1000 m ]
''' m = int(input("Enter Total distance and meters  "))
km = m//1000
m = m%1000
print(km,"km" , m,"m")
'''

# Write a python script to take input for total distance in cm, convert them into m and cm? [ 1 m = 100 cm ]
''' cm = int(input("Enter Total Distance and Cm "))
m = cm//100
cm = cm%100
print(cm,"cm" , m,"m") '''

# Write a python script to take input for total number of days. Further convert it into number of years, months, weeks and days?
d = int(input("Enter Total Days "))
Y = d//356
d = d%356
M = d//30
d = d%30
W = d//7
d = d%7
print(Y," Year ", M, " Month ", W," Week ")