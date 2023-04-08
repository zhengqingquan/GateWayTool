SIGNAL_TYPE = {
    'signed': 'signed',
    'unsigned': 'unsigned',
    'IEEE Fload': 'IEEE Fload',
    'IEEE Double': 'IEEE Double'
}

C_STDINT = {
    8: 'int8_t',
    16: 'int16_t',
    32: 'int32_t',
    64: 'int64_t'
}

# CANdb++支持信号名称最大为32个字符
MAX_SIG_NAME_LEN = 32


def LengthToStdint(length, is_signed):
    """
    将长度转为C标准库格式。
    """
    if length in range(1, 9):
        temp = 8
    elif length in range(9, 17):
        temp = 16
    elif length in range(17, 33):
        temp = 32
    elif length in range(33, 65):
        temp = 64
    else:
        raise ValueError('长度错误。')

    return f'{C_STDINT[temp]}' if is_signed else f'u{C_STDINT[temp]}'


def DBCMotorolaStartBitShift(StartBit: int, Length: int):
    """
    大端模式的开始位进行转换
    dbc文件在摩托罗拉格式下开始位的设计不一致，因此需要使用该方法进行转换
    在dbc文件中，计算的均为msb位的下标。但显示的为lsb。
    根据msb计算lsb
    """
    # 信号开始位取余，表示该信号的开始位在当前字节的比特位。若其长度不够放，表示该信号需要至少两个字节来承载。
    if StartBit % 8 >= Length - 1:
        StartBit = StartBit - Length + 1
    else:
        for i in range(Length - 1):
            StartBit = StartBit - 1
            if StartBit % 8 == 7:
                StartBit = StartBit + 16
    return StartBit


def DBCMotorolaEndBitShift(StartBit: int, Length: int):
    """
    计算大端模式的结束位
    根据lsb计算msb
    """

    if StartBit % 8 + Length <= 8:
        StartBit = StartBit + Length - 1
    else:
        for i in range(Length - 1):
            StartBit = StartBit + 1
            if StartBit % 8 == 0:
                StartBit = StartBit - 16

    return StartBit


def CalculationMask(start, length):
    """
    计算掩码
    """
    temp2 = 0
    for e in range(length):
        temp2 = (1 << start) + temp2
        start += 1
    return temp2


def FormatHexStr(hexValue):
    if hexValue < 0x10:
        return '0x0' + f'{hexValue:x}'.upper() + 'U'
    else:
        return '0x' + f'{hexValue:x}'.upper() + 'U'


def IntelUnpackToStr(start, length):
    """
    开始位为0-63根据DLC来看。
    """

    comStr = ''
    # 信号开始位取余并加上信号长度，当该值大于8时，表示该信号需要至少两个字节来承载。
    if (start % 8 + length) > 8:
        # 当跨了两个或以上字节时，需要分别计算不同字节的情况，最后拼接字符串
        # 下面分别计算了跨字节情况时，第一段字节、最后一字节、中间段字节的情况
        # 例如，某个信号需要三个字节，会分别计算三个字节的条件，最后拼接字符串
        x = range(start // 8, (start + length - 1) // 8 + 1)
        for rangeIndex, byteIndex in enumerate(x):
            if byteIndex == x[0]:
                # 获得在字节内的开始位
                inByteStart = start % 8
                # 获得在字节内的长度
                inByteLength = 8 - inByteStart
                # 获得格式化后的十六进制掩码字符串
                hexMaskStr = FormatHexStr(CalculationMask(inByteStart, inByteLength))
                # 获得右移量
                rightMoveAmount = inByteStart
                # 拼接字符串
                if inByteLength < 8:
                    comStr = f'((_data[{byteIndex}] & {hexMaskStr}) >> {rightMoveAmount})'
                else:
                    comStr = f'(_data[{byteIndex}] & {hexMaskStr})'
            elif byteIndex == x[-1]:
                # 获得在字节内的开始位
                inByteStart = 0
                # 获得在字节内的长度
                inByteLength = (start + length) % 8
                # 获得格式化后的十六进制掩码字符串
                # 获得左移量
                if inByteLength == 0:
                    hexMaskStr = FormatHexStr(CalculationMask(inByteStart, 8))
                    leftMoveAmount = length - 8
                else:
                    hexMaskStr = FormatHexStr(CalculationMask(inByteStart, inByteLength))
                    leftMoveAmount = length - inByteLength
                # 拼接字符串
                comStr = f'((_data[{byteIndex}] & {hexMaskStr}) << {leftMoveAmount}) | {comStr}'
            else:
                # 获得在字节内的开始位
                inByteStart = 0
                # 获得在字节内的长度
                inByteLength = 8
                # 获得格式化后的十六进制掩码字符串
                hexMaskStr = FormatHexStr(CalculationMask(inByteStart, inByteLength))
                # 获得左移量
                leftMoveAmount = - (start % 8) + (rangeIndex * 8)
                # 拼接字符串
                comStr = f'(_data[{byteIndex}] & {hexMaskStr}) << {leftMoveAmount} | {comStr}'
    else:
        inByteStart = start % 8
        hexMaskStr = FormatHexStr(CalculationMask(inByteStart, length))
        if inByteStart == 0:
            comStr = f'_data[{start // 8}] & {hexMaskStr}'
        else:
            rightMoveAmount = inByteStart
            comStr = f'(_data[{start // 8}] & {hexMaskStr}) >> {rightMoveAmount}'

    return comStr


def IntelPackToStr(signalName, start, length):
    comStr = ''
    # 信号开始位取余并加上信号长度，当该值大于8时，表示该信号需要至少两个字节来承载。
    if (start % 8 + length) > 8:
        x = range(start // 8, (start + length - 1) // 8 + 1)
        for rangeIndex, byteIndex in enumerate(x):
            # 当跨了两个或以上字节时，需要分别计算不同字节的情况，最后拼接字符串
            # 下面分别计算了跨字节情况时，第一段字节、最后一字节、中间段字节的情况
            # 例如，某个信号需要三个字节，会分别计算三个字节的条件，最后拼接字符串

            # 使用掩码取信号中的值
            # 把值进行左移或右移
            # 把值填入报文的字节
            if byteIndex == x[0]:
                # 获得在字节内的开始位
                inByteStart = start % 8
                # 获得在字节内的长度
                inByteLength = 8 - inByteStart
                # 获得格式化后的十六进制掩码字符串
                hexMaskStr = FormatHexStr(CalculationMask(0, inByteLength))
                # 获得左移量
                leftMoveAmount = inByteStart
                if inByteLength == 8:
                    comStr = f'_data[{byteIndex}] |= _message->{signalName} & {hexMaskStr};\n'
                else:
                    comStr = f'_data[{byteIndex}] |= (_message->{signalName} & {hexMaskStr}) << {leftMoveAmount};'
            elif byteIndex == x[-1]:
                # 获得在字节内的开始位
                inByteStart = 0
                # 获得在字节内的长度
                inByteLength = (start + length) % 8
                # 获得右移量
                # 获得格式化后的十六进制掩码字符串
                if inByteLength == 0:
                    rightMoveAmount = length - 8
                    hexMaskStr = FormatHexStr(CalculationMask(inByteStart, 8))
                else:
                    rightMoveAmount = length - inByteLength
                    hexMaskStr = FormatHexStr(CalculationMask(inByteStart, inByteLength))
                # 拼接字符串
                comStr = f'{comStr}\n' \
                         f'\t_data[{byteIndex}] |= (_message->{signalName} >> {rightMoveAmount}) & {hexMaskStr};'
            else:
                # 获得在字节内的开始位
                inByteStart = 0
                # 获得在字节内的长度
                inByteLength = 8
                # 获得格式化后的十六进制掩码字符串
                hexMaskStr = FormatHexStr(CalculationMask(inByteStart, inByteLength))
                # 获得右移量
                rightMoveAmount = - (start % 8) + (rangeIndex * 8)
                # 拼接字符串
                comStr = f'{comStr}\n' \
                         f'\t_data[{byteIndex}] |= (_message->{signalName} >> {rightMoveAmount}) & {hexMaskStr};'
    else:
        # 获得在字节内的开始位
        inByteStart = start % 8
        # 获得该字节在字节数组中的下标
        byteIndex = start // 8
        # 拼接字符串。若字节内的开始位为0，不需要信号值左移；若不为0，则需要。
        if inByteStart == 0:
            comStr = f'_data[{byteIndex}] |= _message->{signalName};'
        else:
            # 获得左移量
            leftMoveAmount = inByteStart
            comStr = f'_data[{byteIndex}] |= _message->{signalName} << {leftMoveAmount};'

    return comStr


def MotorolaUnpackToStr(start, length):
    """
    dbc文件对于Motorola格式使用的是Motorola msb的方式存储，在CANdb++中默认使用Motorola lsb显示。
    开始位为0-63。
    即参数start为msb。
    """

    comStr = ''
    # 信号开始位取余并加上信号长度，当该值大于8时，表示该信号需要至少两个字节来承载。
    if (start % 8 + length) > 8:
        # 当跨了两个或以上字节时，需要分别计算不同字节的情况，最后拼接字符串
        # 下面分别计算了跨字节情况时，第一段字节、最后一字节、中间段字节的情况
        # 例如，某个信号需要三个字节，会分别计算三个字节的条件，最后拼接字符串
        msbStart = DBCMotorolaEndBitShift(start, length)
        x = range(msbStart // 8, start // 8 + 1)
        for rangeIndex, byteIndex in enumerate(x):
            if byteIndex == x[0]:
                # 获得在字节内的开始位
                inByteStart = 0
                # 获得在字节内的长度
                inByteLength = (start + length) % 8
                # 获得格式化后的十六进制掩码字符串
                if inByteLength == 0:
                    hexMaskStr = FormatHexStr(CalculationMask(inByteStart, 8))
                    leftMoveAmount = length - 8
                else:
                    hexMaskStr = FormatHexStr(CalculationMask(inByteStart, inByteLength))
                    # 获取左移量
                    leftMoveAmount = length - inByteLength
                # 拼接字符串
                comStr = f'(_data[{byteIndex}] & {hexMaskStr}) << {leftMoveAmount}'
            elif byteIndex == x[-1]:
                # 获得在字节内的开始位
                inByteStart = start % 8
                # 获得在字节内的长度
                inByteLength = 8 - inByteStart
                # 获得格式化后的十六进制掩码字符串
                hexMaskStr = FormatHexStr(CalculationMask(inByteStart, inByteLength))
                # 获得右移量
                rightMoveAmount = inByteStart
                # 拼接字符串
                if rightMoveAmount == 0:
                    comStr = f'{comStr} | (_data[{byteIndex}] & {hexMaskStr})'
                else:
                    comStr = f'{comStr} | (_data[{byteIndex}] & {hexMaskStr}) >> {rightMoveAmount}'
            else:
                # 获得在字节内的开始位
                inByteStart = 0
                # 获得在字节内的长度
                inByteLength = 8
                # 获得格式化后的十六进制掩码字符串
                hexMaskStr = FormatHexStr(CalculationMask(inByteStart, inByteLength))
                # 获得左移量
                if (start + length) % 8 == 0:
                    leftMoveAmount = length - 8 - (rangeIndex * 8)
                else:
                    leftMoveAmount = length - (start + length) % 8 - (rangeIndex * 8)
                # 拼接字符串
                comStr = f'{comStr} | (_data[{byteIndex}] & {hexMaskStr}) << {leftMoveAmount}'
    else:
        inByteStart = start % 8
        hexMaskStr = FormatHexStr(CalculationMask(inByteStart, length))
        if inByteStart == 0:
            comStr = f'_data[{start // 8}] & {hexMaskStr}'
        else:
            rightMoveAmount = inByteStart
            comStr = f'(_data[{start // 8}] & {hexMaskStr}) >> {rightMoveAmount}'

    return comStr


def MotorolaPackToStr(signalName, start, length, isIndent=False):
    """
    dbc文件对于Motorola格式使用的是Motorola msb的方式存储，在CANdb++中默认使用Motorola lsb显示。
    即参数start为msb。
    """
    comStr = ''
    # 信号开始位取余并加上信号长度，当该值大于8时，表示该信号需要至少两个字节来承载。
    if (start % 8 + length) > 8:
        # x表示开始到结束的字节范围。
        # range函数为左开右闭，因此第二个参数后面加1。
        msbStart = DBCMotorolaEndBitShift(start, length)
        x = range(msbStart // 8, start // 8 + 1)
        for rangeIndex, byteIndex in enumerate(x):
            # 当跨了两个或以上字节时，需要分别计算不同字节的情况，最后拼接字符串
            # 下面分别计算了跨字节情况时，第一段字节、最后一字节、中间段字节的情况
            # 例如，某个信号需要三个字节，会分别计算三个字节的条件，最后拼接字符串

            # 使用掩码取信号中的值
            # 把值进行左移或右移
            # 把值填入报文的字节
            if byteIndex == x[0]:
                # 获得在字节内的开始位
                inByteStart = 0
                # 获得在字节内的长度
                inByteLength = (start + length) % 8
                # 获得格式化后的十六进制掩码字符串
                if inByteLength == 0:
                    hexMaskStr = FormatHexStr(CalculationMask(inByteStart, 8))
                    rightMoveAmount = length - 8
                else:
                    hexMaskStr = FormatHexStr(CalculationMask(inByteStart, inByteLength))
                    # 获得右移量
                    rightMoveAmount = length - inByteLength
                # 拼接字符串
                comStr = f'_data[{byteIndex}] |= (_message->{signalName} >> {rightMoveAmount}) & {hexMaskStr};'
            elif byteIndex == x[-1]:
                # 获得在字节内的开始位
                inByteStart = start % 8
                # 获得在字节内的长度
                inByteLength = 8 - inByteStart
                # 获得格式化后的十六进制掩码字符串
                hexMaskStr = FormatHexStr(CalculationMask(inByteStart, inByteLength))
                if inByteStart == 0:
                    # 拼接字符串
                    comStr = f'{comStr}\n' \
                             f'\t_data[{byteIndex}] |= _message->{signalName} & {hexMaskStr};'
                else:
                    # 获取左移量
                    leftMoveAmount = inByteLength
                    # 拼接字符串
                    comStr = f'{comStr}\n' \
                             f'\t_data[{byteIndex}] |= (_message->{signalName} << {leftMoveAmount}) & {hexMaskStr};'

            else:
                # 获得在字节内的开始位
                inByteStart = 0
                # 获得在字节内的长度
                inByteLength = 8
                # 获得格式化后的十六进制掩码字符串
                hexMaskStr = FormatHexStr(CalculationMask(inByteStart, inByteLength))
                # 获得右移量
                if (start + length) % 8 == 0:
                    rightMoveAmount = length - 8 - (rangeIndex * 8)
                else:
                    rightMoveAmount = length - (start + length) % 8 - (rangeIndex * 8)
                # 拼接字符串
                comStr = f'{comStr}\n' \
                         f'\t_data[{byteIndex}] |= (_message->{signalName} >> {rightMoveAmount}) & {hexMaskStr};'
    else:
        # 获得在字节内的开始位
        inByteStart = start % 8
        # 获得该字节在字节数组中的下标
        byteIndex = start // 8
        # 拼接字符串。若字节内的开始位为0，不需要信号值左移；若不为0，则需要。
        if inByteStart == 0:
            comStr = f'_data[{byteIndex}] |= _message->{signalName};'
        else:
            # 获得左移量
            leftMoveAmount = inByteStart
            comStr = f'_data[{byteIndex}] |= _message->{signalName} << {leftMoveAmount};'

    return comStr
