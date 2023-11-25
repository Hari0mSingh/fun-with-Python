import random
print('Welcome to Hangman')
words = ['hacker','bounty','random']# word list

secret_word = random.choice(words)
print(secret_word)
print('You get five guesses!')
dispaly_word = []#empty list
for latter in secret_word:
    dispaly_word+='_'
    # print(dispaly_word)
print(dispaly_word)

#ask the user guess a latter
# print(guess)

#check if the latter in the word
totalGuessCount = 0
game_over = False
while not game_over:
    guess = input('Guess a latter : ').lower()
    for position in range(len(secret_word)):
        latter = secret_word[position]
        if latter==guess:
            dispaly_word[position] = latter
    if guess not in secret_word:
        totalGuessCount+=1
        guesses_left = 5 - totalGuessCount
        print(F"You have {guesses_left} guesses left")
        if(totalGuessCount>=5):
            print('You lose!')
            game_over = True
    print(dispaly_word)

    if '_' not in dispaly_word:
        print('You win')
        game_over = True
    
        
