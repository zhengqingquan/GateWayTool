"""
如果需要写配置的话，需要以下面的方式重构配置类
"""
from abc import ABCMeta, abstractmethod


class class1(metaclass=ABCMeta):
    _p1 = 'a'
    _DEFAULT_CONFIG = {'1234': _p1}

    _config = {}

    @property
    def config(self):
        return self._config

    @config.setter
    def config(self, x):
        self._config = x

    @property
    @abstractmethod
    def DEFAULT_CONFIG(self):
        return self._DEFAULT_CONFIG

    @property
    def p1(self):
        return self._config['1234']

    @p1.setter
    def p1(self, x):
        self._config['1234'] = self._p1
        self._p1 = x


if __name__ == '__main__':
    cls = class1()
    print(cls.p1)
