from pyt.src.ToolModule.FuncTool import CoInitialize


class ExcelDealClass(object):
    """
    初始化时需要打开Excel
    需要读取Excel的内容。
    格式化
    需要根据内容生成代码。
    """

    def __init__(self, excelPath):
        self._routeList = self.openExcel(excelPath)

    @property
    def routeList(self):
        return self._routeList

    @staticmethod
    @CoInitialize
    def openExcel(file) -> list[list]:
        return [[]]


if __name__ == '__main__':
    print(ExcelDealClass('12').routeList)
