from pyt.src.RoutingModule.GenRouting.GenRoutingRootClass import GenRoutingRootClass
from pyt.src.ToolModule.FileGeneration import generate_HeadFileInclude, generate_HeadFileIfndef, generate_description
from pyt.src.config.RouteConfig import RouteConfig


class GenGlobalClass(GenRoutingRootClass):
    __headerFileName = 'GW_global.h'
    __sourceFileName = 'GW_global.c'

    @property
    def headerFileName(self):
        return self.__headerFileName

    @property
    def sourceFileName(self):
        return self.__sourceFileName

    def headerFile(self, filePath):
        stdHeadList = ['stdint.h']
        cusHeadList = []

        with open(filePath, mode='w', encoding='utf-8') as file:
            for e, v in RouteConfig().CHANNEL_MAPPING.items():
                file.writelines(f'#define {e} ({v}U)\n')
            file.writelines('\n\n')

            file.writelines('/*\n'
                            '* 用于接收的报文属性\n'
                            '*/\n')
            file.writelines('extern uint8_t CanDriver_Hrh_Rx; // 报文源地址\n'
                            'extern uint32_t CanDriver_ID_Rx; // 报文ID\n'
                            'extern uint8_t CanDriver_Dlc_Rx; // 报文DLC\n'
                            'extern uint8_t CanDriver_Ide_Rx; // 报文是否为扩展帧\n'
                            'extern uint8_t CanDriver_Data_Rx[8]; // 报文数据\n')
            file.writelines('\n\n')

            file.writelines('/*\n'
                            '* 用于发送的报文属性\n'
                            '*/\n')
            file.writelines('extern uint8_t CanDriver_Hth_Tx; // 报文目的地址\n'
                            'extern uint32_t CanDriver_ID_Tx; // 报文ID\n'
                            'extern uint8_t CanDriver_Dlc_Tx; // 报文DLC\n'
                            'extern uint8_t CanDriver_Ide_Tx; // 报文是否为扩展帧\n'
                            'extern uint8_t CanDriver_Data_Tx[8]; // 报文数据\n')
            file.writelines('\n\n')

            file.writelines('/*\n'
                            '* 节点配置字\n'
                            '*/\n')
            file.writelines('\n\n')

            file.writelines('/*\n'
                            '* 功能配置字\n'
                            '*/\n')
            file.writelines('extern uint8_t MotorcycleType;\n')
            file.writelines('\n\n')

            file.writelines('/*\n'
                            '* 全局变量初始化\n'
                            '*/\n')
            file.writelines('extern void GateWayGlobalInit(void);\n')
            file.writelines('\n\n')

        generate_HeadFileInclude(filePath, stdHeadList, cusHeadList, True)
        generate_HeadFileIfndef(filePath)
        generate_description(filePath)

    def source(self, filePath):
        stdHeadList = []
        cusHeadList = [self.__headerFileName]

        with open(filePath, mode='w', encoding='utf-8') as file:
            file.writelines('/*\n'
                            '* 用于接收的报文属性\n'
                            '*/\n')
            file.writelines('uint8_t CanDriver_Hrh_Rx; // 报文源地址\n'
                            'uint32_t CanDriver_ID_Rx; // 报文ID\n'
                            'uint8_t CanDriver_Dlc_Rx; // 报文DLC\n'
                            'uint8_t CanDriver_Ide_Rx; // 报文是否为扩展帧\n'
                            'uint8_t CanDriver_Data_Rx[8]; // 报文数据\n')
            file.writelines('\n\n')

            file.writelines('/*\n'
                            '* 用于发送的报文属性\n'
                            '*/\n')
            file.writelines('uint8_t CanDriver_Hth_Tx; // 报文目的地址\n'
                            'uint32_t CanDriver_ID_Tx; // 报文ID\n'
                            'uint8_t CanDriver_Dlc_Tx; // 报文DLC\n'
                            'uint8_t CanDriver_Ide_Tx; // 报文是否为扩展帧\n'
                            'uint8_t CanDriver_Data_Tx[8]; // 报文数据\n')
            file.writelines('\n\n')

            file.writelines('/*\n'
                            '* 节点配置字\n'
                            '*/\n')
            file.writelines('\n\n')

            file.writelines('/*\n'
                            '* 功能配置字\n'
                            '*/\n')
            file.writelines('uint8_t MotorcycleType;\n')
            file.writelines('\n\n')

            file.writelines('/*\n'
                            '* 全局变量初始化\n'
                            '*/\n')
            file.writelines('void GateWayGlobalInit(void)\n'
                            '{\n'
                            '   CanDriver_Hrh_Rx = 0U;\n'
                            '   CanDriver_ID_Rx = 0U;\n'
                            '   CanDriver_Dlc_Rx = 0U;\n'
                            '   CanDriver_Ide_Rx = 0U;\n'
                            '   (void)memset(((void*)&CanDriver_Data_Rx), 0, sizeof(CanDriver_Data_Rx));\n'
                            '\n'
                            '   CanDriver_Hth_Tx = 0U;\n'
                            '   CanDriver_ID_Tx = 0U;\n'
                            '   CanDriver_Dlc_Tx = 0U;\n'
                            '   CanDriver_Ide_Tx = 0U;\n'
                            '   (void)memset(((void*)&CanDriver_Data_Tx), 0, sizeof(CanDriver_Data_Tx));\n'
                            '\n'
                            '   MotorcycleType = 0U;\n'
                            '}\n')
            file.writelines('\n\n')

        generate_HeadFileInclude(filePath, stdHeadList, cusHeadList, True)
        generate_description(filePath)
