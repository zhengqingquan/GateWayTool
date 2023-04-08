"""
该类废弃。仅用作参考学习。

报文类
"""

import re
from typing import List

DLC = {
    '3': 3,
    '8': 8,
    '17': 17,
    '39': 39,
}
CHANNEL_MAPPING = {
    'H_CAN': 0,
    'D_CAN': 1,
    'T_CAN': 2,
    'B_CAN': 3,
    'I_CAN': 4,
    'C_CAN': 5,
}


class MessageListClass(List):
    """
    报文列表MessageListClass类，继承自list类。
    可以尝试选择继承字典类。但字典的键值对必须得有键才能有值，在初始化的时候不能出现键值未定的情况，因此选择使用继承列表类。
    MessageListClass对象会按照属性MessageListClass.attribute_dict{}字典的键值对进行对象的初始化。
    其中字典的键代表属性名称，而值代表该属性在对象MessageListClass中的下标位置。
    MessageListClass类有5个关键属性，分别是：source、id、target、dlc、time。
    可以使用关键字参数对MessageListClass对象进行初始化。
    构造方法会按照MessageListClass.attribute_dict{}字典的键值对，把关键字参数分别赋值到对象列表MessageListClass的对应下标位置中。
    例如在字典的键值对{'source':5}，那关键字变量<source='H_CAN'>会被赋值到对象MessageListClass下标为5的位置。
    也就是MessageListClass[5]='H_CAN'

    类MessageListClass的初始化可以使用自定义参数的长度，但在初始化时关键字参数的等级会高于位置参数。

    可以使用MessageListClass.source来访问对象的关键属性。但关键属性为只读属性，无法通过外部调用修改。
    但可以使用列表[]的方式修改，例如self['source']=‘H_CAN’，这同样会修改报文的self.source属性。
    而属性的访问方式可以使用self.source，也可以使用self['source']。

    初始化有以下几种方式：
    方式一，创建空的报文，长度取决于属性_attribute_dict中的最大值：
    MessageListClass() → [None, None, None, ...]
    方式二，使用位置参数创建带有值的报文，长度取决于属性_attribute_dict和位置参数数量的最大值：
    MessageListClass(arg1, arg2, arg3, ...) → [arg1, arg2, arg3, ...]
    方式三，使用关键字参数创建带由值的报文，长度取决于关键属性_attribute_dict中的最大值：
    MessageListClass(source=arg1, id=arg2, dlc=arg3, ...) → [arg1, arg2, arg3, ...]
    方式四，创建带有值的报文：
    MessageListClass(*list[]) → [list[0], list[1], list[2], ...]
    方式五，使用列表创建报文：
    MessageListClass([source, id, dlc, ...])
    """
    _source = None
    _id = None
    _target = None
    _dlc = None
    _time = None

    # 字典的键代表报文的属性，而值代表该属性在列表中存放的下标。
    # 例如键值对{'source': 0}表示，列表下标为0的位置上的数据代表源地址source。
    # 可以添加键值对，也可以修改值，或修改位置，但不应该修改键的字符串名称。
    # 不建议修改这部分代码。可以修改后面的值，但不应该修改其中的key值。
    # 修改这部分内容时需要注意以下内容：
    #   修改类成员属性，同时需要考虑是否设置只读属性。
    #   同步修改self.__modifier_change_attributes()方法。
    #   self.format_message()格式化的验证。
    #   self.find_error()错误列表的输出情况。
    _ATTRIBUTE_DICT = {
        'source': 0,
        'id': 1,
        'dlc': 2,
        'target': 3,
        'time': 4,
    }

    def __init__(self, *arg, **kwargs):
        """
        位置参数会按顺序被初始化。而关键字参数会被放到关键字所在的位置上。关键字参数的等级高于位置参数。
        :param arg: 位置参数，不规定长度。
        :param kwargs: 关键字参数，关键字有<source：str>、<id:str>，<target:str>，<dlc:int>，<time:int>。
        """
        list.__init__([])
        MessageListClass.__setitem__ = self.__modifier_change_attributes(MessageListClass.__setitem__)
        MessageListClass.__getitem__ = self.__modifier_access_attributes(MessageListClass.__getitem__)
        self.__message_init(*arg, **kwargs)

    def __message_init(self, *arg, **kwargs) -> None:
        """
        初始化时使用的方法。执行期间会调用self.__init()开辟长度具体的空间。
        :param arg: 初始化的位置参数
        :param kwargs: 初始化的关键字参数
        :return: None
        """
        # 如果进来的只有一个关键字参数，且为列表，则使用列表方式的初始化。
        if len(arg) == 1 and isinstance(*arg, list):
            # 这里传入的*arg表示的是一个列表，['', '', '', '', ...]
            self.__init(*arg, **kwargs)
        else:
            # 这里传入的arg表示的是一个元组，（arg1, arg2, arg3, ... ,）
            self.__init(arg, **kwargs)

    def __init(self, arg, **kwargs) -> None:
        """
        初始化时使用的方法。用来开辟具体的list长度和内存空间。
        :param arg: 初始化的位置参数
        :param kwargs: 初始化的关键字参数
        :return: None
        """
        # 字典的值转为列表
        attribute_list = list(self._ATTRIBUTE_DICT.values())
        # 对列表排序，也就是对字典的值进行排序。
        attribute_list.sort()
        # 创建一定长度的列表，列表长度取决于字典attribute_dict{}中的值与位置参数个数之间的最大值。
        # 这里+1是因为要将最大下标转为最大长度，不应该删除或更改，否则会出现下标与长度进行取最大值的错误。
        for i in range(max(attribute_list[-1] + 1, len(arg))):
            self.append(None)

        # 进行赋值
        for e in range(len(arg)):
            self[e] = arg[e]

        # 按照字典的索引重新赋值关键字参数。
        # 关键字参数的值会覆盖位置参数的值，换句话说，关键字参数的等级高于位置参数。
        # 而覆盖位置的下标取决于字典attribute_dict{}中对应的值。
        for key, value in self._ATTRIBUTE_DICT.items():
            if key in kwargs:
                self[value] = kwargs.get(f'{key}')

    def new(self, *arg, **kwargs) -> None:
        """
        重新对报文初始化，使用的方法与MessageListClass的初始化方式一样。
        :param arg: 初始化的位置参数
        :param kwargs: 初始化的关键字参数
        :return: None
        """
        self.clear()
        self.__message_init(*arg, **kwargs)

    def __iter__(self):
        """
        迭代器方法
        :return: self
        """
        self.begin = 0
        return self

    def __next__(self):
        """
        迭代器所调用的__next__方法。
        :return: self[index]
        """
        index = self.begin  # 初始值为0
        self.begin += 1  # 递增值为1

        # 下标小于最大值就返回值。
        # 否则抛出StopIteration异常，让迭代停止。
        if index < len(self):
            return self[index]
        else:
            raise StopIteration

    # 参考：
    # https://www.ucloud.cn/yun/45405.html
    # https://zhuanlan.zhihu.com/p/339718510.
    # https://blog.csdn.net/lx_ros/article/details/121216462
    def __modifier_change_attributes(self, func):
        """
        类内部修饰器。当使用列表下标[]直接访问并修改列表中的值时，会同步更改报文中的属性值。
        例如：self[0]='H_CAN'同时也会执行self.source='H_CAN'
        例如：self.source='H_CAN'同时也会执行self[0]='H_CAN'
        :param func: 被修饰的函数。
        :return: 修饰后的函数。
        """

        def wrapper(*arg, **kwargs):
            # 使用self['source']的方式访问并修改列表[0]的值。
            if arg[1] in self._ATTRIBUTE_DICT:
                arg = list(arg)
                arg[1] = self._ATTRIBUTE_DICT[arg[1]]

            # 使用self[0]的方式同时修改属性self.source的值。
            if arg[1] == self._ATTRIBUTE_DICT['source']:
                self._source = arg[2]
            if arg[1] == self._ATTRIBUTE_DICT['id']:
                self._id = arg[2]
            if arg[1] == self._ATTRIBUTE_DICT['dlc']:
                self._dlc = arg[2]
            if arg[1] == self._ATTRIBUTE_DICT['target']:
                self._target = arg[2]
            if arg[1] == self._ATTRIBUTE_DICT['time']:
                self._time = arg[2]

            # 实现__setitem__()
            func(*arg, **kwargs)

        return wrapper

    def __modifier_access_attributes(self, func):
        """
        类内部修饰器。可以直接使用['source']来访问报文属性。
        例如：self['source']相当于self.source
        :param func: 被修饰的函数。
        :return: 修饰后的函数。
        """

        def wrapper(*arg, **kwargs):
            # 使用self['source']的方式访问列表[0]的值。
            if arg[1] in self._ATTRIBUTE_DICT:
                arg = list(arg)
                arg[1] = self._ATTRIBUTE_DICT[arg[1]]

            # 实现__getitem__()
            return func(*arg, **kwargs)

        return wrapper

    @property
    def source(self):
        return self._source

    @property
    def id(self):
        return self._id

    @property
    def target(self):
        return self._target

    @property
    def dlc(self):
        return self._dlc

    @property
    def time(self):
        return self._time

    @property
    def attribute_dict(self):
        return self._ATTRIBUTE_DICT

    def format_message(self):
        """
        格式化报文。
        清楚对象中所有的空格；将对象中所有的值转为大写，若报文id为十六进制数则第二个字符为小写，例如0xAAAAAAAA；将标定转换为1或0。
        :return: 报文本身
        """

        # 清除报文中所有的空格
        self.blank_remove()
        # 将报文的字符串全部转为大写
        self.make_upper()

        # 如果id是个十六进制数，则将大写的“X”变为小写的“x”
        id_index = self._ATTRIBUTE_DICT['id']
        if self.hex_verification(id_index):
            self[id_index] = self[id_index].replace('X', 'x')

        # 如果dlc是个字符串数值，则换成整形数值。
        dle_index = self._ATTRIBUTE_DICT['dlc']
        if self._dlc_verification():
            self[dle_index] = int(self[dle_index])

        # 如果周期是个字符串数值，则换成整形数值。
        time_index = self._ATTRIBUTE_DICT['time']
        if self._time_verification():
            self[time_index] = int(self[time_index])

        # 将主要属性以外的标定使用的None值替换为0，“Y”或“y”替换为1。
        for i in range(len(self)):
            if i not in self._ATTRIBUTE_DICT.values():
                if self[i] is None:
                    self[i] = 0
                if self[i] == 'Y' or self[i] == 'y':
                    self[i] = 1

        return self

    def find_error(self):
        """
        查询列表中的意外值。
        生成空值，空白值和意外值的不符合要求的意外值的下标列表。
        :return:
        """
        none_cell = []  # 为空值的单元格列表
        empty_cell = []  # 为空白值的单元格列表
        error_cell = []  # 为错误值的单元格列表

        # 整个列表中是否有None值，或空白值
        for i in range(len(self)):
            # 寻找None值
            if self.none_verification(i):
                none_cell.append(i)
            # 寻找空白值
            if self.blank_verification(i):
                empty_cell.append(i)

        # 源地址是否在给定值中，否则在error_cell[]列表中添加该值下标。
        if not self._source_verification():
            error_cell.append(self._ATTRIBUTE_DICT['source'])

        # 目标地址是否在给定值中，否则在error_cell[]列表中添加该值下标。
        if not self._target_verification():
            error_cell.append(self._ATTRIBUTE_DICT['target'])

        # 报文id不是十六进制值，否则在error_cell[]列表中添加该值下标。
        if not self._id_8B_verification():
            error_cell.append(self._ATTRIBUTE_DICT['id'])

        # dlc是否在给定值中，否则在error_cell[]列表中添加该值下标。
        if not self._dlc_verification():
            error_cell.append(self._ATTRIBUTE_DICT['dlc'])

        # 周期是否是一个数值，否则在error_cell[]列表中添加该值下标。
        if not self._time_verification():
            error_cell.append(self._ATTRIBUTE_DICT['time'])

        # 标定的变量是否除了0和1以外还有意外值，否则在error_cell[]列表中添加该值下标。
        if not self._calibration_verification():
            for i in range(len(self)):
                # 除了主要属性以外的值都视为标定项，判断是否为1或0。
                if i not in self._ATTRIBUTE_DICT.values():
                    if self[i] != 0 and self[i] != 1:
                        error_cell.append(i)

        # 排序，方便外部调用。
        none_cell.sort()
        empty_cell.sort()
        error_cell.sort()

        return none_cell, empty_cell, error_cell

    def make_upper(self) -> None:
        """
        将报文中所有元素转为大写（如果元素是字符串类型）。
        :return: None
        """
        for i in range(len(self)):
            if isinstance(self[i], str):
                self[i] = self[i].upper()

    def blank_remove(self) -> None:
        """
        移除报文中所有元素的空格（如果元素是字符串类型）。
        :return: None
        """
        pattern = re.compile(r'\s+')
        for i in range(len(self)):
            if isinstance(self[i], str):
                self[i] = re.sub(pattern, '', self[i])

    def message_verification(self) -> bool:
        """
        报文数据验证。检查报文的数据是否都符合要求。
        :return: True or False
        """
        for unexpected_list in self.find_error():
            if len(unexpected_list):
                return False
        return True

    def none_verification(self, index) -> bool:
        """
        None值验证。检查报文某个数据是否是None值。
        如果该值是None值，则返回True，否则返回False。
        :param index: 报文的下标
        :return: True or False
        """
        if self[index] is None:
            return True
        else:
            return False

    def blank_verification(self, index) -> bool:
        """
        空白（或只含有空格）值验证。检查报文某个数据是否是空白（或只含有空格）值。
        如果该值是空白（或只含有空格）字符串，则返回True，否则返回False。
        :param index: 报文的下标
        :return: True or False
        """
        if isinstance(self[index], str):
            pattern = re.compile(r'\s+')
            if re.sub(pattern, '', self[index]) == '':
                return True
        else:
            return False

    def hex_verification(self, index, id_length: int = None) -> bool:
        """
        十六进制值验证。检查报文某个数据是否为符合给定字符串长度的十六进制数。
        如果该值是字符串，且以”0x“开头，且为10个字符串长度（8个字节）的十六进制则返回True，否则返回False。
        参考：
        https://blog.csdn.net/guaguastd/article/details/38920565
        https://www.cnblogs.com/xp1315458571/p/13720333.html
        :param index: 报文的下标
        :param id_length: id长度。
        :return: True or False
        """
        if isinstance(self[index], str):
            if id_length:
                # 限制为给定字符长度（例如8个字节，也就是0x00000000）。忽略大小写。
                pattern = re.compile('\\b0x[0-9a-fA-F]{%s}\\b' % id_length, flags=re.IGNORECASE)
            else:
                # 不限制字符串长度。忽略大小写。
                pattern = re.compile(r'\b0x[0-9a-fA-F]+\b', flags=re.IGNORECASE)
            if pattern.match(self[index]):
                return True
            else:
                return False
        else:
            return False

    def custom_verification(self, index, custom) -> bool:
        """
        自定义数据验证。检查报文某个数据是否在给定值的列表或字典custom中。
        如果该数据在custom中，返回True，否则返回False。
        :param index: 报文的下标
        :param custom: 用于验证的列表
        :return: True or False
        """
        if self[index] in custom:
            return True
        else:
            return False

    def _source_verification(self) -> bool:
        """
        报文源地址的数据验证，检查报文的源地址是否符合给定的值。
        如果是返回True，否则返回False。
        :return: True or False
        """
        if self.custom_verification(self._ATTRIBUTE_DICT['source'], CHANNEL_MAPPING):
            return True
        else:
            return False

    def _id_8B_verification(self) -> bool:
        """
        报文id的数据验证。检查报文的id是否符合8个字节的十六进制值，例如0x00000000。
        如果是返回True，否则返回False。
        :return: True or False
        """
        if self.hex_verification(self._ATTRIBUTE_DICT['id'], 8):
            return True
        else:
            return False

    def _id_3B_verification(self) -> bool:
        """
        报文id的数据验证。检查报文的id是否符合3个字节十六进制值，例如0x000。
        如果是返回True，否则返回False。
        :return: True or False
        """
        if self.hex_verification(self._ATTRIBUTE_DICT['id'], 3):
            return True
        else:
            return False

    def _target_verification(self) -> bool:
        """
        报文目标地址的数据验证。检查报文的目标地址是否符合给定的值。
        如果是返回True，否则返回False。
        :return: True or False
        """
        if self.custom_verification(self._ATTRIBUTE_DICT['target'], CHANNEL_MAPPING):
            return True
        else:
            return False

    def _dlc_verification(self) -> bool:
        """
        报文dlc的数据验证。检查报文的dlc是否符合给定的值。
        如果是返回True，否则返回False。
        :return: True or False
        """
        if (str(self[self._ATTRIBUTE_DICT['dlc']]) in DLC) or (self[self._ATTRIBUTE_DICT['dlc']] in DLC.values()):
            return True
        else:
            return False

    def _time_verification(self) -> bool:
        """
        报文周期的数据验证。检查报文的周期是否是一个数值。
        如果是返回True，否则返回False。
        :return: True or False
        """
        if str(self[self._ATTRIBUTE_DICT['time']]).isdigit():
            return True
        else:
            return False

    def _calibration_verification(self) -> bool:
        """
        报文标定位的数据验证。检查报文的所有标志位是否只由1或0组成。
        如果是返回True，否则返回False。
        :return: True or False
        """
        for i in range(len(self)):
            if i not in self._ATTRIBUTE_DICT.values():
                if self[i] != 0 and self[i] != 1:
                    return False
        return True


if __name__ == '__main__':
    print('————实例化报文————')
    message_var1 = ['h_CAN', '0xa0 000 000', 8.0, 'H_CAN', '123', 'y', 1, 1, 0]
    message_var2 = {'source': 'D_CAN'}
    print(f'位置参数：{message_var1}')
    print(f'关键字参数：{message_var2}')
    message_example = MessageListClass(*message_var1, **message_var2)
    print(f'{message_example}是否是一条合格的报文:' + str(message_example.message_verification()))
    print('————格式化报文————')
    print(f'{message_example.format_message()}是否是一条合格的报文:' + str(message_example.message_verification()))
    print('————打印意外值下标列表————')
    none_list, empty_list, error_list = message_example.find_error()
    print(f'None值下标列表：{none_list}')
    print(f'空白值下标列表：{empty_list}')
    print(f'错误值下标列表：{error_list}')
    print('————测试__setitem__————')
    message_example[1] = '0x 1561'  # 调用__setitem__
    print(f'修改后的id属性为：{message_example.id}')
    message_example['source'] = 'B_CAN'  # 调用__setitem__
    print(f'修改后的source属性为：{message_example.source}')
    print(f'{message_example}是否是一条合格的报文:' + str(message_example.message_verification()))
    print('————测试__getitem__————')
    print(message_example['id'])  # 调用__getitem__
    print(message_example[1])
    print(f'{message_example}是否是一条合格的报文:' + str(message_example.message_verification()))
    print('————打印意外值下标列表————')
    print(message_example.format_message())
    none_list, empty_list, error_list = message_example.find_error()
    print(f'None值下标列表：{none_list}')
    print(f'空白值下标列表：{empty_list}')
    print(f'错误值下标列表：{error_list}')
    print('————测试深拷贝————')
    import copy

    message_example2 = copy.deepcopy(message_example)
    message_example2.append(1312)
    print(message_example2)
    print(message_example2['id'])
