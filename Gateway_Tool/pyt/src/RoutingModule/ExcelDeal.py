import logging
import os

import xlwings as xw
from typing import Union, AnyStr, List

from pyt.src.ToolModule.FuncTool import runTimeMsg, CoInitialize
from pyt.src.config.FileDealConfig import FileDealConfig
from pyt.src.config.RouteConfig import RouteConfig


# TODO 这个结构需要改下。
@runTimeMsg(r'读取Excel文件')
@CoInitialize
def read_excel_file(excelPath: AnyStr, sheetName: AnyStr = 'Sheet1') -> list[list]:
    """
    从Excel的工作表中读取需要的内容并返回列表[]。
    :param excelPath: Excel的文件路径
    :param sheetName: 工作表的名称，默认为’Sheet1‘
    :return: 列表[]
    """

    # 当文件不存在时主动触发FileNotFoundError异常。
    # 若直接使用raise FileNotFoundError需要自己设置FileNotFoundError.filename属性。
    if not os.path.exists(excelPath):
        with open(excelPath):
            pass

    # xlwings详细见官方用例：https://docs.xlwings.org/en/stable/api.html
    app = xw.App(visible=False, add_book=False)  # 设置Excel为不可见，且不自动创建工作簿。
    try:
        wb = app.books.open(excelPath)  # 打开Excel。
        sheet = wb.sheets[sheetName]  # 载入工作表。

        # 获取Excel的单元格内容的几种常规方式。
        # 详细见官方用例：
        # https://docs.xlwings.org/en/stable/api.html#range
        # 方式一：使用行列数。
        # print(type(sheet.range((10, 10)).address))
        # 方式二：使用Excel的行列表达式。
        # print(type(sheet.range('$B$9').address))
        # 方式三：读取某个范围内的值。
        # print(xw.Range('A1:C3').value)

        fileConfig = FileDealConfig()
        if fileConfig.ExcelLoadType == 'CellType':
            # 使用配置文件中的配置项来确定整个表格的操作范围。
            # 该方法可以自由选取数据范围。
            BeginCell = fileConfig.BeginCell  # 开始单元格
            EndCell = fileConfig.EndCell  # 结束单元格
            lines = abs(sheet.range(BeginCell).row - sheet.range(EndCell).row) + 1  # 行数
            ranks = abs(sheet.range(BeginCell).column - sheet.range(EndCell).column) + 1  # 列数
        else:
            # 用表格的第一行和第一列作为基准线，来确定整个表格的操作范围。
            # 这里在A1的位置使用“ctrl+↓”和”ctrl+→“来确定的范围。
            # 需要注意，使用这种方法的话，如果包含空白单元格（只有空格的单元格）也会被计算在内。
            # 该方法有一定局限性，因此作为默认的数据选取方式。
            ranks = sheet.range('A1').end('right').column  # 列数
            columns = excel_num_to_col(ranks)  # 列号
            rows = sheet.range('A1').end('down').row  # 行号
            lines = rows - 1  # 行数
            BeginCell = 'A2'  # 开始单元格
            EndCell = f'{columns}{rows}'  # 结束单元格

        # 要求数据的列数要符合配置项中的属性数量
        routeConfig = RouteConfig()
        assert ranks >= len(routeConfig.ATTRIBUTE_DICT), 'Excel中的列数不符合配置项中的报文属性数量，请检查Excel或相应配置。'

        # 获取的Excel里的数据并返回列表。
        if lines == 1:  # 只有一行数据的情况。
            return [sheet.range(BeginCell, EndCell).value]
        else:
            return sheet.range(BeginCell, EndCell).value

        # wb.save()  # 保存Excel文件。因为不应该对源Excel进行修改，因此不执行保存操作。
        # wb.close()  # 关闭Excel文件
    finally:
        # 确保任何情况下都可以退出应用程序而无需保存任何工作簿。
        app.quit()


def getExcelTableHeader(filePath, sheet=0) -> list:
    """
    获得Excel中表头的名称
    """

    app = xw.App(visible=False)  # 在不可见的状态下打开Excel
    try:
        sheet = app.books.open(filePath).sheets[sheet]  # 打开Excel，载入工作表。

        BeginCell = 'A1'
        # 在A1的位置使用”ctrl+→“来确定的范围。
        EndCell = sheet.range(BeginCell).end('right').address

        return sheet.range(BeginCell, EndCell).value

    finally:
        # 确保任何情况下都可以退出应用程序而无需保存任何工作簿。
        app.quit()


@runTimeMsg(r'打印错误单元格')
def print_excel_error(dataList: List[list], errorList: List[tuple]) -> None:
    """
    根据错误列表errorList，打印列表dataList中不符合预期的意外值。
    :param dataList: 原始列表
    :param errorList: 元组列表，表示错误值的在原始列表的中的下标
    :return: None
    """

    if (errorList is None) or (len(errorList) == 0):
        return

    logging.warning(f'有意料之外的值，共{len(errorList)}个：')
    for e in errorList:
        row = e[0] + 2
        column = excel_num_to_col(e[1] + 1)
        logging.warning(f'({row},{column})：' + str(dataList[e[0]][e[1]]))
    logging.warning(u'请修改上述值后重试。\n')


def excel_col_to_num(column_str: str) -> int:
    """
    将Excel表的列数转为整数，传入的字符串可以是大写也可以是小写。
    例如：列：A -> 列：1
    参考：Excel表格列数的字母表达与数字的相互转换。
    https://blog.csdn.net/boysoft2002/article/details/119794260?utm_medium=distribute.pc_relevant.none-task-blog-2~default~baidujs_title~default-0-119794260-blog-106899430.pc_relevant_default&spm=1001.2101.3001.4242.1&utm_relevant_index=3
    :param column_str: Excel中的列命。
    :return: 对应的列数。
    """

    if not isinstance(column_str, str):
        raise TypeError(u'The input parameter type should be str. 输入的参数类型应该为str。')
    for e in column_str.upper():
        if not 64 < ord(e) < 91:
            raise ValueError(u'Excel Column ValueError. 输入的Excel列值错误。')
    return sum([(ord(n) - 64) * 26 ** e for e, n in enumerate(list(column_str.upper())[::-1])])


def excel_num_to_col(num: Union[int, str]) -> str:
    """
    将整数转为Excel表中的列数。支持int和str类型。
    例如：列：1 -> 列：A
    参考：数字转换为Excel中列名字母。
    https://blog.csdn.net/Nzyr_Lizyx/article/details/106899430#:~:text=%E8%BF%99%E4%B8%AA%E6%98%AF%20openpyxl.utils%20%E4%B8%AD%E9%99%84%E5%B8%A6%E7%9A%84%E4%B8%80%E4%B8%AA%E5%8F%AB%20get_column_letter%20%E7%9A%84%E6%96%B9%E6%B3%95%E6%89%80%E5%AE%9E%E7%8E%B0%EF%BC%8C%20%E6%BA%90%E7%A0%81%E5%A6%82%E4%B8%8B%20def%20_get_column_letter%28col_idx%29%3A,26%20to%20find%20column%20letters%20in%20reverse%20order.
    :param num: 需要转换的列数。
    :return: 对应的Excel列数。
    """

    if not (isinstance(num, int) or isinstance(num, str)):
        raise TypeError(u'The input parameter type should be str or int. 输入的参数类型应该是str或int。')
    if str(num).isdigit():
        num = int(num)
        # 官方给出的Excel列最大到 "XFD"（16384）。
        if num > 16384:
            raise ValueError(u'Exceeded Excel maximum number of columns. 超出Excel最大列数。')
    else:
        raise ValueError(u'The input Column ValueError. 输入的列值错误。')

    excel_col_name = ""
    while num // 26 != 0 or num % 26 != 0:
        if num % 26 == 0:
            excel_col_name = "Z" + excel_col_name
            num = num // 26 - 1
            continue
        else:
            excel_col_name = chr(64 + num % 26) + excel_col_name
        num = num // 26
    return excel_col_name
