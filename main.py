import random
# 0: 剪刀  1: 石頭  2: 布
# =: 代號 = 資料
my = int(input("請輸入 0.剪刀 1.石頭 2. 布"))
com = random.randint(0, 2)

# print(帶入東西)
print("我出的:", my)
print("電腦的:", com)

# if-else: 如果 否則
# if-elif-else: 如果 否則如果 否則
if my == com:
    print("平手")
elif my == (com + 1) % 3:
    print("我贏")
else:
    print("我輸")