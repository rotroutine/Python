import json

# json_data = [{"name": "Amy", "age": 20}, {"name": "John", "age": 22}, {"Hello": "Python", "bye": "Java"}]
# json_str = json.dumps(json_data)
# print(json_str, type(json_str))
# print(json.loads(json_str), type(json.loads(json_str)))

# dict = {"Hello": "English", "nihao": "Chinese"}
# json_str = json.dumps(dict)
# print(json_str, type(json_str))
# print()
# print(json.loads(json_str), type(json.loads(json_str)))

# dic = {"test": 123, "高人": 666}
# print(dic)
# print()

# # json_str = json.dumps(dic) #! 将中文转换为json时会出现编码问题，需要设定参数
# json_str = json.dumps(dic, ensure_ascii= False)
# print(json_str, type(json_str))
# print(help(json.dump))