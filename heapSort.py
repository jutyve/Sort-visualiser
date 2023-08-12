import time

grad = [
  '#6b71f5',
    '#b1c8ed'
]
grad_green = [
    '#C21010',
    '#E64848'
]

swaps = 0


def heapify(data, n, i, draw, timeTick):
    global swaps
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and data[i] < data[left]:
        largest = left

    if right < n and data[largest] < data[right]:
        largest = right

    if largest != i:
        data[i], data[largest] = data[largest], data[i]
        draw(data, [grad_green[x % 2] if x == i or x == largest else grad[x % 2] for x in range(len(data))], swaps)
        time.sleep(timeTick)
        swaps += 1
        heapify(data, n, largest, draw, timeTick)

def heap_sort(data, draw, timeTick):
    global swaps
    n = len(data)
    for i in range(n // 2 - 1, -1, -1):
        heapify(data, n, i, draw, timeTick)
    for i in range(n - 1, 0, -1):
        data[i], data[0] = data[0], data[i]
        draw(data, [grad_green[x % 2] if x == i or x == 0 else grad[x % 2] for x in range(len(data))], swaps)
        time.sleep(timeTick)
        swaps += 1
        heapify(data, i, 0, draw, timeTick)
