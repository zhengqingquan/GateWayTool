import logging
from decimal import Decimal
from functools import wraps
from time import perf_counter
from types import FunctionType

import pythoncom


def runTime(function: FunctionType):
    """
    用于测试时间的修饰器。
    显示当前修饰的函数的运行时间。
    """

    @wraps(function)
    def wrapper(*arg, **kwargs):
        start = perf_counter()  # 开始时间
        result = function(*arg, **kwargs)
        end = perf_counter()  # 结束时间
        timeDifference = Decimal(end - start).quantize(Decimal("0.0000"))
        if timeDifference == 0:
            timeDifference = '<0.0001s'
        logging.debug(f'{function.__name__}，所用时间：{timeDifference}s')

        return result

    return wrapper


def runTimeMsg(message: str = '当前功能执行时间为'):
    """
    用于测试时间的修饰器。
    当前函数所运行的时间，可以通过形参message设置显示内容。
    该修饰器会导致原函数无法使用编辑器的形参提醒。
    """

    def aop(function: FunctionType):
        @wraps(function)
        def wrapper(*arg, **kwargs):
            start = perf_counter()  # 开始时间
            result = function(*arg, **kwargs)
            end = perf_counter()  # 结束时间
            timeDifference = Decimal(end - start).quantize(Decimal("0.0000"))
            if timeDifference == 0:
                timeDifference = '<0.0001'
            logging.debug(f'{message}：{timeDifference}s')

            return result

        return wrapper

    return aop


def CoInitialize(function: FunctionType):
    """
    用于处理多线程条件下使用win32com的报错问题。
    """

    # 在多线程条件下使用win32com中的com组件时需要调用CoInitialize()，否则会出现异常：
    # pywintypes.com_error:(-2147221008,‘尚未调用 CoInitialize。‘, None, None)
    # 解决方法参考：
    # https://blog.csdn.net/weixin_42607789/article/details/90258624
    # https://blog.csdn.net/Erudite_x/article/details/119480825

    @wraps(function)
    def wrapper(*arg, **kwargs):
        pythoncom.CoInitialize()
        try:
            return function(*arg, **kwargs)
        finally:
            pythoncom.CoUninitialize()

    return wrapper


def singleton(cls):
    """
    单例模式的修饰器。
    """

    instances = {}

    @wraps(cls)
    def getinstance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return getinstance


class SingletonClass(object):
    """
    单例模式的继承类
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(SingletonClass, cls).__new__(cls, *args, **kwargs)
        return cls._instance
