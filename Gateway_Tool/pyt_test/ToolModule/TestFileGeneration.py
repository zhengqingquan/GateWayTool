import unittest

import logging
from pyt.src.ToolModule.FileGeneration import generate_description, generate_HeadFileIfndef, generate_HeadFileInclude


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    def test_generate_description_case1(self):
        filePath = '../CaseMaterial/TestTemplate/file.text'
        with open(filePath, mode='w', encoding='utf-8') as file:
            file.truncate()  # 清空
        generate_description(filePath, brief='', attention='')
        self.assertEqual(True, True)

    def test_generate_HeadFileIfndef(self):
        filePath = '../CaseMaterial/TestTemplate/file.text'
        with open(filePath, mode='w', encoding='utf-8') as file:
            file.truncate()  # 清空
        generate_HeadFileIfndef(filePath)
        self.assertEqual(True, True)

    def test_generate_HeadFileInclude(self):
        filePath = '../CaseMaterial/TestTemplate/file.text'
        stdHeadList = ['aaa.h', 'bbd.h', 'bbc.h', 'std.h', 'nostd.h', ""]
        cusHeadList = ['a', 'd', 'b', 'c']
        with open(filePath, mode='w', encoding='utf-8') as file:
            file.truncate()  # 清空
        generate_HeadFileInclude(filePath, stdHeadList, cusHeadList, isSort=True)
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
