from game import Game

results = "-----\t\t------\t\t------\t\t------------\t--------------\t-----\n"
results = results+"Game\t\tWord\t\tStatus\t\tBad Guesses\tMissed Letters\tScore\n"
results = results+"-----\t\t------\t\t------\t\t------------\t--------------\t-----"
i = 1
final_score = 0
while(True):
    g = Game()
    game_result = g.runGame()
    if(game_result == True ):
        if(i>1):
            print(results)
            print("Final Score : "+str(final_score))
            break
    else:
        results =  results + "\n" + str(i)
        for attribute in game_result[:5]:
            results = results+ "\t\t" +attribute
        final_score = final_score + float(game_result[4])
        i = i+1
        if(game_result[5] == True):
            print(results)
            print("Final Score : "+str(final_score))
            break