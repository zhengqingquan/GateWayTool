#coding=utf-8
import sys
import os
from   os.path import abspath, dirname
sys.path.append(abspath(dirname(__file__)))
import tkinter
import tkinter.filedialog
from   tkinter import *
import Fun
ElementBGArray={}  
ElementBGArray_Resize={} 
ElementBGArray_IM={} 

from pyt.src.server import Server
def Form_1_onLoad(uiName):
    """
    当窗口初始化时执行。
    """
    Server.InitFrom(uiName)
def ExcelPathButton_onCommand(uiName,widgetName):
    """
    Excel路径按钮
    """
    Server.ExcelPathButtonFunction(uiName)
def ExcelSavePathButton_onCommand(uiName,widgetName):
    """
    Excel保存路径按钮
    """
    Server.ExcelSavePathButtonFunction(uiName)
def CreateFileButton_onCommand(uiName,widgetName):
    """
    Excel的生成文件按钮
    """
    Server.CreateFileButtonFunction(uiName)
def TemplatePathButton_onCommand(uiName,widgetName):
    """
    模板路径按钮
    """
    Server.TemplatePathButtonFunction(uiName)
def JsonPathButton_onCommand(uiName,widgetName):
    """
    Json路径按钮
    """
    Server.JsonPathButtonFunction(uiName)
def ReplaceTemplateButton_onCommand(uiName,widgetName):
    """
    替换模板按钮
    """
    Server.ReplaceTemplateButtonFunction(uiName)
def TemplateSavePathButton_onCommand(uiName,widgetName):
    """
    模板的保存路径按钮
    """
    Server.TemplateSavePathButtonFunction(uiName)
def ExcelSavePathCheckButton_onCommand(uiName,widgetName):
    """
    Excel重载路径
    """
    Server.ExcelSavePathCheckButtonFunction(uiName, widgetName)
def JsonPathCheckButton_onCommand(uiName,widgetName):
    """
    Json路径重载路径
    """
    Server.JsonPathCheckButtonFunction(uiName, widgetName)
def TemplateSavePathCheckButton_onCommand(uiName,widgetName):
    """
    模板的保存路径重载路径
    """
    Server.TemplateSavePathCheckButtonFunction(uiName, widgetName)
def DBCParseButton_onCommand(uiName,widgetName):
    """
    DBC解析按钮
    """
    Server.DBCParseButtonFunction(uiName)
def DBCPathButton_onCommand(uiName,widgetName):
    """
    DBC路径按钮
    """
    Server.DBCPathButtonFunction(uiName)
def DBCSavePathButton_onCommand(uiName,widgetName):
    """
    DBC保存路径按钮
    """
    Server.DBCSavePathButtonFunction(uiName)
def Menu_菜单1的子菜单1(uiName,itemName):
    pass
def Menu_菜单1的子菜单2(uiName,itemName):
    pass
def Menu_CreateExcelTemplate(uiName,itemName):
    """
    创建Excel模板
    """
    Server.Menu_CreateExcelTemplate()
def Menu_菜单2的子菜单2(uiName,itemName):
    pass
def Menu_菜单3的子菜单1(uiName,itemName):
    pass
def Menu_version(uiName,itemName):
    """
    版本菜单
    """
    Server.Menu_versionFunction()
