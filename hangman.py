# Hangman game
# Created 22.2.2026

import random
from collections import Counter

theWords = '''boxcar bookworm dwarves flapjack onyx kiosk jumbo juicy joking jogging jiujutsu beekeeper 
jackpot scratch stronghold vodka microwave wristwatch zipper zombie farmer boxing wrestling military espionage 
agent walkway matrix megahertz fishhook awkward haiku'''
theWords = theWords.split()
# Lets randomly choose the word from theWords list
word = random.choice(theWords)

if __name__ == '__main__':
	print('Guess the word! HINT: word is a name of a fruit')

	for i in word:
		#for printing empty spaces for the letters
		print('_', end=' ')
	print()

	playing = True
	#List for storing the letters guessed by the player
	letterGuessed = ''
	chances = len (word) + 2
	correct = 0
	flag = 0
	try:
		while (chances != 0) and flag == 0: #Flag is updated when the guess is right
			print()
			chances -= 1

			try:
				guess = str(input('Enter a letter to guess: '))
			except:
				print('Enter only a letter!')
				continue

			# Check the guess
			if not guess.isalpha():
				print('Enter only a LETTER')
				continue
			elif len(guess) > 1:
				print('Enter only a SINGLE letter')
				continue
			elif guess in letterGuessed:
				print('You have already guessed that letter')
				continue

			# if letter is guessed correctly
			if guess in word:
				#k stores the number of times the guessed letter is in the word
				k = word.count(guess)
				for _ in range(k):
					letterGuessed += guess

			#print the word
			for char in word:
				if char in letterGuessed and (Counter(letterGuessed) != Counter(word)):
					print(char, end=' ')
					correct += 1
				#If user has guessed all the letters
				#Once the correct word is guessed fully
				elif (Counter(letterGuessed) == Counter(word)):
					#the game ends
					print("The word is: ", end=' ')
					print(word)
					flag = 1
					print('You WON!')
					break 
			else:
				print('_', end=' ')

		#If user has 0 chances left
		if chances <= 0 and (Counter(letterGuessed) != Counter(word)):
			print()
			print('You lost!')
			print('The word was {}'.format(word))

	except KeyboardInterrupt:
		print()
		print('Bye!')
		exit()

