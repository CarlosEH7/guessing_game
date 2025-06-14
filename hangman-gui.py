from PyQt5.QtWidgets import QApplication, QPushButton, QVBoxLayout, QLineEdit, QLabel, QWidget
import sys
import random

someWords = ['CLEVER', 'TRICKY', 'INNOCENT', 'ABSOLUTE', 'INSANITY', 'WEIRD', 'FUNNIEST']

word = random.choice(someWords).upper()
letterGuessed = set()
chances = len(word) + 2

class Hangman(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Hangman')

        self.layout = QVBoxLayout()

        self.word_display = QLabel('_ ' * len(word))
        self.layout.addWidget(self.word_display)

        self.entry = QLineEdit()
        self.layout.addWidget(self.entry)

        self.button = QPushButton('Guess')
        self.button.clicked.connect(self.check_guess)
        self.layout.addWidget(self.button)

        self.message = QLabel('')
        self.layout.addWidget(self.message)

        self.setLayout(self.layout)

    def check_guess(self):
        global chances
        guess = self.entry.text().upper()
        self.entry.clear()
        if not guess.isalpha() or len(guess) != 1:
            self.message.setText('Please enter a single alphabetical character.')
            return
        if guess in letterGuessed:
            self.message.setText('You already guessed that.')
            return
        
        letterGuessed.add(guess)

        if guess in word:
            self.message.setText('Good!', )
        else:
            chances -= 1
            self.message.setText(f'Wrong! {chances} chances left.')
        
        displayed = ' '.join([c if c in letterGuessed else '_' for c in word]) 
        self.word_display.setText(displayed)

        if set(word).issubset(letterGuessed):
            self.message.setText('Congratulations! You won.')
            self.button.setEnabled(False)
        elif chances <= 0:
            self.message.setText(f'You lose! The word was {word}')
            self.button.setEnabled(False)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    hangman = Hangman()
    hangman.show()
    sys.exit(app.exec_()) 
