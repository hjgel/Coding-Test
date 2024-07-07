import heapq
import sys

n = int(sys.stdin.readline())

lHeap = []
rHeap = []
for i in range(n):
    n = int(sys.stdin.readline())

    if len(lHeap) == len(rHeap):
        heapq.heappush(lHeap, -n)
    else:
        heapq.heappush(rHeap, n)

    if rHeap and rHeap[0] < -lHeap[0]:
        lValue = heapq.heappop(lHeap)
        rValue = heapq.heappop(rHeap)

        heapq.heappush(lHeap, -rValue)
        heapq.heappush(rHeap, -lValue)

    print(-lHeap[0])