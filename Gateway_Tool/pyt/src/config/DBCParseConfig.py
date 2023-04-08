import json

from pyt.src.config.AbstractConfigClass import AbstractConfigClass


class DBCParseConfig(AbstractConfigClass):
    # 配置项
    filePrefix = None

    binutilHeaderName = None
    binutilSourceName = None
    definitionHeaderName = None
    definitionSourceName = None
    configHeaderName = None
    monitorHeaderName = None
    monitorSourceName = None

    unpackBeforeAct = None
    unpackAfterAct = None
    packBeforeAct = None
    packAfterAct = None
    canMonitor = None
    onlyFrame = None
    nodeType = None
    configMerge = None

    motorolaStartFormat = None
    intelStartFormat = None

    def loadConfig(self, configFilePath):
        with open(configFilePath, 'r') as file:
            config_: dict = json.load(file)
            self.filePrefix = config_['file.prefix']

            self.binutilHeaderName = config_['file.name']['binutilHeaderName']
            self.binutilSourceName = config_['file.name']['binutilSourceName']
            self.definitionHeaderName = config_['file.name']['definitionHeaderName']
            self.definitionSourceName = config_['file.name']['definitionSourceName']
            self.configHeaderName = config_['file.name']['configHeaderName']
            self.monitorHeaderName = config_['file.name']['monitorHeaderName']
            self.monitorSourceName = config_['file.name']['monitorSourceName']

            self.unpackBeforeAct = config_['code.config']["unpack-before-act"]
            self.unpackAfterAct = config_['code.config']["unpack-after-act"]
            self.packBeforeAct = config_['code.config']["pack-before-act"]
            self.packAfterAct = config_['code.config']["pack-after-act"]
            self.canMonitor = config_['code.config']["can-monitor"]
            self.onlyFrame = config_['code.config']["frame-only"]
            self.nodeType = config_['code.config']["Node-Type"]
            self.configMerge = config_['code.config']["GateWay-Config-Merge"]

            self.motorolaStartFormat = config_['dbc.config']["signals-start-position-format"]['motorola']
            self.intelStartFormat = config_['dbc.config']["signals-start-position-format"]['intel']

    def getDefaultConfig(self):
        return {
            "file.prefix": "signal",
            "file.name": {
                "binutilHeaderName": "signal_binutil.h",
                "binutilSourceName": "signal_binutil.c",
                "definitionHeaderName": "signal_definition.h",
                "definitionSourceName": "signal_definition.c",
                "configHeaderName": "signal_config.h",
                "monitorHeaderName": "signal_monitor.h",
                "monitorSourceName": "signal_monitor.c"
            },
            "code.config": {
                "unpack-before-act": True,
                "unpack-after-act": True,
                "pack-before-act": True,
                "pack-after-act": True,
                "can-monitor": True,
                "frame-only": False,
                "Node-Type": "GateWay",
                "GateWay-Config-Merge": True,  # 表示当使用网关模式时是合并配置还是CAN通道独立配置。
            },
            "dbc.config": {
                "signals-start-position-format": {
                    "motorola": "Motorola forward LSB",
                    "intel": "Intel standard"
                }
            }
        }
