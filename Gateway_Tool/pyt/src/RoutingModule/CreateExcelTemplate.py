import xlwings as xw

from pyt.src.config.RouteConfig import RouteConfig


def CreateExcelTemplate(filePath):
    """
    根据配置文件的属性创建Excel的模板，方便填写后续的路由矩阵。
    """

    routeConfig = RouteConfig()

    app = xw.App(visible=False)  # 设置Excel为不可见。
    try:
        wb = app.books.add()
        sheet = wb.sheets[0]  # 载入工作表。

        row = 1
        for attribute_name, attribute_index in routeConfig.ATTRIBUTE_DICT.items():
            column = attribute_index + 1
            sheet.range(row, column).value = attribute_name

        wb.save(filePath)  # 保存Excel文件。
        wb.close()  # 关闭Excel文件。
    finally:
        # 确保任何情况下都可以退出应用程序。
        app.quit()
