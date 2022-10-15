# connect_four
A simple python program for the game connect four using recursive backtracking algorithm 

methods:

1. Player class:
- process_move : Takes two parameters: a Player object p for the player whose move is being processed, and a Board object b for the board on which the game is being played.
- next_move : Overrides the next_move method that is inherited form Player. should choose at random from columns in board b that are not yet full, and return the index of the randomly selected col.

2. AI Player class:
- max_score_column : takes a list scores containing a score for each column of the board, and that returns the index of the column with the maximum score. If one or more columns are tied for the maximum score, the method should apply the called AIPlayer‘s tiebreaking strategy to break the tie. 
- scores_for : Takes a Board object b and determines the scores for the columns in b. 
- next_move : that overrides (i.e., replaces) the next_move method that is inherited from Player. Rather than asking the user for the next move,this version of next_move should return the called AIPlayer‘s judgment of its best possible move. 
