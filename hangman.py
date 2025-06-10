import random
from collections import Counter

someWords = ['CLEVER','TRICKY','INNOCENT','ABSOLUTE','INSANITY','WEIRD','FUNNIEST']

word = random.choice(someWords)

if __name__ == '__main__':
    print('Guess the word!')

    print('_ ' * len(word))

    playing = True
    letterGuessed = ''
    chances = len(word) + 2
    correct = 0
    flag = 0
    try:
        while (chances != 0) and flag == 0:
            print()
            chances -= 1
            try: guess = str(input('Enter a letter to guess: '))
            except:
                print('Enter only 1 letter!')
                continue
            if not guess.isalpha():
                print('Enter only a Letter!!')
                continue
            elif len(guess) > 1:
                print('ONLY 1 LETTER')
                continue
            elif guess in letterGuessed:
                print('You have already guessed that letter')
                continue
            if guess in word:
                k = word.count(guess)
                for _ in range(k):
                    letterGuessed += guess

            for char in word:
                if char in letterGuessed and (Counter(letterGuessed) != Counter(word)):
                    print(char, end=" ")
                    correct += 1
                elif (Counter(letterGuessed) == Counter(word)):
                    print("The word is: ", word)
                    flag = 1
                    print('Congrats, you won!')
                    break
                    break
                else:
                    print('_', end=' ')
            if chances <= 0 and (Counter(letterGuessed) != Counter(word)):
                print('You suck')
                print('Try again')
    except KeyboardInterrupt:
            print()
            print('Bye')
            exit()
