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
=========''', '''
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

#step o1:Creating a word list
word_list = ["dangal", "drishyam", "dunki", "bhaubali", "chichore", "animal"]

player_lives=6
#step 02 Randomly choosing a word from the word_list and Assigning it to a variable called choosen_word
import random

chosen_word = random.choice(word_list)
#print(chosen_word)

word_length=len(chosen_word)
blanks="_"
for p in range(word_length):
    blanks+="_"
print(blanks)

gameOver=False
correct_alphabets=[]
while not gameOver:
    guess=input("Guess a letter:")
    display=""
    for letter in chosen_word:
        if letter==guess:
            display+=letter
            correct_alphabets.append(letter)
        elif letter in correct_alphabets:
            display+=letter
        else:
            display+="_"
    print(display)
    if guess not in chosen_word:
        player_lives-=1
        if player_lives==0:
            gameOver=True
            print("You Lose")
    if "_" not in display:
        gameOver=True
        print("You Won")
    print(stages[player_lives])
    






    

