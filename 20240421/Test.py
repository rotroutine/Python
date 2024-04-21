from typing import Union

list1: list[int] = [1, 2, 3, 4, 5]
list2: list[Union[int, str, float]] = [1, 2, 3, "Hello", 3.14]
list3: list[int | float | str] = [1, 2, 3, "Hello", 3.14]
print(list1)
print(list2)
print(list3)
