def replace_last(numbers):
    if len(numbers) > 1:
    # Check if the list of number is more than 1, because replace the last number with 1 number.
        return [numbers[-1]] + numbers[:-1]
        # If the list of number have more than 1 we will process. 
        # ([numbers[-1]) is to take the last number in the list and combine with (numbers[:-1]) all the numbers except the last number in the list.
    return numbers
