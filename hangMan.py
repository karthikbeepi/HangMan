#All the imports
import random

#Class for string I/O
class StringDataBase:
    def getRandomWord ():
        random_number = random.randint(0, 4029)
        current_word_number =0
        random_word = ""
        with open("four_letters.txt", "r") as four_letters_file:
            for line in four_letters_file:
                for word in line.split():
                    if(current_word_number < random_number):
                        current_word_number = current_word_number+1
                    else:
                        return word
    def writeStateToFile():
        s =""

class Game:
    def __init__(self):
        self.current_guess = "----"
        self.random_word = StringDataBase.getRandomWord()   

    def runGame(self):
        flag = True
        while(flag):
            print("\n**The great guessing game**")
            print()
            print("Current Guess: "+self.current_guess+" "+self.random_word)
            choice = input("g = guess, t = tell me, l for letter and q to quit : ")
            if(choice == 'g'):
                word = input("Enter word:")
                if(word == self.random_word):
                    print("Good Work!")
            elif(choice == 't'):
                print(self.random_word)
                return
            elif(choice == 'l'):
                letter = input("Enter a letter:")
                number_of_match = 0
                for i, c in enumerate(self.current_guess):
                    if(self.random_word[i] == letter):
                        number_of_match = number_of_match+1
                        self.current_guess = self.current_guess[:i]+letter+self.current_guess[i+1:]
                print("You found "+str(number_of_match)+" letter(s)")
            elif(choice == 'q'):
                return

g = Game()
g.runGame()