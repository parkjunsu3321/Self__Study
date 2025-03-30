import sys

input = sys.stdin.read
data = list(map(int, input().split()))

N = data[0]
heap = []

def push(val):
    heap.append(val)
    idx = len(heap) - 1
    while idx > 0 and heap[idx] > heap[(idx - 1) // 2]:
        heap[idx], heap[(idx - 1) // 2] = heap[(idx - 1) // 2], heap[idx]
        idx = (idx - 1) // 2

def pop():
    if not heap:
        return 0
    max_val = heap[0]
    heap[0] = heap[-1]
    heap.pop()
    idx, size = 0, len(heap)

    while 2 * idx + 1 < size:
        left, right = 2 * idx + 1, 2 * idx + 2
        max_idx = left
        if right < size and heap[right] > heap[left]:
            max_idx = right
        if heap[idx] >= heap[max_idx]:
            break
        heap[idx], heap[max_idx] = heap[max_idx], heap[idx]
        idx = max_idx

    return max_val

result = []
for i in range(1, N + 1):
    if data[i] == 0:
        result.append(str(pop()))
    else:
        push(data[i])

sys.stdout.write("\n".join(result) + "\n")