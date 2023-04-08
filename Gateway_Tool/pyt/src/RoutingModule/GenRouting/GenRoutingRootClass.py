from abc import ABCMeta, abstractmethod

from pyt.src.ToolModule.FuncTool import SingletonClass


class GenRoutingRootClass(SingletonClass, metaclass=ABCMeta):
    __headerFileName = ''
    __sourceFileName = ''

    @property
    @abstractmethod
    def headerFileName(self):
        return self.__headerFileName

    @property
    @abstractmethod
    def sourceFileName(self):
        return self.__sourceFileName
