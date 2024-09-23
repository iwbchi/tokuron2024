import copy
import random

from Board import Board
from Agent import AgentType
from Action import Actions
import score


def montecarlo_action(board: Board, turn: int) -> Actions:
    max_score: float = 0
    max_actions = None
    for actions in board.get_actions():
        # TODO: actionsを適用する
        nxt_board = copy.deepcopy(board)
        nxt_board.op_actions(actions)
        score = playout(nxt_board, 100, turn)
        if score > max_score:
            max_score = score
            max_actions = actions

    return max_actions


def playout(board: Board, n: int, turn: int) -> float:
    sum_score = 0
    actions_list = board.get_actions()
    for _ in range(n):
        for i in range(turn, 30):
            action_id = random.randint(0, len(actions_list) - 1)
            actions = actions_list[action_id]
            # アクションをランダムに適用する。
            agent_type = AgentType.ally if i % 2 == 0 else AgentType.enemy
            board.op_actions(actions, agent_type)
        ally_score = score.get_score(board, True)
        enemy_score = score.get_score(board, False)
        sum_score += ally_score - enemy_score

    return sum_score / n
