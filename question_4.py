from collections import Counter

def first_odd_flavor(N, C):
    flavor_count = Counter(C)
    for flavor in C:
        if flavor_count[flavor] % 2 != 0:
            return flavor
    return "All are even"

N = int(input())
C = [input().strip() for _ in range(N)]

result = first_odd_flavor(N, C)
print(result)
