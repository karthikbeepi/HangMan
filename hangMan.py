#All the imports
import random
value_to_character = {'a':8.17, 'b':1.49, 'c':2.78, 'd': 4.25, 'e':12.7 , 'f': 2.23 , 'g':2.02, 'h': 6.09, 'i': 6.97, 'j':0.15, 'k':0.77, 'l':4.03, 'm':2.41, 'n':6.75, 'o':7.51, 'p':1.93, 'q':0.1, 'r':5.99, 's': 6.33, 't': 9.06, 'u':2.76, 'v':0.98, 'w':2.36, 'x':0.15, 'y':1.97, 'z':0.07}
#Class for string I/O 
class StringDataBase:
    def getRandomWord ():
        random_number = random.randint(0, 4029)
        current_word_number = 0
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
        self.bad_guesses = 0
        self.score = 0
        self.missed_letters = 0
        self.letter_requested = 0

    def displayResults(self):
        s = ""

    def calculateScore(self):
        multiplier = 0
        for i, c in enumerate(self.current_guess):
            if( c == '-' ):
                multiplier = multiplier + value_to_character[self.random_word[i]]
        multiplier = multiplier / self.letter_requested 
        return 100 * multiplier * (1-0.1*(self.bad_guesses)) 

    def runGame(self):
        flag = True
        print("\n***The great guessing game***")
        while(flag):
            print()
            print("Current Guess: "+self.current_guess+" "+self.random_word)
            choice = input("g = guess, t = tell me, l for letter and q to quit : ")
            if(choice == 'g'):
                word = input("Enter word:")
                if(word == self.random_word):
                    print("Good Work!")
                    self.score = self.calculateScore()
                    return str(self.random_word), "Success", str(self.bad_guesses), str(self.missed_letters), str(self.score)
                else:
                    self.bad_guesses = self.bad_guesses+1
                    print("Try again!")
            elif(choice == 't'):
                print(self.random_word)
                self.score = 0
                return str(self.random_word), "Gave Up", str(self.bad_guesses), str(self.missed_letters), str(self.score)
            elif(choice == 'l'):
                self.letter_requested = self.letter_requested + 1
                letter = input("Enter a letter:")
                number_of_match = 0
                for i, c in enumerate(self.current_guess):
                    if(self.random_word[i] == letter):
                        number_of_match = number_of_match+1
                        self.current_guess = self.current_guess[:i]+letter+self.current_guess[i+1:]
                print("You found "+str(number_of_match)+" letter(s)")
                if(number_of_match == 0):
                    self.missed_letters = self.missed_letters+1
            elif(choice == 'q'):
                if(self.missed_letters != 0 or self.bad_guesses != 0):
                     return str(self.random_word), "Gave Up", str(self.bad_guesses), str(self.missed_letters), str(self.score)
                else:
                    return True

results = "-----\t------\t------\t------------\t----------------\t-----\t\n"
results = results+"Game\tWord\tStatus\tBad Guesses\tMissed Letters\t\tScore"
results = results+"\n-----\t------\t------\t------------\t----------------\t-----\t"
i = 1
while(True):
    g = Game()
    game_result = g.runGame()
    if(game_result == True):
        print(results)
        break
    else:
        results =  results + "\n" + str(i)
        for attribute in game_result:
            results = results+ "\t" +attribute
        i = i+1