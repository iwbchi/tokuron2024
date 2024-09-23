import requests
import numpy as np

url = "http://localhost:8080/matches?token=0"  # token = 試合で自グループに割り当てられたtoken

# ヘッダーの設定
headers = {
    "procon-token": "{admin_token}",  # admin_tokenの部分は実際のトークンに置き換える admin server token
}


# GETリクエストを送信
response = requests.get(url, headers=headers)

# ステータスコードを表示
# print(f"Status Code: {response.status_code}")

# JSONレスポンスをPythonの辞書形式に変換
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
        print(f"id:  {match_id}")
        print(f"turn: {turns}")
        print(f"Structures (NumPy): \n{structures_np}")
        print(f"Masons (NumPy): \n{masons_np}")

else:
    print(f"Failed to get data: {response.status_code}")
