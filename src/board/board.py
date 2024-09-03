# 盤面情報
import numpy as np
from Agent import Agent, AgentType, Agents
from Utils import Point, Direction, next_point
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
        # 0 : 中立, 1 : 陣地,  2 : 城壁
        self.board_territory_ally = np.zeros((13, 13))
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
                AgentType.enemy,
                [
                    Point(6, 4),
                    Point(1, 6),
                    Point(11, 6),
                    Point(6, 8),
                ],
            ),
        }

    def get_obj(self, point: Point):
        return self.board_obj[point.y][point.x]

    def get_territory_ally(self, point: Point):
        return self.board_territory_ally[point.y][point.x]

    def get_territory_enemy(self, point: Point):
        return self.board_territory_enemy[point.y][point.x]

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

                agent_id = action.agent_id
                direction = action.direction
                point = self.agents[agent_type][agent_id].point
                # ここまでやった

                nx_point = next_point(point, direction)
                if ac_type == ActionType.REMOVE:  # 動作が削除なら
                    if self.get_territory_ally(nx_point) == 2:
                        self.set_territory_ally(nx_point, 0)
                    elif self.get_territory_enemy(nx_point) == 2:
                        self.set_territory_enemy(nx_point, 0)

                elif ac_type == ActionType.BUILD:  # 動作が建築なら
                    if agent_type == AgentType.ally:
                        if self.get_territory_ally(nx_point) == 0:
                            self.set_territory_ally(nx_point, 2)
                    elif agent_type == AgentType.enemy:
                        if self.get_territory_enemy(nx_point) == 0:
                            self.set_territory_enemy(nx_point, 2)

                elif ac_type == ActionType.MOVE:  # 動作が移動なら
                    self.agents[agent_type][agent_id].point = nx_point


if __name__ == "__main__":
    actions = Actions(
        [Action(i, Direction.N, ActionType.MOVE) for i in range(4)]
    )
    board = Board()
    board.op_actions(actions, AgentType.ally)
    print(board.agents)
