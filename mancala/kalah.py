## Define the Kalah class

class Kalah():
    """
    Defines the Kalah game with m holes on each side, and n stones in each.  
    
    Here, by convention, the South player ("S") always goes first.
    """

    def __init__(self, m, n):
        """
        Initialize the Kalah game with m holes on each side, and n stones in each.  
    
        Here, by convention, the South player ("S") always goes first.

        """
        ## Store the game size
        self.m = m
        self.n = n
        
        ## Store the board size
        self.board_size = 2*m + 2


        ## Initialize the game history 
        history_list = []

        ## Initialize the game state
        state_list = [n  for _ in range(2*m+3)]
        state_list[0] = 0
        state_list[m+1] = 0
        state_list[2*m+2] = 's'
        
        ## Store the game history and state
        self.game_history_list = history_list
        self.game_state_list = state_list


    def show_board(self):
        """
        Print the board.
        """
        print(self)
        
        

    def __repr__(self):
        """
        Return a string representation of the game.
        """
        ## Initialize the output string
        out_string = ''

        ## Get the game state list
        game_state = self.state_list()    
        
        ## Get the player positions
        north_cradle = game_state[0]
        north_state_list = game_state[self.m+2: self.board_size]
        north_state_list.reverse()
        south_cradle = game_state[self.m+1]
        south_state_list = game_state[1: self.m+1]

        ## Get the current player
        current_player = game_state[-1]
        
        ## Prepare to print the board
        opponent_init_str = ' ' + '     '
        player_init_str = current_player + ' --> '
        cradle_init_str = opponent_init_str
        if current_player == 'n':
            north_init_str = player_init_str
            south_init_str = opponent_init_str
        elif current_player == 's':
            north_init_str = opponent_init_str
            south_init_str = player_init_str        
        else:
            north_init_str = opponent_init_str
            south_init_str = opponent_init_str        

        ## Output the board view
        out_string += "\n" 
        out_string += north_init_str + ' '*4 + ''.join([str(x).rjust(4)  for x in range(2*self.m+1, self.m + 1, -1)]) + '\n'
        out_string += cradle_init_str + '-'*4*(self.m+3) + '\n'
#        out_string += "\n" 
        out_string += cradle_init_str + ' '*4 + ''.join([str(x).rjust(4)  for x in north_state_list]) + '\n'
        out_string += cradle_init_str + str(north_cradle).rjust(4) + ' '*4*self.m + str(south_cradle).rjust(4) + '\n'
        out_string += cradle_init_str + ' '*4 + ''.join([str(x).rjust(4)  for x in south_state_list]) + '\n'
#        out_string += "\n" 
        out_string += cradle_init_str + '-'*4*(self.m+3) + '\n'
        out_string += south_init_str + ' '*4 + ''.join([str(x).rjust(4)  for x in range(1, self.m + 1)]) + '\n'
        out_string += "\n" 

        ## Return the output string
        return out_string


        
    def state_list(self):
        """
        Return the game state list. 
        """
        from copy import deepcopy
        return deepcopy(self.game_state_list)
        
        
        
    def history_list(self):
        """
        Return the game history list (of moves). 
        """
        from copy import deepcopy
        return deepcopy(self.game_history_list)
        
    
    def next_player(self):
        """
        Returns the name of the next player to move.
        """
        return self.state_list()[-1]
    
    
    def north_score(self):
        return self.game_state_list[0]
    
    def south_score(self):
        return self.game_state_list[self.m + 1]

    def score(self):
        return (self.north_score(), self.south_score())
    
    
    def number_of_remaining_north_pieces(self):
        return sum(self.game_state_list[self.m + 2: self.board_size])
    
    def number_of_remaining_south_pieces(self):
        return sum(self.game_state_list[1: self.m + 1])
    
    def number_of_remaining_pieces(self):
        return self.number_of_remaining_north_pieces() + self.number_of_remaining_south_pieces() 
    
    
    def is_finished(self):
        """
        Returns if the game is finished.
        """
        return (self.number_of_remaining_pieces() == 0)
    

    def winner_player(self):
        """
        Returns the game winner.
        """
        ## SANITY CHECK: Is the game finished?
        if not self.is_finished():
            raise RuntimeError("The game is not yet finished!")
            
        ## Return the winner
        return self.player_ahead()

        
    def loser_player(self):
        """
        Returns the game loser.
        """
        ## SANITY CHECK: Is the game finished?
        if not self.is_finished():
            raise RuntimeError("The game is not yet finished!")
            
        ## Return the loser
        return self.player_behind()
        
    
    def is_tie(self):
        """
        Returns returns if the game is currently a tie between the two players.
        """
        return self.north_score() == self.south_score()
    
    
    
    def player_ahead(self):
        """
        Returns returns the player currently ahead in score.
        """
        ## Return the loser
        if self.north_score() > self.south_score():
            return 'n'
        elif self.north_score() < self.south_score():
            return 's'
        else:
            return 'x'
    
    
    def player_behind(self):
        """
        Returns returns the player currently behind in score.
        """
        ## Return the loser
        if self.north_score() < self.south_score():
            return 'n'
        elif self.north_score() > self.south_score():
            return 's'
        else:
            return 'x'
    
    
    
    
    def switch_player(self):
        """
        Switch the current player.
        """
        ## Get the player 
        player_str = self.game_state_list[-1]
        
        ## Switch the player
        if (player_str == 's'):
            self.game_state_list[-1] = 'n'
        elif (player_str == 'n'):
            self.game_state_list[-1] = 's'

            
            
                
    def is_position_on_player_side(self, position, player_str):   
        """
        Returns if the position is on the side of the given player (i.e. 'n' or 's').
        """
        ## Alias the number of board holes
        m = self.m
        
        ## Is this move location allowed for the moving player?
        if (player_str == 's'):
            return (position >= 1) and (position <= m)
        elif (player_str == 'n'):
            return (position >= m + 2) and (position <= 2*m + 1)
#        else:
#            raise RuntimeError(f"The player to move '{player_str}' is not one of the allowed values ('n' or 's').")
   



    def is_allowed_move_for_player(self, move_position, player_str):
        """
        Determines if the move (starting at position 'x') is allowed for the given player ('n' or 's').
        """
        ## Is this move location allowed for the moving player?
        if not self.is_position_on_player_side(move_position, player_str):
            return False
        
        ## Return if there are pieces in this location
        return self.game_state_list[move_position] != 0
        
        
        
    def allowed_move_list(self):
        """
        Determines the allowed moves in the current game state.
        """
        ## Get the player 
        player = self.game_state_list[-1]

        ## Get the list of allowed moves
        allowed_move_list = [x  for x in range(self.board_size)  if self.is_allowed_move_for_player(x, player)]
        
        ## Return the desired list
        return allowed_move_list
    
        
        
    def perform_move(self, x):
        """
        Perform the given move, updating the game state and history.
        """        
        ## Get the player 
        player = self.game_state_list[-1]
        
        
        ## Check if the move is allowed
        if self.is_allowed_move_for_player(x, player):


            ## Determine the player's cradle position
            if player == 's':
                player_cradle_position = self.m + 1
            else:
                player_cradle_position = 0

            ## Determine the opponent's cradle position
            opponent_cradle_position = (player_cradle_position + self.m + 1) % self.board_size



            ## Append the move to the game history
            self.game_history_list.append(x)


            ## Distribute all of the stones from location x
            r = self.game_state_list[x]
            self.game_state_list[x] = 0
            position = (x+1) % self.board_size
            while (r > 0):

                ## Determine if we can add a stone to this position
                can_add_stone_here = (position != opponent_cradle_position)

                ## Add the stone and decrease the number of stones to distribute
                if can_add_stone_here:

                    ## DIAGNOSTIC
                    #print(f"Adding a stone to position {position}")

                    self.game_state_list[position] += 1
                    r -= 1

                    
                ## Increment to the next position (if needed)
                if r != 0:
                    position = (position + 1) % self.board_size

                    

            ## Take the opponent's stones if appropriate (i.e. the final position is an allowed move and the final position was empty)
            if self.is_position_on_player_side(position, player) and (self.game_state_list[position] == 1):
                opposite_position =  (2 * self.m + 2 - position) % self.board_size
                extra = self.game_state_list[opposite_position]
                self.game_state_list[opposite_position] = 0
                self.game_state_list[player_cradle_position] += extra


            ## Change the player if they didn't finish in their cradle
            if position != player_cradle_position:
                self.switch_player()            

                
            ## Check if there are any allowed moves
            if self.number_of_remaining_pieces() == 0:
                self.game_state_list[-1] = 'x'
            else:
                ## Check if there are any allowed moves for the current player
                if self.allowed_move_list() == []:
                    self.switch_player()
                    

        