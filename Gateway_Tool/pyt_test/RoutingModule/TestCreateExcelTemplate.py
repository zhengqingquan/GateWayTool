import logging
import unittest

from pyt.src.RoutingModule.CreateExcelTemplate import CreateExcelTemplate
from pyt.src.config.ConfigFolderCheck import loadConfig, configFolderCheck


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        configFolderCheck(r'../CaseMaterial/config')
        loadConfig(r'../CaseMaterial/config')

    def test_something(self):
        filePath = r'../CaseMaterial/CreateExcelTemplate.xlsx'
        CreateExcelTemplate(filePath)
        self.assertEqual(True, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()
