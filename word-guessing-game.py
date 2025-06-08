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




