print("\nConstructor")
class user43:
    def __init__(self,name,passion,work):
        self.name = name
        self.passion = passion
        self.work = work
    def getinfo(self):
        print(self.name)
        print(self.passion)
        print(self.work)

obj2=user43("arun Vijay","Programming","Coder")
obj2.getinfo()


print("\nFuntion calling inside the constructor")
class user43:
    def __init__(self,name,passion,work):
        self.name = name
        self.passion = passion
        self.work = work
        obj2.getinfo()
    def getinfo(self):
        print(self.name)
        print(self.passion)
        print(self.work)

obj2=user43("arun Vijay","Programming","Coder")

