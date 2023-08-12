import time

grad = [
  '#6b71f5',
    '#b1c8ed'
]

grad_green = [
    '#C21010',
    '#E64848'
]

swaps=0

def selection_sort(data, draw, timeTick):
    global swaps
    for i in range(len(data)):
        min_index = i
        for j in range(i + 1, len(data)):
            if data[j] < data[min_index]:
                min_index = j
            colors = [grad_green[x % 2] if x == min_index else grad[x % 2] for x in range(len(data))]
            draw(data, colors, swaps)
            time.sleep(timeTick)
        data[i], data[min_index] = data[min_index], data[i]
        swaps += 1
    colors = [grad[x % 2] for x in range(len(data))]
    draw(data, colors, swaps)
    swaps = 0
    return data
