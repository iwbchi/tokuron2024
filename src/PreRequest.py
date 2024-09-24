import requests
import numpy as np


def pre_request(token) -> tuple[int, bool]:

    url = f"http://192.168.2.61:8080/matches?token={token}"  # token = 試合で自グループに割り当てられたtoken

    # ヘッダーの設定
    headers = {
        "procon-token": "{admin_token}",  # admin_tokenの部分は実際のトークンに置き換える admin server token
    }

    # GETリクエストを送信
    response = requests.get(url, headers=headers)

    # ステータスコードを表示
    # print(f"Status Code: {response.status_code}")

    # JSONレスポンスをPythonの辞書形式に変換
    match_id = 0
    first = True
    if response.status_code == 200:
        response_data = response.json()

        # matchesのデータを取り出す
        matches = response_data.get("matches", [])

        for match in matches:
            match_id = match["id"]
            turns = match["turns"]
            turn_seconds = match["turnSeconds"]
            bonus = match["bonus"]
            board = match["board"]
            opponent = match["opponent"]
            first = match["first"]

            # Board情報の取得
            structures = board["structures"]
            masons = board["masons"]

            # NumPy配列に変換
            structures_np = np.array(structures)
            masons_np = np.array(masons)

            # NumPy配列を表示

            print(f"Structures (NumPy): \n{structures_np}")
            print(f"Masons (NumPy): \n{masons_np}")
            print(f"id:  {match_id}")
            print(f"turn: {turns}")
            print(first)

    else:
        print(f"Failed to get data: {response.status_code}")

    return match_id, first
