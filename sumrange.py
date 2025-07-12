def sum_range(start, stop, step = 1):
    sum = 0
    for n in range(start, stop + 1, step):
        sum += n

    return sum
if __name__ == '__main__':
        print(sum_range(1, 10))
        print(sum_range(1, 10, 2))