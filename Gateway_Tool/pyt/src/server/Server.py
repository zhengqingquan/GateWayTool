import tkinter
from pathlib import Path
from tkinter import filedialog, messagebox

import Fun
from pyt.src.SoftwareInfo import *
from pyt.src.config.ConfigFolderCheck import configFolderCheck, loadConfig
from pyt.src.server import Redirect
from pyt.src.server import Task, Log


# tkinter-filedialog-asksaveasfilename参数
# https://blog.csdn.net/dhcdhcdhcdhcdhc/article/details/83308214

def InitFrom(uiName):
    """
    当窗口初始化时执行。
    """

    # 初始化日志
    Log.InitLog(uiName)

    # 重定向标准输出和错误输出
    TestFrame = Fun.GetElement(uiName, 'PrintTextFrame')
    if TestFrame:
        Redirect.StdOutRedirectClass(TestFrame).beginStd()
        Redirect.StdErrRedirectClass(TestFrame).beginStd()

    # 检查配置
    while True:
        try:
            configFolderCheck()
            break
        except FileExistsError as error:
            # FIXME 这里有个BUG
            # 在弹窗出来后，可以操作界面的菜单，之后就可以继续操作界面。
            # 可以使用showerror或其他弹窗。
            if not tkinter.messagebox.askretrycancel('错误！',
                                                     '创建配置文件夹错误，存在同名文件。'
                                                     f'请检查路径：{Path(error.filename).resolve()}。'
                                                     '在删除或修改重名文件后重试。'):
                # 退出程序
                quit()

    # 读取配置
    try:
        loadConfig()
    except FileNotFoundError as error:
        tkinter.messagebox.showerror('错误！', f'未发现配置文件：{Path(error.filename).resolve()}。')
    except KeyError as error:
        tkinter.messagebox.showerror('错误！', f'未发现配置项：{error.args}。')

    # 初始化线程
    Task.InitTaskThreads()


def ExcelPathButtonFunction(uiName):
    """
    Excel路径按钮
    """
    openPath = tkinter.filedialog.askopenfilename(title='打开文件',
                                                  filetypes=[('Excel文件', ['*.xlsx', '*.xls']), ('所有文件', '*')])
    Fun.SetText(uiName, 'ExcelPathEntry', openPath)


def ExcelSavePathButtonFunction(uiName):
    """
    Excel保存路径按钮
    """
    savePath = tkinter.filedialog.askdirectory(title='保存文件')
    Fun.SetText(uiName, 'ExcelSavePathEntry', savePath)


def CreateFileButtonFunction(uiName):
    """
    Excel的生成文件按钮
    """
    ExcelPath = Fun.GetElement(uiName, 'ExcelPathEntry').get()
    if not ExcelPath:
        return tkinter.messagebox.showinfo(title='信息', message='请填入Excel路径。')

    ExcelSavePath = Fun.GetElement(uiName, 'ExcelSavePathEntry').get()
    if not ExcelSavePath:
        return tkinter.messagebox.showinfo(title='信息', message='请填入保存路径。')

    Task.SaveFileTask(uiName, ExcelPath, ExcelSavePath)


def TemplatePathButtonFunction(uiName):
    """
    模板路径按钮
    """
    openPath = tkinter.filedialog.askopenfilename(title='打开文件', filetypes=[('template文件', '*.template'), ('所有文件', '*')])
    Fun.SetText(uiName, 'TemplatePathEntry', openPath)


def JsonPathButtonFunction(uiName):
    """
    Json路径按钮
    """
    openPath = tkinter.filedialog.askopenfilename(title='打开文件', filetypes=[('json文件', '*.json'), ('所有文件', '*')])
    Fun.SetText(uiName, 'JsonPathEntry', openPath)


def TemplateSavePathButtonFunction(uiName):
    """
    模板的保存路径按钮
    """
    savePath = tkinter.filedialog.asksaveasfilename(title='保存文件', filetypes=[('所有文件', '*')])
    Fun.SetText(uiName, 'TemplateSavePathEntry', savePath)


def ReplaceTemplateButtonFunction(uiName):
    """
    替换模板按钮
    """
    TemplatePath = Fun.GetElement(uiName, 'TemplatePathEntry').get()
    if not TemplatePath:
        return tkinter.messagebox.showinfo(title='信息', message='请填入模板路径。')

    JsonPath = Fun.GetElement(uiName, 'JsonPathEntry').get()
    if not JsonPath:
        return tkinter.messagebox.showinfo(title='信息', message='请填入Json路径。')

    TemplateSavePath = Fun.GetElement(uiName, 'TemplateSavePathEntry').get()
    if not TemplateSavePath:
        return tkinter.messagebox.showinfo(title='信息', message='请填入保存路径。')

    Task.ReplaceTemplateTask(uiName, TemplatePath, JsonPath, TemplateSavePath)


def ExcelSavePathCheckButtonFunction(uiName, widgetName):
    pass


def JsonPathCheckButtonFunction(uiName, widgetName):
    pass


def TemplateSavePathCheckButtonFunction(uiName, widgetName):
    pass


def DBCParseButtonFunction(uiName):
    """
    DBC解析按钮
    """
    DBCPath = Fun.GetElement(uiName, 'DBCPathEntry').get()
    if not DBCPath:
        return tkinter.messagebox.showinfo(title='信息', message='请填入DBC路径。')

    FolderSavePath = Fun.GetElement(uiName, 'DBCSavePathEntry').get()
    if not FolderSavePath:
        return tkinter.messagebox.showinfo(title='信息', message='请填入保存路径。')

    Task.DBCParseTask(uiName, DBCPath, FolderSavePath)


def DBCPathButtonFunction(uiName):
    """
    DBC路径按钮
    """
    openPath = tkinter.filedialog.askopenfilename(title='打开文件', filetypes=[('dbc文件', '*.dbc'), ('所有文件', '*')])
    Fun.SetText(uiName, 'DBCPathEntry', openPath)


def DBCSavePathButtonFunction(uiName):
    """
    DBC保存路径按钮
    """
    savePath = tkinter.filedialog.askdirectory(title='保存文件')
    Fun.SetText(uiName, 'DBCSavePathEntry', savePath)


def Menu_CreateExcelTemplate():
    """
    创建Excel模板
    """
    savePath = tkinter.filedialog.asksaveasfilename(title='保存文件',
                                                    defaultextension='template.xlsx',
                                                    filetypes=[('Excel文件', ['*.xlsx', '*.xls']), ('所有文件', '*')])
    if savePath:
        Task.CreateExcelTemplateTask(savePath)


def Menu_versionFunction():
    """
    版本菜单
    """
    message = f'软件名：{SOFTWARE_NAME}\n' \
              f'软件版本：{SOFTWARE_VERSION}'
    tkinter.messagebox.showinfo(title='版本信息', message=message)
