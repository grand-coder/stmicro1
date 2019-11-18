import random
win = 0
lose = 0
for _ in range(100000):
    # Step1. 準備門
    doors = ["羊"] * 2
    c = random.randint(0, 2)
    doors.insert(c, "車")
    print("一開始的門:", doors)
    # Step2. 選一道門
    c = random.randint(0, 2)
    print("我選:", doors[c])
    del doors[c]
    print("剩下的門:", doors)
    # Step3. 開一隻羊
    doors.remove("羊")
    print("剩下的門:", doors)
    # Step4. 確認勝負
    if doors[0] == "車":
        print("我贏了")
        win = win + 1
    else:
        print("我輸了")
        lose = lose + 1

total = win + lose
print("WIN", win)
print("WIN ratio", win / total)
print("LOSE", lose)
print("LOSE ratio", lose / total)