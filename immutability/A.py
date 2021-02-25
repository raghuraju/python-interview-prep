class A:
    def __init__(self, name):
        self.name = name

    def __setattr__(self, key, value):
        try:
            if self.__getattribute__(key):
                raise ValueError
        except AttributeError:
            self.__dict__[key] = value

