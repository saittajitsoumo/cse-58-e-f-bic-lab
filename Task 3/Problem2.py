pattern = input()
text = input()
d = int(input())

ans = []

k = len(pattern)

for i in range(len(text) - k + 1):
    substring = text[i:i+k]

    mismatch = 0

    for j in range(k):
        if pattern[j] != substring[j]:
            mismatch += 1

    if mismatch <= d:
        ans.append(i)

print(*ans)
