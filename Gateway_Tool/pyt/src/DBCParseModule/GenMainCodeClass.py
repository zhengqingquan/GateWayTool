import cantools
from cantools import database
from typing import AnyStr
import os

from prettytable import PrettyTable

from pyt.src.ToolModule.FileGeneration import generate_description, generate_HeadFileIfndef, generate_HeadFileInclude
from pyt.src.DBCParseModule.GenMainCodeTemplateClass import GenMainCodeTemplateClass
from pyt.src.DBCParseModule.GenTool import LengthToStdint, IntelUnpackToStr, IntelPackToStr, MotorolaPackToStr, \
    MotorolaUnpackToStr, DBCMotorolaStartBitShift


# dbc的使用环境是表示在这个网段上存在那些报文，这些报文有那些信号。
# 并不是针对仪表，而是针对网段。
# 例如网关有6路CAN，可以拆分为6个dbc文件。
# dbc文件使用的是ASCII编码
# https://blog.csdn.net/qfmzhu/article/details/104534088
# https://blog.csdn.net/qfmzhu/article/details/111403266
# https://blog.csdn.net/qq_41908302/article/details/127524015
# https://blog.csdn.net/qq_41908302/article/details/127503876?spm=1001.2014.3001.5502
class GenGenMainCodeClass(GenMainCodeTemplateClass):
    def __init__(self, dbcFilePath: AnyStr, folderPath: AnyStr, callBackName: AnyStr = 'signal'):
        self._dbcFilePath = dbcFilePath
        self._folderPath = folderPath
        self._callBackName = callBackName

        self._definitionHeaderName = f'{self._callBackName}_definition.h'
        self._definitionHeaderPath = os.path.join(self._folderPath, self._definitionHeaderName)

        self._definitionSourceName = f'{self._callBackName}_definition.c'
        self._definitionSourcePath = os.path.join(self._folderPath, self._definitionSourceName)

        self._binutilHeaderName = f'{self._callBackName}_binutil.h'
        self._binutilHeaderPath = os.path.join(self._folderPath, self._binutilHeaderName)

        self._binutilSourceName = f'{self._callBackName}_binutil.c'
        self._binutilSourcePath = os.path.join(self._folderPath, self._binutilSourceName)

        self._monitorutilHeaderName = f'{self._callBackName}_monitorutil.h'
        self._monitorutilHeaderPath = os.path.join(self._folderPath, self._monitorutilHeaderName)

        self._monitorutilSourceName = f'{self._callBackName}_monitorutil.c'
        self._monitorutilSourcePath = os.path.join(self._folderPath, self._monitorutilSourceName)

        self._cycleactHeaderName = f'{self._callBackName}_CycleAct.h'
        self._cycleactHeaderPath = os.path.join(self._folderPath, self._cycleactHeaderName)

        self._cycleactSourceName = f'{self._callBackName}_CycleAct.c'
        self._cycleactSourcePath = os.path.join(self._folderPath, self._cycleactSourceName)

        self._configHeaderName = f'{self._callBackName}_config.h'
        self._configHeaderPath = os.path.join(self._folderPath, self._configHeaderName)

        self._MsgParseAOPHeaderName = f'{self._callBackName}_MsgParseAOP.h'
        self._MsgParseAOPHeaderPath = os.path.join(self._folderPath, self._MsgParseAOPHeaderName)

        self._MsgParseAOPSourceName = f'{self._callBackName}_MsgParseAOP.c'
        self._MsgParseAOPSourcePath = os.path.join(self._folderPath, self._MsgParseAOPSourceName)

        self._MsgCycAOPHeaderName = f'{self._callBackName}_MsgCycAOP.h'
        self._MsgCycAOPHeaderPath = os.path.join(self._folderPath, self._MsgCycAOPHeaderName)

        self._MsgCycAOPSourceName = f'{self._callBackName}_MsgCycAOP.c'
        self._MsgCycAOPSourcePath = os.path.join(self._folderPath, self._MsgCycAOPSourceName)

        # 读取dbc文件可以参考文档：
        # https://github.com/cantools/cantools
        # 使用"ANSI"编码来解决注释中的中文字符乱码问题。
        self.db = cantools.database.load_file(self._dbcFilePath, encoding='ANSI')

    def Gen_DefinitionHeader(self):
        stdHeadList = ['stdint.h']
        cusHeadList = [self._monitorutilHeaderName]

        with open(self._definitionHeaderPath, mode='w', encoding='utf-8') as file:
            # 1、计算空间量，为了后续结构体的对齐。需要找出信号行中字符数最大的。
            temp = []
            for message in sorted(self.db.messages, key=lambda x: x.frame_id):
                for signal in message.signals:
                    context = f'\t{LengthToStdint(signal.length, signal.is_signed)} {signal.name} : {signal.length};'
                    temp.append(context)
            maxLen = len(max(temp))
            # 2、写具体的结构体内容
            for message in sorted(self.db.messages, key=lambda x: x.frame_id):
                # 3、验证报文合法性
                if not message.signals:
                    continue

                messageComment = PrettyTable()
                messageComment.field_names = ["Is Extended Frame", "Length", "Comment"]
                messageComment.add_row([message.is_extended_frame, message.length, message.comment])
                file.writelines(f'/*\n'
                                f'def @{message.name} CAN Message ({message.frame_id} 0x{message.frame_id:x})\n'
                                f'{messageComment}\n'
                                f'*/\n')
                file.writelines(f'#define {message.name}_IDE ({int(message.is_extended_frame)}U)\n')
                file.writelines(f'#define {message.name}_DLC ({message.length}U)\n')
                file.writelines(f'#define {message.name}_ID (0x{message.frame_id:x})\n')
                file.writelines(f'#define {message.name}_CYC ({message.cycle_time}U) // ms\n')

                # 转换公式
                # [Physical value] = ( [Raw value] * [Factor] ) + [Offset]
                # https://blog.csdn.net/qq_34414530/article/details/107228510
                # raw_value = (physical_value - Offset) / Factor
                # https://blog.csdn.net/qgccdd061313/article/details/125078551
                # raw_value表示报文数组中的值。
                # physical_value表示实际的具有物理意义的值，也就是计算后的值，例如实际的车速。

                # 如果系数或偏移量不为1的，则需要添加宏定义
                # for signal in message.signals:
                #     file.writelines(f'// signal: @{signal.name}')
                #     # 系数
                #     file.writelines(f'#define {self._callBackName}_{signal.name}_CovFactor ({signal.scale})')
                #     # 偏移量
                #     # file.writelines(f'#define {message.name}')

                file.writelines('\n')
                file.writelines('typedef struct\n')
                file.writelines('{\n')

                for signal in message.signals:
                    signalText = f'\t{LengthToStdint(signal.length, signal.is_signed)} {signal.name} : {signal.length};'
                    file.writelines(signalText)
                    alignSpaceAmount = maxLen - len(signalText) + 10  # 对其空间量
                    file.writelines(' ' * alignSpaceAmount)
                    file.writelines('//  ')
                    # 是否带符号
                    if signal.is_signed:
                        file.writelines('[-]')
                    else:
                        file.writelines('   ')
                    # 信号长度
                    file.writelines(f' Bits= {signal.length}')
                    # 系数
                    if signal.scale:
                        file.writelines(f' Factor= {signal.scale}')
                    # 偏移量
                    if signal.offset:
                        file.writelines(f' Offset= {signal.offset}')
                    # 信号单位
                    if signal.unit:
                        file.writelines(f" Unit:'{signal.unit}'\n")
                    else:
                        file.writelines(f'\n')
                    file.writelines('\n')
                file.writelines(f'\t{self._callBackName}_FrameMonitor_t monitor;\n\n')

                structName = f'{self._callBackName}_{message.name}_t'
                file.writelines('}%s;\n' % structName)
                file.writelines('\n')

                # 三、写打包和解包函数
                file.writelines(
                    f'uint32_t Unpack_{self._callBackName}_{message.name}({structName}* _message, '
                    f'const uint8_t _data[], uint8_t _dlc);\n')
                file.writelines(
                    f'uint32_t Pack_{self._callBackName}_{message.name}({structName}* _message, '
                    f'uint8_t* _data, uint8_t* _len, uint8_t* '
                    f'_ide);\n')
                file.writelines('\n\n')

        generate_HeadFileInclude(self._definitionHeaderPath, stdHeadList, cusHeadList, True)
        generate_HeadFileIfndef(self._definitionHeaderPath)
        generate_description(self._definitionHeaderPath)

    def Gen_DefinitionSource(self):
        stdHeadList = ['string.h']
        cusHeadList = [self._definitionHeaderName,
                       self._MsgParseAOPHeaderName]

        with open(self._definitionSourcePath, mode='w', encoding='utf-8') as file:
            for message in sorted(self.db.messages, key=lambda x: x.frame_id):

                structName = f'{self._callBackName}_{message.name}_t'

                # 报文说明
                unpackComment = PrettyTable()
                unpackComment.field_names = ["Signal Name", "Start Bit", "Length", "Byte Order", "Value Type(Signed)",
                                             "Factor", "Offset", "Unit", "comments"]
                for signal in message.signals:
                    if signal.byte_order == 'little_endian':
                        startBit = signal.start
                    else:
                        startBit = DBCMotorolaStartBitShift(signal.start, signal.length)
                    unpackComment.add_row(
                        [signal.name, startBit, signal.length, signal.byte_order, signal.is_signed, signal.scale,
                         signal.offset, signal.unit, signal.comment])
                file.writelines(f'/*\n'
                                f'Message Name: {message.name}\n'
                                f'Message Id: 0x{message.frame_id:x} ({message.frame_id})\n'
                                f'{unpackComment}\n'
                                f'*/\n')

                # 解包报文
                file.writelines(
                    f'uint32_t Unpack_{self._callBackName}_{message.name}({structName}* _message, '
                    f'const uint8_t _data[], uint8_t _dlc)\n')
                file.writelines('{\n')

                # 解析前执行函数
                file.writelines(f'\tBeforeParse_{self._callBackName}_{message.name}();\n')
                file.writelines('\n')

                # 解析
                for signal in message.signals:
                    if signal.byte_order == 'little_endian':
                        file.writelines(
                            f'\t_message->{signal.name} = {IntelUnpackToStr(signal.start, signal.length)};\n')
                    else:
                        startBit = DBCMotorolaStartBitShift(signal.start, signal.length)
                        file.writelines(
                            f'\t_message->{signal.name} = {MotorolaUnpackToStr(startBit, signal.length)};\n')
                file.writelines('\n')

                # TODO 调整这部分的位子，放到一个单独的函数中去，优先级不高。
                # 配合配置项nodeType使用。
                file.writelines(f'\t_message->monitor.last_cycle = {self._callBackName}_GetSystemTick();\n')
                file.writelines(f'\t_message->monitor.timeout_cnt = 0;\n')
                file.writelines(f'\t_message->monitor.frame_cnt++;\n')
                file.writelines(f'\t_message->monitor.dlc_error = (_dlc != {message.name}_DLC);\n')
                file.writelines('\n')

                # 解析后执行函数
                file.writelines(f'\tAfterParse_{self._callBackName}_{message.name}();\n')
                file.writelines('\n')

                file.writelines(f'\treturn {message.name}_ID;\n')
                file.writelines('}\n')
                file.writelines('\n')

                # 打包报文
                file.writelines(
                    f'uint32_t Pack_{self._callBackName}_{message.name}({structName}* _message, '
                    f'uint8_t* _data, uint8_t* _dlc, uint8_t* _ide)\n')
                file.writelines('{\n')
                file.writelines(f'\t(void)memset(_data, 0, sizeof(_data));\n')
                file.writelines('\n')
                for signal in message.signals:
                    if signal.byte_order == 'little_endian':
                        file.writelines(f'\t{IntelPackToStr(signal.name, signal.start, signal.length)}\n')
                    else:
                        startBit = DBCMotorolaStartBitShift(signal.start, signal.length)
                        file.writelines(f'\t{MotorolaPackToStr(signal.name, startBit, signal.length)}\n')
                file.writelines('\n')

                # TODO 这里可以保存最后一次打包的时间，最后一次打包的数据
                file.writelines(f'\t*_dlc = {message.name}_DLC;\n')
                file.writelines(f'\t*_ide = {message.name}_IDE;\n')
                file.writelines(f'\treturn {message.name}_ID;\n')
                file.writelines('}\n')
                file.writelines('\n')

        generate_HeadFileInclude(self._definitionSourcePath, stdHeadList, cusHeadList, True)
        generate_description(self._definitionSourcePath)

    def Gen_BinutilHeader(self):
        stdHeadList = ['stdint.h']
        cusHeadList = [self._definitionHeaderName]

        with open(self._binutilHeaderPath, mode='w', encoding='utf-8') as file:
            file.writelines('/*\n'
                            '* 报文列表结构体\n'
                            '*/\n')
            file.writelines('typedef struct\n'
                            '{\n')
            for message in sorted(self.db.messages, key=lambda x: x.frame_id):
                file.writelines(f'\t{self._callBackName}_{message.name}_t {message.name};\n')
            structName = f'{self._callBackName}_msglist_t'
            file.writelines('} %s;\n' % structName)
            file.writelines('\n\n')

            file.writelines('/*\n'
                            '* 声明外部变量\n'
                            '*/\n')
            file.writelines(f'extern {structName} {self._callBackName}_msglist;\n')
            file.writelines('\n\n')

            # 信号报文初始化
            file.writelines('/*\n'
                            '* 信号报文初始化\n'
                            '*/\n')
            file.writelines(f'void {self._callBackName}_init_msglist(void);\n')
            file.writelines('\n\n')

            # 信号报文周期函数
            file.writelines('/*\n'
                            '* 定期执行周期相关的函数，主要用于信号报文的发送。\n'
                            '* pollingCycle为轮询周期，单位为毫秒（ms），通常设置为10ms。\n'
                            '* 在配置文件中修改\n'
                            '*/\n')
            file.writelines(f'void {self._callBackName}_CycleAct(void);\n')
            file.writelines('\n\n')

            # 重置周期
            file.writelines('/*\n'
                            '* 重置所有信号报文的超时计时和周期计时。\n'
                            '*/\n')
            file.writelines(f'void {self._callBackName}_ResetAllInit(void);\n')
            file.writelines('\n\n')

            # 信号报文的打包
            file.writelines('/*\n'
                            '* 根据_msgID，将信号实际值打包到数组_data、_dlc和_ide上。\n'
                            '*/\n')
            file.writelines(f'uint32_t {self._callBackName}_Pack(const uint32_t _msgID, uint8_t* _data, '
                            f'uint8_t* _dlc, uint8_t* _ide);\n')
            file.writelines('\n\n')

            # 信号报文的解析
            file.writelines('/*\n'
                            '* 根据输入的_msgID和数据数组_data，对信号进行解析。\n'
                            '*/\n')
            file.writelines(f'uint32_t {self._callBackName}_Unpack(const uint32_t _msgID, '
                            f'const uint8_t* _data, const uint8_t _dlc);\n')
            file.writelines('\n\n')

        generate_HeadFileInclude(self._binutilHeaderPath, stdHeadList, cusHeadList, True)
        generate_HeadFileIfndef(self._binutilHeaderPath)
        generate_description(self._binutilHeaderPath)

    def Gen_BinutilSource(self):
        stdHeadList = []
        cusHeadList = [self._binutilHeaderName,
                       self._cycleactHeaderName,
                       self._MsgCycAOPHeaderName]

        with open(self._binutilSourcePath, mode='w', encoding='utf-8') as file:
            # 定义信号路由列表
            structName = f'{self._callBackName}_msglist_t'
            file.writelines(f'{structName} {self._callBackName}_msglist = ')
            file.writelines('{\n')
            for message in sorted(self.db.messages, key=lambda x: x.frame_id):
                # 报文ID注释
                file.writelines(f'\t/* 0x{message.frame_id:x} */\n')
                # 报文周期
                file.writelines(f'\t.{message.name}.monitor.cycle = {message.name}_CYC,\n')
                # 报文超时周期
                if message.cycle_time:
                    file.writelines(f'\t.{message.name}.monitor.timeout_cycle = {5 * message.cycle_time},\n')
                else:
                    file.writelines(f'\t.{message.name}.monitor.timeout_cycle = {0},\n')
                # 超时执行函数
                file.writelines(f'\t.{message.name}.monitor.TimeoutFunc = '
                                f'{self._callBackName}_TimeoutFunc_{message.name},\n')
                # 调用周期定时执行函数
                file.writelines(f'\t.{message.name}.monitor.TimingFunc = '
                                f'{self._callBackName}_TimingFunc_{message.name},\n')
                # 周期循环执行函数
                file.writelines(f'\t.{message.name}.monitor.CycleOverFunc = '
                                f'{self._callBackName}_CycleOverFunc_{message.name},\n')
                file.writelines('\n')
            file.writelines('};\n')
            file.writelines('\n\n')

            # 信号报文初始化
            file.writelines(f'void {self._callBackName}_init_msglist(void)\n')
            file.writelines('{\n')
            file.writelines('\n')
            file.writelines('}\n')
            file.writelines('\n\n')

            # 信号报文周期函数
            file.writelines(f'void {self._callBackName}_CycleAct(void)\n'
                            '{\n'
                            '\tCycleActFunc();\n'
                            '}\n')
            file.writelines('\n\n')

            # 重置周期
            file.writelines(f'void {self._callBackName}_ResetAllInit(void)\n'
                            '{\n'
                            '\n'
                            '}\n')
            file.writelines('\n\n')

            # 打包函数
            file.writelines(f'uint32_t {self._callBackName}_Pack(const uint32_t _msgID, uint8_t* _data, '
                            f'uint8_t* _dlc, uint8_t* _ide)\n')
            file.writelines('{\n')
            file.writelines('\tuint32_t traID = 0;\n')
            file.writelines('\n')
            file.writelines(f'\tswitch (_msgID)\n')
            file.writelines('\t{\n')
            for message in sorted(self.db.messages, key=lambda x: x.frame_id):
                file.writelines(f'\tcase 0x{message.frame_id:x}:\n')
                file.writelines(
                    f'\t\ttraID = Pack_{self._callBackName}_{message.name}'
                    f'(&({self._callBackName}_msglist.{message.name}), _data, _dlc, _ide);\n')
                file.writelines('\t\tbreak;\n')
            file.writelines('\tdefault:\n')
            file.writelines('\t\tbreak;\n')
            file.writelines('\t}\n')
            file.writelines('\treturn traID;\n')
            file.writelines('}\n')
            file.writelines('\n\n')

            # 解包函数
            file.writelines(f'uint32_t {self._callBackName}_Unpack(const uint32_t _msgID, '
                            f'const uint8_t* _data, const uint8_t _dlc)\n')
            file.writelines('{\n')
            file.writelines('\tuint32_t recID = 0;\n')
            file.writelines('\n')
            file.writelines(f'\tswitch (_msgID)\n')
            file.writelines('\t{\n')
            for message in sorted(self.db.messages, key=lambda x: x.frame_id):
                file.writelines(f'\tcase 0x{message.frame_id:x}:\n')
                file.writelines(
                    f'\t\trecID = Unpack_{self._callBackName}_{message.name}'
                    f'(&({self._callBackName}_msglist.{message.name}), _data, _dlc);\n')
                file.writelines('\t\tbreak;\n')
            file.writelines('\tdefault:\n')
            file.writelines('\t\tbreak;\n')
            file.writelines('\t}\n')
            file.writelines('\treturn recID;\n')
            file.writelines('}\n')
            file.writelines('\n\n')

        generate_HeadFileInclude(self._binutilSourcePath, stdHeadList, cusHeadList, True)
        generate_description(self._binutilSourcePath)

    def Gen_MonitorutilHeader(self):
        stdHeadList = ['stdint.h',
                       'stdbool.h']
        cusHeadList = []

        # TODO 需要处理换行符导致的字符编码警告
        with open(self._monitorutilHeaderPath, mode='w', encoding='utf-8') as file:
            file.writelines('typedef struct\n'
                            '{\n'
                            '\t// 报文周期，单位毫秒（ms）。\n'
                            '\tconst uint32_t cycle;\n'
                            '\n'
                            '\t// 报文周期计时，单位毫秒（ms）。\n'
                            '\tuint32_t cycle_cnt;\n'
                            '\n'
                            '\t// 周期循环执行函数。\n'
                            '\tvoid(*CycleOverFunc)(void);\n'
                            '\n'
                            '\t// 当最后一帧报文被接收的时候保存时值。\n'
                            '\tuint32_t last_cycle;\n'
                            '\n'
                            '\t// 报文的最大超时时间，单位毫秒（ms）。\n'
                            '\tconst uint32_t timeout_cycle;\n'
                            '\n'
                            '\t// 报文超时计数，单位毫秒（ms）。\n'
                            '\tuint32_t timeout_cnt;\n'
                            '\n'
                            '\t// 超时执行函数。\n'
                            '\tvoid(*TimeoutFunc)(void);\n'
                            '\n'
                            '\t// 记录最近的一帧报文的数据。\n'
                            # '\tuint32_t frame_cnt;\n'
                            '\n'
                            '\t// 记录接收到的报文帧数。\n'
                            '\tuint32_t frame_cnt;\n'
                            '\n'
                            '\t// 该位表示收到CAN帧的实际长度与CAN矩阵定义的长度不符。\n'
                            '\tbool dlc_error;\n'
                            '\n'
                            '\t// 调用周期定时执行函数\n'
                            '\tvoid(*TimingFunc)(void);\n'
                            '} ')
            file.writelines(f'{self._callBackName}_FrameMonitor_t;\n')
            file.writelines('\n\n')

            file.writelines('/*\n'
                            '* 执行解包时将调用此函数。\n'
                            '* 返回值将保存在@last_cycle变量中。表示某条报文最后一次接收到的时间。\n'
                            '*/\n')
            file.writelines(f'uint32_t {self._callBackName}_GetSystemTick(void);\n')
            file.writelines('\n\n')

            file.writelines('/*\n'
                            '* 重置监视器计时。\n'
                            '* 重置以下变量:\n'
                            '* @cycle_cnt、@timeout_cnt\n'
                            '*/\n')
            file.writelines(f'void {self._callBackName}_ResetMonitor({self._callBackName}_FrameMonitor_t* monitor);')

        generate_HeadFileInclude(self._monitorutilHeaderPath, stdHeadList, cusHeadList, True)
        generate_HeadFileIfndef(self._monitorutilHeaderPath)
        generate_description(self._monitorutilHeaderPath)

    def Gen_MonitorutilSource(self):
        stdHeadList = []
        cusHeadList = [self._monitorutilHeaderName]

        with open(self._monitorutilSourcePath, mode='w', encoding='utf-8') as file:
            file.writelines(f'uint32_t {self._callBackName}_GetSystemTick(void)\n'
                            '{\n'
                            '\treturn 0;\n'
                            '}\n')
            file.writelines('\n\n')

            file.writelines(f'void {self._callBackName}_ResetMonitor({self._callBackName}_FrameMonitor_t* monitor)\n'
                            '{\n'
                            '\tmonitor->cycle_cnt = 0;\n'
                            '\tmonitor->timeout_cnt = 0;\n'
                            '}\n')
            file.writelines('\n\n')

        generate_HeadFileInclude(self._monitorutilSourcePath, stdHeadList, cusHeadList, True)
        generate_description(self._monitorutilSourcePath)

    def Gen_CycleActHeader(self):
        stdHeadList = []
        cusHeadList = [self._monitorutilHeaderName]

        with open(self._cycleactHeaderPath, mode='w', encoding='utf-8') as file:
            file.writelines('/*\n'
                            '* 该函数用来放需要进行周期动作的信号报文。\n'
                            '* 需要自行添加。\n'
                            '*/\n')
            file.writelines('void CycleActFunc(void);\n')
            file.writelines('\n\n')

            file.writelines('/*\n'
                            '* 该函数用来执行具体的周期动作。\n'
                            '*/\n')
            file.writelines(f'void RegularlyCallFunc({self._callBackName}_FrameMonitor_t* monitor);\n')

        generate_HeadFileInclude(self._cycleactHeaderPath, stdHeadList, cusHeadList, True)
        generate_HeadFileIfndef(self._cycleactHeaderPath)
        generate_description(self._cycleactHeaderPath)

    def Gen_CycleActSource(self):
        stdHeadList = []
        cusHeadList = [self._cycleactHeaderName,
                       self._configHeaderName,
                       self._binutilHeaderName]

        with open(self._cycleactSourcePath, mode='w', encoding='utf-8') as file:
            file.writelines('void CycleActFunc(void)\n'
                            '{\n'
                            '\n'
                            '}\n\n')

            file.writelines(
                f'void RegularlyCallFunc({self._callBackName}_FrameMonitor_t* monitor)\n'
                '{\n'
                '\tmonitor->timeout_cnt += CYCLE_FACTOR;\n'
                '\tmonitor->cycle_cnt += CYCLE_FACTOR;\n'
                '\n'
                '\tif(monitor->timeout_cnt >= monitor->timeout_cycle){\n'
                '\t\tmonitor->timeout_cnt = monitor->timeout_cycle;\n'
                '\t\tmonitor->TimeoutFunc();\n'
                '\t}\n'
                '\n'
                '\tmonitor->TimingFunc();\n'
                '\n'
                '\tif(monitor->cycle_cnt >= monitor->cycle){\n'
                '\t\tmonitor->cycle_cnt = 0;\n'
                '\t\tmonitor->CycleOverFunc();\n'
                '\t}\n'
                '}\n\n\n')

        generate_HeadFileInclude(self._cycleactSourcePath, stdHeadList, cusHeadList, True)
        generate_description(self._cycleactSourcePath)

    def Gen_ConfigHeader(self):
        with open(self._configHeaderPath, mode='w', encoding='utf-8') as file:
            file.writelines('/*\n'
                            '* 该宏定义是信号报文周期相关功能的系数。与信号报文的发送，信号报文的超时处理相关。\n'
                            f'* 该值代表{self._callBackName}_Cyc_Transmit(void)函数每次执行的间隔（调用周期），单位为毫秒（ms）。\n'
                            '* 总累加时间 = 当前累加时间 + 周期系数;\n'
                            f'* 当总累加时间超过报文周期，会执行{self._MsgCycAOPHeaderName}中的以CycleOverFunc以前缀的方法，通常在这里执行发送信号报文。\n'
                            f'* 当总累加时间大于超时时间，会执行{self._MsgCycAOPHeaderName}中的以TimeoutFunc为前缀的方法，通常在这里执行超时处理。\n'
                            '*/\n')
            file.writelines('#define CYCLE_FACTOR (10U)\n')

        generate_HeadFileIfndef(self._configHeaderPath)
        generate_description(self._configHeaderPath)

    def Gen_MsgParseAOPHeader(self):
        with open(self._MsgParseAOPHeaderPath, mode='w', encoding='utf-8') as file:
            for message in sorted(self.db.messages, key=lambda x: x.frame_id):
                # 解析前执行函数
                file.writelines(f'void BeforeParse_{self._callBackName}_{message.name}(void);\n')
                # 解析后执行函数
                file.writelines(f'void AfterParse_{self._callBackName}_{message.name}(void);\n')
                # 换行
                file.writelines('\n')

        generate_HeadFileIfndef(self._MsgParseAOPHeaderPath)
        generate_description(self._MsgParseAOPHeaderPath)

    def Gen_MsgParseAOPSource(self):
        stdHeadList = []
        cusHeadList = [self._MsgParseAOPHeaderName,
                       self._binutilHeaderName]

        with open(self._MsgParseAOPSourcePath, mode='w', encoding='utf-8') as file:
            for message in sorted(self.db.messages, key=lambda x: x.frame_id):
                # 注释说明
                messageComment = PrettyTable()
                messageComment.field_names = ["Name", "ID"]
                messageComment.add_row([message.name, f'0x{message.frame_id:x}'])
                file.writelines(f'/*\n'
                                f'{messageComment}\n'
                                f'*/\n')
                # 解析前执行函数
                file.writelines(f'void BeforeParse_{self._callBackName}_{message.name}(void)\n'
                                '{\n'
                                '\n'
                                '}\n\n')
                # 解析后执行函数
                file.writelines(f'void AfterParse_{self._callBackName}_{message.name}(void)\n'
                                '{\n'
                                '\n'
                                '}\n\n')
                # 换行
                file.writelines('\n')

        generate_HeadFileInclude(self._MsgParseAOPSourcePath, stdHeadList, cusHeadList, True)

    def Gen_MsgCycAOPHeader(self):
        with open(self._MsgCycAOPHeaderPath, mode='w', encoding='utf-8') as file:
            for message in sorted(self.db.messages, key=lambda x: x.frame_id):
                # 超时执行函数
                file.writelines(f'void {self._callBackName}_TimeoutFunc_{message.name}(void);\n')
                # 调用周期定时执行函数
                file.writelines(f'void {self._callBackName}_TimingFunc_{message.name}(void);\n')
                # 周期循环执行函数
                file.writelines(f'void {self._callBackName}_CycleOverFunc_{message.name}(void);\n')
                # 换行
                file.writelines('\n')

        generate_HeadFileIfndef(self._MsgCycAOPHeaderPath)
        generate_description(self._MsgCycAOPHeaderPath)

    def Gen_MsgCycAOPSource(self):
        stdHeadList = []
        cusHeadList = [self._MsgCycAOPHeaderName,
                       self._binutilHeaderName]

        with open(self._MsgCycAOPSourcePath, mode='w', encoding='utf-8') as file:
            for message in sorted(self.db.messages, key=lambda x: x.frame_id):
                # 注释说明
                messageComment = PrettyTable()
                messageComment.field_names = ["Name", "ID"]
                messageComment.add_row([message.name, f'0x{message.frame_id:x}'])
                file.writelines(f'/*\n'
                                f'{messageComment}\n'
                                f'*/\n')
                # 超时执行函数
                file.writelines(f'void {self._callBackName}_TimeoutFunc_{message.name}(void)\n'
                                '{\n'
                                '\n'
                                '}\n\n')
                # 调用周期定时执行函数
                file.writelines(f'void {self._callBackName}_TimingFunc_{message.name}(void)\n'
                                '{\n'
                                '\n'
                                '}\n\n')
                # 周期循环执行函数
                file.writelines(f'void {self._callBackName}_CycleOverFunc_{message.name}(void)\n'
                                '{\n'
                                '\n'
                                '}\n\n')
                # 换行
                file.writelines('\n')

        generate_HeadFileInclude(self._MsgCycAOPSourcePath, stdHeadList, cusHeadList, True)
