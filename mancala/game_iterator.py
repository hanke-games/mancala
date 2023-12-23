
from .kalah import Kalah



def kalah_game_iterator(candidate_game_history=[1], candidate_game_score='', 
                        m=6, n=4,
                        SHOW_DIAGNOSTIC=False):
    """
    Returns the next hypothetical mancala game after the given one
    """    
    from copy import deepcopy
    
    
    ## Set the player allowed move lists
    north_allowed_moves = range(m+2, 2*m+2)
    south_allowed_moves = range(1, m+1)



    ####################################################
    ## Prepare the iterated version of the given game ##
    ####################################################

    ## Make the list of iterated game states
    game = Kalah(m,n)
    game_list = [game]
    for i in range(len(candidate_game_history)):
        
        ## Make a copy of the last game
        tmp_game = deepcopy(game_list[-1])

        ## Perform the next move
        tmp_game.perform_move(candidate_game_history[i])
    
        ## Check if the move was valid (i.e. added to the internal game history) -- this filters out invalid moves
        if len(tmp_game.history_list()) == len(game_list):
            game_list.append(deepcopy(tmp_game))
        else:
            pass

    ## Get the new partial game history from the deepest valid game history
    try:
        valid_game_history = game_list[-1].history_list()
    except:
        raise RuntimeError(f"No valid game history was found for the given candidate game history.")   ## THIS SHOULD NEVER HAPPEN!

    
    ## DIAGNOSTIC
#    if True:
    if SHOW_DIAGNOSTIC:
        print(f"CHECKPOINT 1:")
        print(f"valid_game_history = {valid_game_history}")
        print(f"game_list = {game_list}")
        print(f"len(game_list) = {len(game_list)}")
        print()
    
    
    
    ########################
    ## Main iterator loop ##
    ########################

    done_flag = False
    while not done_flag:
        
        ## Get the current game
        current_game = game_list[-1]
        
        
        ## DIAGNOSTIC
#        if True:
        if SHOW_DIAGNOSTIC:
            print(f"CHECKPOINT 2:")
            print(f"len(game_list) = {len(game_list)}")
            print(f"game_list = {game_list}")
            print(f"type(current_game) = {type(current_game)}")
            print(f"current_game = {current_game}")



        ########################################################################
        ## 1. Generate the first complete game with this partial game history ##
        ########################################################################

        ## Play the next game continuing from this partial game until we have a finished game
        while not current_game.is_finished():

            ## Start the next game (one more move in from the last one)
            next_game = deepcopy(current_game)

            ## Determine the next player and the next move
            if current_game.next_player() == 's':
                for next_move in range(1, m+1):
                    next_game.perform_move(next_move)                
                    if len(next_game.history_list()) > len(current_game.history_list()):
                        break
            elif current_game.next_player() == 'n':
                for next_move in range(m+2, 2*m+2):
                    next_game.perform_move(next_move)                
                    if len(next_game.history_list()) > len(current_game.history_list()):
                        break

            ## Append the next game to the list
            game_list.append(next_game)

            ## Update the current game
            current_game = game_list[-1]

            ## DIAGNOSTIC
#            if True:
            if SHOW_DIAGNOSTIC:
                print(f"CHECKPOINT 3:")
                print(f"len(game_list) = {len(game_list)}")
                print(f"len(current_game.state_list()) = {current_game.state_list()}")
                print(f"len(current_game.history_list()) = {current_game.history_list()}")
                print(f"len(current_game.next_player()) = {current_game.next_player()}")
                

                
        #########################
        ## 2. Yield the result ##
        #########################
                
        ## Return the finished game and its score 
        history = current_game.history_list()
        score = current_game.score()
        yield history, score        

    
        
        ## DIAGNOSTIC:
#        if True:
        if SHOW_DIAGNOSTIC:
            print(f"PRE-INCREMENT VALUES:")
            print(f" - history = {history}")
            print(f" - score = {score}")
            print()
        
        
        
        #######################################
        ## 3. Increment to get the next game ##
        #######################################
        
        ## Remove the last game since the previous game is what we need to apply the last move to
        game_list.pop()

        ## Increment the game history last move, or move further back
        increment_success_flag = False
        while not increment_success_flag and not done_flag:

            ## DIAGNOSTIC:
            if SHOW_DIAGNOSTIC:
                print("\n")
                print("INCREMENT LOOP DIAGNOSTICS:")
                print("history = ", history)


            ## Look at the last game (state) in game_list and the last move
            last_game = game_list[-1]
            last_move = history[-1]

            ## Get its list of allowed moves
            last_game_allowed_move_list = last_game.allowed_move_list()

            ## Look for the next move -- NOTE: THIS CAN BE GREATLY IMPROVED... =)
            next_move_list = [x  for x in last_game_allowed_move_list  if x > last_move]


            ## DIAGNOSTIC:
#            print("history = ", history)
            if SHOW_DIAGNOSTIC:
                print("last_game = ", last_game)
                print("last_move = ", last_move)
                print("next_move_list = ", next_move_list)


            ## Check if there is a next move
            if len(next_move_list) > 0:
                next_move = min(next_move_list)

                ## Apply the next move
                history[-1] = next_move
                next_game = deepcopy(game_list[-1])
                next_game.perform_move(next_move)
                game_list.append(next_game)
                increment_success_flag = True

            else:

                ## Move backwards in the history (removing the last move) to look for the next move (if possible), otherwise we're done.
                if game_list != []:
                    game_list.pop()
                    history.pop()
                else:
                    done_flag = True



        ## DIAGNOSTIC:
#        if True:
        if SHOW_DIAGNOSTIC:
            print(f"POST-INCREMENT VALUES:")
            print(f" - history = {history}")
#            print(f" - score = {score}")
            print(f" - len(history) = {len(history)}")
            print(f" - len(game_list) = {len(game_list)}")
            print(f" - game_list[-2:] = {game_list[-2:]}")
            print()

                    
        ## Break if we're done
        if done_flag:
            break

    
