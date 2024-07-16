# 盤面情報
import numpy as np
from Agent import Agent, AgentType, Agents
from Utils import Point


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

        self._init_agents()

    def _init_agents(self):
        self.agents_ally = Agents(
            AgentType.ally,
            [
                Agent(1, Point(6, 1)),
                Agent(2, Point(4, 6)),
                Agent(3, Point(8, 6)),
                Agent(4, Point(6, 11)),
            ],
        )
        self.agents_enemy = Agents(
            AgentType.enemy,
            [
                Agent(1, Point(6, 4)),
                Agent(2, Point(1, 6)),
                Agent(3, Point(11, 6)),
                Agent(4, Point(6, 8)),
            ],
        )
    
    def score(self, agent_type: AgentType):
        if agent_type == AgentType.ally:
            territory = self.board_territory_ally.copy()
        else:
            return self.agents_enemy.score

