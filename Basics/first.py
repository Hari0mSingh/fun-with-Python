print('Hello world')
print('Hello world 1 \nHellow world 2')
print('Hello world 1'+ ' Hellow world 2')
print('Hello world 1'+ ' '+'Hellow world 2')

Fname = 'Hariom'
Lname = 'Singh'
print('Name is : ',Fname,Lname)
print('Name is : ',Fname + ' ' + Lname)
#f string in python
print(f"Name is : {Fname} {Lname}")

#Input 
# ip = input('enter the IP : ')
# print(f"Scanning the Target : {ip}")

# print('You are Targating : ' + input("What would you like to Target ?"))

# print('Your name is : ' + input("What is your name ? "))

# Variables
x = 4
y = 45
z = 'hariom'
print(x+y)
print(z)
# print(x+z) unsupported operand type(s) for +: 'int' and 'str'

# but we can convert number into string
print(str(x)+' '+ z) #4 hariom

x = '6'
y = 5
# print(x+y)  can only concatenate str (not "int") to str
print(int(x) + y) #11

fname =input('Enter your first name ')
Lname = input('enter your last name')
print(f"Your name is : {fname} {Lname}")
print('Your name is '+ fname+Lname)
print("your name is ",fname,Lname)

