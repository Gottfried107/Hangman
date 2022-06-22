from words import word_list
from random import randint
import re

# removing words whose lenght is less than 3 and those which contain a '-'
for word in word_list:
    if len(word) < 3 or '-' in word:
        word_list.remove(word)


# function to choose word for the game
def choose_word():
    word = word_list[randint(0, len(word_list) - 1)]
    return word

# function to find letter occurences:
def find_occurences(letter, word):
    matches = re.finditer(letter, word)
    matches_positions = [match.start() for match in matches]
    return matches_positions


# function to play the game
def play(word, max_wrong_guesses):
    # printing as many '-' as the word's length
    secret_word = list('-' * len(word))
    print(''.join(secret_word))

    wrong_guesses = 0
    letters_used = []
    # asking the player for a letter
    while True:
        letter = str(input('Enter a letter: '))
        while letter in letters_used:
            letter = str(input('You already entered that letter. Try again: '))
        letters_used.append(letter)

        # checking if the letter is in the word; if it is, reveal its position
        matches_positions = find_occurences(letter, word)
        if matches_positions == []:
            wrong_guesses += 1
        else:
            for index in matches_positions:
                secret_word[index] = letter

        # printing the word and checking whether the player has won
        print(''.join(secret_word))
        if ''.join(secret_word) != word and wrong_guesses != max_wrong_guesses:
            print('Number of wrong guesses allowed: {}'.format(max_wrong_guesses - wrong_guesses))
            print('Letters already used: ' + ' '.join(letters_used))
        elif wrong_guesses == max_wrong_guesses:
            print('Game over! The word was ' + word + '.')
            break
        else:
            print('You won!')
            break


# let's begin playing hangman!
if __name__ == '__main__':
    word = choose_word()

    max_wrong_guesses = int(input('How many wrong guesses are allowed? '))

    play(word, max_wrong_guesses)