import random

someWords = ['CLEVER', 'TRICKY', 'INNOCENT', 'ABSOLUTE', 'INSANITY', 'WEIRD', 'FUNNIEST']

word = random.choice(someWords).upper()
letterGuessed = set()
chances = len(word) + 2

print('Guess the word!')
print('_ ' * len(word))

try:
    while chances > 0:
        print()
        guess = input('Enter a letter to guess: ').upper()

        if not guess.isalpha():
            print('Enter only a Letter!!')
            continue
        if len(guess) > 1:
            print('Enter ONLY 1 LETTER')
            continue
        if guess in letterGuessed:
            print('You have already guessed that letter')
            continue

        letterGuessed.add(guess)

        if guess in word:
            print('Correct!')
        else:
            chances -= 1
            print(f'Wrong! {chances} chances left.')

        display = ''
        for char in word:
            if char in letterGuessed:
                display += char + ' '
            else:
                display += '_ '

        print(display)

        if all([char in letterGuessed for char in word]):
            print('Congratulations, you won! The word was', word)
            break

    if chances == 0:
        print('Sorry, you lose. The word was', word)

except KeyboardInterrupt:
    print()
    print('Bye')
    exit()