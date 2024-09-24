import time

import app as api
from PreRequest import pre_request
from Board import Board
from montecarlo import montecarlo_action
from Agent import AgentType

from actions_api import post_actions


TOKEN = "C"


def main() -> None:
    id, is_first = pre_request(TOKEN)
    res = api.api_request(id, TOKEN)
    start_turn = 0
    if res is not None:
        start_turn = res[2] + 1

    mod = 0 if is_first else 1

    for turn in range(start_turn, 30):
        # TODO api_requestがboardを返すようにする
        while True:
            time.sleep(1)
            res = api.api_request(id, TOKEN)
            if res is None:
                continue
            masons, _, get_turn, walls, territories = res
            if turn == get_turn:
                break
        board = Board(walls, masons)

        if turn % 2 == mod:
            # 自分のターンの時
            actions = montecarlo_action(board, turn, is_first)
            print(actions)
            board.op_actions(actions, agent_type=AgentType.ally)
            print(board)
            print("おくったお")
            post_actions(id, TOKEN, turn + 1, actions)
        else:
            # 相手のターンの時
            pass


if __name__ == "__main__":
    main()
