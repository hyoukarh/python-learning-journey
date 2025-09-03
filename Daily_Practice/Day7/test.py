import random

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

word_list = ["Bully", "Ally", "Enemy"]
chosen_word = random.choice(word_list).lower()
lives_left = 6
print(chosen_word)

display_underscore = ["__"] * len(chosen_word)


while "__" in display_underscore and lives_left > 0:
    guess_letter = input("Guess a letter: ").lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess_letter:
            display_underscore[position] = letter

    if guess_letter not in chosen_word:
        lives_left -= 1
        print(f"You have {lives_left} left.")
        
    print(HANGMANPICS[6 - lives_left])
    print(display_underscore)

if lives_left == 0:
    print("You lose.")
else:
    print("You win.")
