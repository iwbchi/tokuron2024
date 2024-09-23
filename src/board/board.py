# 盤面情報
import itertools

import numpy as np
from Agent import AgentType, Agents
from Utils import Point, Direction, Only4Direction, next_point
from Action import Action, Actions, ActionType


class Board:

    def __init__(self):
        # 0: 空白, 1: 堀, 2: 城
        self.board_obj = np.array(
            [
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 2, 1, 0, 0, 1, 0, 1, 0, 0, 1, 2, 0],
                [0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0],
                [0, 0, 0, 2, 0, 0, 1, 0, 0, 2, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 2, 0, 2, 0, 0, 0, 1, 0],
                [0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0],
                [0, 1, 0, 0, 0, 2, 0, 2, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 2, 0, 0, 1, 0, 0, 2, 0, 0, 0],
                [0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0],
                [0, 2, 1, 0, 0, 1, 0, 1, 0, 0, 1, 2, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ]
        )
        # 0 : 中立,  2 : 城壁
        self.board_territory_ally= np.zeros((13, 13))
        self.board_territory_enemy = np.zeros((13, 13))

        # 0:空白, 1:味方エージェント, 2: 敵エージェント
        """ 多分使わん
        self.board_agent = np.array(
            [
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 2, 0, 0, 1, 0, 0, 0, 1, 0, 0, 2, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ]
        )  # 0 : いない, 1 : 味方, 2 : 相手
        """

        self._init_agents()

    def _init_agents(self):

        self.agents = {
            AgentType.ally: Agents(
                AgentType.ally,
                [
                    Point(6, 1),
                    Point(4, 6),
                    Point(8, 6),
                    Point(6, 11),
                ],
            ),
            AgentType.enemy: Agents(
                AgentType. enemy,
                [
                    Point(6, 4),
                    Point(1, 6),
                    Point(11, 6),
                    Point(6, 8),
                ],
            ),
        }

    def __str__(self):
        """ボードの状態を文字列で返す"""
        BLUE = "\033[34m"
        RED = "\033[31m"
        END = "\033[0m"
        res_board = [["" for _ in range(13)] for _ in range(13)]
        for i in range(13):
            for j in range(13):
                if self.board_obj[i][j] == 0:
                    res_board[i][j] = "口"
                elif self.board_obj[i][j] == 1:
                    res_board[i][j] = "堀"
                elif self.board_obj[i][j] == 2:
                    res_board[i][j] = "城"
                if self.board_territory_ally[i][j] == 1:
                    res_board[i][j] = f"{BLUE}{res_board[i][j]}{END}"
                elif self.board_territory_ally[i][j] == 2:
                    res_board[i][j] = f"{BLUE}壁{END}"
                if self.board_territory_enemy[i][j] == 1:
                    res_board[i][j] = f"{RED}{res_board[i][j]}{END}"
                elif self.board_territory_enemy[i][j] == 2:
                    res_board[i][j] = f"{RED}壁{END}"
        for agent in self.agents[AgentType.ally]:
            res_board[agent.point.y][agent.point.x] = f"{BLUE}人{END}"
        for agent in self.agents[AgentType.enemy]:
            res_board[agent.point.y][agent.point.x] = f"{RED}人{END}"
        res = "\n".join(
            map(
                lambda x: " ".join(x),
                res_board,
            )
        )

        return res

    def get_obj(self, point: Point):
        return self.board_obj[point.y][point.x]

    def get_territory_ally(self, point: Point):
        return self.board_territory_ally[point.y][point.x]

    def get_territory_enemy(self, point: Point):
        return self.board_territory_enemy[point.y][point.x]

    def check_agent_position_overlap(self, point: Point) -> bool:
        """指定した座標に何らかの動作をするとき、そこにエージェントがいるか判定
        重複がある場合はFalse、ない場合はTrueを返す
        """
        for types in [AgentType.ally, AgentType.enemy]:  # 敵、味方すべて判定
            for agent in self.agents[types]:
                if agent.point == point:
                    return False
        return True

    def set_obj(self, point: Point, num):
        self.board_obj[point.y][point.x] = num

    def set_territory_ally(self, point: Point, num):
        self.board_territory_ally[point.y][point.x] = num

    def set_territory_enemy(self, point: Point, num):
        self.board_territory_enemy[point.y][point.x] = num

    def op_actions(self, actions: Actions, agent_type: AgentType):

        for ac_type in [
            ActionType.REMOVE,
            ActionType.BUILD,
            ActionType.MOVE,
        ]:  # 動作順番ごとに実行
            for action in actions:  # エージェント一人ずつ実行
                # 優先動作とエージェント動作が合致しているか判定　合致していない場合はcontinue
                if action.action_type != ac_type:
                    continue

                agent_id = action.agent_id
                direction = action.direction
                point = self.agents[agent_type][agent_id].point

                nx_point = next_point(point, direction)  # 動作を適用する座標

                if ac_type == ActionType.REMOVE:  # 動作が削除なら
                    # print(f"agent {agent_id} 削除")  # 動作確認用

                    if self.get_territory_ally(nx_point) == 2:
                        self.set_territory_ally(nx_point, 0)
                        # print("削除完了")
                    elif self.get_territory_enemy(nx_point) == 2:
                        self.set_territory_enemy(nx_point, 0)
                        # print("削除完了")

                elif ac_type == ActionType.BUILD:  # 動作が建築なら
                    # print(f"agent {agent_id} 建築")  # 動作確認用

                    if agent_type == AgentType.ally:
                        if (
                            self.get_territory_ally(nx_point) != 2
                            and self.get_obj(nx_point) == 0
                            and self.check_agent_position_overlap(nx_point)
                        ):
                            self.set_territory_ally(nx_point, 2)
                            # print("建築完了")
                    elif agent_type == AgentType.enemy:
                        if (
                            self.get_territory_enemy(nx_point) != 2
                            and self.get_obj(nx_point) == 0
                            and self.check_agent_position_overlap(nx_point)
                        ):
                            self.set_territory_enemy(nx_point, 2)
                            # print("建築完了")

                elif ac_type == ActionType.MOVE:  # 動作が移動なら
                    # print(f"agent {agent_id} 移動")  # 動作確認用
                    # 重複判定
                    if (
                        self.get_territory_ally(nx_point) == 0
                        and self.get_territory_enemy(nx_point) == 0
                        and self.get_obj(nx_point) == 0
                        and self.check_agent_position_overlap(nx_point)
                    ):
                        self.agents[agent_type][agent_id].point = nx_point
                        # print("移動完了")

    def check_in_board(self, point: Point):
        return 0 <= point.x < 13 and 0 <= point.y < 13

    def get_actions_list(self):
        remove = [(ActionType.REMOVE, dir) for dir in Only4Direction]
        build = [(ActionType.BUILD, dir) for dir in Only4Direction]
        move = [(ActionType.MOVE, dir) for dir in Direction]
        for action in itertools.product(
            *[
                [
                    Action(id, ac[1], ac[0])
                    for ac in itertools.chain(remove, build, move)
                ]
                for id in range(4)
            ]
        ):
            actions = Actions(action)
            yield actions


if __name__ == "__main__":
    board = Board()
    for actions in board.get_actions_list(AgentType.ally):
        print(actions)
    # actions = Actions([Action(i, Direction.W, ActionType.BUILD) for i in range(4)])
    # actions = Actions(
    #     [
    #         Action(0, Direction.N, ActionType.BUILD),
    #         Action(1, Direction.S, ActionType.BUILD),
    #         Action(2, Direction.N, ActionType.MOVE),
    #         Action(3, Direction.S, ActionType.MOVE),
    #     ]
    # )
    # board = Board()
    # board.get_legal_actions(AgentType.ally)
    # board.op_actions(actions, AgentType.ally)

    # print("Agent Point")
    # print(board.agents[AgentType.ally])
    # print(board.agents[AgentType.enemy])
    # print("board_territory_ally")
    # print(board.board_territory_ally)
    # print("board_territory_enemy")
    # print(board.board_territory_enemy)


    print(board)


    def isDone(self):
        for i in range(13):
            for j in range(13):
                if self.board_obj[i][j] == 0 \
                or self.board_territory_ally[i][j] == 0 \
                or self.board_territory_enemy[i][j] == 0:
                    return False
                
        return True

