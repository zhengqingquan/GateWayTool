import json

from pyt.src.config.AbstractConfigClass import AbstractConfigClass


class FileDealConfig(AbstractConfigClass):
    # 配置项
    HeadFileDefType = None
    ExcelLoadType = None
    BeginCell = None
    EndCell = None

    def loadConfig(self, configFilePath):
        with open(configFilePath, 'r') as file:
            config_: dict = json.load(file)
            # 配置项：DefType。头文件防止重复引用的方式，一种是默认方式‘pragma’，另一种是‘ifndef’，还有一种‘max’。
            self.HeadFileDefType = config_['HeadFile']['DefType']
            # 配置项：ExcelLoadType。Excel的加载方式有两种，一种是默认方式‘Default'，另一种是’CellType‘。
            self.ExcelLoadType = config_['Excel.load.type']
            self.BeginCell = config_['Excel.load.CellType']['BeginCell']
            self.EndCell = config_['Excel.load.CellType']['EndCell']

    def getDefaultConfig(self):
        return {
            'HeadFile': {
                'DefType': 'pragma',
            },
            'Excel.load.type': 'Default',
            'Excel.load.CellType': {
                'BeginCell': 'A2',
                'EndCell': 'A1'
            },
        }
