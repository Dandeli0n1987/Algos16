n = int(input())
a = list(map(int, input().split()))

dp = [1] * n
prev = [-1] * n # массив для восстановления ответа

for i in range(n):
    for j in range(i):
        # Если элемент j больше или равен i, мы можем продолжить цепочку
        if a[j] >= a[i]:
            if dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                prev[i] = j # запоминаем, откуда пришли

# Находим индекс, где заканчивается самая длинная цепочка
best_end = 0
for i in range(1, n):
    if dp[i] > dp[best_end]:
        best_end = i

# Восстанавливаем индексы (идем с конца в начало)
ans = []
curr = best_end
while curr != -1:
    ans.append(curr + 1) # +1, так как индексы в задаче с 1
    curr = prev[curr]

ans.reverse() # разворачиваем, так как шли с конца

print(len(ans))
print(*ans)
