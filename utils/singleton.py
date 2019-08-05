class Singleton:

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance


obj1 = Singleton()
obj1.asc = "123"

obj2 = Singleton()
print(obj1, obj2)
print(obj1, obj2.asc)
