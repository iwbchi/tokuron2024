from api.app import api_post
from board.Action import Actions


def post_actions(id: int, token: str, turn: int, actions: Actions) -> None:
    types = [action.action_type.value for action in actions]
    dirs = [action.direction.value for action in actions]
    api_post(
        id,
        token,
        turn,
        type1=types[0],
        type2=types[1],
        type3=types[2],
        type4=types[3],
        dir1=dirs[0],
        dir2=dirs[1],
        dir3=dirs[2],
        dir4=dirs[3],
    )
