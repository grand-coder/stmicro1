import random
from random_words import RandomWords
rw = RandomWords()

total = 0
while True:
    word = rw.random_word()
    # 第三個:2
    # [0:2] + "_" + [3:]
    i = random.randint(0, len(word)-1)
    guess = word[:i] + "_" + word[i+1:]
    g = input(guess + "是什麼?")

    if g == word[i]:
        print("猜對了")
        total = total + 1
    else:
        print("猜錯了")
        print("正確答案:", word)

    if total >= 5:
        print("今天結束了")
        break


