# List: [20, 30, 40, 50]
# X -> [20, "hello", True] -> 同類型
# 順序性: [], [:], [::-1]

a = [20, 30, 40, 10]
print(a)
print(a[-1])
print(a[:3])
print(a[::-1])
print(a + [50])

print(max(a))
print(sum(a))
print(sorted(a))
print(a)

lessthan30 = 0
for score in a:
    if score < 30:
        lessthan30 = lessthan30 + 1
print(lessthan30)

# range(0, 10)/range(10) -> [0, 1, 2, 3, ... 9]
total = 0
for i in range(5):
    total = total + (2 * i + 1)
print(total)