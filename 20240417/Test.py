class Student:
    __name = None
    __gender = None
    __addr = None
    
    def __init__(self, name:str= None, gender:str= None, addr:str= None):
        self.__name = name
        self.__gender = gender
        self.__addr = addr
        
    def __str__(self):
        return (f"name:{self.__name}, gender:{self.__gender}, addr:{self.__addr}")
    
    def __lt__(self, other):
        return self.__name < other.__name
    
    def __le__(self, other):
        return self.__name <= other.__name
    
    def __eq__(self, other) -> bool:
        return self.__name == other.__name
    
    def set(self, name, gender, addr):
        self.__name = name
        self.__gender = gender
        self.__addr = addr
    

stu1 = Student()
stu1.set("Test", "Dont't Know", "Your House")
# stu1.name = "Test"
# stu1.gender = "Dont't Know"
# stu1.addr = "Your Home"

print(stu1)
# print(stu1.name)
# print(stu1.gender)
# print(stu1.addr)

stu2 = Student("zs", "nan", "jiali")
print(stu2)
# print(stu2.name)
# print(stu2.gender)
# print(stu2.addr)

print()

print(stu1 < stu2)
print(stu1 <= stu2)
print(stu1 == stu2)


# print(len(stu2))

class Test(Student):
    def __init__(self, name: str = None, gender: str = None, addr: str = None):
        super().__init__(name, gender, addr)