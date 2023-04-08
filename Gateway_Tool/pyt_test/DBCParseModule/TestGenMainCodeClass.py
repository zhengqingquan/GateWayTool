import unittest
import logging
from pyt.src.DBCParseModule import GenMainCodeClass
from pyt.src.config.ConfigFolderCheck import loadConfig, configFolderCheck


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        # 加载日志
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        # 生成配置
        configFolderCheck('../../config')
        # 载入配置
        loadConfig('../../config')

    def test_Gen_DefinitionHeader(self):
        Gen_Main = GenMainCodeClass.GenGenMainCodeClass('../CaseMaterial/gw_dbc.dbc', '../CaseMaterial')
        Gen_Main.Gen_DefinitionHeader()
        self.assertEqual(True, True)  # add assertion here

    def test_Gen_DefinitionSource(self):
        Gen_Main = GenMainCodeClass.GenGenMainCodeClass('../CaseMaterial/gw_dbc.dbc', '../CaseMaterial')
        Gen_Main.Gen_DefinitionSource()
        self.assertEqual(True, True)  # add assertion here

    def test_Gen_BinutilHeader(self):
        Gen_Main = GenMainCodeClass.GenGenMainCodeClass('../CaseMaterial/gw_dbc.dbc', '../CaseMaterial')
        Gen_Main.Gen_BinutilHeader()
        self.assertEqual(True, True)  # add assertion here

    def test_Gen_BinutilSource(self):
        Gen_Main = GenMainCodeClass.GenGenMainCodeClass('../CaseMaterial/gw_dbc.dbc', '../CaseMaterial')
        Gen_Main.Gen_BinutilSource()
        self.assertEqual(True, True)  # add assertion here

    def test_Gen_MonitorutilHeader(self):
        Gen_Main = GenMainCodeClass.GenGenMainCodeClass('../CaseMaterial/gw_dbc.dbc', '../CaseMaterial')
        Gen_Main.Gen_MonitorutilHeader()
        self.assertEqual(True, True)  # add assertion here

    def test_Gen_MonitorutilSource(self):
        Gen_Main = GenMainCodeClass.GenGenMainCodeClass('../CaseMaterial/gw_dbc.dbc', '../CaseMaterial')
        Gen_Main.Gen_MonitorutilSource()
        self.assertEqual(True, True)  # add assertion here

    def test_Gen_CycleActHeader(self):
        Gen_Main = GenMainCodeClass.GenGenMainCodeClass('../CaseMaterial/gw_dbc.dbc', '../CaseMaterial')
        Gen_Main.Gen_CycleActHeader()
        self.assertEqual(True, True)  # add assertion here

    def test_Gen_CycleActSource(self):
        Gen_Main = GenMainCodeClass.GenGenMainCodeClass('../CaseMaterial/gw_dbc.dbc', '../CaseMaterial')
        Gen_Main.Gen_CycleActSource()
        self.assertEqual(True, True)  # add assertion here

    def test_Gen_ConfigHeader(self):
        Gen_Main = GenMainCodeClass.GenGenMainCodeClass('../CaseMaterial/gw_dbc.dbc', '../CaseMaterial')
        Gen_Main.Gen_ConfigHeader()
        self.assertEqual(True, True)  # add assertion here

    def test_Gen_MsgParseAOPHeader(self):
        Gen_Main = GenMainCodeClass.GenGenMainCodeClass('../CaseMaterial/gw_dbc.dbc', '../CaseMaterial')
        Gen_Main.Gen_MsgParseAOPHeader()
        self.assertEqual(True, True)  # add assertion here

    def test_Gen_MsgParseAOPSource(self):
        Gen_Main = GenMainCodeClass.GenGenMainCodeClass('../CaseMaterial/gw_dbc.dbc', '../CaseMaterial')
        Gen_Main.Gen_MsgParseAOPSource()
        self.assertEqual(True, True)  # add assertion here

    def test_Gen_MsgCycAOPHeader(self):
        Gen_Main = GenMainCodeClass.GenGenMainCodeClass('../CaseMaterial/gw_dbc.dbc', '../CaseMaterial')
        Gen_Main.Gen_MsgCycAOPHeader()
        self.assertEqual(True, True)  # add assertion here

    def test_MsgCycAOPSource(self):
        Gen_Main = GenMainCodeClass.GenGenMainCodeClass('../CaseMaterial/gw_dbc.dbc', '../CaseMaterial')
        Gen_Main.Gen_MsgCycAOPSource()
        self.assertEqual(True, True)  # add assertion here

    def test_Gen_MainCode(self):
        Gen_Main = GenMainCodeClass.GenGenMainCodeClass('../CaseMaterial/gw_dbc.dbc', '../CaseMaterial/ACAN', 'ACAN')
        Gen_Main.Gen_MainCode()
        # Gen_Main = GenMainCodeClass.GenGenMainCodeClass('../CaseMaterial/DBC_BCAN.dbc', '../CaseMaterial/BCAN', 'BCAN')
        # Gen_Main.Gen_MainCode()
        # Gen_Main = GenMainCodeClass.GenGenMainCodeClass('../CaseMaterial/DBC_CCAN.dbc', '../CaseMaterial/CCAN', 'CCAN')
        # Gen_Main.Gen_MainCode()
        self.assertEqual(True, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()
