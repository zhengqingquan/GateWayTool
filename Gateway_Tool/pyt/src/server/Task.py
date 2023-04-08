import logging
from typing import Dict
import threading
from threading import Thread
import tkinter
import tkinter.ttk
from tkinter import messagebox

from pyt.src.server import TaskThread
import Fun

# 任务线程池
TaskThreadPool: Dict[str, Thread] = {}


def InitTaskThreads():
    """
    初始化任务线程
    """
    global TaskThreadPool
    TaskThreadPool['SaveFileTask'] = threading.Thread()
    TaskThreadPool['ReplaceTemplateTask'] = threading.Thread()
    TaskThreadPool['DBCParseTask'] = threading.Thread()
    TaskThreadPool['CreateExcelTemplateTask'] = threading.Thread()


def GetTaskThreadPool():
    """
    获取线程池
    """
    global TaskThreadPool
    return TaskThreadPool


def SaveFileTask(uiName, filePath, savePath):
    """
    Excel文件保存任务
    """
    global TaskThreadPool
    ProgressBar: tkinter.ttk.Progressbar = Fun.GetElement(uiName, 'ProgressBar')
    ProgressBar.config(mode='indeterminate')
    ProgressBar.start(interval=10)

    def stopProgress(threadFun):
        if threadFun.is_alive():
            ProgressBar.after(ms=10, func=lambda: stopProgress(threadFun))
        else:
            ProgressBar.stop()

    # 如果线程不活跃，则重新设置并启动线程。
    if TaskThreadPool['SaveFileTask'].is_alive() is False:
        TaskThreadPool['SaveFileTask'] = threading.Thread(target=TaskThread.SaveFileTaskThread,
                                                          args=(filePath, savePath),
                                                          daemon=True)
        TaskThreadPool['SaveFileTask'].start()
        return stopProgress(TaskThreadPool['SaveFileTask'])
    else:
        tkinter.messagebox.showinfo(title='信息', message='文件正在生成，请稍等。')


def ReplaceTemplateTask(uiName, templatePath, jsonPath, savePath):
    """
    模板替换任务
    """
    global TaskThreadPool

    ProgressBar: tkinter.ttk.Progressbar = Fun.GetElement(uiName, 'ProgressBar')
    ProgressBar.config(mode='indeterminate')
    ProgressBar.start(interval=10)

    def stopProgress(threadFun):
        if threadFun.is_alive():
            ProgressBar.after(ms=10, func=lambda: stopProgress(threadFun))
        else:
            ProgressBar.stop()

    # 如果线程不活跃，则重写设置并启动线程。
    if TaskThreadPool['ReplaceTemplateTask'].is_alive() is False:
        TaskThreadPool['ReplaceTemplateTask'] = threading.Thread(target=TaskThread.ReplaceTemplateTaskThread,
                                                                 args=(templatePath, jsonPath, savePath),
                                                                 daemon=True)
        TaskThreadPool['ReplaceTemplateTask'].start()
        return stopProgress(TaskThreadPool['ReplaceTemplateTask'])
    else:
        tkinter.messagebox.showinfo(title='信息', message='文件正在替换，请稍等。')


def DBCParseTask(uiName, dbcPath, folederPath):
    """
    DBC解析任务
    """
    global TaskThreadPool
    ProgressBar: tkinter.ttk.Progressbar = Fun.GetElement(uiName, 'ProgressBar')
    ProgressBar.config(mode='indeterminate')
    ProgressBar.start(interval=10)

    def stopProgress(threadFun):
        if threadFun.is_alive():
            ProgressBar.after(ms=10, func=lambda: stopProgress(threadFun))
        else:
            ProgressBar.stop()

    # 如果线程不活跃，则重新设置并启动线程。
    if TaskThreadPool['DBCParseTask'].is_alive() is False:
        TaskThreadPool['DBCParseTask'] = threading.Thread(target=TaskThread.DBCParseTaskThread,
                                                          args=(dbcPath, folederPath),
                                                          daemon=True)
        TaskThreadPool['DBCParseTask'].start()
        return stopProgress(TaskThreadPool['DBCParseTask'])
    else:
        tkinter.messagebox.showinfo(title='信息', message='文件正在生成，请稍等。')


def CreateExcelTemplateTask(savePath):
    """
    创建Excel模板
    """
    global TaskThreadPool

    # 如果线程不活跃，则重新设置并启动线程。
    if TaskThreadPool['CreateExcelTemplateTask'].is_alive() is False:
        TaskThreadPool['CreateExcelTemplateTask'] = threading.Thread(target=TaskThread.CreateExcelTemplateTaskThread,
                                                                     args=(savePath,),
                                                                     daemon=True)
        TaskThreadPool['CreateExcelTemplateTask'].start()
    else:
        logging.info('Excel模板正在生成，请等待。')
