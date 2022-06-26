from collections import deque
import sys

deq = deque()
input = sys.stdin.readline

N,K = map(int, input().split())
result = []

for i in range(N):
    deq.append(i+1)

while len(deq) != 0:
    for i in range(K-1):
        deq.append(deq.popleft())
    result.append(deq.popleft())

resultStr = "<" + ", ".join([str(i) for i in result]) + ">"
print(resultStr)

# 아래는 Queue를 사용해서 해결 -> 시간초과

# import queue
# import sys

# que = queue.Queue()
# input = sys.stdin.readline

# N,K = map(int, input().split())
# result = []

# for i in range(N):
#     que.put(i+1)

# while que.qsize() != 0:
#     for i in range(K-1):
#         que.put(que.get())
#     result.append(que.get())

# resultStr = "<" + ", ".join([str(i) for i in result]) + ">"
# print(resultStr)