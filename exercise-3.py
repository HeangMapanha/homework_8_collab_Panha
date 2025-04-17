def remove_all_after(numbers, n):
    new_list = [] 
    for num in numbers:
        new_list.append(num)
        if num == n: 
            break 
    return new_list
