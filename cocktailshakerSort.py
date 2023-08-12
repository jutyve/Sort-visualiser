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



def cocktail_shaker_sort(data, draw, timeTick):
    global swaps
    n = len(data)
    swapped = True
    start = 0
    end = n - 1

    while swapped:
        swapped = False
        for i in range(start, end):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                swapped = True
                draw(data, [grad_green[x % 2] if x == i or x == i + 1 else grad[x % 2] for x in range(len(data))], swaps)
                time.sleep(timeTick)
                swaps += 1
        if not swapped:
            break
        swapped = False
        end -= 1
        for i in range(end - 1, start - 1, -1):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                swapped = True
                draw(data, [grad_green[x % 2] if x == i or x == i + 1 else grad[x % 2] for x in range(len(data))], swaps)
                time.sleep(timeTick)
                swaps += 1
        start += 1
