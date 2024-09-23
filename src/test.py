from app import api_post, api_request
import time
# type 0: 滞在, 1: 移動, 2: 建築, 3: 解体 dir 0: 無方向, 1: 左上, 2: 上, 3: 右上, 4: 右, 5: 右下, 6: 下, 7: 左下, 8: 左
id = "1"
token = "aaa"
type1 = 1
type2 = 1
type3 = 2
type4 = 2
dir1 = 2
dir2 = 2
dir3 = 2
dir4 = 2
while True:
    time.sleep(1)
    try:
        a, b, turn, walls, territories = api_request(id=id, token=token)
        print(turn)
        time.sleep(1)
    except:
        continue

    try:
        api_post(id, token, turn + 1, type1, type2, type3, type4, dir1, dir2, dir3, dir4)
    except:
        print("おくれん")
