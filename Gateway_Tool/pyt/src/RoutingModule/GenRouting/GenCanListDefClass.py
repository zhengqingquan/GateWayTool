from pyt.src.RoutingModule.GenRouting.GenGlobalClass import GenGlobalClass
from pyt.src.RoutingModule.GenRouting.GenRoutingRootClass import GenRoutingRootClass
from pyt.src.ToolModule.CodeGeneration import structCode
from pyt.src.ToolModule.FileGeneration import generate_HeadFileInclude, generate_description, generate_HeadFileIfndef


class GenCanListDefClass(GenRoutingRootClass):
    __headerFileName = 'CanListDef.h'
    __sourceFileName = 'CanListDef.c'

    __routingStructName = 'Msgdef_t'
    __routingTableName = 'ListMsg'
    __routingTableLengthName = 'ListMsgLenght'

    @property
    def headerFileName(self):
        return self.__headerFileName

    @property
    def sourceFileName(self):
        return self.__sourceFileName

    @property
    def routingStructName(self):
        return self.__routingStructName

    @property
    def routingTableName(self):
        return self.__routingTableName

    @property
    def routingTableLengthName(self):
        return self.__routingTableLengthName

    def headerFile(self, filePath, tableHeaderList: list):
        """
        生成头文件CanListDef.h
        """

        stdHeadList = ['stdint.h']
        cusHeadList = []

        structContent = ''
        for e in tableHeaderList:
            header = str(e).strip()
            if header == 'source' or header == 'id' or header == 'time':
                dataType = 'uint32_t'
                structContent = f'{structContent}\t{dataType} {header};\n'
            elif header == 'dlc' or header == 'target':
                dataType = 'uint8_t'
                structContent = f'{structContent}\t{dataType} {header};\n'
            else:
                dataType = 'uint8_t'
                structContent = f'{structContent}\t{dataType} {header} : 1;\n'

        with open(filePath, 'w', encoding='utf-8') as file:
            file.writelines('/*\n'
                            '* 路由结构体\n'
                            '*/\n')
            file.writelines(structCode(self.__routingStructName, structContent))
            file.writelines('\n\n')

            file.writelines('/*\n'
                            '* 路由列表\n'
                            '*/\n')
            file.writelines(f'extern const {self.__routingStructName} {self.__routingTableName}[];\n')
            file.writelines('\n\n')

            file.writelines('/*\n'
                            '* 路由列表的长度\n'
                            '*/\n')
            file.writelines(f'extern const uint16_t {self.__routingTableLengthName};\n')

        generate_HeadFileInclude(filePath, stdHeadList, cusHeadList, True)
        generate_HeadFileIfndef(filePath)
        generate_description(filePath)

    def sourceFile(self, filePath, data: list[list]):

        stdHeadList = []
        cusHeadList = [self.__headerFileName,
                       GenGlobalClass().headerFileName]

        with open(filePath, mode='w', encoding='utf-8') as file:

            # 写入数组
            file.writelines(f'const {self.__routingStructName} {self.__routingTableName}[] = '
                            '{\n')

            separator = None
            for a in data:
                # 在不同的CAN中间添加一个换行
                if separator != a[0]:
                    file.writelines('\n')
                    separator = a[0]

                # TODO 这里需要进行对齐，可以在上面再添加说明。
                # 单独占用每个比特位来表示标定的打印方法——使用直接打印
                file.writelines('\t{')
                for value in a:
                    file.writelines(f' {value},')
                file.writelines(' },\n')

            file.writelines('\n};\n')
            file.writelines('\n\n')

            # 写入数组长度
            file.writelines(f'const uint16_t {self.__routingTableLengthName} = '
                            f'sizeof({self.__routingTableName}) / sizeof({self.__routingTableName}[0]);\n')

        generate_HeadFileInclude(filePath, stdHeadList, cusHeadList, True)
        generate_description(filePath)
