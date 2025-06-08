import random                                                #Module for choosing random words

words = ['plant', 'soft', 'apple', 'bus','poeple']           #Predefined List
word = random.choice(words)

guess_letter = []
incorrect_guess = 0
max_guess = 6
display_word = ["_" for _ in word]                            #Underscore in place of words

while incorrect_guess < max_guess and "_" in display_word:
    print("\nCurrent word:", " ".join(display_word))
    letter = input("Guess a Letter: ").lower()

    if letter in guess_letter:
        print("\nYou arleady guessed that letter.")
        continue
    guess_letter.append(letter)

    if letter in word:                                        #Loop for checking letter.
        print("\nGood Job! Letter Found.")
        for i in range(len(word)):
            if word[i] == letter:
                display_word[i] = letter
    else:
        incorrect_guess +=1
        print("\nIncorrect Guess.")
        print("\nYou have", max_guess - incorrect_guess, "chances Left.")

#Game Result 

if "_" not in display_word:
    print("\n Congratulatons! You have guessed the correct word:", word)
else:
    print("\n Game Over! The word was:", word)
    

