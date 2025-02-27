class A:

    funcs = []

    def setup(self):
        self.a = 1

    def __init_subclass__(cls, *args, **kwargs):
        for base in cls.__bases__:
            print(cls, issubclass(cls, A))
            if issubclass(cls, A):
                cls.funcs = base.funcs.copy()
                cls.funcs.append(base.setup)
                break
        print(cls, cls.funcs)


class B(A):
    def setup(self):
        self.b = 2


class C(B):
    def setup(self):
        self.c = 3


print([B == c for c in C.__bases__])
