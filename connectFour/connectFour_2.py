
#
# AI Player for use in Connect Four   
#

import random  
from ps9pr3 import *

class AIPlayer(Player):
    
    def __init__(self, checker, tiebreak, lookahead):
        """constructs a new AIPlayer object
        """
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        # call the constructor inherited from the superclass, so that it can initialize the inherited attributes
        super().__init__(checker)
        # new constructor should initialize the two attributes that are not inherited from Player
        Player.__init__(self,checker)
        # Make sure that you do not redefine the inherited attributes by trying to assign something to them here.
        self.tiebreak = tiebreak
        self.lookahead = lookahead
    
    def __repr__(self):
        """ returns the string representation of AIPlayer object
        """
        tiebreaking_strategy = ' (' + self.tiebreak + ', ' + str(self.lookahead) + ')'
        return('Player ' + self.checker + tiebreaking_strategy)
        
    def max_score_column(self, scores):
        """ takes a list scores containing a score for each column of the board, and that returns the index of the 
        column with the maximum score. If one or more columns are tied for the maximum score, the method should apply 
        the called AIPlayer‘s tiebreaking strategy to break the tie. 
        """
        # first determine the maximum score in scores
        max_score = max(scores)
        # create a list containing the indices of all elements in scores that match this maximum score.
        max_score_index = []
        for i in range(len(scores)):
            if scores[i] == max_score:
                max_score_index += [i]
        # choose from the list based on the AIPlayer‘s tiebreaking strategy.
        if self.tiebreak == 'RIGHT':
            return max_score_index[-1]
        if self.tiebreak == 'LEFT':
            return max_score_index[0]
        if self.tiebreak == 'RANDOM':
            return random.choice(max_score_index)
        
    def scores_for(self, b):
        """Takes a Board object b and determines the scores for the columns in b. 
        """
        # create a list that is long enough to store a score for each column
        scores = [50] * b.width
        # loop over all of the columns in board
        for col in range(b.width):
        # If the current column is full, use a score of -1 for it.
            if b.can_add_to(col) == False:
                scores[col] = -1
        # if b is already a win for the called AIPlayer use a score of 100 for the current column.
            elif b.is_win_for(self.checker) == True:
                scores[col] = 100
        # if b is already a win for the player’s opponent, use a score of 0 for the current column.
            elif b.is_win_for(self.opponent_checker()) == True:
                scores[col] = 0
        # if the player has a lookahead of 0, use a score of 50 for the column.
            elif self.lookahead == 0:
                scores[col] = 50
            else:
                # Add one of the called AIPlayer‘s checkers to the current column 
                # using the appropriate method in the board b.
                b.add_checker(self.checker, col)
                # create an opponent (an AIPlayer object) with the same tiebreaking strategy as self
                # but with a lookahead that is one less than the one used by self.
                opp_player = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead-1)
                # Make a recursive call to determine the scores that this created opponent would give to the current board 
                opp_scores = opp_player.scores_for(b)
                
                max_opp_score = max(opp_scores)
                if max_opp_score == 0:
                    scores[col] = 100
                elif max_opp_score == 100:
                    scores[col] = 0
                elif max_opp_score == 50:
                    scores[col] = 50
                # Remove the checker that was placed in this column so that you can restore the board b to its prior state.
                b.remove_checker(col)
        return scores
        
    def next_move(self, b):
        """ that overrides (i.e., replaces) the next_move method that is inherited from Player. Rather than asking the user for 
        the next move,this version of next_move should return the called AIPlayer‘s judgment of its best possible move. 
        """
        # use scores_for and max_score_column methods to determine the column number that should be returned.
        # In addition, make sure that you increment the number of moves that the AIPlayer object has made.
        self.num_moves += 1
        num_moves_scores = self.scores_for(b)
        col_num = self.max_score_column(num_moves_scores)
        return col_num
        
        






