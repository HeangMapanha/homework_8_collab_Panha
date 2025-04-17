## Method 1


# def reverse_ascending(numbers):
#     ...

# from typing import Iterable, Iterator, TypeVar

# T = TypeVar("T")

# def reverse_ascending(items: Iterable[T]) -> Iterator[T]:
#     it = iter(items)
#     try:
#         run = [next(it)]
#     except StopIteration:
#         return

#     for x in it:
#         if x > run[-1]:
#             run.append(x)
#         else:
#             yield from reversed(run)
#             run = [x]
#     yield from reversed(run)

# print(list(reverse_ascending([1, 2, 3, 2, 4, 5, 1])))
# print(list(reverse_ascending([1, 2, 3, 4, 5])))   


## Method 2


def reverse_ascending(items):
    if not items:
        return []

    result = []
    current = [items[0]]

    for i in range(1, len(items)):
        if items[i] > current[-1]:
            current.append(items[i])
        else:
            result.extend(reversed(current))
            current = [items[i]]

    result.extend(reversed(current))
    return result

print(reverse_ascending([1, 2, 3, 2, 4, 5, 1]))
print(reverse_ascending([1, 2, 3, 4, 5]))
print(reverse_ascending([5, 4, 3, 2, 1]))