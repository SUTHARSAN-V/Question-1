def count_bees_between_flowers(s, startIndex, endIndex):
    n = len(s)
    nearest_left_flower = [-1] * n
    nearest_right_flower = [-1] * n

    last_flower = -1
    for i in range(n):
        if s[i] == '|':
            last_flower = i
        nearest_left_flower[i] = last_flower

    last_flower = -1
    for i in range(n - 1, -1, -1):
        if s[i] == '|':
            last_flower = i
        nearest_right_flower[i] = last_flower

    prefix_bees = [0] * (n + 1)
    for i in range(n):
        prefix_bees[i + 1] = prefix_bees[i] + (1 if s[i] == '*' else 0)

    results = []
    for i in range(len(startIndex)):
        start = startIndex[i] - 1
        end = endIndex[i] - 1
        right_flower = nearest_right_flower[start]
        left_flower = nearest_left_flower[end]
        
        if right_flower != -1 and left_flower != -1 and right_flower <= left_flower:
            bees_between = prefix_bees[left_flower + 1] - prefix_bees[right_flower + 1]
            results.append(bees_between)
        else:
            results.append(0)

    return results

s = input().strip()
n = int(input())
startIndex = [int(input()) for _ in range(n)]
m = int(input())
endIndex = [int(input()) for _ in range(m)]

result = count_bees_between_flowers(s, startIndex, endIndex)
print(result)
