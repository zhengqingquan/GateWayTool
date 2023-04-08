import json

from pyt.src.config.AbstractConfigClass import AbstractConfigClass


class RouteConfig(AbstractConfigClass):
    # 配置项
    _CHANNEL_MAPPING = {}
    _DLC = {}
    _ATTRIBUTE_DICT = {}
    _NODE_CONFIG_WORD = []
    _FUNC_CONFIG_WORD = []

    @property
    def CHANNEL_MAPPING(self):
        return self._CHANNEL_MAPPING

    @property
    def DLC(self):
        return self._DLC

    @property
    def ATTRIBUTE_DICT(self):
        return self._ATTRIBUTE_DICT

    @property
    def NODE_CONFIG_WORD(self):
        return self._NODE_CONFIG_WORD

    @property
    def FUNC_CONFIG_WORD(self):
        return self._FUNC_CONFIG_WORD

    def loadConfig(self, configFilePath):
        with open(configFilePath, 'r') as file:
            config_: dict = json.load(file)
            self._CHANNEL_MAPPING = config_['CHANNEL_MAPPING']
            self._DLC = config_['DLC']
            self._ATTRIBUTE_DICT = config_['ATTRIBUTE_DICT']
            self._NODE_CONFIG_WORD = config_['NodeConfigurationWord']
            self._FUNC_CONFIG_WORD = config_['FunctionConfigurationWord']

    def getDefaultConfig(self):
        return {
            "CHANNEL_MAPPING": {
                "PT_CAN": 0,
                "H_CAN": 0,
                "D_CAN": 1,
                "T_CAN": 2,
                "B_CAN": 3,
                "I_CAN": 4,
                "C_CAN": 5
            },
            "DLC": {
                "3": 3,
                "8": 8,
                "17": 17,
                "19": 19,
                "39": 39
            },
            "ATTRIBUTE_DICT": {
                "source": 0,
                "id": 1,
                "dlc": 2,
                "target": 3,
                "time": 4
            },
            "NodeConfigurationWord": [

            ],
            "FunctionConfigurationWord": [

            ]
        }
