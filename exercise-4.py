list1 = []



def chunking_by(numbers, chunck):
    i = chunck
    x = -1
    new_list = []
    for number in numbers:
        if i == chunck:
            new_list.append([])
            i = 0
            x += 1
        new_list[x].append(number)
        i += 1

    return new_list

print(chunking_by(list1,4))
