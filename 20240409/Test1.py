str = "this is a test string"
print(str)
print(len(str))
print("python也太像C了吧")
print("感觉python非常的面向过程啊")
# print("python的字符串也是可以直接改变的，和Java完全不同")
print("坏了，我搞错了，python对字符串的态度和Java一样，是不可变的")
print("但是呢，和java不同的是，python的字符串可以通过[]访问，而java不行，它只能通过charAt()方法访问")
# str[0] = 'T'
# print(str)

count = 0
for ch in str:
    count += 1

print(count)

print(str[0:4]) #切片操作，返回的是一个新的字符串

print(2 ** 6)

print("字符串的长度是", count, "个字符")

def add(a, b) -> int:
    return a + b

print(add(1, 2))