import logging
import os.path
import tkinter
from tkinter import messagebox

from pyt.src.RoutingModule.CreateExcelTemplate import CreateExcelTemplate
from pyt.src.RoutingModule.ExcelDeal import read_excel_file, print_excel_error, getExcelTableHeader
from pyt.src.RoutingModule.GenRouting.GenCanListDefClass import GenCanListDefClass
from pyt.src.TemplateModule.TemplateFile import generate_file
from pyt.src.RoutingModule.RouteDeal import format_route, source_sort, ID_sort, remove_duplicate, error_route
from pyt.src.DBCParseModule.GenMainCodeClass import GenGenMainCodeClass
from pyt.src.config.ConfigFolderCheck import configDecorator


@configDecorator
def SaveFileTaskThread(filePath, savePath):
    logging.info('===================开始生成文件===================')
    try:
        # 读取路由表
        messageList = read_excel_file(filePath)
        # 列表的长度检测
        if len(messageList) > 2 ** 16:
            assert '报文数量超过定义的uint16_t'
        # 格式化路由表
        format_route(messageList)
        # 源地址排序
        source_sort(messageList)
        # ID排序
        ID_sort(messageList)
        # 去重
        remove_duplicate(messageList)
        # 查找错误
        errorList = error_route(messageList)
        # 打印错误的单元格
        print_excel_error(messageList, errorList)

        # 读取表头
        excelTableHeader = getExcelTableHeader(filePath)

        # 写入文件
        GenCanListDefClass().headerFile(os.path.join(savePath, GenCanListDefClass().headerFileName), excelTableHeader)
        GenCanListDefClass().sourceFile(os.path.join(savePath, GenCanListDefClass().sourceFileName), messageList)

        logging.info(f'文件保存路径 {os.path.abspath(savePath)}')
    except FileNotFoundError as e:
        return tkinter.messagebox.showinfo(title='信息', message=f'未找到文件:\n{e.filename}')


@configDecorator
def ReplaceTemplateTaskThread(templatePath, jsonPath, savePath):
    logging.info('===================开始替换文件===================')
    try:
        generate_file(jsonPath, templatePath, savePath)
        logging.info(f'文件保存路径 {os.path.abspath(savePath)}')
    except FileNotFoundError as e:
        logging.error(f'未找到文件 {os.path.abspath(e.filename)}')
        return tkinter.messagebox.showinfo(title='信息', message=f'未找到文件:\n{e.filename}')


@configDecorator
def DBCParseTaskThread(dbcPath, folderPath):
    logging.info('===================开始解析BDC并生成C文件===================')
    try:
        GenGenMainCodeClass(dbcPath, folderPath, os.path.basename(folderPath)).Gen_MainCode()
        logging.info(f'文件保存路径 {os.path.abspath(folderPath)}')
    except FileNotFoundError as e:
        logging.error(f'未找到文件 {os.path.abspath(e.filename)}')
        return tkinter.messagebox.showinfo(title='信息', message=f'未找到文件:\n{e.filename}')


@configDecorator
def CreateExcelTemplateTaskThread(savePath):
    CreateExcelTemplate(savePath)
    logging.info(f'Excel模板创建完成，路径：{savePath}')
