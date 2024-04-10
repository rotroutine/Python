# test_list = [1, True, 1.2, "Hello", [1, 2, 3], None]
# print(test_list)

# for any in test_list:
#     print(any)
# print("Length of the list is: ", len(test_list))
# print("Type of the list is: ", type(test_list))
# print("Type of the elements in the list are: ")
# for any in test_list:
#     print(type(any))
# print('python太方便了！')

# def test() -> list:
#     test_list = [1, True, 1.2, "Hello", [1, 2, 3], None]
#     return test_list

# test_list1 = []
# test_list2 = list()

# def test() -> list[list]:
#     test_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#     return test_list

# def test1() -> list[tuple]:
#     test_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
#     return test_list

# test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for i in range(0, len(test_list)):
#     print(test_list[i], end = " ")

# test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(test_list[-1]) #* Python还支持负数索引，-1表示倒数第一个元素，这样就不会出现索引越界的问题了，dodge

# test_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for outer in test_list:
#     for inner in outer:
#         print(inner, end = " ")
#     print()

# print(test_list)
# print(test_list[0])
# print(test_list[0][0])

# test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(1 in test_list)
# print(11 in test_list)

# python的类既有C++风格也有Java风格
# class Test:
#     def __init__(self, name: str, age: int):
#         self.name = name
#         self.age = age

#     def __str__(self) -> str:
#         return f"Name: {self.name}, Age: {self.age}"

#     def __repr__(self) -> str:
#         return f"Name: {self.name}, Age: {self.age}"

#     def __eq__(self, other) -> bool:
#         return self.name == other.name and self.age == other.age

# test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30]

# test_list.index(10).print()
# print(test_list.index(100))

# test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# test_list.extend([11, 12, 13, 14, 15])
# print(test_list)

# test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# del test_list[0]
# print(test_list)
# test_list.pop(len(test_list) - 1)
# print(test_list)

# help(print)

# print("Hello", "World", "Python" , sep='@', end='!', file=open("output.txt", "w", encoding="utf-8" ,newline=""), flush=True)


# from random import randint


# test_list = [1, 2, 3, 4, 2, 1, 3, 4, 5, 6, 7, 8, 9, 10]
# # print(test_list)
# # # # test = randint(1, 10)
# # # test = randint(1, 10)
# # test_list.remove(2)
# # print(test_list)

# print(test_list.count(1))
# print(test_list.count(2))

# print(2**63 - 1)

# tets_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# tets_list.sort(reverse=True)
# print(tets_list)

# sorted([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], reverse=True)

# for i in range(0, 100):
#     print(i, end=" ")
# print()

# del i
# print(i)

# test_tuple = tuple(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# print(test_tuple)

# test_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# print(test_tuple)

# t1 = (1)
# t2 = (1,)
# print(type(t1))
# print(type(t2))

# 不能修改元组中的内容，但是可以修改元组中的列表的内容
# 这一点非常的有意思
# t1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, [1, 2, 3])
# print(t1)
# t1[-1].reverse()
# print(t1)

# from re import S


# str = "Hello World Python"
# str.translate(str.maketrans(" ", "_"))
# print(str)

# str = "   187238129   Hello World Python111111"
# print(str)
# # # print(str.index("World"))
# # # print(str.find("World"))
# # # print(str.split(" "))

# print(str.strip())
# print(str.strip(" 1234567890"))