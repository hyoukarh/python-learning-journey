import random
import hangman_words
import hangman_art

chosen_word = random.choice(hangman_words.word_list).lower()
lives_left = 6

print(hangman_art.logo)
print(chosen_word)

display_underscore = ["__"] * len(chosen_word)
already_guessed = []

while "__" in display_underscore and lives_left > 0:
    guess_letter = input("Guess a letter: ").lower()
    if guess_letter in already_guessed:
      print("You've guessed this letter already.")

    already_guessed.append(guess_letter)
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess_letter:
            display_underscore[position] = letter

    if guess_letter not in chosen_word:
        lives_left -= 1
        print(f"The letter {guess_letter} is wrong, and you have {lives_left} left.")
        
    print(hangman_art.HANGMANPICS[6 - lives_left])
    print(display_underscore)

if lives_left == 0:
    print("You lose.")
else:
    print("You win.")
