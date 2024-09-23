import copy
import random

from Board import Board
from Agent import AgentType
from Action import Actions
import score
from tqdm.auto import tqdm


def montecarlo_action(board: Board, turn: int, is_first: bool) -> Actions:
    max_score: float = 0
    max_actions = None
    actions_list = board.get_actions_list()
    for actions in tqdm(actions_list):
        nxt_board = copy.deepcopy(board)
        nxt_board.op_actions(actions, AgentType.ally)
        score = playout(nxt_board, 10, turn, is_first, actions_list)
        if score > max_score:
            max_score = score
            max_actions = actions

    return max_actions


def playout(
    board: Board,
    n: int,
    turn: int,
    is_first: bool,
    actions_list: list[Actions],
) -> float:
    sum_score = 0
    for _ in range(n):
        for i in range(turn, 30):
            action_id = random.randint(0, len(actions_list) - 1)
            actions = actions_list[action_id]
            # アクションをランダムに適用する。
            if is_first:
                agent_type = AgentType.ally if i % 2 == 0 else AgentType.enemy
            else:
                agent_type = AgentType.ally if i % 2 == 1 else AgentType.enemy
            board.op_actions(actions, agent_type)
        ally_score = score.get_score(board, True)
        enemy_score = score.get_score(board, False)
        sum_score += ally_score - enemy_score

    return sum_score / n


if __name__ == "__main__":
    board = Board()
    is_first = True
    actions = montecarlo_action(board, 0, is_first)
    board.op_actions(actions, AgentType.ally)
    print(board)
