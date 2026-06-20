import gc


class MyObject:

    def __init__(self, name):
        self.name = name
        print(f"{self.name} created")

    def __del__(self):
        print(f"{self.name} deleted")


obj1 = MyObject("Object1")
obj2 = MyObject("Object2")

obj1.reference = obj2
obj2.reference = obj1

del obj1
del obj2

gc.collect()