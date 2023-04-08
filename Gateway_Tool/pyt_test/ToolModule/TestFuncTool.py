import logging
import time
import unittest

from pyt.src.ToolModule.FuncTool import runTime, runTimeMsg, singleton, SingletonClass


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    def test_runTime(self):
        @runTime
        def tempFuncCase(arg1=None, arg2=None):
            time.sleep(3)

        tempFuncCase(None, None)
        self.assertEqual(True, True)

    def test_runTimeMsg(self):
        @runTimeMsg(r'测试用例')
        def tempFuncCase(arg1=None, arg2=None):
            logging.info(f'{arg1},{arg2}')
            time.sleep(3)

        tempFuncCase()
        self.assertEqual(True, True)

    def test_singleton(self):
        @singleton
        class testClass:
            pass

        instanceA = testClass()
        instanceB = testClass()
        logging.info(instanceA)
        logging.info(instanceB)

        self.assertEqual(instanceA, instanceB)

    def test_singletonClass(self):
        class testClass(SingletonClass):
            pass

        instanceA = testClass()
        instanceB = testClass()
        logging.info(instanceA)
        logging.info(instanceB)

        self.assertEqual(instanceA, instanceB)


if __name__ == '__main__':
    unittest.main()
