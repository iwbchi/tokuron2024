from Utils import Point
from enum import Enum


class AgentType(Enum):
    ally = 1
    enemy = 2


class Agent:
    def __init__(self, agent_id, point: Point, agent_type: AgentType) -> None:
        self.agent_id = agent_id
        self.point = point
        self.agent_type = agent_type
