import random


# Step 1: Predefined list of 5 words
words = ['apple', 'banana', 'grape', 'mango', 'peach']

# Step 2: Randomly choose one word
word_to_guess = random.choice(words)

# Step 3: Initialize game variables
guessed_letters = []           # List to store guessed letters
incorrect_guesses = 0
max_guesses = 6
display_word = ['_'] * len(word_to_guess)

# Step 4: Welcome message
print("🎉 Welcome to Hangman!")
print("Guess the word one letter at a time.")
print("You have", max_guesses, "wrong guesses allowed.\n")

# Step 5: Main game loop
while incorrect_guesses < max_guesses and '_' in display_word:
    print("Word: ", ' '.join(display_word))
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("❗ Please enter a single valid letter.\n")
        continue

    # Check if already guessed
    if guess in guessed_letters:
        print("⚠ You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    # Check if the guess is in the word
    if guess in word_to_guess:
        for i in range(len(word_to_guess)):
            if word_to_guess[i] == guess:
                display_word[i] = guess
        print("✅ Good guess!\n")
    else:
        incorrect_guesses += 1
        print("❌ Wrong guess! You have", max_guesses - incorrect_guesses, "guesses left.\n")

# Step 6: End of game message
if '_' not in display_word:
    print("🎊 Congratulations! You guessed the word:", word_to_guess)
else:
    print("💀 Game Over! The correct word was:",word_to_guess)