import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ['bharath','notbharath','maybebharath']
choosen_word = random.choice(word_list)
print(f'the sol is {choosen_word}.')
word_length = len(choosen_word)

end_of_game = False

lives = 6

display = []
for i in choosen_word:
    display += "_"

print(display)

while not end_of_game:
    guess= input("Guess a letter: ").lower()
    for position in range(word_length):
        letter = choosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in choosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")



    print(f"\n{display}")



    if "_" not in display:
        end_of_game = True
        print("you won boii")

    print(stages[lives])
