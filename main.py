import random

guessing_words = ['rock', 'paper', 'scissors']
random_index = random.randint(0, len(guessing_words) - 1)
word_to_guess = guessing_words[random_index]
max_incorrect_guesses = 4
count_of_guesses = 0

print(word_to_guess)

len_of_gWord = len(word_to_guess)

guess_list = ["_"] * len_of_gWord

print(guess_list)

print("Guess a letter, hint: words are rock, paper, and scissors")

while guess_list != list(word_to_guess):
    user_guess = input("Enter a letter: ")

    found_match = False
    for i in range(len_of_gWord):
        if user_guess == word_to_guess[i]:
            guess_list[i] = user_guess
            found_match = True

    if not found_match:
        count_of_guesses += 1
        print(f"Incorrect guess! You have {max_incorrect_guesses - count_of_guesses} attempts left.")

    print(guess_list)

    if count_of_guesses == max_incorrect_guesses:
        print("You've exceeded the maximum incorrect guesses. The word was:", word_to_guess)
        exit(1)

print("Congratulations! You guessed the word:", word_to_guess)
