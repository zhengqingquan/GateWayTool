#!/usr/bin/env python
#coding=utf-8
#此文件不支持直接编辑
import os
from   os.path import abspath, dirname
import tkinter
import tkinter.simpledialog
from   PIL import Image,ImageTk
import math

G_UIElementArray={}
G_UIElementPlaceArray={}
G_UIElementUserDataArray={}
G_UIElementVariableArray={}
G_UIElementIconArray={}
G_UIInputDataArray={} 
G_UIElementAlias={}
G_UIGroupDictionary={}
G_UIStyleDictionary={}
G_CanvasShapeDictory={}
G_CanvasFontDictory={}
G_CanvasImageDictory={}
G_CanvasPointDictory={}
G_CanvasEventDictory={}
G_CurrentFilePath=None
G_CutContent=None
def Register(uiName,elementName,element,alias=None,groupName=None,styleName=None):
    """注册一个控件,用于记录它:参数1 :界面类名, 参数2:控件名称,参数3 :控件。"""
    if uiName not in G_UIElementArray:
        G_UIElementArray[uiName]={}
        G_UIElementAlias[uiName]={}
        G_UIElementPlaceArray[uiName]={}
        G_UIGroupDictionary[uiName]={}
        G_UIStyleDictionary[uiName]={}
        G_CanvasShapeDictory[uiName]={}
        G_CanvasFontDictory[uiName]={}
        G_CanvasImageDictory[uiName]={}
        G_CanvasEventDictory[uiName]={}
        G_CanvasPointDictory[uiName]={}
        G_UIElementIconArray[uiName]={}
        G_UIElementIconArray[uiName]['MainMenu'] = {}
        G_UIElementIconArray[uiName]['SysTray'] = {}
    G_UIElementArray[uiName][elementName]=element
    if alias:
        G_UIElementAlias[uiName][alias]=elementName
    if groupName:
        G_UIGroupDictionary[uiName][elementName]=groupName
    if styleName:
        G_UIStyleDictionary[uiName][elementName]=styleName
    if elementName.find('TreeView_') >= 0:
        G_UIElementIconArray[uiName][elementName]={}
def DestroyUI(uiName):
    """销毁一个界面:参数1 :界面类名"""
    if uiName in G_UIElementArray:
        root = GetElement(uiName,"root")
        if root is not None:
            root.destroy()
        G_UIElementArray.pop(uiName)
        G_UIElementAlias.pop(uiName)
        G_UIElementPlaceArray.pop(uiName)
        G_UIGroupDictionary.pop(uiName)
        G_UIStyleDictionary.pop(uiName)
        G_CanvasShapeDictory.pop(uiName)
        G_CanvasFontDictory.pop(uiName)
        G_CanvasImageDictory.pop(uiName)
        G_CanvasEventDictory.pop(uiName)
        G_CanvasPointDictory.pop(uiName)
        G_UIElementIconArray.pop(uiName)
def GetElement(uiName,elementName):
    """取得控件:参数1 :界面类名, 参数2:控件名称。"""
    if uiName in G_UIElementAlias:
        if uiName in G_UIElementAlias.keys() and elementName in G_UIElementAlias[uiName].keys():
            elementName = G_UIElementAlias[uiName][elementName]
    if uiName in G_UIElementArray:
        if elementName in G_UIElementArray[uiName]:
            return G_UIElementArray[uiName][elementName]
    return None
def GetElementName(element):
    """取得控件的界面类名与控件名称:参数1 :控件"""
    for uiName in G_UIElementArray:
        for elementName in G_UIElementArray[uiName]:
            if G_UIElementArray[uiName][elementName] == element:
                return uiName,elementName
    return None,None
def GetElementType(uiName,elementName):
    """取得控件类型:参数1 :界面类名, 参数2:控件名称。"""
    if uiName in G_UIElementAlias:
        if uiName in G_UIElementAlias.keys() and elementName in G_UIElementAlias[uiName].keys():
            elementName = G_UIElementAlias[uiName][elementName]
    if uiName in G_UIElementArray:
        if elementName in G_UIElementArray[uiName]:
            splitArray = elementName.split('_')
            return splitArray[0] 
    return None
def AddTKVariable(uiName,elementName,defaultValue = None):
    """为控件增加一个Tkinter的内置控件变量,参数1 :界面类名, 参数2:控件名称,参数3:默认值。"""
    if uiName not in G_UIElementVariableArray:
        G_UIElementVariableArray[uiName]={}
    NameLower = elementName.lower()
    if NameLower.find('combobox_') >= 0:
        G_UIElementVariableArray[uiName][elementName]=tkinter.IntVar()
    elif NameLower.find('group_') >= 0:
        G_UIElementVariableArray[uiName][elementName]=tkinter.IntVar()
    elif NameLower.find('checkbutton_') >= 0:
        G_UIElementVariableArray[uiName][elementName]=tkinter.BooleanVar()
    else:
        G_UIElementVariableArray[uiName][elementName]=tkinter.StringVar()
    if defaultValue:
        G_UIElementVariableArray[uiName][elementName].set(defaultValue) 
    return G_UIElementVariableArray[uiName][elementName]
def SetTKVariable(uiName,elementName,value):
    """设置控件的tkinter变量.参数1 :界面类名, 参数2:控件名称,参数3:值。"""
    if uiName in G_UIElementVariableArray:
        if uiName in G_UIElementAlias.keys() and elementName in G_UIElementAlias[uiName].keys():
            elementName = G_UIElementAlias[uiName][elementName]
        if elementName in G_UIElementVariableArray[uiName]:
            G_UIElementVariableArray[uiName][elementName].set(value)
        if elementName in G_UIGroupDictionary[uiName]:
            GroupName = G_UIGroupDictionary[uiName][elementName]
            if GroupName in G_UIElementVariableArray[uiName]:
                G_UIElementVariableArray[uiName][GroupName].set(value)
def GetTKVariable(uiName,elementName):
    """取得控件的tkinter变量.参数1 :界面类名, 参数2:控件名称。"""
    if uiName in G_UIElementVariableArray:
        if uiName in G_UIElementAlias.keys() and elementName in G_UIElementAlias[uiName].keys():
            elementName = G_UIElementAlias[uiName][elementName]
        if elementName in G_UIElementVariableArray[uiName]:
            return G_UIElementVariableArray[uiName][elementName].get()
        if elementName in G_UIGroupDictionary[uiName]:
            GroupName = G_UIGroupDictionary[uiName][elementName]
            if GroupName in G_UIElementVariableArray[uiName]:
                return G_UIElementVariableArray[uiName][GroupName].get()
    return None
def AddUserData(uiName,elementName,dataName,datatype,datavalue,isMapToText):
    """为控件添加一个用户数据,参数1 :界面类名, 参数2:控件名称,参数3:dataname为数据名,datatype为数据类型,可以包括int、float、string、list、dictionary等,一般在设计软件中用鼠标右键操作控件,在弹出的“绑定数据”对话枉中设置,参数4:datavalue为数据值,而ismaptotext则是是否将数据直接反映到控件的text变量中。"""
    global G_UIElementUserDataArray
    if uiName not in G_UIElementUserDataArray:
        G_UIElementUserDataArray[uiName]={} 
    if uiName in G_UIElementAlias.keys() and elementName in G_UIElementAlias[uiName].keys():
        elementName = G_UIElementAlias[uiName][elementName]
    if elementName not in G_UIElementUserDataArray[uiName]:
        G_UIElementUserDataArray[uiName][elementName]=[]
    else:
        for EBData in G_UIElementUserDataArray[uiName][elementName]:
            if EBData[0] == dataName:
                EBData[1] = datatype
                EBData[2] = datavalue
                EBData[3] = isMapToText
                if EBData[3] == 1:
                    SetText(uiName,elementName,datavalue) 
                return
    G_UIElementUserDataArray[uiName][elementName].append([dataName,datatype,datavalue,isMapToText])
def SetUserData(uiName,elementName,dataName,datavalue):
    """设置控件的用户数据值。参数1 :界面类名, 参数2:控件名称,参数3:dataname为数据名,参数4:datavalue为数据值。"""
    global G_UIElementUserDataArray
    if uiName in G_UIElementUserDataArray:
        if uiName in G_UIElementAlias.keys() and elementName in G_UIElementAlias[uiName].keys():
            elementName = G_UIElementAlias[uiName][elementName]
        if elementName in G_UIElementUserDataArray[uiName]:
            for EBData in G_UIElementUserDataArray[uiName][elementName]:
                if EBData[0] == dataName:
                    EBData[2] = datavalue
                    if EBData[3] == 1:
                        SetText(uiName,elementName,datavalue) 
                    return
def GetUserData(uiName,elementName,dataName):
    """取得控件的用户数据值。参数1 :界面类名, 参数2:控件名称,参数3:dataname为数据名。"""
    global G_UIElementUserDataArray
    if  uiName in G_UIElementUserDataArray:
        if uiName in G_UIElementAlias.keys() and elementName in G_UIElementAlias[uiName].keys():
            elementName = G_UIElementAlias[uiName][elementName]
        if elementName in G_UIElementUserDataArray[uiName]:
            for EBData in G_UIElementUserDataArray[uiName][elementName]:
                if EBData[0] == dataName:
                    if EBData[1]=='int':
                        return int(EBData[2])
                    elif EBData[1]=='float':
                        return float(EBData[2])
                    else:
                        return EBData[2]
    return None
def SetTKAttrib(uiName,elementName,AttribName,attribValue):
    """设置控件的tkinter属性值。参数1 :界面类名, 参数2:控件名称,参数3:AttribName为属性名,参数4:attribValue为数据值。"""
    global G_UIElementArray
    if uiName in G_UIElementArray:
        if uiName in G_UIElementAlias.keys() and elementName in G_UIElementAlias[uiName].keys():
            elementName = G_UIElementAlias[uiName][elementName]
        if AttribName in G_UIElementArray[uiName][elementName].configure().keys():
            G_UIElementArray[uiName][elementName][AttribName]=attribValue
def GetTKAttrib(uiName,elementName,AttribName):
    """获取控件的tkinter属性值。参数1 :界面类名, 参数2:控件名称,参数3:AttribName为属性名。"""
    global G_UIElementArray
    if uiName in G_UIElementArray:
        if uiName in G_UIElementAlias.keys() and elementName in G_UIElementAlias[uiName].keys():
            elementName = G_UIElementAlias[uiName][elementName]
        return G_UIElementArray[uiName][elementName].cget(AttribName)
def SetElementVisible(uiName,elementName,Visible):
    """设置控件显示或隐藏"""
    if Visible == True:
        element = GetElement(uiName,elementName)
        if G_UIElementPlaceArray[uiName][elementName]["type"] == "pack":
            fill = G_UIElementPlaceArray[uiName][elementName]["fill"]
            side = G_UIElementPlaceArray[uiName][elementName]["side"]
            padx = G_UIElementPlaceArray[uiName][elementName]["padx"]
            pady = G_UIElementPlaceArray[uiName][elementName]["pady"]
            SetControlPack(uiName,elementName,fill,side,padx,pady)
        elif G_UIElementPlaceArray[uiName][elementName]["type"] == "grid":
            row = G_UIElementPlaceArray[uiName][elementName]["row"]
            column = G_UIElementPlaceArray[uiName][elementName]["column"]
            rowspan = G_UIElementPlaceArray[uiName][elementName]["rowspan"]
            columnspan = G_UIElementPlaceArray[uiName][elementName]["columnspan"]
            SetControlGrid(uiName,elementName,row,column,rowspan,columnspan)
        elif G_UIElementPlaceArray[uiName][elementName]["type"] == "place":
            x = 0
            if "relx" in G_UIElementPlaceArray[uiName][elementName]:
                x = G_UIElementPlaceArray[uiName][elementName]["relx"]
            else:
                x = G_UIElementPlaceArray[uiName][elementName]["x"]
            y = 0
            if "rely" in G_UIElementPlaceArray[uiName][elementName]:
                y = G_UIElementPlaceArray[uiName][elementName]["rely"]
            else:
                y = G_UIElementPlaceArray[uiName][elementName]["y"]
            w = 0
            if "relwidth" in G_UIElementPlaceArray[uiName][elementName]:
                w = G_UIElementPlaceArray[uiName][elementName]["relwidth"]
            else:
                w = G_UIElementPlaceArray[uiName][elementName]["width"]
            h = 0
            if "relheight" in G_UIElementPlaceArray[uiName][elementName]:
                h = G_UIElementPlaceArray[uiName][elementName]["relheight"]
            else:
                h = G_UIElementPlaceArray[uiName][elementName]["height"]
            SetControlPlace(uiName,elementName,x,y,w,h)
    else:
        element = GetElement(uiName,elementName)
        if G_UIElementPlaceArray[uiName][elementName]["type"] == "pack":
            element.pack_forget()
        elif G_UIElementPlaceArray[uiName][elementName]["type"] == "grid":
            element.grid_forget()
        elif G_UIElementPlaceArray[uiName][elementName]["type"] == "place":
            element.place_forget()
        G_UIElementPlaceArray[uiName][elementName]['visible'] = False
def IsElementVisible(uiName,elementName):
    """取得控件显示或隐藏"""
    return G_UIElementPlaceArray[uiName][elementName]['visible']
def SetText(uiName,elementName,textValue):
    """设置控件的文本(Label、Button、Entry、Text、ComboBox, SpinBox)。参数1 :界面类名, 参数2:控件名称,参数3:文本内容。"""
    global G_UIElementArray
    global G_UIElementVariableArray
    showtext = str("%s"%textValue)
    if uiName in G_UIElementAlias.keys() and elementName in G_UIElementAlias[uiName].keys():
        elementName = G_UIElementAlias[uiName][elementName]
    if uiName in G_UIElementVariableArray:
        if elementName in G_UIElementVariableArray[uiName]:
            G_UIElementVariableArray[uiName][elementName].set(showtext)
            return
    if uiName in G_UIElementArray:
        if elementName in G_UIElementArray[uiName]:
            if elementName == "root":
                G_UIElementArray[uiName][elementName].title(textValue)
            if elementName.find('Text_') >= 0:
                G_UIElementArray[uiName][elementName].delete('0.0',tkinter.END)
                G_UIElementArray[uiName][elementName].insert(tkinter.END,showtext)
            else:
                G_UIElementArray[uiName][elementName].configure(text=showtext)
def GetText(uiName,elementName):
    """获取控件的文本(Label、Button、Entry、Text、 ComboBox, SpinBox)。参数1 :界面类名, 参数2:控件名称。"""
    global G_UIElementArray
    global G_UIElementVariableArray
    if uiName in G_UIElementAlias.keys() and elementName in G_UIElementAlias[uiName].keys():
        elementName = G_UIElementAlias[uiName][elementName]
    if uiName in G_UIElementArray:
        if elementName in G_UIElementArray[uiName]:
            if elementName.find('Text_') >= 0:
                return G_UIElementArray[uiName][elementName].get('0.0', tkinter.END)
            elif elementName.find('Spinbox_') >= 0:
                return str(G_UIElementArray[uiName][elementName].get())
            elif elementName.find('ComboBox_') >= 0:
                return str(G_UIElementArray[uiName][elementName].get())
            elif elementName.find('ListBox_') >= 0:
                currIndex = G_UIElementArray[uiName][elementName].curselection()
                if len(currIndex) > 0 and currIndex[0] >= 0:
                    return  G_UIElementArray[uiName][elementName].get(currIndex[0])
            else:
                if uiName in G_UIElementVariableArray:
                    if elementName in G_UIElementVariableArray[uiName]:
                        text = G_UIElementVariableArray[uiName][elementName].get()
                        return text
                return G_UIElementArray[uiName][elementName].cget('text')
    return str("")
def SetImage(uiName,elementName,imagePath):
    """设置控件的背景图片(Label,Button)。参数1 :界面类名, 参数2:控件名称,参数3:图片名称。"""
    global G_UIElementVariableArray
    if uiName in G_UIElementAlias.keys() and elementName in G_UIElementAlias[uiName].keys():
        elementName = G_UIElementAlias[uiName][elementName]
    if elementName.find('Label_') == 0 or elementName.find('Button_') == 0 :
        Control = GetElement(uiName,elementName)
        if Control != None:
            if uiName in G_UIElementUserDataArray:
                if elementName in G_UIElementUserDataArray[uiName]:
                    for EBData in G_UIElementUserDataArray[uiName][elementName]:
                        if EBData[0] == 'image':
                            EBData[1] = imagePath
                            from   PIL import Image,ImageTk
                            if os.path.exists(imagePath) == False:
                                imagePath = os.getcwd() + "\\Resources\\"+imagePath
                                if os.path.exists(imagePath) == False:
                                    return
                            image=Image.open(imagePath).convert('RGBA')
                            image_Resize = image.resize((Control.winfo_width(), Control.winfo_height()),Image.ANTIALIAS)
                            EBData[2] = ImageTk.PhotoImage(image_Resize)
                            Control.configure(image = EBData[2])
                            return 
            from   PIL import Image,ImageTk
            if os.path.exists(imagePath) == False:
                imagePath = os.getcwd() + "\\Resources\\"+imagePath
                if os.path.exists(imagePath) == False:
                    return
            image=Image.open(imagePath).convert('RGBA')
            image_Resize = image.resize((Control.winfo_width(), Control.winfo_height()),Image.ANTIALIAS)
            EBData2 = ImageTk.PhotoImage(image_Resize)
            AddUserData(uiName,elementName,'image',imagePath,EBData2,0)
            Control.configure(image = EBData2)
def GetImage(uiName,elementName):
    """获取控件的背景图像文件(Label、Button)。参数1 :界面类名, 参数2:控件名称。"""
    global G_UIElementVariableArray
    if uiName in G_UIElementAlias.keys() and elementName in G_UIElementAlias[uiName].keys():
        elementName = G_UIElementAlias[uiName][elementName]
    if elementName.find('Label_') == 0 or elementName.find('Button_') == 0 :
        Control = GetElement(uiName,elementName)
        if Control != None:
            if uiName in G_UIElementUserDataArray:
                if elementName in G_UIElementUserDataArray[uiName]:
                    for EBData in G_UIElementUserDataArray[uiName][elementName]:
                        if EBData[0] == 'image':
                            return EBData[1]
    return str("")
def LoadImageToIconList(uiName,elementName,ItemName,imageFile):
    """加载控件的图像文件:参数1 :界面类名, 参数2:控件名称, 参数3:树项名称, 参数4:图片文件"""
    ResourcePath = os.path.join(os.getcwd(),"Resources")
    imagePath = os.path.join(ResourcePath,imageFile)
    if os.path.exists(imagePath) == True:
        image = ImageTk.PhotoImage(file = imagePath)
        G_UIElementIconArray[uiName][elementName][ItemName] = image
        return image
    return None
def AddItemText(uiName,elementName,text,lineIndex="end"):
    """增加当前ListBox和ComboBox的文字项内容。参数1 :界面类名, 参数2:控件名称 ,参数3:文本内容。"""
    global G_UIElementArray
    if uiName in G_UIElementAlias.keys() and elementName in G_UIElementAlias[uiName].keys():
        elementName = G_UIElementAlias[uiName][elementName]
    if uiName in G_UIElementArray:
        if elementName in G_UIElementArray[uiName]:
            if elementName.find('ComboBox_') >= 0:
                ValueArray = list(G_UIElementArray[uiName][elementName]['value'])
                if type(lineIndex)==type(1):
                    ValueArray.insert(lineIndex,text)
                else:
                   ValueArray.append(text)
                G_UIElementArray[uiName][elementName]['value'] = ValueArray
            elif elementName.find('ListBox_') >= 0:
                if type(lineIndex)==type(1):
                    G_UIElementArray[uiName][elementName].insert(lineIndex,text)
                else:
                    G_UIElementArray[uiName][elementName].insert(lineIndex, text)
def AddLineText(uiName,elementName,text,lineIndex="end"):
    """为Text控件增加一行文字:参数1 :界面类名, 参数2:控件名称, 参数3:文字内容,参数4:目标行号"""
    global G_UIElementArray
    if uiName in G_UIElementAlias.keys() and elementName in G_UIElementAlias[uiName].keys():
        elementName = G_UIElementAlias[uiName][elementName]
    if uiName in G_UIElementArray:
        if elementName in G_UIElementArray[uiName]:
            if elementName.find('Text_') >= 0:
                if type(lineIndex)==type(1):
                    G_UIElementArray[uiName][elementName].insert("%d.0"%(lineIndex+1), text)
                else:
                    G_UIElementArray[uiName][elementName].insert(lineIndex, text)
def AddTreeItem(uiName,elementName,itemText,parentItem="",insertItemText="end",values=(),iconImage="",tag=""):
    """增加树项:参数1 :界面类名, 参数2:控件名称, 参数3:文字内容,参数4:父结点,参数5:插入位置项文字,参数6:树项值,参数7:图标文件,参数8:标记名称"""
    global G_UIElementArray
    global G_UIElementIconArray
    Item = None
    if uiName in G_UIElementAlias.keys() and elementName in G_UIElementAlias[uiName].keys():
        elementName = G_UIElementAlias[uiName][elementName]
    if uiName in G_UIElementArray:
        if elementName in G_UIElementArray[uiName]:
            if elementName.find('TreeView_') >= 0:
                if iconImage != "":
                    ItemIcon = ImageTk.PhotoImage(file = iconImage)
                    Item = G_UIElementArray[uiName][elementName].insert(parentItem,insertItemText,itemText,text=itemText,values=values,image=ItemIcon,tag=tag)
                    G_UIElementIconArray[uiName][elementName][Item] = ItemIcon
                else:
                    Item = G_UIElementArray[uiName][elementName].insert(parentItem,insertItemText,itemText,text=itemText,values=values,tag=tag)
    return Item
def SetTreeItemText(uiName,elementName,item,text):
    """设置树项的文字"""
    global G_UIElementArray
    if uiName in G_UIElementAlias.keys() and elementName in G_UIElementAlias[uiName].keys():
        elementName = G_UIElementAlias[uiName][elementName]
    if uiName in G_UIElementArray:
        if elementName in G_UIElementArray[uiName]:
            if elementName.find('TreeView_') >= 0:
                G_UIElementArray[uiName][elementName].item(item,text=text)
def SetTreeItemValue(uiName,elementName,item,values):
    """设置树项的值"""
    global G_UIElementArray
    if uiName in G_UIElementAlias.keys() and elementName in G_UIElementAlias[uiName].keys():
        elementName = G_UIElementAlias[uiName][elementName]
    if uiName in G_UIElementArray:
        if elementName in G_UIElementArray[uiName]:
            if elementName.find('TreeView_') >= 0:
                G_UIElementArray[uiName][elementName].item(item,values=values)
def SetTreeItemImage(uiName,elementName,item,iconImage=""):
    """设置树项的图片"""
    global G_UIElementArray
    if uiName in G_UIElementAlias.keys() and elementName in G_UIElementAlias[uiName].keys():
        elementName = G_UIElementAlias[uiName][elementName]
    if uiName in G_UIElementArray:
        if elementName in G_UIElementArray[uiName]:
            if elementName.find('TreeView_') >= 0:
                ItemIcon = ImageTk.PhotoImage(file = iconImage)
                G_UIElementArray[uiName][elementName].item(item,image=ItemIcon)
                G_UIElementIconArray[uiName][elementName][Item] = ItemIcon
def ExpandTreeItem(uiName,elementName,item,expand=True):
    """展开或收缩树项"""
    global G_UIElementArray
    if uiName in G_UIElementAlias.keys() and elementName in G_UIElementAlias[uiName].keys():
        elementName = G_UIElementAlias[uiName][elementName]
    if uiName in G_UIElementArray:
        if elementName in G_UIElementArray[uiName]:
            if elementName.find('TreeView_') >= 0:
                G_UIElementArray[uiName][elementName].item(item,open=expand)
def DelItemText(uiName,elementName,lineIndexOrText):
    """删除当前ListBox和ComboBox的文字项内容。参数1 :界面类名, 参数2:控件名称 ,参数3:文本内容。"""
    global G_UIElementArray
    if uiName in G_UIElementAlias.keys() and elementName in G_UIElementAlias[uiName].keys():
        elementName = G_UIElementAlias[uiName][elementName]
    if uiName in G_UIElementArray:
        if elementName in G_UIElementArray[uiName]:
            if elementName.find('ComboBox_') >= 0:
                ValueArray = list(G_UIElementArray[uiName][elementName]['value'])
                if type(lineIndexOrText)==type(1):
                    ValueArray.pop(lineIndexOrText)
                    G_UIElementArray[uiName][elementName]['value'] = ValueArray
                else:
                    ValueIndex = ValueArray.index(lineIndexOrText)
                    if ValueIndex >= 0:
                        ValueArray.pop(ValueIndex)
                    G_UIElementArray[uiName][elementName]['value'] = ValueArray
            elif elementName.find('ListBox_') >= 0:
                if type(lineIndexOrText)==type(1):
                    G_UIElementArray[uiName][elementName].delete(lineIndexOrText)
                else:
                    ValueArray = G_UIElementArray[uiName][elementName].get(0,tkinter.END)
                    ValueIndex = ValueArray.index(lineIndexOrText)
                    if ValueIndex >= 0:
                        G_UIElementArray[uiName][elementName].delete(ValueIndex)
def DelLineText(uiName,elementName,text,lineIndex="end"):
    """删除Text控件指定行文字:参数1 :界面类名, 参数2:控件名称, 参数3:行数"""
    global G_UIElementArray
    if uiName in G_UIElementAlias.keys() and elementName in G_UIElementAlias[uiName].keys():
        elementName = G_UIElementAlias[uiName][elementName]
    if uiName in G_UIElementArray:
        if elementName in G_UIElementArray[uiName]:
            if elementName.find('Text_') >= 0:
                if type(lineIndex)==type(1):
                    G_UIElementArray[uiName][elementName].delete("%d.0,%d.end"%((lineIndex+1),(lineIndex+1)))
                else:
                    G_UIElementArray[uiName][elementName].delete("%s.0,%s.end"%(lineIndex,lineIndex))
def DelTreeItem(uiName,elementName,item):
    """删除树项"""
    global G_UIElementArray
    if uiName in G_UIElementAlias.keys() and elementName in G_UIElementAlias[uiName].keys():
        elementName = G_UIElementAlias[uiName][elementName]
    if uiName in G_UIElementArray:
        if elementName in G_UIElementArray[uiName]:
            if elementName.find('TreeView_') >= 0:
                G_UIElementArray[uiName][elementName].delete(item)
def SetSelectIndex(uiName,elementName,index):
    """设置ListBox和ComboBox的选中索引值。参数1 :界面类名, 参数2:控件名称,参数3:索引值。"""
    if uiName in G_UIElementAlias.keys() and elementName in G_UIElementAlias[uiName].keys():
        elementName = G_UIElementAlias[uiName][elementName]
    Control = GetElement(uiName,elementName)
    if Control != None:
        if elementName.find('ComboBox_') == 0 :
            Control.current(index)
        elif elementName.find('ListBox_') == 0 :
            Control.select_set(index)
def GetSelectIndex(uiName,elementName):
    """取得ListBox和ComboBox的选中索引值。参数1 :界面类名, 参数2:控件名称。"""
    if uiName in G_UIElementAlias.keys() and elementName in G_UIElementAlias[uiName].keys():
        elementName = G_UIElementAlias[uiName][elementName]
    Control = GetElement(uiName,elementName)
    if Control != None:
        if elementName.find('ComboBox_') == 0 :
            return Control.current()
        elif elementName.find('ListBox_') == 0 :
            currIndex = Control.curselection()
            if len(currIndex) > 0 and currIndex[0] >= 0:
                return currIndex[0]
    return -1
def GetCurrentValue(uiName,elementName):
    """取得控件的选中值(Scale,Progress,ListBox,ComboBox)"""
    if uiName in G_UIElementAlias.keys() and elementName in G_UIElementAlias[uiName].keys():
        elementName = G_UIElementAlias[uiName][elementName]
    Control = GetElement(uiName,elementName)
    if Control != None:
        if elementName.find('ComboBox_') == 0 :
            return Control.get()
        elif elementName.find('Scale_') == 0 :
            return Control.get()
        elif elementName.find('ListBox_') == 0 :
            currIndex = Control.curselection()
            if len(currIndex) > 0 and currIndex[0] >= 0:
                return Control["values"][currIndex[0]]
        elif elementName.find('Progress_') == 0 :
            return Control["value"]
    return -1
def SetCurrentValue(uiName,elementName,value):
    """设置控件的选中值(Scale,Progress,ListBox,ComboBox)"""
    if uiName in G_UIElementAlias.keys() and elementName in G_UIElementAlias[uiName].keys():
        elementName = G_UIElementAlias[uiName][elementName]
    Control = GetElement(uiName,elementName)
    if Control != None:
        if elementName.find('ComboBox_') == 0 :
            Control.set(value)
        elif elementName.find('Scale_') == 0 :
            Control.set(value)
        elif elementName.find('ListBox_') == 0 :
            itemIndex = 0
            for itemText in Control["values"]:
                if itemText == value:
                    Control.select_set(itemIndex)
                    break
                itemIndex = itemIndex + 1
        elif elementName.find('Progress_') == 0 :
            Control["value"] = value 
def SetScale(uiName,elementName,from_,to,tickinterval):
    """设置Slider"""
    if uiName in G_UIElementAlias.keys() and elementName in G_UIElementAlias[uiName].keys():
        elementName = G_UIElementAlias[uiName][elementName]
    Control = GetElement(uiName,elementName)
    if Control != None:
        Control.configure(from_=from_)
        Control.configure(to=to)
        Control.configure(tickinterval=tickinterval)
def InitElementData(uiName):
    """初始化界面各控件初始数。参数1 :界面类名。"""
    global G_UIElementUserDataArray
    if uiName in G_UIElementUserDataArray:
        for elementName in G_UIElementUserDataArray[uiName].keys():
            for EBData in G_UIElementUserDataArray[uiName][elementName]:
                if EBData[3] == 1:
                    SetText(uiName,elementName,EBData[2])
                    SetText(uiName,elementName,EBData[2])
    LoadCanvasRecord(uiName)
def InitElementStyle(uiName,Style):
    """初始化界面各控件初始样式。参数1 :界面类名, 参数2:样式名称。"""
    StyleArray = ReadStyleFile(Style+".py")
    global G_UIElementArray
    if uiName in G_UIElementArray:
        Root = GetElement(uiName,'root')
        TFormKey = '.TForm'
        if TFormKey in StyleArray:
            if 'background' in StyleArray[TFormKey]:
                Root['background'] = StyleArray[TFormKey]['background']
        for elementName in G_UIElementArray[uiName].keys():
            Widget = G_UIElementArray[uiName][elementName]
            try:
                if  Widget.winfo_exists() == 1:
                    WinClass = Widget.winfo_class()
                    StyleName = ".T"+WinClass
                    for attribute in StyleArray[StyleName].keys():
                        Widget[attribute] = StyleArray[StyleName][attribute]
            except BaseException:
                continue
def GetInputDataArray(uiName):
    """取得界面的所有输入数据。参数1 :界面类名。"""
    global G_UIElementArray
    global G_UIInputDataArray
    global G_UIElementVariableArray
    G_UIInputDataArray.clear()
    if uiName in G_UIElementArray:
        for elementName in G_UIElementArray[uiName].keys():
            G_UIInputDataArray[elementName] = []
            Widget = G_UIElementArray[uiName][elementName]
            if elementName.find('Text_') >= 0:
                content = Widget.get('0.0', tkinter.END)
                G_UIInputDataArray[elementName].append(content)
            elif elementName.find('Entry_') >= 0:
                content = G_UIElementVariableArray[uiName][elementName].get()
                G_UIInputDataArray[elementName].append(content)
    if uiName in G_UIElementVariableArray:
        for elementName in G_UIElementVariableArray[uiName].keys():
           if elementName.find('Group_') >= 0:
                ElementIntValue = G_UIElementVariableArray[uiName][elementName].get()
                G_UIInputDataArray[elementName] = []
                G_UIInputDataArray[elementName].append(ElementIntValue)
    return G_UIInputDataArray
def ShowWindow(uiName,WindowState):
    """设置窗口显示状态(0:隐藏,1:正常显示,2:最小化,3最大化)"""
    root = GetElement(uiName,'root')
    import ctypes
    from ctypes import windll
    import win32gui
    hwnd = windll.user32.GetParent(root.winfo_id())
    win32gui.ShowWindow(hwnd,WindowState)
def CenterDlg(uiName,popupDlg,dw=0,dh=0):
    """将弹出界面对话框居中。参数1 :界面类名, 参数2:对话框窗体,参数3:窗体宽度,参数4:窗体高度。"""
    if dw == 0:
        dw = popupDlg.winfo_width()
    if dh == 0:
        dh = popupDlg.winfo_height()
    root = GetElement(uiName,'root')
    if root != None and popupDlg != root:
       sw = root.winfo_width()
       sh = root.winfo_height()
       sx = root.winfo_x()
       sy = root.winfo_y()
       popupDlg.geometry('%dx%d+%d+%d'%(dw,dh,sx+(sw-dw)/2,sy+(sh-dh)/2))
    else:
       import ctypes
       user32 = ctypes.windll.user32
       sw = user32.GetSystemMetrics(0)
       sh = user32.GetSystemMetrics(1)
       sx = 0
       sy = 0
       popupDlg.geometry('%dx%d+%d+%d'%(dw,dh,sx+(sw-dw)/2,sy+(sh-dh)/2))
def SetRoundedRectangle(control,WidthEllipse=20,HeightEllipse=20):
    """在界面布局文件中调用设置控件的圆角属性,但由于尚未创建接口,因此有必要在两次之后调用ShowRoundedRectangle。注意 :此功能不跨平台。参数1 :控件, 参数2:圆角宽度,参数3:圆角高度。"""
    if control != None:
       control.after(10, lambda: ShowRoundedRectangle(control,WidthEllipse,HeightEllipse))
def ShowRoundedRectangle(control,WidthEllipse,HeightEllipse):
    """立即设置控件的圆角属性。注意 :此功能不跨平台。参数1 :控件, 参数2:圆角宽度,参数3:圆角高度。"""
    import win32gui
    control_width = control.winfo_width()
    control_height = control.winfo_height()
    if control_width > 1 and control_height > 1:
        HRGN = win32gui.CreateRoundRectRgn(0,0,control_width,control_height,WidthEllipse,HeightEllipse)
        win32gui.SetWindowRgn(control.winfo_id(), HRGN,1)
    else:
        control.after(10, lambda: ShowRoundedRectangle(control,WidthEllipse,HeightEllipse))
def SetTransparencyFunction(root,alpha):
    """设置窗体透明值。注意 :此功能不跨平台。"""
    if root != None:
        try :
            import ctypes
            from ctypes import windll
            hwnd = windll.user32.GetParent(root.winfo_id())
            _winlib = ctypes.windll.user32
            style = _winlib.GetWindowLongA( hwnd, 0xffffffec ) | 0x00080000
            _winlib.SetWindowLongA( hwnd, 0xffffffec, style )
            _winlib.SetLayeredWindowAttributes( hwnd, 0, alpha, 2 )
        except ImportError:
            pass
def ExpandAllTreeItem(targetTree,isOpen,parentItem = None):
    """展开或关闭树项"""
    ParentItemArray = [parentItem]
    if parentItem == None:
        ParentItemArray = targetTree.get_children()
    for Item in ParentItemArray:
        targetTree.item(Item,open=isOpen)
        for childItem in targetTree.get_children(Item):
            targetTree.item(childItem,open=isOpen)
            ExpandAllTreeItem(targetTree,isOpen,childItem)
def MessageBox(text):
    """弹出一个信息对话框。参数1 :对话框显示文字 。"""
    tkinter.messagebox.showwarning('info',text)
def InputBox(title,text):
    """弹出一个输入对话框。参数1 :对话框标题文字 ,参数2 :对话框默认框输入文字 。"""
    res = tkinter.simpledialog.askstring(title,'Input Box',initialvalue=text)
    return res
def AskBox(title,text):
    """弹出一个选择对话框,你需要选择YES或NO。参数1 :对话框标题文字 ,参数2 :对话框显示文字 。"""
    res = tkinter.messagebox.askyesno(title,text)
    return res
def WalkAllResFiles(parentPath,alldirs=True,extName=None):
    """返回对应目录的所有指定类型文件。参数1 :目录名称 ,参数2 :是否进入子目录,参数3:是否有扩展名筛选 。"""
    ResultFilesArray = []
    if os.path.exists(parentPath) == True:
        for fileName in os.listdir(parentPath):
            if '__pycache__' not in fileName:
                if '.git' not in fileName:
                    newPath = parentPath +'\\'+ fileName
                    if os.path.isdir(newPath):
                        if extName == None:
                           ResultFilesArray.append(newPath)
                        if alldirs == True:
                            ResultFilesArray.extend(WalkAllResFiles(newPath,alldirs,extName))
                    else:
                        if extName == None:
                            ResultFilesArray.append(newPath)
                        else:
                            file_extension = os.path.splitext(fileName)[1].replace('.','')
                            file_extension_lower = file_extension.lower().strip()
                            file_extName_lower = extName.lower().strip()
                            if file_extension_lower == file_extName_lower:
                                ResultFilesArray.append(newPath)
    return ResultFilesArray
def EventFunction_Adaptor(fun,  **params):
    """重新定义消息映射函数,自定义参数。"""
    return lambda event, fun=fun, params=params: fun(event, **params)
def MenuFunction_Adaptor(fun,  **params):
    """重新定义消息映射函数,自定义参数。"""
    return lambda event, fun=fun, params=params: fun(**params)
def SetControlPack(uiName,elementName,fill,side,padx,pady):
    """设置控件的打包布局。参数1 :界面类名, 参数2:控件名称 ,参数3 :填充方式,参数4:方位 ,参数5 :横向边距,参数6:纵向边距。"""
    if uiName in G_UIElementAlias.keys() and elementName in G_UIElementAlias[uiName].keys():
        elementName = G_UIElementAlias[uiName][elementName]
    Control = GetElement(uiName,elementName)
    if Control != None:
        Control.pack(fill = fill,side = side,padx = padx,pady = pady)
        PlaceDictory = {}
        PlaceDictory["type"] = "pack"
        PlaceDictory["fill"] = fill
        PlaceDictory["side"] = side
        PlaceDictory["padx"] = padx
        PlaceDictory["pady"] = pady
        PlaceDictory["visible"] = True
        G_UIElementPlaceArray[uiName][elementName]=PlaceDictory
def SetControlGrid(uiName,elementName,row,column,rowspan,columnspan):
    """设置控件的表格布局。参数1 :界面类名, 参数2:控件名称 ,参数3 :行位置,参数4:列位置 ,参数5 :合并行数,参数6:合并列数。"""
    if uiName in G_UIElementAlias.keys() and elementName in G_UIElementAlias[uiName].keys():
        elementName = G_UIElementAlias[uiName][elementName]
    Control = GetElement(uiName,elementName)
    if Control != None:
        Control.grid(row = row,column = column,rowspan = rowspan,columnspan = columnspan)
        PlaceDictory = {}
        PlaceDictory["type"] = "grid"
        PlaceDictory["row"] = row
        PlaceDictory["column"] = column
        PlaceDictory["rowspan"] = rowspan
        PlaceDictory["columnspan"] = columnspan
        PlaceDictory["visible"] = True
        G_UIElementPlaceArray[uiName][elementName]=PlaceDictory
def SetControlPlace(uiName,elementName,x,y,w,h):
    """设置控件的绝对或相对位置。参数1 :界面类名, 参数2:控件名称 ,参数3 :x位置,参数4:y位置 ,参数5 :宽度,参数6:高度 。"""
    if uiName in G_UIElementAlias.keys() and elementName in G_UIElementAlias[uiName].keys():
        elementName = G_UIElementAlias[uiName][elementName]
    Control = GetElement(uiName,elementName)
    if Control != None:
        if type(x) == type(1.0):
            if type(y) == type(1.0):
                if type(w) == type(1.0):
                    if type(h) == type(1.0):
                        Control.place(relx=x,rely=y,relwidth=w,relheight=h)
                        PlaceDictory = {}
                        PlaceDictory["type"] = "place"
                        PlaceDictory["relx"] = x
                        PlaceDictory["rely"] = y
                        PlaceDictory["relwidth"] = w
                        PlaceDictory["relheight"] = h
                        PlaceDictory["visible"] = True
                        G_UIElementPlaceArray[uiName][elementName]=PlaceDictory
                    else:
                        Control.place(relx=x,rely=y,relwidth=w,height=h)
                        PlaceDictory = {}
                        PlaceDictory["type"] = "place"
                        PlaceDictory["relx"] = x
                        PlaceDictory["rely"] = y
                        PlaceDictory["relwidth"] = w
                        PlaceDictory["height"] = h
                        PlaceDictory["visible"] = True
                        G_UIElementPlaceArray[uiName][elementName]=PlaceDictory
                else:
                    if type(h) == type(1.0):
                        Control.place(relx=x,rely=y,width=w,relheight=h)
                        PlaceDictory = {}
                        PlaceDictory["type"] = "place"
                        PlaceDictory["relx"] = x
                        PlaceDictory["rely"] = y
                        PlaceDictory["width"] = w
                        PlaceDictory["relheight"] = h
                        PlaceDictory["visible"] = True
                        G_UIElementPlaceArray[uiName][elementName]=PlaceDictory
                    else:
                        Control.place(relx=x,rely=y,width=w,height=h)
                        PlaceDictory = {}
                        PlaceDictory["type"] = "place"
                        PlaceDictory["relx"] = x
                        PlaceDictory["rely"] = y
                        PlaceDictory["width"] = w
                        PlaceDictory["height"] = h
                        PlaceDictory["visible"] = True
                        G_UIElementPlaceArray[uiName][elementName]=PlaceDictory
            else:
                if type(w) == type(1.0):
                    if type(h) == type(1.0):
                        Control.place(relx=x,y=y,relwidth=w,relheight=h)
                        PlaceDictory = {}
                        PlaceDictory["type"] = "place"
                        PlaceDictory["relx"] = x
                        PlaceDictory["y"] = y
                        PlaceDictory["relwidth"] = w
                        PlaceDictory["relheight"] = h
                        PlaceDictory["visible"] = True
                        G_UIElementPlaceArray[uiName][elementName]=PlaceDictory
                    else:
                        Control.place(relx=x,y=y,relwidth=w,height=h)
                        PlaceDictory = {}
                        PlaceDictory["type"] = "place"
                        PlaceDictory["relx"] = x
                        PlaceDictory["y"] = y
                        PlaceDictory["relwidth"] = w
                        PlaceDictory["height"] = h
                        PlaceDictory["visible"] = True
                        G_UIElementPlaceArray[uiName][elementName]=PlaceDictory
                else:
                    if type(h) == type(1.0):
                        Control.place(relx=x,y=y,relwidth=w,relheight=h)
                        PlaceDictory = {}
                        PlaceDictory["type"] = "place"
                        PlaceDictory["relx"] = x
                        PlaceDictory["y"] = y
                        PlaceDictory["relwidth"] = w
                        PlaceDictory["relheight"] = h
                        PlaceDictory["visible"] = True
                        G_UIElementPlaceArray[uiName][elementName]=PlaceDictory
                    else:
                        Control.place(relx=x,y=y,relwidth=w,height=h)
                        PlaceDictory = {}
                        PlaceDictory["type"] = "place"
                        PlaceDictory["relx"] = x
                        PlaceDictory["y"] = y
                        PlaceDictory["relwidth"] = w
                        PlaceDictory["height"] = h
                        PlaceDictory["visible"] = True
                        G_UIElementPlaceArray[uiName][elementName]=PlaceDictory
        else:
            if type(y) == type(1.0):
                if type(w) == type(1.0):
                    if type(h) == type(1.0):
                        Control.place(x=x,rely=y,relwidth=w,relheight=h)
                        PlaceDictory = {}
                        PlaceDictory["type"] = "place"
                        PlaceDictory["x"] = x
                        PlaceDictory["rely"] = y
                        PlaceDictory["relwidth"] = w
                        PlaceDictory["relheight"] = h
                        PlaceDictory["visible"] = True
                        G_UIElementPlaceArray[uiName][elementName]=PlaceDictory
                    else:
                        Control.place(x=x,rely=y,relwidth=w,height=h)
                        PlaceDictory = {}
                        PlaceDictory["type"] = "place"
                        PlaceDictory["x"] = x
                        PlaceDictory["rely"] = y
                        PlaceDictory["relwidth"] = w
                        PlaceDictory["height"] = h
                        PlaceDictory["visible"] = True
                        G_UIElementPlaceArray[uiName][elementName]=PlaceDictory
                else:
                    if type(h) == type(1.0):
                        Control.place(x=x,rely=y,width=w,relheight=h)
                        PlaceDictory = {}
                        PlaceDictory["type"] = "place"
                        PlaceDictory["x"] = x
                        PlaceDictory["rely"] = y
                        PlaceDictory["width"] = w
                        PlaceDictory["relheight"] = h
                        PlaceDictory["visible"] = True
                        G_UIElementPlaceArray[uiName][elementName]=PlaceDictory
                    else:
                        Control.place(x=x,rely=y,width=w,height=h)
                        PlaceDictory = {}
                        PlaceDictory["type"] = "place"
                        PlaceDictory["x"] = x
                        PlaceDictory["rely"] = y
                        PlaceDictory["width"] = w
                        PlaceDictory["height"] = h
                        PlaceDictory["visible"] = True
                        G_UIElementPlaceArray[uiName][elementName]=PlaceDictory
            else:
                if type(w) == type(1.0):
                    if type(h) == type(1.0):
                        Control.place(x=x,y=y,relwidth=w,relheight=h)
                        PlaceDictory = {}
                        PlaceDictory["type"] = "place"
                        PlaceDictory["x"] = x
                        PlaceDictory["y"] = y
                        PlaceDictory["relwidth"] = w
                        PlaceDictory["relheight"] = h
                        PlaceDictory["visible"] = True
                        G_UIElementPlaceArray[uiName][elementName]=PlaceDictory
                    else:
                        Control.place(x=x,y=y,relwidth=w,height=h)
                        PlaceDictory = {}
                        PlaceDictory["type"] = "place"
                        PlaceDictory["x"] = x
                        PlaceDictory["y"] = y
                        PlaceDictory["relwidth"] = w
                        PlaceDictory["height"] = h
                        PlaceDictory["visible"] = True
                        G_UIElementPlaceArray[uiName][elementName]=PlaceDictory
                else:
                    if type(h) == type(1.0):
                        Control.place(x=x,y=y,width=w,relheight=h)
                        PlaceDictory = {}
                        PlaceDictory["type"] = "place"
                        PlaceDictory["x"] = x
                        PlaceDictory["y"] = y
                        PlaceDictory["width"] = w
                        PlaceDictory["relheight"] = h
                        PlaceDictory["visible"] = True
                        G_UIElementPlaceArray[uiName][elementName]=PlaceDictory
                    else:
                        Control.place(x=x,y=y,width=w,height=h)
                        PlaceDictory = {}
                        PlaceDictory["type"] = "place"
                        PlaceDictory["x"] = x
                        PlaceDictory["y"] = y
                        PlaceDictory["width"] = w
                        PlaceDictory["height"] = h
                        PlaceDictory["visible"] = True
                        G_UIElementPlaceArray[uiName][elementName]=PlaceDictory
def DoCanvasRecord(drawCanvas,type,x,y,x2,y2,fillcolor,outlinecolor,fillwidth,dash1=0,dash2=0,newImage=None,text='',textFont = None,ShapeTag=''):
    """画板动作处理函数"""
    if  drawCanvas != None:
        if type == 'line' or type == 'pen'  :
            if  dash1 > 0 :
                drawCanvas.create_line(x, y, x2, y2, fill=fillcolor,dash=(dash1,dash2),width = fillwidth,tag=ShapeTag)
            else:
                drawCanvas.create_line(x, y, x2, y2,fill=fillcolor, width = fillwidth,tag=ShapeTag)
        elif type == 'arrow':
            if  dash1 > 0 :
                drawCanvas.create_line(x, y, x2, y2, arrow=tkinter.LAST,fill=fillcolor,dash=(dash1,dash2),width = fillwidth,tag=ShapeTag)
            else:
                drawCanvas.create_line(x, y, x2, y2,arrow=tkinter.LAST,fill=fillcolor, width = fillwidth,tag=ShapeTag)
        elif type == 'triangle':
            width = x2 - x
            height = y2 - y
            points = [
                x,
                y + height,
                x + int(width/2),
                y ,
                x + width,
                y + height,
                x,
                y + height,]
            drawCanvas.create_polygon(
                points,
                fill=fillcolor,
                outline=outlinecolor, 
                width= fillwidth,
                tag=ShapeTag)
        elif type == 'diamond':
            width = x2 - x
            height = y2 - y
            points = [
                x,
                y + int(height/2),
                x + int(width/2),
                y ,
                x + width,
                y + int(height/2),
                x + int(width/2),
                y + height,]
            drawCanvas.create_polygon(
                points,
                fill=fillcolor,
                outline=outlinecolor, 
                width= fillwidth,
                tag=ShapeTag)
        elif type == 'rect':
            if  dash1 > 0 :
                drawCanvas.create_rectangle(x, y, x2, y2, fill=fillcolor,outline=outlinecolor,dash=(dash1,dash2),width = fillwidth,tag=ShapeTag)
            else:
                drawCanvas.create_rectangle(x, y, x2, y2,fill=fillcolor,outline=outlinecolor, width = fillwidth,tag=ShapeTag)
        elif type == 'circle':
            if  dash1 > 0 :
                drawCanvas.create_oval(x, y, x2, y2, fill=fillcolor,outline=outlinecolor,dash=(dash1,dash2),width = fillwidth,tag=ShapeTag)
            else:
                drawCanvas.create_oval(x, y, x2, y2,fill=fillcolor,outline=outlinecolor, width = fillwidth,tag=ShapeTag)
        elif type == 'cylinder':
            width = x2 - x
            height = y2 - y
            OvalHeight = height * 0.2
            OvalHeight_Half = height * 0.1
            if  dash1 > 0 :
                drawCanvas.create_oval(x,y2-OvalHeight,x2,y2,fill=fillcolor,outline=outlinecolor,dash=(dash1,dash2),width = fillwidth,tag=ShapeTag)
                drawCanvas.create_rectangle(x,y+OvalHeight_Half,x2,y2-OvalHeight_Half,fill=fillcolor,width=0,tag=ShapeTag)
                drawCanvas.create_oval(x,y,x2,y+OvalHeight,fill=fillcolor,outline=outlinecolor,dash=(dash1,dash2),width = fillwidth,tag=ShapeTag)
                drawCanvas.create_line(x,y+OvalHeight_Half,x,y2-OvalHeight_Half,fill=fillcolor,dash=(dash1,dash2),width = fillwidth,tag=ShapeTag)
                drawCanvas.create_line(x2,y+OvalHeight_Half,x2,y2-OvalHeight_Half,fill=fillcolor,dash=(dash1,dash2),width = fillwidth,tag=ShapeTag)
            else:
                drawCanvas.create_oval(x,y2-OvalHeight,x2,y2,fill=fillcolor,outline=outlinecolor,width = fillwidth,tag=ShapeTag)
                drawCanvas.create_rectangle(x,y+OvalHeight_Half,x2,y2-OvalHeight_Half,fill=fillcolor,width=0,tag=ShapeTag)
                drawCanvas.create_oval(x,y,x2,y+OvalHeight,fill=fillcolor,outline=outlinecolor,width = fillwidth,tag=ShapeTag)
                drawCanvas.create_line(x,y+OvalHeight_Half,x,y2-OvalHeight_Half,fill=fillcolor,width = fillwidth,tag=ShapeTag)
                drawCanvas.create_line(x2,y+OvalHeight_Half,x2,y2-OvalHeight_Half,fill=fillcolor,width = fillwidth,tag=ShapeTag)
        elif type == 'star':
            center_x = (x + x2)/2
            center_y = (y + y2)/2
            rx = (x2 - x)/2
            ry = (y2 - y)/2
            points = [
                center_x - int(rx * math.sin(2 * math.pi / 5)),
                center_y - int(ry * math.cos(2 * math.pi / 5)),
                center_x + int(rx * math.sin(2 * math.pi / 5)),
                center_y - int(ry * math.cos(2 * math.pi / 5)),
                center_x - int(rx * math.sin(math.pi / 5)),
                center_y + int(ry * math.cos(math.pi / 5)),
                center_x,
                center_y - ry,
                center_x + int(rx * math.sin(math.pi / 5)),
                center_y + int(ry * math.cos(math.pi / 5)),
                ]
            drawCanvas.create_polygon(
                points,
                fill=fillcolor,
                outline=outlinecolor, 
                width= fillwidth,
                tag=ShapeTag)
        elif type == 'earsor':
            drawCanvas.create_rectangle(x, y, x2, y2,fill=fillcolor, width = 0,tag=ShapeTag) 
        elif type == 'text':
            drawCanvas.create_text(x, y,fill=fillcolor,text=text,font = textFont,anchor='nw',tag=ShapeTag)
        elif type == 'button':
            center_x = (x + x2)/2
            center_y = (y + y2)/2
            if newImage:
                drawCanvas.create_image(x, y,image=newImage,anchor='nw',tag=ShapeTag)
            else:
                oval_rx = 20
                if  dash1 > 0 :
                    drawCanvas.create_oval(x,y,x+2*oval_rx,y2,fill=fillcolor,outline=outlinecolor,dash=(dash1,dash2),width = fillwidth,tag=ShapeTag)
                    drawCanvas.create_oval(x2-2*oval_rx,y,x2,y2,fill=fillcolor,outline=outlinecolor,dash=(dash1,dash2),width = fillwidth,tag=ShapeTag)
                    drawCanvas.create_rectangle(x+oval_rx, y, x2-oval_rx, y2,fill=fillcolor, width = 0,tag=ShapeTag)
                    drawCanvas.create_line(x+oval_rx,y,x2-oval_rx,y,fill=outlinecolor,dash=(dash1,dash2),width = fillwidth,tag='cav')
                    drawCanvas.create_line(x+oval_rx,y2,x2-oval_rx,y2,fill=outlinecolor,dash=(dash1,dash2),width = fillwidth,tag='cav')
                else:
                    drawCanvas.create_oval(x,y,x+2*oval_rx,y2,fill=fillcolor,outline=outlinecolor,width = fillwidth,tag=ShapeTag)
                    drawCanvas.create_oval(x2-2*oval_rx,y,x2,y2,fill=fillcolor,outline=outlinecolor,width = fillwidth,tag=ShapeTag)
                    drawCanvas.create_rectangle(x+oval_rx, y, x2-oval_rx, y2,fill=fillcolor, width = 0,tag=ShapeTag)
                    drawCanvas.create_line(x+oval_rx,y,x2-oval_rx,y,fill=outlinecolor,width = fillwidth,tag='cav')
                    drawCanvas.create_line(x+oval_rx,y2,x2-oval_rx,y2,fill=outlinecolor,width = fillwidth,tag='cav')
            if len(text) > 0:
                drawCanvas.create_text(center_x, center_y,fill=outlinecolor,text=text,anchor='center',tag=ShapeTag+"_text")
        elif type == 'image':
            drawCanvas.create_image(x, y,image=newImage,anchor='nw',tag=ShapeTag)
def LoadCanvasRecord(uiName):
    """读取画板动作记录"""
    drawCanvasName = None
    drawCanvas = None
    canvasFile = os.getcwd() + "\\Resources\\" + uiName + ".cav"
    if os.path.exists(canvasFile) == True:
        f = open(canvasFile,encoding='utf-8')
        line ="" 
        while True:
            line = f.readline()
            if not line:
                break
            text = line.strip()
            if not text:
                continue
            if text.find('Canvas:') >= 0:
                splitArray = text.split(':')
                drawCanvasName = splitArray[1].strip()
                drawCanvas = GetElement(uiName,drawCanvasName)
                G_CanvasShapeDictory[uiName][drawCanvasName] = {}
                G_CanvasFontDictory[uiName][drawCanvasName] = []
                G_CanvasImageDictory[uiName][drawCanvasName] = []
                G_CanvasPointDictory[uiName][drawCanvasName] = {}
                G_CanvasEventDictory[uiName][drawCanvasName] = {}
                continue
            elif text.find(',') >= 0:
                if drawCanvas != None:
                    splitArray = text.split(',')
                    ShapeType = splitArray[0]
                    if ShapeType == 'image':
                        x1 = round(float(splitArray[1]))
                        y1 = round(float(splitArray[2]))
                        x2 = round(float(splitArray[3]))
                        y2 = round(float(splitArray[4]))
                        w = x2 - x1
                        h = y2 - y1
                        fill = splitArray[5]
                        outline = splitArray[6]
                        width = int(splitArray[7])
                        dashx = int(splitArray[8])
                        dashy = int(splitArray[9])
                        imagefile = splitArray[10]
                        newImage = None
                        text = ''
                        textFont = None
                        ShapeTag = ''
                        if len(splitArray) > 12:
                            ShapeTag = splitArray[11]
                        for ImageInfo in G_CanvasImageDictory[uiName][drawCanvasName]:
                            if ImageInfo[0] == imagefile and ImageInfo[2] == w and ImageInfo[3] == h :
                                newImage = ImageInfo[1]
                                continue
                        if newImage == None:
                            projPath = os.getcwd() 
                            projPath = projPath.replace('/','\\')
                            resourPath = projPath+"\\Resources\\"+imagefile
                            if os.path.exists(resourPath) == True:
                                try:
                                    imageRGBA = Image.open(resourPath).convert('RGBA')
                                    resizeImage = imageRGBA.resize((w, h),Image.ANTIALIAS)
                                    newImage = ImageTk.PhotoImage(resizeImage)
                                except:
                                    return 
                            G_CanvasImageDictory[uiName][drawCanvasName].append([imagefile,newImage,w,h])
                        G_CanvasShapeDictory[uiName][drawCanvasName][ShapeTag]=[ShapeType,x1,y1,x2,y2,newImage]
                    elif ShapeType == 'text':
                        x1 = round(float(splitArray[1]))
                        y1 = round(float(splitArray[2]))
                        x2 = round(float(splitArray[3]))
                        y2 = round(float(splitArray[4]))
                        w = x2 - x1
                        h = y2 - y1
                        fill = splitArray[5]
                        outline = splitArray[6]
                        width = int(splitArray[7])
                        dashx = int(splitArray[8])
                        dashy = int(splitArray[9])
                        imagefile = ''
                        ShapeTag = ''
                        text = splitArray[10]
                        familytext = splitArray[11]
                        sizetext = splitArray[12]
                        weighttext = splitArray[13]
                        slanttext = splitArray[14]
                        underlinetext = splitArray[15]
                        overstriketext = splitArray[16]
                        textFont = tkinter.font.Font(family=familytext, size=sizetext,weight=weighttext,slant=slanttext,underline=underlinetext,overstrike=overstriketext)
                        if len(splitArray) > 18:
                            ShapeTag = splitArray[17]
                            G_CanvasShapeDictory[uiName][drawCanvasName][ShapeTag]=[ShapeType,x1,y1,x2,y2,text,textFont,fill]
                        #字体
                        fontFind = False
                        for fontInfo in G_CanvasFontDictory[uiName][drawCanvasName]:
                            if fontInfo[0] == familytext and fontInfo[1] == sizetext and fontInfo[2] == weighttext and fontInfo[3] == slanttext and fontInfo[4] == underlinetext and fontInfo[5] == overstriketext:
                                fontFind = True
                                continue
                        if fontFind == False:
                            G_CanvasFontDictory[uiName][drawCanvasName].append([textFont,familytext,sizetext,weighttext,slanttext,underlinetext,overstriketext])
                    elif ShapeType == 'button':
                        x1 = round(float(splitArray[1]))
                        y1 = round(float(splitArray[2]))
                        x2 = round(float(splitArray[3]))
                        y2 = round(float(splitArray[4]))
                        w = x2 - x1
                        h = y2 - y1
                        fill = splitArray[5]
                        outline = splitArray[6]
                        width = int(splitArray[7])
                        dashx = int(splitArray[8])
                        dashy = int(splitArray[9])
                        ShapeTag = ''
                        text = splitArray[10]
                        familytext = splitArray[11]
                        sizetext = splitArray[12]
                        weighttext = splitArray[13]
                        slanttext = splitArray[14]
                        underlinetext = splitArray[15]
                        overstriketext = splitArray[16]
                        textFont = tkinter.font.Font(family=familytext, size=sizetext,weight=weighttext,slant=slanttext,underline=underlinetext,overstrike=overstriketext)
                        #字体
                        fontFind = False
                        for fontInfo in G_CanvasFontDictory[uiName][drawCanvasName]:
                            if fontInfo[0] == familytext and fontInfo[1] == sizetext and fontInfo[2] == weighttext and fontInfo[3] == slanttext and fontInfo[4] == underlinetext and fontInfo[5] == overstriketext:
                                fontFind = True
                                continue
                        if fontFind == False:
                            G_CanvasFontDictory[uiName][drawCanvasName].append([textFont,familytext,sizetext,weighttext,slanttext,underlinetext,overstriketext])
                        imagefile = splitArray[17]
                        newImage = None
                        if imagefile != "":
                            for ImageInfo in G_CanvasImageDictory[uiName][drawCanvasName]:
                                if ImageInfo[0] == imagefile and ImageInfo[2] == w and ImageInfo[3] == h :
                                    newImage = ImageInfo[1]
                                    continue
                            if newImage == None:
                                projPath = os.getcwd() 
                                projPath = projPath.replace('/','\\')
                                resourPath = projPath+"\\Resources\\"+imagefile
                                if os.path.exists(resourPath) == True:
                                    try:
                                        imageRGBA = Image.open(resourPath).convert('RGBA')
                                        resizeImage = imageRGBA.resize((w, h),Image.ANTIALIAS)
                                        newImage = ImageTk.PhotoImage(resizeImage)
                                    except:
                                        return 
                                G_CanvasImageDictory[uiName][drawCanvasName].append([imagefile,newImage,w,h])
                        if len(splitArray) > 19:
                            ShapeTag = splitArray[19]
                            G_CanvasShapeDictory[uiName][drawCanvasName][ShapeTag]=[ShapeType,x1,y1,x2,y2,text,textFont,fill,outline,width,dashx,dashy,newImage]
                    elif ShapeType == 'point':
                        x1 = round(float(splitArray[1]))
                        y1 = round(float(splitArray[2]))
                        x2 = round(float(splitArray[3]))
                        y2 = round(float(splitArray[4]))
                        w  = x2 - x1
                        h  = y2 - y1
                        fill = splitArray[5]
                        outline = splitArray[6]
                        width = int(splitArray[7])
                        dashx = int(splitArray[8])
                        dashy = int(splitArray[9])
                        parentShapeTag = splitArray[10]
                        imagefile = ''
                        newImage = None
                        text = ''
                        textFont = None
                        ShapeTag = ''
                        centerX = (x1 + x2)//2
                        centerY = (y1 + y2)//2
                        if len(splitArray) > 12:
                            ShapeTag = splitArray[11]
                            G_CanvasShapeDictory[uiName][drawCanvasName][ShapeTag]=(ShapeType,x1,y1,x2,y2)
                        if parentShapeTag not in G_CanvasPointDictory[uiName][drawCanvasName]:
                            G_CanvasPointDictory[uiName][drawCanvasName][parentShapeTag] = {}
                        G_CanvasPointDictory[uiName][drawCanvasName][parentShapeTag][ShapeTag] = [centerX,centerY]
                    elif ShapeType == 'SetShapeRect':
                        ShapeTag = splitArray[1]
                        EventName = splitArray[2]
                        TargetShapeTag = splitArray[3]
                        x = round(float(splitArray[4]))
                        y = round(float(splitArray[5]))
                        w = round(float(splitArray[6]))
                        h = round(float(splitArray[7]))   
                        actionInfo = ["SetShapeRect",TargetShapeTag,x,y,w,h]
                        if ShapeTag not in G_CanvasEventDictory[uiName][drawCanvasName]:
                            G_CanvasEventDictory[uiName][drawCanvasName][ShapeTag] = {}
                        if EventName not in G_CanvasEventDictory[uiName][drawCanvasName][ShapeTag]:
                            G_CanvasEventDictory[uiName][drawCanvasName][ShapeTag][EventName] = []
                        G_CanvasEventDictory[uiName][drawCanvasName][ShapeTag][EventName].append(actionInfo)
                    elif ShapeType == 'SetFillColor':
                        ShapeTag = splitArray[1]
                        EventName = splitArray[2]
                        TargetShapeTag = splitArray[3]
                        Color = splitArray[4]   
                        actionInfo = ["SetFillColor",TargetShapeTag,Color]
                        if ShapeTag not in G_CanvasEventDictory[uiName][drawCanvasName]:
                            G_CanvasEventDictory[uiName][drawCanvasName][ShapeTag] = {}
                        if EventName not in G_CanvasEventDictory[uiName][drawCanvasName][ShapeTag]:
                            G_CanvasEventDictory[uiName][drawCanvasName][ShapeTag][EventName] = []
                        G_CanvasEventDictory[uiName][drawCanvasName][ShapeTag][EventName].append(actionInfo)
                    elif ShapeType == 'SetOutlineColor':
                        ShapeTag = splitArray[1]
                        EventName = splitArray[2]
                        TargetShapeTag = splitArray[3]
                        Color = splitArray[4]   
                        actionInfo = ["SetOutlineColor",TargetShapeTag,Color]
                        if ShapeTag not in G_CanvasEventDictory[uiName][drawCanvasName]:
                            G_CanvasEventDictory[uiName][drawCanvasName][ShapeTag] = {}
                        if EventName not in G_CanvasEventDictory[uiName][drawCanvasName][ShapeTag]:
                            G_CanvasEventDictory[uiName][drawCanvasName][ShapeTag][EventName] = []
                        G_CanvasEventDictory[uiName][drawCanvasName][ShapeTag][EventName].append(actionInfo)
                    elif ShapeType == 'ChangeImage':
                        ShapeTag = splitArray[1]
                        EventName = splitArray[2]
                        TargetShapeTag = splitArray[3]
                        ImageFile = splitArray[4]
                        actionInfo = ["ChangeImage",TargetShapeTag,ImageFile]
                        if ShapeTag not in G_CanvasEventDictory[uiName][drawCanvasName]:
                            G_CanvasEventDictory[uiName][drawCanvasName][ShapeTag] = {}
                        if EventName not in G_CanvasEventDictory[uiName][drawCanvasName][ShapeTag]:
                            G_CanvasEventDictory[uiName][drawCanvasName][ShapeTag][EventName] = []
                        G_CanvasEventDictory[uiName][drawCanvasName][ShapeTag][EventName].append(actionInfo)
                    elif ShapeType == 'ChangeText':
                        ShapeTag = splitArray[1]
                        EventName = splitArray[2]
                        TargetShapeTag = splitArray[3]
                        Text = splitArray[4]
                        TextColor = splitArray[5]
                        actionInfo = ["ChangeText",TargetShapeTag,Text,TextColor]
                        if ShapeTag not in G_CanvasEventDictory[uiName][drawCanvasName]:
                            G_CanvasEventDictory[uiName][drawCanvasName][ShapeTag] = {}
                        if EventName not in G_CanvasEventDictory[uiName][drawCanvasName][ShapeTag]:
                            G_CanvasEventDictory[uiName][drawCanvasName][ShapeTag][EventName] = []
                        G_CanvasEventDictory[uiName][drawCanvasName][ShapeTag][EventName].append(actionInfo)
                    else:
                        if len(splitArray) > 11:
                            x1 = round(float(splitArray[1]))
                            y1 = round(float(splitArray[2]))
                            x2 = round(float(splitArray[3]))
                            y2 = round(float(splitArray[4]))
                            w  = x2 - x1
                            h  = y2 - y1
                            fill = splitArray[5]
                            outline = splitArray[6]
                            width = int(splitArray[7])
                            dashx = int(splitArray[8])
                            dashy = int(splitArray[9])
                            imagefile = ''
                            newImage = None
                            text = ''
                            textFont = None
                            ShapeTag = splitArray[10]
                            G_CanvasShapeDictory[uiName][drawCanvasName][ShapeTag]=[ShapeType,x1,y1,x2,y2,fill,outline,width,dashx,dashy]
                    DoCanvasRecord(drawCanvas,ShapeType,x1,y1,x2,y2,fill,outline,width,dashx,dashy,newImage,text,textFont,ShapeTag)
                continue
        f.close()  
        def checkPtInRect(x,y,left,right,top,bottom):
            if x < left:return 0
            if x > right:return 0
            if y < top:return 0
            if y > bottom:return 0
            return 1
        def Shape_MouseEvent(event,uiName,canvasName,shapeTag,eventName):
            if eventName == 'MouseLeave':
                x1 = G_CanvasShapeDictory[uiName][canvasName][shapeTag][1]
                y1 = G_CanvasShapeDictory[uiName][canvasName][shapeTag][2]
                x2 = G_CanvasShapeDictory[uiName][canvasName][shapeTag][3]
                y2 = G_CanvasShapeDictory[uiName][canvasName][shapeTag][4]
                borderwidth = 0
                if G_CanvasShapeDictory[uiName][canvasName][shapeTag][0] == 'button':
                    borderwidth = 1 + G_CanvasShapeDictory[uiName][canvasName][shapeTag][9]
                if checkPtInRect(event.x,event.y,x1+borderwidth,x2-borderwidth,y1+borderwidth,y2-borderwidth) == 1:
                    return 
            for actionInfo in G_CanvasEventDictory[uiName][canvasName][shapeTag][eventName]:
                if actionInfo[0] == "SetShapeRect":
                    SetShapeRect(uiName ,canvasName,actionInfo[1],actionInfo[2],actionInfo[3],actionInfo[4],actionInfo[5])
                elif actionInfo[0] == "SetFillColor":
                    SetShapeFillColor(uiName ,canvasName,actionInfo[1],actionInfo[2])
                elif actionInfo[0] == "SetOutlineColor":
                    SetShapeOutlineColor(uiName ,canvasName,actionInfo[1],actionInfo[2])
                elif actionInfo[0] == "ChangeImage":
                    SetShapeImage(uiName ,canvasName,actionInfo[1],actionInfo[2])
                elif actionInfo[0] == "ChangeText":
                    SetShapeText(uiName ,canvasName,actionInfo[1],actionInfo[2],actionInfo[3])
        for ShapeTag in G_CanvasEventDictory[uiName][drawCanvasName]:
            for EventName in G_CanvasEventDictory[uiName][drawCanvasName][ShapeTag]:
                if EventName == "MouseEnter":
                    drawCanvas.tag_bind(ShapeTag, "<Any-Enter>",EventFunction_Adaptor(Shape_MouseEvent,uiName = uiName,canvasName = drawCanvasName,shapeTag=ShapeTag,eventName="MouseEnter"))
                    if G_CanvasShapeDictory[uiName][drawCanvasName][ShapeTag][0] == 'button':
                        TextTag = ShapeTag+"_text"
                        drawCanvas.tag_bind(TextTag, "<Any-Enter>",EventFunction_Adaptor(Shape_MouseEvent,uiName = uiName,canvasName = drawCanvasName,shapeTag=ShapeTag,eventName="MouseEnter"))
                elif EventName == "MouseLeave":
                    drawCanvas.tag_bind(ShapeTag, "<Any-Leave>",EventFunction_Adaptor(Shape_MouseEvent,uiName = uiName,canvasName = drawCanvasName,shapeTag=ShapeTag,eventName="MouseLeave"))
                    if G_CanvasShapeDictory[uiName][drawCanvasName][ShapeTag][0] == 'button':
                        TextTag = ShapeTag+"_text"
                        drawCanvas.tag_bind(TextTag, "<Any-Leave>",EventFunction_Adaptor(Shape_MouseEvent,uiName = uiName,canvasName = drawCanvasName,shapeTag=ShapeTag,eventName="MouseLeave"))
                elif EventName == "ButtonDown":
                    drawCanvas.tag_bind(ShapeTag, "<Button-1>",EventFunction_Adaptor(Shape_MouseEvent,uiName = uiName,canvasName = drawCanvasName,shapeTag=ShapeTag,eventName="ButtonDown"))
                    if G_CanvasShapeDictory[uiName][drawCanvasName][ShapeTag][0] == 'button':
                        TextTag = ShapeTag+"_text"
                        drawCanvas.tag_bind(TextTag, "<Button-1>",EventFunction_Adaptor(Shape_MouseEvent,uiName = uiName,canvasName = drawCanvasName,shapeTag=ShapeTag,eventName="ButtonDown"))
                elif EventName == "ButtonUp":
                    drawCanvas.tag_bind(ShapeTag, "<ButtonRelease-1>",EventFunction_Adaptor(Shape_MouseEvent,uiName = uiName,canvasName = drawCanvasName,shapeTag=ShapeTag,eventName="ButtonUp"))
                    if G_CanvasShapeDictory[uiName][drawCanvasName][ShapeTag][0] == 'button':
                        TextTag = ShapeTag+"_text"
                        drawCanvas.tag_bind(TextTag, "<ButtonRelease-1>",EventFunction_Adaptor(Shape_MouseEvent,uiName = uiName,canvasName = drawCanvasName,shapeTag=ShapeTag,eventName="ButtonUp"))
                elif EventName == "DoubleClick":
                    drawCanvas.tag_bind(ShapeTag, "<Double-1>",EventFunction_Adaptor(Shape_MouseEvent,uiName = uiName,canvasName = drawCanvasName,shapeTag=ShapeTag,eventName="DoubleClick"))
                    if G_CanvasShapeDictory[uiName][drawCanvasName][ShapeTag][0] == 'button':
                        TextTag = ShapeTag+"_text"
                        drawCanvas.tag_bind(TextTag, "<Double-1>",EventFunction_Adaptor(Shape_MouseEvent,uiName = uiName,canvasName = drawCanvasName,shapeTag=ShapeTag,eventName="DoubleClick"))
def GetShapePoint(uiName,drawCanvasName,shapeTag,pointTag):
    """获取绑定点位置"""
    if drawCanvasName in G_CanvasPointDictory[uiName]:
       if shapeTag in G_CanvasShapeDictory[uiName][drawCanvasName]:
           if shapeTag in G_CanvasPointDictory[uiName][drawCanvasName]:
               if pointTag in G_CanvasPointDictory[uiName][drawCanvasName][shapeTag]:
                   shapeX = G_CanvasShapeDictory[uiName][drawCanvasName][shapeTag][1] + G_CanvasPointDictory[uiName][drawCanvasName][shapeTag][pointTag][0]
                   shapeY = G_CanvasShapeDictory[uiName][drawCanvasName][shapeTag][2] + G_CanvasPointDictory[uiName][drawCanvasName][shapeTag][pointTag][1]
                   return (shapeX,shapeY)
    return None
def SetShapePosition(uiName,drawCanvasName,shapeTag,x1,y1,x2,y2):
    """设置画布图形位置与大小"""
    if drawCanvasName in G_CanvasPointDictory[uiName]:
       if shapeTag in G_CanvasShapeDictory[uiName][drawCanvasName]:
           drawCanvas = GetElement(uiName,drawCanvasName)
           drawCanvas.delete(shapeTag)
           ShapeType = G_CanvasShapeDictory[uiName][drawCanvasName][shapeTag][0]
           G_CanvasShapeDictory[uiName][drawCanvasName][shapeTag][1] = x1
           G_CanvasShapeDictory[uiName][drawCanvasName][shapeTag][2] = y1
           G_CanvasShapeDictory[uiName][drawCanvasName][shapeTag][3] = x2
           G_CanvasShapeDictory[uiName][drawCanvasName][shapeTag][4] = y2
           if ShapeType == 'text':
               text = G_CanvasShapeDictory[uiName][drawCanvasName][shapeTag][5]
               textFont = G_CanvasShapeDictory[uiName][drawCanvasName][shapeTag][6]
               textcolor = G_CanvasShapeDictory[uiName][drawCanvasName][shapeTag][7]
               drawCanvas.create_text(x1, y1,fill=textcolor,text=text,font = textFont,anchor='nw',tag=shapeTag)
           elif ShapeType == 'image':
               theImage = G_CanvasShapeDictory[uiName][drawCanvasName][shapeTag][5]
               drawCanvas.create_image(x1, y1,image=theImage,anchor='nw',tag=shapeTag)
           else:
               fill = G_CanvasShapeDictory[uiName][drawCanvasName][shapeTag][5]
               outline = G_CanvasShapeDictory[uiName][drawCanvasName][shapeTag][6]
               width = G_CanvasShapeDictory[uiName][drawCanvasName][shapeTag][7]
               dashx = G_CanvasShapeDictory[uiName][drawCanvasName][shapeTag][8]
               dashy = G_CanvasShapeDictory[uiName][drawCanvasName][shapeTag][9]
               DoCanvasRecord(drawCanvas,ShapeType,x1,y1,x2,y2,fill,outline,width,dashx,dashy,None,'','#FFFFFF',shapeTag)
    return None
def SetShapeRect(uiName,canvasName,shapeTag,x1,y1,x2,y2):
    drawCanvas = GetElement(uiName,canvasName)
    drawCanvas.coords(shapeTag, x1,y1,x2,y2) 
    G_CanvasShapeDictory[uiName][canvasName][shapeTag][1] = x1
    G_CanvasShapeDictory[uiName][canvasName][shapeTag][2] = y1
    G_CanvasShapeDictory[uiName][canvasName][shapeTag][3] = x2
    G_CanvasShapeDictory[uiName][canvasName][shapeTag][4] = y2
def SetShapeFillColor(uiName,canvasName,shapeTag,color):
    if G_CanvasShapeDictory[uiName][canvasName][shapeTag][0] == 'button':
        if G_CanvasShapeDictory[uiName][canvasName][shapeTag][-1] == None:
            drawCanvas = GetElement(uiName,canvasName)
            drawCanvas.itemconfig(shapeTag, fill=color)
    else:
        drawCanvas = GetElement(uiName,canvasName)
        drawCanvas.itemconfig(shapeTag, fill=color)
def SetShapeOutlineColor(uiName,canvasName,shapeTag,color):
    if G_CanvasShapeDictory[uiName][canvasName][shapeTag][0] == 'button':
        if G_CanvasShapeDictory[uiName][canvasName][shapeTag][-1] == None:
            drawCanvas = GetElement(uiName,canvasName)
            drawCanvas.itemconfig(shapeTag, outline=color)
    else:
        drawCanvas = GetElement(uiName,canvasName)
        drawCanvas.itemconfig(shapeTag, outline=color)
def SetShapeImage(uiName,canvasName,shapeTag,imageFile):
    drawCanvas = GetElement(uiName,canvasName)
    x1 = G_CanvasShapeDictory[uiName][canvasName][shapeTag][1]
    y1 = G_CanvasShapeDictory[uiName][canvasName][shapeTag][2]
    x2 = G_CanvasShapeDictory[uiName][canvasName][shapeTag][3]
    y2 = G_CanvasShapeDictory[uiName][canvasName][shapeTag][4]
    w = x2 - x1
    h = y2 - y1
    newImage = None
    for ImageInfo in G_CanvasImageDictory[uiName][canvasName]:
        if ImageInfo[0] == imageFile and ImageInfo[2] == w and ImageInfo[3] == h :
            newImage = ImageInfo[1]
            continue
    if newImage == None:
        projPath = os.getcwd() 
        projPath = projPath.replace('/','\\')
        resourPath = projPath+"\\Resources\\"+imageFile
        if os.path.exists(resourPath) == True:
            try:
                imageRGBA = Image.open(resourPath).convert('RGBA')
                resizeImage = imageRGBA.resize((w, h),Image.ANTIALIAS)
                newImage = ImageTk.PhotoImage(resizeImage)
            except:
                return 
        G_CanvasImageDictory[uiName][canvasName].append([imageFile,newImage,w,h])
    drawCanvas.itemconfig(shapeTag, image=newImage) 
def SetShapeText(uiName,drawCanvasName,shapeTag,text,fillcolor = None):
    """设置画布文字及颜色"""
    if drawCanvasName in G_CanvasPointDictory[uiName]:
        if shapeTag in G_CanvasShapeDictory[uiName][drawCanvasName]:
            drawCanvas = GetElement(uiName,drawCanvasName)
            drawCanvas.delete(shapeTag)
            x1 = G_CanvasShapeDictory[uiName][drawCanvasName][shapeTag][1]
            y1 = G_CanvasShapeDictory[uiName][drawCanvasName][shapeTag][2]
            x2 = G_CanvasShapeDictory[uiName][drawCanvasName][shapeTag][3]
            y2 = G_CanvasShapeDictory[uiName][drawCanvasName][shapeTag][4]
            G_CanvasShapeDictory[uiName][drawCanvasName][shapeTag][5] = text
            textFont = G_CanvasShapeDictory[uiName][drawCanvasName][shapeTag][6]
            textcolor = G_CanvasShapeDictory[uiName][drawCanvasName][shapeTag][7]
            if fillcolor:
                textcolor = fillcolor
            drawCanvas.create_text(x1, y1,fill=textcolor,text=text,font = textFont,anchor='nw',tag=shapeTag)
def DeleteShape(uiName,drawCanvasName,shapeTag):
    """删除画布中的画形"""
    if drawCanvasName in G_CanvasPointDictory[uiName]:
        if shapeTag in G_CanvasShapeDictory[uiName][drawCanvasName]:
            drawCanvas = GetElement(uiName,drawCanvasName)
            drawCanvas.delete(shapeTag)
            G_CanvasShapeDictory[uiName][drawCanvasName].pop(shapeTag)
class WindowDraggable():
    """定义一个可拖拽移动和拖拽边框大小的窗口类。"""
    def __init__(self,widget,bordersize = 6,bordercolor = '#444444'):
        self.widget = widget
        widget.bind('<Enter>',self.Enter)
        widget.bind('<Motion>',self.Motion)
        widget.bind('<Leave>',self.Leave)
        widget.bind('<ButtonPress-1>',self.StartDrag)
        widget.bind('<ButtonRelease-1>',self.StopDrag)
        widget.bind('<B1-Motion>',self.MoveDragPos)
        self.bordersize = bordersize
        self.bordercolor = bordercolor
        self.top_drag = None
        self.left_drag = None
        self.right_drag = None
        self.bottom_drag = None
        self.topleft_drag = None
        self.bottomleft_drag = None
        self.topright_drag = None
        self.bottomright_drag = None
        widget.after(10, lambda: self.ShowWindowIcoToBar(widget))
    def ShowWindowIcoToBar(self,widget):
        GWL_EXSTYLE=-20
        WS_EX_APPWINDOW=0x00040000
        WS_EX_TOOLWINDOW=0x00000080
        from ctypes import windll
        hwnd = windll.user32.GetParent(widget.winfo_id())
        style = windll.user32.GetWindowLongPtrW(hwnd, GWL_EXSTYLE)
        style = style & ~WS_EX_TOOLWINDOW
        style = style | WS_EX_APPWINDOW
        res = windll.user32.SetWindowLongPtrW(hwnd, GWL_EXSTYLE, style)
        widget.wm_withdraw()
        widget.after(10, lambda: widget.wm_deiconify())
    def Enter(self,event):
        if self.widget == event.widget or event.widget.winfo_class() =="Canvas":
            formx = self.widget.winfo_x() 
            formy = self.widget.winfo_y() 
            formw = self.widget.winfo_width() 
            formh = self.widget.winfo_height()
            x = event.x_root - formx
            y = event.y_root - formy
    def Motion(self,event):
        if self.widget == event.widget or event.widget.winfo_class() =="Canvas":
            formx = self.widget.winfo_x() 
            formy = self.widget.winfo_y() 
            formw = self.widget.winfo_width() 
            formh = self.widget.winfo_height()
            x = event.x_root - formx
            y = event.y_root - formy
            if ((x >= 0) and (x <= self.bordersize) and (y >= 0) and (y <= self.bordersize)):
                if self.top_drag == None:
                    self.top_drag = tkinter.Label(self.widget)
                self.top_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.top_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.top_drag.bind('<B1-Motion>',self.MoveDragSize_TL)
                self.top_drag.bind('<Leave>',self.LeaveDragBorder_TL)
                if self.left_drag == None:
                    self.left_drag = tkinter.Label(self.widget)
                self.left_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.left_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.left_drag.bind('<B1-Motion>',self.MoveDragSize_TL)
                self.left_drag.bind('<Leave>',self.LeaveDragBorder_TL)
                self.top_drag.place(x = 0,y = 0,width = formw,height = self.bordersize)
                self.top_drag.configure(bg = self.bordercolor)
                self.left_drag.place(x = 0,y = 0,width = self.bordersize,height = formh)
                self.left_drag.configure(bg = self.bordercolor)
            if ((y >= 0) and (y <= self.bordersize)):
                if self.top_drag == None:
                    self.top_drag = tkinter.Label(self.widget)
                self.top_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.top_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.top_drag.bind('<B1-Motion>',self.MoveDragSize_V1)
                self.top_drag.bind('<Motion>',self.MotionDragBorder)
                self.top_drag.bind('<Leave>',self.LeaveDragBorder)
                self.top_drag.place(x = 0,y = 0,width = formw,height = self.bordersize)
                self.top_drag.configure(bg = self.bordercolor)
            if ((y >= (formh - self.bordersize)) and (y <= formh)):
                if self.bottom_drag == None:
                    self.bottom_drag = tkinter.Label(self.widget)
                self.bottom_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.bottom_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.bottom_drag.bind('<B1-Motion>',self.MoveDragSize_V2)
                self.bottom_drag.bind('<Motion>',self.MotionDragBorder)
                self.bottom_drag.bind('<Leave>',self.LeaveDragBorder)
                self.bottom_drag.place(x = 0,y = (formh - self.bordersize),width = formw,height = self.bordersize)
                self.bottom_drag.configure(bg = self.bordercolor)
            if ((x >= 0 ) and (x <= self.bordersize)):
                if self.left_drag == None:
                    self.left_drag = tkinter.Label(self.widget)
                self.left_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.left_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.left_drag.bind('<B1-Motion>',self.MoveDragSize_H1)
                self.left_drag.bind('<Motion>',self.MotionDragBorder)
                self.left_drag.bind('<Leave>',self.LeaveDragBorder)
                self.left_drag.place(x = 0,y = 0,width = self.bordersize,height = formh)
                self.left_drag.configure(bg = self.bordercolor)
            if ((x >= (formw - self.bordersize)) and (x <= formw)):
                if self.right_drag == None:
                    self.right_drag = tkinter.Label(self.widget)
                self.right_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.right_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.right_drag.bind('<B1-Motion>',self.MoveDragSize_H2)
                self.right_drag.bind('<Motion>',self.MotionDragBorder)
                self.right_drag.bind('<Leave>',self.LeaveDragBorder)
                self.right_drag.place(x = (formw - self.bordersize),y = 0,width = self.bordersize,height = formh)
                self.right_drag.configure(bg = self.bordercolor)
    def Leave(self,event):
        if self.widget == event.widget or event.widget.winfo_class() =="Canvas":
            pass
    def StartDrag(self,event):
        self.x = event.x_root
        self.y = event.y_root
    def StopDrag(self,event):
        self.x = None
        self.y = None
        self.widget.configure(cursor='arrow')
    def MoveDragPos(self,event):
        if self.widget == event.widget or event.widget.winfo_class() =="Canvas":
            formx = self.widget.winfo_x() 
            formy = self.widget.winfo_y() 
            formw = self.widget.winfo_width() 
            formh = self.widget.winfo_height()
            x = event.x_root - formx
            y = event.y_root - formy
            deltaX = event.x_root - self.x
            deltaY = event.y_root - self.y
            newX = self.widget.winfo_x() + deltaX
            newY = self.widget.winfo_y() + deltaY
            geoinfo = str('%dx%d+%d+%d'%(self.widget.winfo_width(),self.widget.winfo_height(),newX,newY))
            self.widget.geometry(geoinfo)
            self.x = event.x_root
            self.y = event.y_root
    def MoveDragSize_H1(self,event):
        deltaX = event.x_root - self.x
        formx = self.widget.winfo_x() + deltaX
        newW = self.widget.winfo_width() - deltaX
        geoinfo = str('%dx%d+%d+%d'%(newW,self.widget.winfo_height(),formx,self.widget.winfo_y()))
        self.widget.geometry(geoinfo)
        self.left_drag.place(x = 0,y = 0,width = self.bordersize,height = self.widget.winfo_height())
        self.x = event.x_root
        self.widget.configure(cursor='plus')
    def MoveDragSize_H2(self,event):
        deltaX = event.x_root - self.x
        formw = self.widget.winfo_width() 
        formh = self.widget.winfo_height()
        newW = self.widget.winfo_width() + deltaX
        geoinfo = str('%dx%d+%d+%d'%(newW,self.widget.winfo_height(),self.widget.winfo_x(),self.widget.winfo_y()))
        self.widget.geometry(geoinfo)
        self.right_drag.place(x = newW-self.bordersize,y = 0,width = self.bordersize,height = formh)
        self.x = event.x_root
        self.widget.configure(cursor='plus')
    def MoveDragSize_V1(self,event):
        deltaY = event.y_root - self.y
        formy = self.widget.winfo_y() + deltaY
        newH = self.widget.winfo_height() - deltaY
        geoinfo = str('%dx%d+%d+%d'%(self.widget.winfo_width() ,newH,self.widget.winfo_x(),formy))
        self.widget.geometry(geoinfo)
        self.top_drag.place(x = 0,y = 0,width = self.widget.winfo_width(),height = self.bordersize)
        self.y = event.y_root
        self.widget.configure(cursor='plus')
    def MoveDragSize_V2(self,event):
        deltaY = event.y_root - self.y
        newH = self.widget.winfo_height() + deltaY
        geoinfo = str('%dx%d+%d+%d'%(self.widget.winfo_width(),newH,self.widget.winfo_x(),self.widget.winfo_y()))
        self.widget.geometry(geoinfo)
        self.bottom_drag.place(x = 0,y = (newH - self.bordersize),width = self.widget.winfo_width(),height = self.bordersize)
        self.y = event.y_root
        self.widget.configure(cursor='plus')
    def MotionDragBorder(self,event):
        formx = self.widget.winfo_x() 
        formy = self.widget.winfo_y() 
        formw = self.widget.winfo_width() 
        formh = self.widget.winfo_height() 
        x = event.x_root - formx
        y = event.y_root - formy
        if event.widget == self.left_drag:
            if y >=0 and y <= self.bordersize:
                if self.top_drag == None:
                    self.top_drag = tkinter.Label(self.widget)
                self.top_drag.place(x = 0,y = 0,width = formw,height = self.bordersize)
                self.top_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.top_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.top_drag.bind('<B1-Motion>',self.MoveDragSize_TL)
                self.top_drag.bind('<Leave>',self.LeaveDragBorder_TL)
                if self.left_drag == None:
                    self.left_drag = tkinter.Label(self.widget)
                self.left_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.left_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.left_drag.bind('<B1-Motion>',self.MoveDragSize_TL)
                self.left_drag.bind('<Leave>',self.LeaveDragBorder_TL)
            if y >=(formh-self.bordersize) and y <= formh:
                if self.bottom_drag == None:
                    self.bottom_drag = tkinter.Label(self.widget)
                self.bottom_drag.place(x = 0,y = formh-self.bordersize,width = formw,height = self.bordersize)
                self.bottom_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.bottom_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.bottom_drag.bind('<B1-Motion>',self.MoveDragSize_BL)
                self.bottom_drag.bind('<Leave>',self.LeaveDragBorder_BL)
                if self.left_drag == None:
                    self.left_drag = tkinter.Label(self.widget)
                self.left_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.left_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.left_drag.bind('<B1-Motion>',self.MoveDragSize_BL)
                self.left_drag.bind('<Leave>',self.LeaveDragBorder_BL)
        if event.widget == self.right_drag:
            if y >=0 and y <= self.bordersize:
                if self.top_drag == None:
                    self.top_drag = tkinter.Label(self.widget)
                self.top_drag.place(x = 0,y = 0,width = formw,height = self.bordersize)
                self.top_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.top_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.top_drag.bind('<B1-Motion>',self.MoveDragSize_TR)
                self.top_drag.bind('<Leave>',self.LeaveDragBorder_TR)
                if self.right_drag == None:
                    self.right_drag = tkinter.Label(self.widget)
                self.right_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.right_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.right_drag.bind('<B1-Motion>',self.MoveDragSize_TR)
                self.right_drag.bind('<Leave>',self.LeaveDragBorder_TR)
            if y >=(formh-self.bordersize) and y <= formh:
                if self.bottom_drag == None:
                    self.bottom_drag = tkinter.Label(self.widget)
                self.bottom_drag.place(x = 0,y = formh-self.bordersize,width = formw,height = self.bordersize)
                self.bottom_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.bottom_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.bottom_drag.bind('<B1-Motion>',self.MoveDragSize_BR)
                self.bottom_drag.bind('<Leave>',self.LeaveDragBorder_BR)
                if self.right_drag == None:
                    self.right_drag = tkinter.Label(self.widget)
                self.right_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.right_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.right_drag.bind('<B1-Motion>',self.MoveDragSize_BR)
                self.right_drag.bind('<Leave>',self.LeaveDragBorder_BR)
        if event.widget == self.top_drag:
            if x >=0 and x <= self.bordersize:
                if self.top_drag == None:
                    self.top_drag = tkinter.Label(self.widget)
                self.top_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.top_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.top_drag.bind('<B1-Motion>',self.MoveDragSize_TL)
                self.top_drag.bind('<Leave>',self.LeaveDragBorder_TL)
                if self.left_drag == None:
                    self.left_drag = tkinter.Label(self.widget)
                self.left_drag.place(x = 0,y = 0,width = self.bordersize,height = formh)
                self.left_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.left_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.left_drag.bind('<B1-Motion>',self.MoveDragSize_TL)
                self.left_drag.bind('<Leave>',self.LeaveDragBorder_TL)
            if x >=(formw-self.bordersize) and x <= formw:
                if self.top_drag == None:
                    self.top_drag = tkinter.Label(self.widget)
                self.top_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.top_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.top_drag.bind('<B1-Motion>',self.MoveDragSize_TR)
                self.top_drag.bind('<Leave>',self.LeaveDragBorder_TR)
                if self.right_drag == None:
                    self.right_drag = tkinter.Label(self.widget)
                self.right_drag.place(x = formw-self.bordersize,y = 0,width = self.bordersize,height = formh)
                self.right_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.right_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.right_drag.bind('<B1-Motion>',self.MoveDragSize_TR)
                self.right_drag.bind('<Leave>',self.LeaveDragBorder_TR)
        if event.widget == self.bottom_drag:
            if x >=0 and x <= self.bordersize:
                if self.bottom_drag == None:
                    self.bottom_drag = tkinter.Label(self.widget)
                self.bottom_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.bottom_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.bottom_drag.bind('<B1-Motion>',self.MoveDragSize_BL)
                self.bottom_drag.bind('<Leave>',self.LeaveDragBorder_BL)
                if self.left_drag == None:
                    self.left_drag = tkinter.Label(self.widget)
                self.left_drag.place(x = 0,y = 0,width = self.bordersize,height = formh)
                self.left_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.left_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.left_drag.bind('<B1-Motion>',self.MoveDragSize_BL)
                self.left_drag.bind('<Leave>',self.LeaveDragBorder_BL)
            if x >=(formw-self.bordersize) and x <= formw:
                if self.bottom_drag == None:
                    self.bottom_drag = tkinter.Label(self.widget)
                self.bottom_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.bottom_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.bottom_drag.bind('<B1-Motion>',self.MoveDragSize_BR)
                self.bottom_drag.bind('<Leave>',self.LeaveDragBorder_BR)  
                if self.right_drag == None:
                    self.right_drag = tkinter.Label(self.widget)
                self.right_drag.place(x = formw-self.bordersize,y = 0,width = self.bordersize,height = formh)
                self.right_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.right_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.right_drag.bind('<B1-Motion>',self.MoveDragSize_BR)
                self.right_drag.bind('<Leave>',self.LeaveDragBorder_BR)
    def LeaveDragBorder(self,event):
        event.widget.place_forget()
    def MoveDragSize_TL(self,event):
        deltaX = event.x_root - self.x
        deltaY = event.y_root - self.y
        formx = self.widget.winfo_x() + deltaX
        newW = self.widget.winfo_width() - deltaX
        formy = self.widget.winfo_y() + deltaY
        newH = self.widget.winfo_height() - deltaY
        geoinfo = str('%dx%d+%d+%d'%(newW,newH,formx,formy))
        self.widget.geometry(geoinfo)
        self.left_drag.place(x = 0,y = 0,width = self.bordersize,height = self.widget.winfo_height())
        self.top_drag.place(x = 0,y = 0,width = self.widget.winfo_width(),height = self.bordersize)
        self.x = event.x_root
        self.y = event.y_root
        self.widget.configure(cursor='plus')
    def LeaveDragBorder_TL(self,event):
        self.left_drag.place_forget()
        self.top_drag.place_forget()
        self.widget.configure(cursor='arrow')
    def MoveDragSize_TR(self,event):
        deltaX = event.x_root - self.x
        deltaY = event.y_root - self.y
        formx = self.widget.winfo_x()
        newW = self.widget.winfo_width() + deltaX
        formy = self.widget.winfo_y() + deltaY
        newH = self.widget.winfo_height() - deltaY
        geoinfo = str('%dx%d+%d+%d'%(newW,newH,formx,formy))
        self.widget.geometry(geoinfo)
        self.right_drag.place(x = newW-self.bordersize,y = 0,width = self.bordersize,height = self.widget.winfo_height())
        self.top_drag.place(x = 0,y = 0,width = self.widget.winfo_width(),height = self.bordersize)
        self.x = event.x_root
        self.y = event.y_root
        self.widget.configure(cursor='plus')
    def LeaveDragBorder_TR(self,event):
        self.right_drag.place_forget()
        self.top_drag.place_forget()
        self.widget.configure(cursor='arrow')
    def MoveDragSize_BL(self,event):
        deltaX = event.x_root - self.x
        deltaY = event.y_root - self.y
        formx = self.widget.winfo_x() + deltaX
        newW = self.widget.winfo_width() - deltaX
        formy = self.widget.winfo_y()
        newH = self.widget.winfo_height() + deltaY
        geoinfo = str('%dx%d+%d+%d'%(newW,newH,formx,formy))
        self.widget.geometry(geoinfo)
        self.left_drag.place(x = 0,y = 0,width = self.bordersize,height = self.widget.winfo_height())
        self.bottom_drag.place(x = 0,y = newH-self.bordersize,width = self.widget.winfo_width(),height = self.bordersize)
        self.x = event.x_root
        self.y = event.y_root
        self.widget.configure(cursor='plus')
    def LeaveDragBorder_BL(self,event):
        self.left_drag.place_forget()
        self.bottom_drag.place_forget()
        self.widget.configure(cursor='arrow')
    def MoveDragSize_BR(self,event):
        deltaX = event.x_root - self.x
        deltaY = event.y_root - self.y
        formx = self.widget.winfo_x()
        newW = self.widget.winfo_width() + deltaX
        formy = self.widget.winfo_y()
        newH = self.widget.winfo_height() + deltaY
        geoinfo = str('%dx%d+%d+%d'%(newW,newH,formx,formy))
        self.widget.geometry(geoinfo)
        self.right_drag.place(x = newW-self.bordersize,y = 0,width = self.bordersize,height = self.widget.winfo_height())
        self.bottom_drag.place(x = 0,y = newH-self.bordersize,width = self.widget.winfo_width(),height = self.bordersize)
        self.x = event.x_root
        self.y = event.y_root
        self.widget.configure(cursor='plus')
    def LeaveDragBorder_BR(self,event):
        self.right_drag.place_forget()
        self.bottom_drag.place_forget() 
        self.widget.configure(cursor='arrow')
def SetRootRoundRectangle(canvas,x1, y1, x2, y2, radius=25,**kwargs):
    """使用TKinter方式设置窗口圆角, 支持跨平台。参数1:Canvas控件,参数2:左上x位置,参数3:左上y位置,参数4 :右下x位置,参数5:右下y位置,参数6:圆角半径。"""
    points = [x1+radius, y1,
              x1+radius, y1,
              x2-radius, y1,
              x2-radius, y1,
              x2, y1,
              x2, y1+radius,
              x2, y1+radius,
              x2, y2-radius,
              x2, y2-radius,
              x2, y2,
              x2-radius, y2,
              x2-radius, y2,
              x1+radius, y2,
              x1+radius, y2,
              x1, y2,
              x1, y2-radius,
              x1, y2-radius,
              x1, y1+radius,
              x1, y1+radius,
              x1, y1]
    return canvas.create_polygon(points, smooth=True, **kwargs)
def ReadFromFile(filePath):
    """从一个文件中读取内容。参数1 :文件路径 。"""
    content = None
    if filePath != None:
        if os.path.exists(filePath) == True: 
            f = open(filePath,mode='r',encoding='utf-8')
            if f != None:
                content = f.read()
                f.close()
    return content
def WriteToFile(filePath,content):
    """将内容写入到一个文件中。参数1 :文件路径,参数2 :写入的内容 。 """
    if filePath != None:
        f = open(filePath,mode='w',encoding='utf-8')
        if f != None:
            if content != None:
                f.write(content)
            f.close()
            return True
    return False
def ReadStyleFile(filePath):
    """读取样式定义文件,返回样式列表。参数1 :文件路径 。"""
    StyleArray = {}
    if len(filePath)==0 :
        return StyleArray
    if os.path.exists(filePath) == False:
        return StyleArray
    f = open(filePath,encoding='utf-8')
    line =""
    while True:
        line = f.readline()
        if not line:
            break
        text = line.strip()
        if not text:
            continue
        if text.find('style = tkinter.ttk.Style()') >= 0:
            continue
        if text.find('style.configure(') >= 0:
            splitarray1 = text.partition('style.configure(')
            stylename = None
            splitarray2 = None
            if splitarray1[2].find(',') >= 0:
                splitarray2 = splitarray1[2].partition(',')
                stylename = splitarray2[0].replace('"','')
            else:
                splitarray2 = splitarray1[2].partition(')')
                stylename = splitarray2[0].replace('"','')
            sytleValueText = splitarray2[2]
            fontindex_begin = sytleValueText.find('font=(')
            fontindex_end = fontindex_begin
            StyleArray[stylename] = {}
            othertext = sytleValueText
            if fontindex_begin >= 0:
                fontindex_end = sytleValueText.find(')')
                fonttext = sytleValueText[fontindex_begin+6:fontindex_end]
                fontsplitarray = fonttext.split(',')
                StyleArray[stylename]['font'] = tkinter.font.Font(family=fontsplitarray[0].replace('"','').strip(), size=int(fontsplitarray[1].replace('"','').strip()),weight=fontsplitarray[2].replace('"','').strip())
                othertext = sytleValueText[0:fontindex_begin] + sytleValueText[fontindex_end+1:-1]
            else:
                splitarray4 = sytleValueText.partition(')')
                othertext = splitarray4[0]
            splitarray3 = othertext.split(',')
            for stylecfgtext in splitarray3:
                if stylecfgtext.find('=') > 0:
                    splitarray4 = stylecfgtext.partition('=')
                    key = splitarray4[0].replace('"','').strip()
                    value = splitarray4[2].replace('"','').strip()
                    StyleArray[stylename][key] = value
            continue
        if text.find('style.map(') >= 0:
            continue
    f.close()
    return StyleArray 
