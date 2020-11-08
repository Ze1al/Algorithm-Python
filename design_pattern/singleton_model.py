# 用__new__方法实现单例，单例就是确保某一个类只有一个实例存在

class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,"_instance"):
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance



s1 = Singleton()
s2 = Singleton()

print(s1 is s2)