import random
from copy import deepcopy

from connect4 import (
    state,
    check_for_win,
    display_board
)
from connect4 import go as board_from_go

class BasicBot():
    SEARCH_DEPTH = 3

    def __init__(self, color) -> None:
        self.color = color
        self.other_color = state.RED if self.color==state.YELLOW else state.YELLOW

    def take_go(self, board):

        go_scores = [0 for c in range(len(board)+1)]

        for i in range(len(board[0])):
            go_scores[i] = self.build_tree(board, i, True, 0)

        min_loss_go = go_scores[0]
        for go in go_scores:
            if go[1] < min_loss_go[1]: min_loss_go = go

        print(go_scores)

        return go_scores.index(min_loss_go)

    # Returns int from -1 to 1 to indicate how close the bot is to winning or losing no it doesnt
    def rate_board(self, board):
        won = check_for_win(board)
        if won != state.EMPTY:
            if won == self.color: return [1.0, 0.0]
            return [0.0, 1.0]

        directions = [ [-1,-1],[-1,0],[-1,1], [0,-1],[0,1], [1,-1],[1,0],[1,1] ]
        
        score = [0.0, 0.0]

        for color in (state.RED, state.YELLOW):
            colors_score = 0
            for c in range(len(board)):
                for r in range(len(board[c])):
                    space = board[c][r]
                    if space != color: continue

                    scoring_dirs = 0
                    for dir in directions:
                        this_dir_score = 1
                        for i in range(1,4):
                            try:
                                if board[c + dir[0]*i][r + dir[1]*i] != (color or state.EMPTY):
                                    this_dir_score = 0
                                    break
                            except IndexError:
                                break

                        scoring_dirs += this_dir_score
                    colors_score += scoring_dirs

            if color == self.color: score[0] += colors_score/24
            else: score[1] += colors_score/24
            
            #print(score)

        return score

    def build_tree(self, board, go, our_go, iteration):
        new_board = [list(row) for row in board]
        board_from_go(self.color if our_go else self.other_color, new_board, go)
        #display_board(new_board)
        new_board_rating = self.rate_board(new_board)

        if iteration > self.SEARCH_DEPTH: return new_board_rating
        if new_board_rating[0] == 1.0 or new_board_rating[1] == 1.0:
            return new_board_rating

        iteration += 1
        our_go = not our_go

        this_branch_score = [0.0, 0.0]

        for i in range(len(new_board)):
            tree_res = self.build_tree(new_board, i, our_go, iteration)

            this_branch_score[0] = self.adjust_score(this_branch_score[0], tree_res[0]) * iteration/self.SEARCH_DEPTH
            this_branch_score[1] = self.adjust_score(this_branch_score[0], tree_res[1]) * iteration/self.SEARCH_DEPTH

        return this_branch_score
    
    def adjust_score(self, score, modifier):
        if score == 0: return modifier
        #if modifier == (1.0 or -1.0): return modifier

        return (score + modifier) / 2