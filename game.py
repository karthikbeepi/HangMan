from stringDatabase import StringDataBase, value_to_character

class Game:
    def __init__(self):
        self.current_guess = "----"
        self.random_word = StringDataBase.getRandomWord()   
        self.bad_guesses = 0
        self.score = 0
        self.missed_letters = 0
        self.letter_requested = 0

    def calculateScoreSuccess(self):
        multiplier = 0
        for i, c in enumerate(self.current_guess):
            if( c == '-' ):
                multiplier = multiplier + value_to_character[self.random_word[i]]
        if(self.letter_requested > 0):
            multiplier = multiplier / self.letter_requested 
        return 100 * multiplier * (1-0.1*(self.bad_guesses)) 

    def calculateScoreGaveUp(self):
        multiplier = 0
        for i, c in enumerate(self.current_guess):
            if( c == '-' ):
                multiplier = multiplier + value_to_character[self.random_word[i]]
        return -multiplier

    def letterChoice(self):
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
                    self.score = self.calculateScoreSuccess()
                    return str(self.random_word), "Success", str(self.bad_guesses), str(self.missed_letters), str(self.score)
                else:
                    self.bad_guesses = self.bad_guesses+1
                    print("Sorry, Try again!")
            elif(choice == 't'):
                print(self.random_word)
                self.score = self.calculateScoreGaveUp()
                return str(self.random_word), "Gave Up", str(self.bad_guesses), str(self.missed_letters), str(self.score)
            elif(choice == 'l'):
                self.letterChoice()
            elif(choice == 'q'):
                if(self.missed_letters != 0 or self.bad_guesses != 0):
                     return str(self.random_word), "Gave Up", str(self.bad_guesses), str(self.missed_letters), str(self.score)
                else:
                    return True
