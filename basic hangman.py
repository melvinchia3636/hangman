#This is a very basic hangman
import os
import random
import string

word = random.choice([i.strip() for i in open('words.txt', 'r').readlines()])
guessed_word = ['_']*len(word)
guessed_letter = []
chance = 7
warning = ''

while '_' in guessed_word and chance:
	os.system('cls')
	print(warning) if warning else ''
	print('You have {} more chance\n{}\n'.format(chance, ''.join(guessed_word)))
	ask = input('Please enter a letter:')
	if not (ask in string.ascii_lowercase and len(ask) == 1):
		warning = "Please enter a valid letter!"
		continue
	elif ask in guessed_letter:
		warning = 'You\'ve guessed this letter before!'
		continue
	if ask in word:
		guessed_letter.append(ask)
		guessed_word = [ask if word[i] == ask else guessed_word[i] if guessed_word[i] != '_' else '_' for i in range(len(guessed_word))]
		warning = ''
	else:
		guessed_letter.append(ask)
		warning = 'You have guessed a wrong letter!'
		chance -= 1

os.system('cls')
if not chance > 0:
	print('You lose!')
else:
	print('You win!')
os.system('pause > nul')
