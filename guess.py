#Main file to run

#for all the imports 
from game import Game

#The class where all the program runs
class Guess:
    '''  This is the main Guess class where the program is run
    This primarily has one static method to run the program called as run()
    Implicitly, it calls the Game class to run
    Note: Here, the score for a successful guess is far more than a
    give up to decrease the difficulty of the game'''

    @staticmethod
    def run():
        ''' This method runs the basic method which runs the program'''
        results = "-----\t\t------\t\t------\t\t------------\t--------------\t-----\n"
        results = results+"Game\t\tWord\t\tStatus\t\tBad Guesses\tMissed Letters\tScore\n"
        results = results+"-----\t\t------\t\t------\t\t------------\t--------------\t-----"
        i = 1
        final_score = 0
        while(True):
            g = Game()
            game_result = g.runGame()
            # print(game_result)
            if (game_result[5] != 'no try'):
                results = results + "\n" + str(i)
                for attribute in game_result[:5]:
                    results = results + "\t\t" + attribute
                final_score = final_score + float(game_result[4])
                i = i + 1
                if (game_result[5] == 'try'):
                    print("\n\n\nScoreBoard!!!")
                    print(results)
                    print("\nFinal Score : "+str(final_score))
                    break
            else:
                if(i>1):
                    print("\n\n\nScoreBoard!!!")
                    print(results)
                    print("\nFinal Score : "+str(final_score))
                else:
                    print("No games played to show the results of scoreboard!")
                break

Guess.run()
''' The game is run'''