from Board import Board
from app import api_post, api_request


def kakehasi(id, token):

    masons, structures, turn, walls, territories = api_request(id=id, token=token)
    board = Board(walls=walls, masons=masons)
    print(board)
    return board



if __name__ == '__main__':
    kakehasi(1, 'aaa')
