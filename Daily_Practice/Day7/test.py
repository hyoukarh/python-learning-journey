import random

word_list = ["Bully", "Ally", "Enemy"]
chosen_word = random.choice(word_list).lower()
print(chosen_word)

display_underscore = ["__"] * len(chosen_word)


while "__" in display_underscore:
    guess_letter = input("Guess a letter: ").lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess_letter:
            display_underscore[position] = letter

    print(display_underscore)

print("You win.")