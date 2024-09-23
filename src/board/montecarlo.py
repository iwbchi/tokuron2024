from board import Board
import score
import numpy as np

def montecarlo_action(board):
    max_score = 0
    max_actions = None
    nxt_actions = [] # TODO: 列挙したやつ入れる
    for actions in nxt_actions:
        # TODO: actionsを適用する
        nxt_board = ...
        score = playout(nxt_board, 100)
        if score > max_score:
            max_score = score
            max_actions = actions
    
    return max_actions

def playout(board, n: int):
    sum_score = 0
    for _ in range(n):
        while not board.isDone():
            # アクションをランダムに適用する。
            pass
        ally_score = score.get_score(board, True)
        enemy_score = score.get_score(board, False)
        sum_score += abs(ally_score - enemy_score)
        
    return sum_score / n