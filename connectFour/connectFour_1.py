
#
# Playing the game connect four
#   

from ps9pr1 import Board
from ps9pr2 import Player
import random
    
def connect_four(p1, p2):
    """ Plays a game of Connect Four between the two specified players,
        and returns the Board object as it looks at the end of the game.
        inputs: p1 and p2 are objects representing Connect Four
        players (objects of the Player class or a subclass of Player).
        One player should use 'X' checkers and the other should
        use 'O' checkers.
    """
    # Make sure one player is 'X' and one player is 'O'.
    if p1.checker not in 'XO' or p2.checker not in 'XO' \
       or p1.checker == p2.checker:
        print('need one X player and one O player.')
        return None

    print('Welcome to Connect Four!')
    print()
    b = Board(6, 7)
    print(b)
    
    while True:
        if process_move(p1, b) == True:
            return b

        if process_move(p2, b) == True:
            return b

def process_move(p, b):
    '''takes two parameters: a Player object p for the player whose move is
    being processed, and a Board object b for the board on which the game is being played.'''
    # Print a message that specifies whose turn it is
    repr_str = p.__repr__()
    print(repr_str,"'s turn")
    
    # Obtain player p‘s next move by using p to call the appropriate Player method, and store in a variable
    p_next_move = p.next_move(b)
    # Apply the move to the board by using b to call the appropriate Board method
    b.add_checker(p.checker, p_next_move)
        
    # Print a blank line, and then print board b
    print()
    print(b)
    
    # Check to see if the move resulted in a win or a tie by using the appropriate methods in b
    moves_number = p.num_moves
    if b.is_win_for(p.checker) == True:
        print('Player',p,'wins in ', moves_number,'moves.')
        print('Congratulations!')
        return True
    elif b.is_full() == True:
        print("It's a tie!")
        return True
    else:
        return False
    
class RandomPlayer(Player):
    
    def next_move(self, b):
        """ overrides the next_move method that is inherited form Player. should choose at random from 
        columns in board b that are not yet full, and return the index of the randomly selected col
        """
        # make sure that you increment the number of moves that the RandomPlayer object has made
        self.num_moves += 1
        # begin by constructing a list containing the indices of all available columns
        # consider the columns one at a time, and add the index of any available column to the list. 
        # This can be done using a loop
        index_cols = []
        for col in range(b.width):
            if b.can_add_to(col) == True:
                index_cols += [col]

        return random.choice(index_cols)
