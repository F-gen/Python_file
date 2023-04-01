import random

from hangman_words import word_list

chosen_word = random.choice(word_list)
word_len = len(chosen_word)
end_of_game = False
lives = 6

from hangeman_log import logo, stages

print(logo)

display = []
# 生成对应长度的 ["_"]
for i in range(word_len):
    display += '_'

while not end_of_game:
    guess = input("Guess a letter:").lower()
    if guess in display:
        print(f"you already guess {guess}")
    for position in range(word_len):
        if chosen_word[position] == guess:
            display[position] = guess
    print(display)
    if guess not in chosen_word:
        print(f"you guess {guess},that's not in the word. you lose life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("you lose")
    if "_" not in display:
        end_of_game = True
        print("you,win")
    print(stages[lives])
