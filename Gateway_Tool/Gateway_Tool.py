#coding=utf-8
#import libs 
import sys
import Gateway_Tool_cmd
import Gateway_Tool_sty
import Fun
import os
import tkinter
from   tkinter import *
import tkinter.ttk
import tkinter.font
#Add your Varial Here: (Keep This Line of comments)
#Define UI Class
class  Gateway_Tool:
    def __init__(self,root,isTKroot = True):
        uiName = self.__class__.__name__
        self.uiName = uiName
        Fun.Register(uiName,'UIClass',self)
        self.root = root
        self.isTKroot = isTKroot
        Fun.Register(uiName,'root',root)
        style = Gateway_Tool_sty.SetupStyle()
        if isTKroot == True:
            root.title("GatewayTool")
            root.resizable(False,False)
            Fun.CenterDlg(uiName,root,800,677)
            root['background'] = '#efefef'
            root.bind('<Configure>',self.Configure)
        Form_1= tkinter.Canvas(root,width = 10,height = 4)
        Form_1.pack(fill=BOTH,expand=True)
        Form_1.configure(bg = "#efefef")
        Form_1.configure(highlightthickness = 0)
        Fun.Register(uiName,'Form_1',Form_1)
        #Create the elements of root 
        Text_3 = tkinter.Text(Form_1)
        Fun.Register(uiName,'Text_3',Text_3,'PrintTextFrame')
        Fun.SetControlPlace(uiName,'Text_3',17,187,767,160)
        Text_3.configure(relief = "sunken")
        Text_3.configure(state = "disabled")
        Text_3_Scrollbar = tkinter.Scrollbar(Text_3,orient=tkinter.VERTICAL)
        Text_3_Scrollbar.place(x = 747,y = 0,width = 20,height = 160)
        Text_3_Scrollbar.config(command = Text_3.yview)
        Text_3.config(yscrollcommand = Text_3_Scrollbar.set)
        Fun.Register(uiName,'Text_3_Scrollbar',Text_3_Scrollbar)
        Button_6 = tkinter.Button(Form_1,text="Excel路径")
        Fun.Register(uiName,'Button_6',Button_6,'ExcelPathButton')
        Fun.SetControlPlace(uiName,'Button_6',17,25,100,28)
        Button_6.configure(command=lambda:Gateway_Tool_cmd.ExcelPathButton_onCommand(uiName,"Button_6"))
        Entry_7_Variable = Fun.AddTKVariable(uiName,'Entry_7','')
        Entry_7 = tkinter.Entry(Form_1,textvariable=Entry_7_Variable)
        Fun.Register(uiName,'Entry_7',Entry_7,'ExcelPathEntry')
        Fun.SetControlPlace(uiName,'Entry_7',143,26,561,26)
        Entry_7.configure(relief = "sunken")
        Button_8 = tkinter.Button(Form_1,text="保存路径")
        Fun.Register(uiName,'Button_8',Button_8,'ExcelSavePathButton')
        Fun.SetControlPlace(uiName,'Button_8',17,81,100,28)
        Button_8.configure(command=lambda:Gateway_Tool_cmd.ExcelSavePathButton_onCommand(uiName,"Button_8"))
        Entry_9_Variable = Fun.AddTKVariable(uiName,'Entry_9','')
        Entry_9 = tkinter.Entry(Form_1,textvariable=Entry_9_Variable)
        Fun.Register(uiName,'Entry_9',Entry_9,'ExcelSavePathEntry')
        Fun.SetControlPlace(uiName,'Entry_9',143,81,561,28)
        Entry_9.configure(relief = "sunken")
        Button_10 = tkinter.Button(Form_1,text="生成文件")
        Fun.Register(uiName,'Button_10',Button_10,'CreateFileButton')
        Fun.SetControlPlace(uiName,'Button_10',323,121,100,28)
        Button_10.configure(command=lambda:Gateway_Tool_cmd.CreateFileButton_onCommand(uiName,"Button_10"))
        Button_11 = tkinter.Button(Form_1,text="模板路径")
        Fun.Register(uiName,'Button_11',Button_11,'TemplatePathButton')
        Fun.SetControlPlace(uiName,'Button_11',17,374,100,28)
        Button_11.configure(command=lambda:Gateway_Tool_cmd.TemplatePathButton_onCommand(uiName,"Button_11"))
        Entry_12_Variable = Fun.AddTKVariable(uiName,'Entry_12','')
        Entry_12 = tkinter.Entry(Form_1,textvariable=Entry_12_Variable)
        Fun.Register(uiName,'Entry_12',Entry_12,'TemplatePathEntry')
        Fun.SetControlPlace(uiName,'Entry_12',142,373,563,29)
        Entry_12.configure(relief = "sunken")
        Button_13 = tkinter.Button(Form_1,text="JSON路径")
        Fun.Register(uiName,'Button_13',Button_13,'JsonPathButton')
        Fun.SetControlPlace(uiName,'Button_13',17,423,100,28)
        Button_13.configure(command=lambda:Gateway_Tool_cmd.JsonPathButton_onCommand(uiName,"Button_13"))
        Entry_14_Variable = Fun.AddTKVariable(uiName,'Entry_14','')
        Entry_14 = tkinter.Entry(Form_1,textvariable=Entry_14_Variable)
        Fun.Register(uiName,'Entry_14',Entry_14,'JsonPathEntry')
        Fun.SetControlPlace(uiName,'Entry_14',142,423,564,28)
        Entry_14.configure(relief = "sunken")
        Button_15 = tkinter.Button(Form_1,text="替换模板")
        Fun.Register(uiName,'Button_15',Button_15,'ReplaceTemplateButton')
        Fun.SetControlPlace(uiName,'Button_15',330,511,100,28)
        Button_15.configure(command=lambda:Gateway_Tool_cmd.ReplaceTemplateButton_onCommand(uiName,"Button_15"))
        Button_16 = tkinter.Button(Form_1,text="保存路径")
        Fun.Register(uiName,'Button_16',Button_16,'TemplateSavePathButton')
        Fun.SetControlPlace(uiName,'Button_16',17,470,100,28)
        Button_16.configure(command=lambda:Gateway_Tool_cmd.TemplateSavePathButton_onCommand(uiName,"Button_16"))
        Entry_17_Variable = Fun.AddTKVariable(uiName,'Entry_17','')
        Entry_17 = tkinter.Entry(Form_1,textvariable=Entry_17_Variable)
        Fun.Register(uiName,'Entry_17',Entry_17,'TemplateSavePathEntry')
        Fun.SetControlPlace(uiName,'Entry_17',142,471,564,27)
        Entry_17.configure(relief = "sunken")
        CheckButton_18_Variable = Fun.AddTKVariable(uiName,'CheckButton_18')
        CheckButton_18_Variable.set(False)
        CheckButton_18 = tkinter.Checkbutton(Form_1,variable=CheckButton_18_Variable,text="重载路径",anchor=tkinter.W)
        Fun.Register(uiName,'CheckButton_18',CheckButton_18,'ExcelSavePathCheckButton')
        Fun.SetControlPlace(uiName,'CheckButton_18',715,89,77,20)
        CheckButton_18.configure(command=lambda:Gateway_Tool_cmd.ExcelSavePathCheckButton_onCommand(uiName,"CheckButton_18"))
        CheckButton_19_Variable = Fun.AddTKVariable(uiName,'CheckButton_19')
        CheckButton_19_Variable.set(False)
        CheckButton_19 = tkinter.Checkbutton(Form_1,variable=CheckButton_19_Variable,text="重载路径",anchor=tkinter.W)
        Fun.Register(uiName,'CheckButton_19',CheckButton_19,'JsonPathCheckButton')
        Fun.SetControlPlace(uiName,'CheckButton_19',715,431,78,20)
        CheckButton_19.configure(command=lambda:Gateway_Tool_cmd.JsonPathCheckButton_onCommand(uiName,"CheckButton_19"))
        CheckButton_20_Variable = Fun.AddTKVariable(uiName,'CheckButton_20')
        CheckButton_20_Variable.set(False)
        CheckButton_20 = tkinter.Checkbutton(Form_1,variable=CheckButton_20_Variable,text="重载路径",anchor=tkinter.W)
        Fun.Register(uiName,'CheckButton_20',CheckButton_20,'TemplateSavePathCheckButton')
        Fun.SetControlPlace(uiName,'CheckButton_20',716,478,76,20)
        CheckButton_20.configure(command=lambda:Gateway_Tool_cmd.TemplateSavePathCheckButton_onCommand(uiName,"CheckButton_20"))
        Progress_21 = tkinter.ttk.Progressbar(Form_1)
        Fun.Register(uiName,'Progress_21',Progress_21,'ProgressBar')
        Fun.SetControlPlace(uiName,'Progress_21',17,161,767,20)
        Progress_21.configure(orient = tkinter.HORIZONTAL)
        Progress_21.configure(mode = "determinate")
        Progress_21.configure(maximum = "100")
        Progress_21.configure(value = "0.0")
        Button_22 = tkinter.Button(Form_1,text="DBC解析")
        Fun.Register(uiName,'Button_22',Button_22,'DBCParseButton')
        Fun.SetControlPlace(uiName,'Button_22',330,639,100,28)
        Button_22.configure(command=lambda:Gateway_Tool_cmd.DBCParseButton_onCommand(uiName,"Button_22"))
        Button_23 = tkinter.Button(Form_1,text="DBC路径")
        Fun.Register(uiName,'Button_23',Button_23,'DBCPathButton')
        Fun.SetControlPlace(uiName,'Button_23',16,546,100,28)
        Button_23.configure(command=lambda:Gateway_Tool_cmd.DBCPathButton_onCommand(uiName,"Button_23"))
        Button_24 = tkinter.Button(Form_1,text="保存路径")
        Fun.Register(uiName,'Button_24',Button_24,'DBCSavePathButton')
        Fun.SetControlPlace(uiName,'Button_24',16,590,100,28)
        Button_24.configure(command=lambda:Gateway_Tool_cmd.DBCSavePathButton_onCommand(uiName,"Button_24"))
        Entry_25_Variable = Fun.AddTKVariable(uiName,'Entry_25','')
        Entry_25 = tkinter.Entry(Form_1,textvariable=Entry_25_Variable)
        Fun.Register(uiName,'Entry_25',Entry_25,'DBCPathEntry')
        Fun.SetControlPlace(uiName,'Entry_25',138,546,565,28)
        Entry_25.configure(relief = "sunken")
        Entry_26_Variable = Fun.AddTKVariable(uiName,'Entry_26','')
        Entry_26 = tkinter.Entry(Form_1,textvariable=Entry_26_Variable)
        Fun.Register(uiName,'Entry_26',Entry_26,'DBCSavePathEntry')
        Fun.SetControlPlace(uiName,'Entry_26',138,589,566,31)
        Entry_26.configure(relief = "sunken")
        #Create the Menu of root 
        MainMenu=tkinter.Menu(root)
        root.config(menu = MainMenu)
        Menu1=tkinter.Menu(MainMenu,tearoff = 0)
        Menu1.add_command(label="菜单1的子菜单1",command=lambda:Gateway_Tool_cmd.Menu_菜单1的子菜单1(uiName,"菜单1的子菜单1"))
        Menu1.add_command(label="菜单1的子菜单2",command=lambda:Gateway_Tool_cmd.Menu_菜单1的子菜单2(uiName,"菜单1的子菜单2"))
        MainMenu.add_cascade(label="Menu1",menu=Menu1)
        Menu2=tkinter.Menu(MainMenu,tearoff = 0)
        Menu2.add_command(label="CreateExcelTemplate",command=lambda:Gateway_Tool_cmd.Menu_CreateExcelTemplate(uiName,"CreateExcelTemplate"))
        Menu2.add_command(label="菜单2的子菜单2",command=lambda:Gateway_Tool_cmd.Menu_菜单2的子菜单2(uiName,"菜单2的子菜单2"))
        MainMenu.add_cascade(label="Menu2",menu=Menu2)
        Menu3=tkinter.Menu(MainMenu,tearoff = 0)
        Menu3.add_command(label="菜单3的子菜单1",command=lambda:Gateway_Tool_cmd.Menu_菜单3的子菜单1(uiName,"菜单3的子菜单1"))
        Menu3.add_command(label="version",command=lambda:Gateway_Tool_cmd.Menu_version(uiName,"version"))
        MainMenu.add_cascade(label="Menu3",menu=Menu3)
        #Inital all element's Data 
        Fun.InitElementData(uiName)
        #Call Form_1's OnLoad Function
        Gateway_Tool_cmd.Form_1_onLoad(uiName)
        #Add Some Logic Code Here: (Keep This Line of comments)



        #Exit Application: (Keep This Line of comments)
        if self.isTKroot == True:
            self.root.protocol('WM_DELETE_WINDOW', self.Exit)
    def Exit(self):
        if self.isTKroot == True:
            self.root.destroy()

    def Configure(self,event):
        if self.root == event.widget:
            pass
#Create the root of Kinter 
if  __name__ == '__main__':
    root = tkinter.Tk()
    MyDlg = Gateway_Tool(root)
    root.mainloop()
