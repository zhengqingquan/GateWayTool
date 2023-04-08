import os
from functools import wraps
from pathlib import Path
import logging
from types import FunctionType

from pyt.src.SoftwareInfo import CONFIG_DIR_PATH
from pyt.src.config.AbstractConfigClass import AbstractConfigClass
from pyt.src.config.DBCParseConfig import DBCParseConfig
from pyt.src.config.FileDealConfig import FileDealConfig
from pyt.src.config.RouteConfig import RouteConfig

# 配置文件与配置类的对象映射列表
CONFIG_LIST: dict[str:AbstractConfigClass] = {
    'DBCParseConfig.json': DBCParseConfig,
    'RouteConfig.json': RouteConfig,
    'FileDealConfig.json': FileDealConfig,
}


def configFolderCheck(folderPath=CONFIG_DIR_PATH) -> None:
    """
    检测配置目录是否存在。若不存在则创建文件夹，并生成默认配置。
    """

    configFolderPath = Path(folderPath)

    if configFolderPath.exists() and configFolderPath.is_dir():
        pass
    else:
        # 当路径下存在同名的文件时，无法创建同名文件夹。会抛出FileExistsError异常。
        os.makedirs(folderPath)

    for configFileName, configClass in CONFIG_LIST.items():
        configFilePath = configFolderPath.joinpath(configFileName)

        if not configFilePath.exists():
            configClass().genDefaultConfig(configFilePath)
            logging.info(f'生成默认配置：{configFilePath.resolve()}')


def loadConfig(folderPath=CONFIG_DIR_PATH) -> None:
    """
    加载配置文件
    """

    for configFileName, configClass in CONFIG_LIST.items():
        configFilePath = Path(folderPath, configFileName)
        configClass().loadConfig(configFilePath)
        logging.info(f'读取配置：{configFilePath.resolve()}')


def configDecorator(function: FunctionType):
    """
    用于读取配置的修饰器。
    在函数执行前会读取配置。
    """

    @wraps(function)
    def wrapper(*arg, **kwargs):
        loadConfig(CONFIG_DIR_PATH)
        result = function(*arg, **kwargs)
        return result

    return wrapper
