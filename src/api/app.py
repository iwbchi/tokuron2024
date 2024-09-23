import requests
import numpy as np


def api_post(id, token, turn, type1, type2, type3, type4, dir1, dir2, dir3, dir4):
    url = f"http://localhost:8080/matches/{id}?token={token}"  # token = 試合で自グループに割り当てられたtoken

    # ヘッダーの設定
    headers = {
        "procon-token": "{admin_token}",  # admin_tokenの部分は実際のトークンに置き換える admin server token
        "Content-Type": "application/json",
    }
    # type 0: 滞在, 1: 移動, 2: 建築, 3: 解体 dir 0: 無方向, 1: 左上, 2: 上, 3: 右上, 4: 右, 5: 右下, 6: 下, 7: 左下, 8: 左
    data = {
        "turn": turn,
        "actions": [
            {"type": type1, "dir": dir1},
            {"type": type2, "dir": dir2},
            {"type": type3, "dir": dir3},
            {"type": type4, "dir": dir4},
        ],
    }

    datas = {
        "turn": 1,
        "actions": [
            {"type": 2, "dir": 2},
            {"type": 2, "dir": 2},
            {"type": 2, "dir": 2},
            {"type": 2, "dir": 2},
        ],
    }

    # GETリクエストを送信
    response = requests.post(url, headers=headers, json=data)

    print(response.json())


def api_request(id, token):

    # API URL and token setup
    url = f"http://localhost:8080/matches/{id}?token={token}"  # replace with actual token and match id

    # Header setup
    headers = {
        "procon-token": "{admin_token}",  # replace with actual admin token
    }

    # Send GET request
    response = requests.get(url, headers=headers)
    print(response.status_code)

    # Check if the response is successful
    if response.status_code == 200:
        response_data = response.json()
        # Retrieve match information

        match_id = response_data["id"]
        turns = response_data["turn"]
        board = response_data["board"]

        # Display board structures and masons as NumPy arrays
        structures = np.array(board["structures"])
        masons = np.array(board["masons"])
        walls = np.array(board["walls"])
        territories = np.array(board["territories"])

        print(f"Match ID: {match_id}")
        print(f"Total Turns: {turns}")
        print(f"Structures: \n{structures}")
        print(f"Masons: \n{masons}")
        print(f"territories: \n{territories}")
        print(f"walls: \n{walls}")

        # 最新のターン番号を取得
        current_turn = response_data.get("turn", None)

        if current_turn is not None:
            print(f"現在のターン: {current_turn}")
        else:
            print("ターン情報が見つかりませんでした。")

        return masons, structures, turns, walls, territories

    else:
        print(f"Failed to get data: {response.status_code}")

    #def convert_op_action():
