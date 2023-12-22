
from .kalah import Kalah


def play_kalah(m=6, n=4):
    """
    Play a turn-based game of kalah, with the south player playing first.
    """
    ## Initialize the game
    game = Kalah(m, n)

    ## Display the initial board
    game.show_board()

    ## Run a game loop
    move_str = ''
    move_int_flag = False
    while (move_str != 'Q') and not game.is_finished():

        ## Get the next move
        while not move_int_flag:
            move_str = input("Your move (Q to quit)?  ")
            try:
                move_int = int(move_str)
                move_int_flag = True
            except:
                move_str = input("Your move (Q to quit)?  ")    
        
        ## Act on the move
        game.perform_move(move_int)
        game.show_board()
        move_int_flag = False

    ## Return the completed game
    return game