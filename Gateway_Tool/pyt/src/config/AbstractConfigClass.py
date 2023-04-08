import json
from pathlib import Path
from abc import ABCMeta, abstractmethod

from pyt.src.ToolModule.FuncTool import SingletonClass


class AbstractConfigClass(SingletonClass, metaclass=ABCMeta):
    _config = {}
    _DEFAULT_CONFIG = {}

    @property
    def config(self):
        return self._config

    @config.setter
    def config(self, x):
        self._config = x

    @property
    def DEFAULT_CONFIG(self):
        return self._DEFAULT_CONFIG

    @abstractmethod
    def loadConfig(self, configFilePath) -> None:
        """
        根据路径加载配置文件。
        """
        pass

    @abstractmethod
    def getDefaultConfig(self) -> dict:
        """
        获取默认配置
        """
        pass

    def genDefaultConfig(self, configFilePath) -> None:
        """
        根据默认配置生成默认配置文件。
        """
        with open(configFilePath, 'w+', encoding='utf-8') as file:
            file.writelines(
                json.dumps(self.getDefaultConfig(), indent=4, sort_keys=False, ensure_ascii=False))
