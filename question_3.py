from collections import deque, Counter

def minimum_of_maximums(k, arr):
    n = len(arr)
    max_elements = []
    deq = deque()

    for i in range(n):
        if deq and deq[0] < i - k + 1:
            deq.popleft()
        
        while deq and arr[deq[-1]] <= arr[i]:
            deq.pop()
        
        deq.append(i)

        if i >= k - 1:
            max_elements.append(arr[deq[0]])

    minimum = Counter(max_elements)
    most_minimum = minimum.most_common(1)[0][0]

    return most_minimum

k = int(input())
n = int(input())
arr = list(map(int, input().split()))

result = minimum_of_maximums(k, arr)
print(result)
