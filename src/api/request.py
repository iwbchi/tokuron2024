import requests
import numpy as np


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
        logs = response_data["logs"]

        # Display board structures and masons as NumPy arrays
        structures = np.array(board["structures"])
        masons = np.array(board["masons"])

        # 最新のターン番号を取得
        current_turn = response_data.get("turn", None)

        print(f"Match ID: {match_id}")
        print(f"Total Turns: {turns}")
        print(f"Structures: \n{structures}")
        print(f"Masons: \n{masons}")

        # Format and display logs
        # print("\nLogs:")
        for log in logs:
            turn_num = log["turn"]
            actions = log["actions"]

            # print(f"\nTurn {turn_num}:")
            for action in actions:
                action_type = action["type"]
                direction = action["dir"]
                succeeded = action["succeeded"]

                # Action types and directions for better understanding
                action_type_str = "Build" if action_type == 0 else "Unknown"
                direction_str = (
                    ["Up", "Right", "Down", "Left"][direction]
                    if 0 <= direction <= 3
                    else "Unknown"
                )

                # print(f"  Action: {action_type_str}, Direction: {direction_str}, Success: {succeeded}")

        if current_turn is not None:
            print(f"現在のターン: {current_turn}")
        else:
            print("ターン情報が見つかりませんでした。")
    else:
        print(f"Failed to get data: {response.status_code}")
