import random
#function in pythpn
import time
# choice = int(input('enter the range number.'))

def myfunction(choice):
    # print('hello there!')
    for i in range(1,choice):
        if(i%3==0 and i%5==0):
            print('fizzBuzz')
        elif(i%3==0):
            print('fizz')
        elif(i%5==0):
            print('buzz')
        else:
            print(i)

# print('We are about to run fizzBuzz game')
# time.sleep(3)
# myfunction(choice)#function call

#example 1
# yourName = input('Enter your Name.')
def printname(Name):
    print(f"Hello {Name}")

# printname(yourName)

#Hangman challange example
words = ['hacker','bounty','random']
secret_word = random.choice(words)
print(secret_word)

# guess = input('guess a latter ').lower()#converted in lower case
# print(guess)
display_word = []
for latter in secret_word:#each time loop runs it will add _ in the list(display_word)
    display_word +='_'
    # print(display_word)
print(display_word)    


#check the  letter in word
# for letter in secret_word:
#     if(letter==guess):
#         print('right')
#     else:
#         print('wrong')


game_over = False
while not game_over:
    guess = input('guess a latter ')
    for position in range(len(secret_word)):
        letter = secret_word[position]
        if(letter==guess):
            display_word[position] = letter     
print(display_word)