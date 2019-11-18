# 專屬功能
# 專屬資料.功能()
a = "hello" * 3
print(a)
b = a.replace("hello", "bye")
print(a)
print(b)
a = a.replace("hello", "QQQ", 1)
print(a)
print("-".join(["2019", "09", "30"]))
print("2019/09/30".split("/"))

# List
a = ["hello"] * 3
print(a)
b = a.append("bye")
print(a)
print(b)

# X: print(a.append("hello"))
# a = a.append("hello")
# print(a[-1])
a.append("hello")
print(a)