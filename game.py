#Main logic file

#for all imports from StringDatabase and frequency of character
from stringDatabase import StringDataBase, value_to_character

class Game:
    ''' The Game class which basically holds the logic for the game implementation'''

    @classmethod
    def __init__(self):
        ''' Basic constructor which is responsible for initialisation of instance variables'''

        self.current_guess = "----"
        self.random_word = StringDataBase.getRandomWord()   
        self.random_word = "abcd"
        self.bad_guesses = 0
        self.score = 0
        self.missed_letters = 0
        self.letter_requested = 0

    @classmethod
    def calculateScoreSuccess(self):
        '''Method for calculating the score on successful guess'''

        multiplier = 0
        for i, c in enumerate(self.current_guess):
            if( c == '-' ):
                multiplier = multiplier + value_to_character[self.random_word[i]]
        if(self.letter_requested > 0):
            multiplier = multiplier / self.letter_requested 
        reducer = self.bad_guesses
        while(reducer>0): #if was done iteratively
            multiplier = multiplier * 0.9
            reducer = reducer-1
        # return multiplier * (1-0.1*(self.bad_guesses)) #to give constant 10% decrease
        return multiplier #if reduced by a variable 10% decrease

    @classmethod
    def calculateScoreGaveUp(self):
        '''Method for calculating the score when the user gives up '''

        multiplier = 0
        for i, c in enumerate(self.current_guess):
            if( c == '-' ):
                multiplier = multiplier + value_to_character[self.random_word[i]]
        return -multiplier

    @classmethod
    def letterChoice(self):
        '''When the user requests to guess a letter'''

        self.letter_requested = self.letter_requested + 1
        letter = input("Enter a letter:")
        letter = letter.lower()
        number_of_match = 0
        for i, c in enumerate(self.current_guess):
            if(self.random_word[i] == letter):
                number_of_match = number_of_match+1
                self.current_guess = self.current_guess[:i]+letter+self.current_guess[i+1:]
        print("You found "+str(number_of_match)+" letter(s)")
        if(number_of_match == 0):
            self.missed_letters = self.missed_letters+1
    
    @classmethod
    def runGame(self):
        ''' Method to run the game'''

        print("\n***The great guessing game***")
        while(True):

            print()
            print("Current Guess: "+self.current_guess)
            # print("The word: "+" "+self.random_word)
            choice = input("g = guess, t = tell me, l for letter and q to quit : ")
            choice = choice.lower()

            if(choice == 'g'):
                word = input("Enter word:")
                word = word.lower()
                if(word == self.random_word):
                    print("Good Work!")
                    self.score = self.calculateScoreSuccess()
                    return str(self.random_word), "Success", str(self.bad_guesses), str(self.missed_letters), str(self.score), "correct guess"
                else:
                    self.bad_guesses = self.bad_guesses+1
                    print("Sorry, Try again!")

            elif(choice == 't'):
                print(self.random_word)
                self.score = self.calculateScoreGaveUp()
                return str(self.random_word), "Gave Up", str(self.bad_guesses), str(self.missed_letters), str(self.score), "gave word"
            
            elif(choice == 'l'):
                self.letterChoice()
            
            elif(choice == 'q'):
                if(self.letter_requested > 0 or self.bad_guesses > 0):
                    self.score = self.calculateScoreGaveUp()
                    return str(self.random_word), "Gave Up", str(self.bad_guesses), str(self.missed_letters), str(self.score), 'try'
                else:
                    return str(self.random_word), "Gave Up", str(self.bad_guesses), str(self.missed_letters), str(self.score), 'no try'
            else:
                print("Please enter valid choice [g, t, l, q]")
