import logging
import unittest

from pyt.src.config.ConfigFolderCheck import configFolderCheck, loadConfig


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        # 加载日志
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    def test_configFolderCheck(self):
        configFolderCheck(r'../CaseMaterial/config')
        self.assertEqual(True, True)  # add assertion here

    def test_loadConfig(self):
        loadConfig(r'../CaseMaterial/config')
        self.assertEqual(True, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()
