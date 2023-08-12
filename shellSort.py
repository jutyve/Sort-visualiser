import time

grad = [
  '#6b71f5',
    '#b1c8ed'
]

swaps = 0

def getclr(datalen, currindx, currmin, swaping=False):
    colors = []
    for i in range(datalen):
        if i == currindx:
            colors.append('#FEC260')
        elif i == currmin:
            colors.append(grad[1])
        else:
            colors.append(grad[i % 2])

        if swaping:
            if i == currindx or i == currmin:
                colors[i] = '#EB1D36'
    return colors

def shell_sort(data, draw, timeTick):
    global swaps
    n = len(data)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = data[i]
            j = i
            while j >= gap and data[j - gap] > temp:
                data[j] = data[j - gap]
                j -= gap
            data[j] = temp
            swaps += 1
            draw(data, getclr(len(data), i, j, swaps), swaps)
            time.sleep(timeTick)
        gap //= 2

    colors = [grad[x % 2] for x in range(len(data))]
    draw(data, colors, swaps)
    swaps = 0
