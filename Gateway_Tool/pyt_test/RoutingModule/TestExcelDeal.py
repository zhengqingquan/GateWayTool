import logging
import unittest

from pyt.src.RoutingModule.ExcelDeal import read_excel_file, excel_col_to_num, excel_num_to_col, getExcelTableHeader
from pyt.src.config.ConfigFolderCheck import configFolderCheck, loadConfig


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        configFolderCheck(r'../CaseMaterial/config')
        loadConfig(r'../CaseMaterial/config')

    def test_read_excel_file_case1(self):
        result = read_excel_file('../CaseMaterial/新建 Microsoft Excel 工作表.xlsx')
        for e in result:
            logging.info(e)

        self.assertEqual(True, True)

    def test_getExcelTableHeader(self):
        result = getExcelTableHeader('../CaseMaterial/新建 Microsoft Excel 工作表.xlsx')
        for e in result:
            logging.info(e)

        self.assertEqual(True, True)

    def test_excel_col_to_num_case1(self):
        # 测试数据
        data = 'z'
        # 预期结果
        expected = 26
        # 执行结果
        result = excel_col_to_num(data)

        self.assertEqual(expected, result)

    def test_excel_col_to_num_case2(self):
        # 测试数据
        data = 'AA'
        # 预期结果
        expected = 27
        # 执行结果
        result = excel_col_to_num(data)

        self.assertEqual(expected, result)

    def test_excel_col_to_num_case3(self):
        # 测试数据
        data = 'AsFf'
        # 预期结果
        expected = 30582
        # 执行结果
        result = excel_col_to_num(data)

        self.assertEqual(expected, result)

    def test_excel_num_to_col_case1(self):
        # 测试数据
        data = 6
        # 预期结果
        expected = 'F'
        # 执行结果
        result = excel_num_to_col(data)

        self.assertEqual(expected, result)

    def test_excel_num_to_col_case2(self):
        # 测试数据
        data = '26'
        # 预期结果
        expected = 'Z'
        # 执行结果
        result = excel_num_to_col(data)

        self.assertEqual(expected, result)

    def test_excel_num_to_col_case3(self):
        # 测试数据
        data = '27'
        # 预期结果
        expected = 'AA'
        # 执行结果
        result = excel_num_to_col(data)

        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
