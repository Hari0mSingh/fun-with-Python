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

# fname =input('Enter your first name ')
# Lname = input('enter your last name')
# print(f"Your name is : {fname} {Lname}")
# print('Your name is '+ fname+Lname)
# print("your name is ",fname,Lname)

# DataTypes
print(type("Hello world"))#<class 'str'>
#access values using index
print('hello'[4])# o

# sting ,int, float , boolean etc


# if-else
num1 = input("enter first no.")
num2 = input("enter second no.")
if(num1>num2):
    print(f"{num1} num1 is bigger then {num2}")
elif(num2>num1):
    print(f"{num2} num2 is bigger then {num1}")
else:
    print('numbers are same')

#grade program
score = input('enter youe score out of 100: ')
score = int(score)
if(score>=90):
    age = int(input('Enter your age: '))
    if(age<10):
        print('+A')
    else:
        print('A')
elif(score>=80):
    print('B')
elif(score>=70):
    print('c')
elif(score>=60):
    print('B')
else:
    print('f')

#for loop
fruits = ['banana','apple','cherry']
for i in fruits:
    print(i)
    print(i+'pie')

print(type(fruits))#list

#range in for  loop
for num in range(1,10):
    print(num)

#every number divisible by 2
for num in range(0,100,2):
    print(num)
#odd number
for num in range(1,100,2):
    print(num)

#number divisible by 3
for i in range(1,100):
    if(i%3==0):
        print(f"{i} is divisible by 3")

#fizzbuzz
for num in range(1,100):
    num = int(input('enter a number'))
    if(num%3==0 and num%5==0):
        print('fizzbuzz')
    if(num%3==0):
        print('fizz')
    elif(num%5==0):
        print('buzz')
    else:
        print(num)