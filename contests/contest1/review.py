#!/usr/bin/python3
from collections import deque
import heapq

def main():
    set_ = {"banana", "maçã", "manga"}
    hash_map = {"banana": 1, "maça": 2, "manga": 3}
    dq = deque()
    heap = []
    heapq.heappush(heap, 4) 
    heapq.heappush(heap, 1)
    heapq.heappush(heap, 7)
    heapq.heappush(heap, 2)

    print(heap)


if __name__ == "__main__":
    main()
