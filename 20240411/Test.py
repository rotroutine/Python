str = "1234567890abcdefg"

print(str[0:5:1]) # 因为切片是左闭右开的，所以右边的下标减去左边的下标得到的结果就是切片的长度(在步长为1的情况下)
print(str[0::2])
print(str[::-1]) # 这样可以达到字符串的反转效果
