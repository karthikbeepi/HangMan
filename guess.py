from game import Game

results = "-----\t\t------\t\t------\t\t------------\t--------------\t-----\n"
results = results+"Game\t\tWord\t\tStatus\t\tBad Guesses\tMissed Letters\tScore\n"
results = results+"-----\t\t------\t\t------\t\t------------\t--------------\t-----"
i = 1
while(True):
    g = Game()
    game_result = g.runGame()
    if(game_result == True):
        if(i>1):
            print(results)
        break
    else:
        results =  results + "\n" + str(i)
        for attribute in game_result:
            results = results+ "\t\t" +attribute
        i = i+1