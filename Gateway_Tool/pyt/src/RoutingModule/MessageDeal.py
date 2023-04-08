import re

from pyt.src.config.RouteConfig import RouteConfig


def make_upper(aMessage: list) -> None:
    """
    将报文中所有元素转为大写（如果元素是字符串类型）。
    :return: None
    """
    for i in range(len(aMessage)):
        if isinstance(aMessage[i], str):
            aMessage[i] = aMessage[i].upper()


def blank_remove(aMessage: list) -> None:
    """
    移除报文中所有元素的空格（如果元素是字符串类型）。
    :return: None
    """
    pattern = re.compile(r'\s+')
    for i in range(len(aMessage)):
        if isinstance(aMessage[i], str):
            aMessage[i] = re.sub(pattern, '', aMessage[i])


def format_message(aMessage: list) -> list:
    """
    格式化报文。
    清除对象中所有的空格；将对象中所有的值转为大写，若报文id为十六进制数则第二个字符为小写，例如0xAAAAAAAA；将标定转换为1或0。
    :return: 报文本身
    """

    ATTRIBUTE_DICT = RouteConfig().ATTRIBUTE_DICT

    # 清除报文中所有的空格
    blank_remove(aMessage)
    # 将报文的字符串全部转为大写
    make_upper(aMessage)

    # 如果id是个十六进制数，则将大写的“X”变为小写的“x”
    id_index = ATTRIBUTE_DICT['id']
    if hex_verification(aMessage, id_index):
        aMessage[id_index] = aMessage[id_index].replace('X', 'x')

    # 如果dlc是个字符串数值，则换成整形数值。
    dle_index = ATTRIBUTE_DICT['dlc']
    if dlc_verification(aMessage):
        aMessage[dle_index] = int(aMessage[dle_index])

    # 如果周期是个字符串数值，则换成整形数值。
    time_index = ATTRIBUTE_DICT['time']
    if time_verification(aMessage):
        aMessage[time_index] = int(aMessage[time_index])

    # 将主要属性以外的标定使用的None值替换为0，“Y”或“y”替换为1。
    for i in range(len(aMessage)):
        if i not in ATTRIBUTE_DICT.values():
            if aMessage[i] is None:
                aMessage[i] = 0
            if aMessage[i] == 'Y' or aMessage[i] == 'y':
                aMessage[i] = 1

    return aMessage


def find_error(aMessage) -> list:
    ATTRIBUTE_DICT = RouteConfig().ATTRIBUTE_DICT

    error_cell = []  # 为意外值的单元格列表

    # 源地址是否在给定值中，否则在error_cell[]列表中添加该值下标。
    if not source_verification(aMessage):
        error_cell.append(ATTRIBUTE_DICT['source'])

    # 目标地址是否在给定值中，否则在error_cell[]列表中添加该值下标。
    if not target_verification(aMessage):
        error_cell.append(ATTRIBUTE_DICT['target'])

    # 报文id不是十六进制值，否则在error_cell[]列表中添加该值下标。
    if not id_8B_verification(aMessage) and not id_3B_verification:
        error_cell.append(ATTRIBUTE_DICT['id'])

    # dlc是否在给定值中，否则在error_cell[]列表中添加该值下标。
    if not dlc_verification(aMessage):
        error_cell.append(ATTRIBUTE_DICT['dlc'])

    # 周期是否是一个数值，否则在error_cell[]列表中添加该值下标。
    if not time_verification(aMessage):
        error_cell.append(ATTRIBUTE_DICT['time'])

    # 标定的变量是否除了0和1以外还有意外值，否则在error_cell[]列表中添加该值下标。
    if not calibration_verification(aMessage):
        for i in range(len(aMessage)):
            # 除了主要属性以外的值都视为标定项，判断是否为1或0。
            if i not in ATTRIBUTE_DICT.values():
                if aMessage[i] != 0 and aMessage[i] != 1:
                    error_cell.append(i)

    return error_cell


def hex_verification(aMessage: list, index: int, id_length: int = None) -> bool:
    """
    十六进制值验证。检查报文某个数据是否为符合给定字符串长度的十六进制数。默认为不限制长度
    如果该值是字符串，且以”0x“开头，且为10个字符串长度（8个字节）的十六进制则返回True，否则返回False。
    参考：
    https://blog.csdn.net/guaguastd/article/details/38920565
    https://www.cnblogs.com/xp1315458571/p/13720333.html
    :param aMessage:
    :param index: 报文的下标
    :param id_length: id长度。
    :return: True or False
    """
    if isinstance(aMessage[index], str):
        if id_length:
            # 限制为给定字符长度（例如8个字节，也就是0x00000000）。忽略大小写。
            pattern = re.compile('\\b0x[0-9a-fA-F]{%s}\\b' % id_length, flags=re.IGNORECASE)
        else:
            # 不限制字符串长度。忽略大小写。
            pattern = re.compile(r'\b0x[0-9a-fA-F]+\b', flags=re.IGNORECASE)
        if pattern.match(aMessage[index]):
            return True
        else:
            return False
    else:
        return False


def id_3B_verification(aMessage: list) -> bool:
    """
    报文id的数据验证。检查报文的id是否符合3个字节十六进制值，例如0x000。
    如果是返回True，否则返回False。
    :return: True or False
    """
    ATTRIBUTE_DICT = RouteConfig().ATTRIBUTE_DICT
    if hex_verification(aMessage, ATTRIBUTE_DICT['id'], 3):
        return True
    else:
        return False


def id_8B_verification(aMessage: list) -> bool:
    """
    报文id的数据验证。检查报文的id是否符合8个字节的十六进制值，例如0x00000000。
    如果是返回True，否则返回False。
    :return: True or False
    """
    ATTRIBUTE_DICT = RouteConfig().ATTRIBUTE_DICT
    if hex_verification(aMessage, ATTRIBUTE_DICT['id'], 8):
        return True
    else:
        return False


def source_verification(aMessage: list) -> bool:
    """
    报文源地址的数据验证，检查报文的源地址是否符合给定的值。
    如果是返回True，否则返回False。
    :return: True or False
    """
    ATTRIBUTE_DICT = RouteConfig().ATTRIBUTE_DICT
    if aMessage[ATTRIBUTE_DICT['source']] in RouteConfig().CHANNEL_MAPPING:
        return True
    else:
        return False


def target_verification(aMessage: list) -> bool:
    """
    报文目标地址的数据验证。检查报文的目标地址是否符合给定的值。
    如果是返回True，否则返回False。
    :return: True or False
    """
    ATTRIBUTE_DICT = RouteConfig().ATTRIBUTE_DICT
    if aMessage[ATTRIBUTE_DICT['target']] in RouteConfig().CHANNEL_MAPPING:
        return True
    else:
        return False


def dlc_verification(aMessage: list) -> bool:
    """
    报文dlc的数据验证。检查报文的dlc是否符合给定的值。
    如果是返回True，否则返回False。
    :return: True or False
    """
    ATTRIBUTE_DICT = RouteConfig().ATTRIBUTE_DICT
    DLC = RouteConfig().DLC
    if (str(aMessage[ATTRIBUTE_DICT['dlc']]) in DLC) or (aMessage[ATTRIBUTE_DICT['dlc']] in DLC.values()):
        return True
    else:
        return False


def time_verification(aMessage: list) -> bool:
    """
    报文周期的数据验证。检查报文的周期是否是一个数值。
    如果是返回True，否则返回False。
    :return: True or False
    """
    ATTRIBUTE_DICT = RouteConfig().ATTRIBUTE_DICT
    if isinstance(aMessage[ATTRIBUTE_DICT['time']], int):
        return True
    elif isinstance(aMessage[ATTRIBUTE_DICT['time']], str) and aMessage[ATTRIBUTE_DICT['time']].isdigit():
        return True
    elif isinstance(aMessage[ATTRIBUTE_DICT['time']], float) and aMessage[ATTRIBUTE_DICT['time']].is_integer():
        return True
    else:
        return False


def calibration_verification(aMessage) -> bool:
    """
    报文标定位的数据验证。检查报文的所有标志位是否只由1或0组成。
    如果是返回True，否则返回False。
    :return: True or False
    """
    ATTRIBUTE_DICT = RouteConfig().ATTRIBUTE_DICT
    for i in range(len(aMessage)):
        if i not in ATTRIBUTE_DICT.values():
            if aMessage[i] != 0 and aMessage[i] != 1:
                return False
    return True
