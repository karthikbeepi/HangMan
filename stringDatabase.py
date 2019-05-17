#String IO file

import random #Import random

#frequency values
value_to_character = {'a':8.17, 'b':1.49, 'c':2.78, 'd': 4.25, 'e':12.7 , 'f': 2.23 , 'g':2.02, 'h': 6.09, 'i': 6.97, 'j':0.15, 'k':0.77, 'l':4.03, 'm':2.41, 'n':6.75, 'o':7.51, 'p':1.93, 'q':0.1, 'r':5.99, 's': 6.33, 't': 9.06, 'u':2.76, 'v':0.98, 'w':2.36, 'x':0.15, 'y':1.97, 'z':0.07}
""" Stores all the frequency of the characters"""

#Class for string I/O
class StringDataBase:
    """ Basically a class for generating a random word
    contains only 1 method namely getRandomWord"""

    @staticmethod
    def getRandomWord ():
        """This is a function which returns a random word for the file
        Returns:
            word {string} -- A random word
        """

        no_of_words = 0
        with open("four_letters.txt", "r") as four_letters_file:
            for line in four_letters_file:
                for word in line.split():
                    no_of_words = no_of_words +1
        random_number = random.randint(0, no_of_words-1)
        current_word_number = 0
        random_word = ""
        with open("four_letters.txt", "r") as four_letters_file:
            for line in four_letters_file:
                for word in line.split():
                    if(current_word_number < random_number):
                        current_word_number = current_word_number+1
                    else:
                        return word
