def index_power(numbers, n):

    if n<0 or n >= len(numbers):
        return -1
    return numbers[n] ** n