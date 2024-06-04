import random


word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
chosen_word_1 = list(chosen_word)
chosen_word_1 = ['_' for _ in chosen_word_1]
erros = 0


while str(chosen_word_1) != list(chosen_word):
    guess = input("Guess a letter: ").lower()
    if guess not in list(chosen_word):
        print("Try again")
        erros+=1
    if erros == 1:
                print()
        print("|----- ")
        print("|    | ")
        print("|    O ")
        print("|      ")
        print("|      ")
        print("|      ")
        print("_      ")
        print()
    if erros == 2:
               print()
        print("|----- ")
        print("|    | ")
        print("|    O ")
        print("|   /  ")
        print("|       )
        print("|      ")
        print("_      ")
        print()
    if erros == 3:
                print()
        print("|----- ")
        print("|    | ")
        print("|    O ")
        print("|   /| ")
        print("|    | ")
        print("|      ")
        print("_      ")
        print()
    if erros == 4:
               print()
        print("|----- ")
        print("|    | ")
        print("|    O ")
        print("|   /|\\")
        print("|    | ")
        print("|      ")
        print("_      ")
        print()
    if erros == 5:
         print()
        print("|----- ")
        print("|    | ")
        print("|    O ")
        print("|   /|\\")
        print("|    | ")
        print("|   / ")
        print("_      ")
        print()
    if erros == 6:
        print()
        print("|----- ")
        print("|    | ")
        print("|    O ")
        print("|   /|\\")
        print("|    | ")
        print("|   / \\")
        print("_      ")
        print()

        break
    else:
        i=0
        for i in range (0, len(list(chosen_word))):
            if guess == list(chosen_word)[i]:
                chosen_word_1[i] = guess        
            i+=1
        print(chosen_word_1)
                
    if chosen_word_1 == chosen_word:
        print(chosen_word_1)
        break