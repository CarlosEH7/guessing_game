import random

#Get their name
name = input("What is your name? ") 

#Print their name
print("Good Luck ! ", name)


#List of random words
words = ['rainbow', 'computer', 'science', 'programming', 'python', 'mathematics', 'player', 'condition', 'reverse', 'water', 'board', 'geeks']

#random word the user has to guess from the list words
word = random.choice(words)

#print the question for the user to guess the word
print('Ok ', name, " guess the characters")

#An empty string that will hold the charaters guessed by the user
guesses = ''

#the number of attempts the user has to guess
turns = 12

while turns > 0:
    
    failed = 0
        
        for char in word:
            
            if char in guesses:
                print(char, end=" ")
            else:
                print("_")
                failed += 1

        if failed == 0:
            print("You Win")
            print("The word is : ", word)
            break
        
        print()
        
        guess = input("guess a character:")
            
        guesses += guess
                
        if guess not in word:
            turns -= 1
            print("Wrong")
            print("You have ", + turns, " more guesses")
                
            if turns == 0:
                print("You Lose")




