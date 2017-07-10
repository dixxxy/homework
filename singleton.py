#单例模式
#使用__new__方法
class Singleton(object):
    def __new__(cls,*args,**kw):
        if not hasattr(cls,'_instance_'):
            orig = super(Singleton,cls)
            cls._instance_ = orig.__new__(cls,*args,**kw)
        return cls._instance_
class Myclass(Singleton):
    a = 1

#共享属性
class Borg(object):
    _state_ = {}
    def __new__(cls,*args,**kw):
        ob = super(Borg,cls).__new__(cls,*args,**kw)
        ob.__dict__ = cls._state_
        return ob
class Myclass2(Borg):
    a = 1

#装饰器版本
def singleton(cls,*args,**kw):
    instances = {}
    def getinstance():
        if cls not in instances:
            instances[cls] = cls(*args,**kw)
        return instances[cls]
    return getinstance

@singleton
class MyClass:
    ...

#import方法
class My_Singleton(object):
    def foo(self):
        pass
my_singleton = My_Singleton()

# to use
from mysingleton import my_singleton

my_singleton.foo()