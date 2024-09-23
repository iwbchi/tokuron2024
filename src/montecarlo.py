import copy
import random
from concurrent.futures import ProcessPoolExecutor
from functools import partial
import time

import numpy as np

from Board import Board
from Agent import AgentType
from Action import Actions
import score
from tqdm.auto import tqdm

import random


def score_calc(
    board: Board,
    turn: int,
    is_first: bool,
    actions_list: list[Actions],
    actions: Actions,
) -> tuple[float, Actions]:
    nxt_board = copy.deepcopy(board)
    nxt_board.op_actions(actions, AgentType.ally)
    score = playout(nxt_board, 10, turn, is_first, actions_list)

    return score, actions


def montecarlo_action(board: Board, turn: int, is_first: bool) -> Actions:
    max_score = 0
    max_actions = ""
    actions_list = board.get_actions_list()
    # partial_socre_calc = partial(
    #     score_calc,
    #     board=board,
    #     turn=turn,
    #     is_first=is_first,
    #     actions_list=actions_list,
    # )
    # with ProcessPoolExecutor() as executor:
    #     results = list(executor.map(partial_socre_calc, actions_list))
    # max_actions = max(results)[1]

    for actions in random.sample(actions_list, 100):
        score, actions = score_calc(
            board, turn, is_first, actions_list, actions
        )
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
            actions = random.choice(actions_list)
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
    walls = np.zeros((13, 13))
    masons = np.array(
        [
            [
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
            ],
            [
                0,
                0,
                0,
                0,
                0,
                0,
                1,
                0,
                0,
                0,
                0,
                0,
                0,
            ],
            [
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
            ],
            [
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
            ],
            [
                0,
                0,
                0,
                0,
                0,
                0,
                -1,
                0,
                0,
                0,
                0,
                0,
                0,
            ],
            [
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
            ],
            [
                0,
                -2,
                0,
                0,
                2,
                0,
                0,
                0,
                3,
                0,
                0,
                -3,
                0,
            ],
            [
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
            ],
            [
                0,
                0,
                0,
                0,
                0,
                0,
                -4,
                0,
                0,
                0,
                0,
                0,
                0,
            ],
            [
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
            ],
            [
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
            ],
            [
                0,
                0,
                0,
                0,
                0,
                0,
                4,
                0,
                0,
                0,
                0,
                0,
                0,
            ],
            [
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
            ],
        ]
    )

    board = Board(walls, masons)
    is_first = True

    start = time.time()
    actions = montecarlo_action(board, 0, is_first)
    end = time.time()
    print(end - start)

    print(actions)
    board.op_actions(actions, AgentType.ally)
    print(board)
