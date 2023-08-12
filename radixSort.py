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


def counting_sort(data, exp, draw, timeTick):
    global swaps
    n = len(data)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = data[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = data[i] // exp
        output[count[index % 10] - 1] = data[i]
        count[index % 10] -= 1
        i -= 1
        draw(output, [grad_green[x % 2] if x == i else grad[x % 2] for x in range(len(data))], swaps)
        time.sleep(timeTick)
        swaps += 1

    for i in range(n):
        data[i] = output[i]
        draw(data, [grad_green[x % 2] if x == i else grad[x % 2] for x in range(len(data))], swaps)
        time.sleep(timeTick)
    swaps = 0



def radix_sort(data, draw, timeTick):
    global swaps
    max_num = max(data)
    exp = 1
    while max_num // exp > 0:
        counting_sort(data, exp, draw, timeTick)
        exp *= 10
