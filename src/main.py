import time

import api.app as api
from api.PreRequest import pre_request
from board.Board import Board
from board.montecarlo import montecarlo_action

from actions_api import post_actions


TOKEN = "0"


def main() -> None:
    id, is_first = pre_request()

    mod = 0 if is_first else 1

    for turn in range(30):
        # TODO api_requestがboardを返すようにする
        while True:
            masons, _, get_turn, walls, territories = api.api_request(
                id, TOKEN
            )
            if turn == get_turn:
                break
            time.sleep(1)
            board = Board(walls, masons)

        if turn % 2 == mod:
            # 自分のターンの時
            actions = montecarlo_action(board, turn + 1, is_first)
            post_actions(id, TOKEN, actions)
        else:
            # 相手のターンの時
            pass


if __name__ == "__main__":
    main()
