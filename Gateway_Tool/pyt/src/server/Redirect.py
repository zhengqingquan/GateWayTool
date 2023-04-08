import sys
from abc import ABCMeta, abstractmethod
from tkinter import Text, NORMAL, DISABLED, END


class StreamHandlerInterface(object):
    """
    流处理器接口
    根据流的需要重写write()方法，可以使用该方法进行重定向或对流使用钩子。
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def write(self, message):
        pass


class StreamRedirectClass(StreamHandlerInterface):
    """
    流重定向类
    """

    def __init__(self, widget: Text):
        self.widget = widget

    def write(self, message):
        self.widget.config(state=NORMAL)  # 启用编辑
        self.widget.insert(END, message)
        self.widget.see(END)  # 当文本溢出控件时，自动显示最后一行
        self.widget.config(state=DISABLED)  # 禁用编辑


class RedirectInterface(StreamHandlerInterface):
    """
    重定向接口
    参考：输出重定向
    https://blog.csdn.net/PengDW12/article/details/121379323
    https://blog.csdn.net/weixin_49317370/article/details/108878373
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def flush(self):
        pass

    @abstractmethod
    def beginStd(self):
        pass

    @abstractmethod
    def restoreStd(self):
        pass


class StdOutRedirectClass(RedirectInterface):
    """
    标准输出重定向类
    """

    def __init__(self, widget: Text):
        self.widget = widget
        # 备份原本的数据流位置
        self._stdoutBackup = sys.stdout

    def flush(self):
        self._stdoutBackup.flush()

    def write(self, message):
        self._stdoutBackup.write(message)  # 同时在旧的数据流位置进行输出
        self.widget.config(state=NORMAL)  # 启用编辑
        self.widget.insert(END, message)
        self.widget.see(END)  # 当文本溢出控件时，自动显示最后一行
        self.widget.config(state=DISABLED)  # 禁用编辑

    def beginStd(self):
        """
        开始重定向
        """
        sys.stdout = self

    def restoreStd(self):
        """
        恢复标准输出流
        """
        sys.stdout = self._stdoutBackup


class StdErrRedirectClass(RedirectInterface):
    """
    标准错误重定向类
    """

    def __init__(self, widget: Text):
        self.widget = widget
        # 备份原本的数据流位置
        self._stderrBackup = sys.stderr

    def flush(self):
        self._stderrBackup.flush()

    def write(self, message):
        self._stderrBackup.write(message)  # 同时在旧的数据流位置进行输出
        self.widget.config(state=NORMAL)  # 启用编辑
        self.widget.insert(END, message)
        self.widget.see(END)  # 当文本溢出控件时，自动显示最后一行
        self.widget.config(state=DISABLED)  # 禁用编辑

    def beginStd(self):
        """
        开始重定向
        """
        sys.stderr = self

    def restoreStd(self):
        """
        恢复标准输出流
        """
        sys.stderr = self._stderrBackup
