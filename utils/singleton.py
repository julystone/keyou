class Singleton:
    # _ins = None

    def __new__(cls, *a, **ka):
        if not hasattr(cls, "_ins"):
            cls._ins = super().__new__(cls, *a, **ka)
        return cls._ins


obj1 = Singleton()
obj1.asc = "123"

obj2 = Singleton()
print(obj1, obj2)
# print(obj1, obj2.asc)
print(obj2.asc )
