"""
该类废弃。仅用作参考学习。

路由列表类
"""

from typing import List
import copy

from pyt.Deprecated.MessageListClass import MessageListClass, CHANNEL_MAPPING


class RouteTableClass(List):
    """
    路由表类
    初始化有一下几种方式。
    方式一，创建空的路由表：
    RouteTableClass()
    方式二，创建含有一条报文的路由表：
    RouteTableClass(MessageListClass)
    方式三，创建含有多条报文的路由表：
    RouteTableClass(MessageListClass1, MessageListClass2, MessageListClass3, ...)
    方式四，创建含有多条报文的路由表：
    RouteTableClass(*MessageListClass[])
    """

    def __init__(self, *arg):
        """
        初始化方法
        :param arg:
        """
        list.__init__([])
        RouteTableClass.append = self.__append_message(RouteTableClass.append)
        RouteTableClass.__setitem__ = self.__modifier_setitem_attributes(RouteTableClass.__setitem__)
        self.__route_init(*arg)

    def __route_init(self, *arg) -> None:
        """
        位置参数会按类型和顺序被初始化。
        :param arg: 初始化的位置参数
        :param kwargs: 初始化的关键字参数
        :return: None
        """
        # 如果进来的只有一个关键字参数，且为列表，则使用列表的方式初始化。
        if len(arg) == 1 and isinstance(*arg, list):
            # 这里传入的*arg表示的是一个列表，[['','',...], '', MessageListClass1, '', ...]
            self.__init(*arg)
        else:
            # 这里传入的arg表示的是一个元组，（arg1, arg2, arg3, ... ,）
            self.__init(arg)

    def __init(self, arg) -> None:
        """
        初始化时使用的方法。用来开辟具体的list长度和内存空间。
        :param arg: 初始化的位置参数
        :return: None
        """
        # 遍历arg中的每个元素，如果是MessageListClass直接添加，否则创建新的MessageListClass实例后再添加。
        for i in arg:
            if isinstance(i, MessageListClass):
                self.append(i)
            else:
                self.append(MessageListClass(i))

    def new(self, *arg) -> None:
        """
        重新对路由表初始化，使用的方法与RouteTableClass的初始化方式一样。
        :param arg: 初始化的位置参数
        :return: None
        """
        self.clear()
        self.__route_init(*arg)

    def __modifier_setitem_attributes(self, func):
        """

        :param func:
        :return:
        """

        def wrapper(*arg, **kwargs):
            if isinstance(arg[2], MessageListClass):
                # 实现__setitem__()
                func(*arg, **kwargs)
            else:
                raise TypeError(f'输入的类型应该是{MessageListClass}对象，实际输入的类型为{type(arg[2])}')

        return wrapper

    # def __setitem__(self,*args,**kwargs):
    #     """
    #     重写设置属性方法，无法直接修改路由表中的报文实例。如果需要更改某条报文，可以使用例如self[0].new()的方式。
    #     :param args:
    #     :param kwargs:
    #     :return:
    #     """
    #     raise AttributeError (u"can't set attribute. 无法设置属性。")

    def __iter__(self):
        """
        迭代器方法
        :return:
        """
        self.iterator_begin = 0
        return self

    def __next__(self):
        index = self.iterator_begin  # 初始值为0
        self.iterator_begin += 1  # 递增值为1

        # 下标小于自身长度就返回对应值。
        # 否则抛出StopIteration异常，停止迭代。
        if index < len(self):
            return self[index]
        else:
            self.iterator_begin = 0
            raise StopIteration

    def __append_message(self, func):
        """
        类内部修饰器。用来限制路由列表的append方法的输入类型只能为MessageListClass对象。
        :param func: 被修饰的函数。
        :return: 修饰后的函数。
        """

        def wrapper(*arg, **kwargs):

            if isinstance(arg[1], MessageListClass):
                # 执行list.append方法。
                func(*arg, **kwargs)
            elif isinstance(arg[1], RouteTableClass) or isinstance(arg[1], list):
                for message in arg[1]:
                    self.append(message)
            else:
                raise TypeError(f'输入的类型应该是{MessageListClass}对象或其集合，实际输入的类型为{type(arg[1])}')

        return wrapper

    def print_error(self):
        """
        输出全部的错误的列表。
        :return:
        """
        none_cell = []
        empty_cell = []
        error_cell = []

        # 这里写得不好，因为self[i]不能确定是什么类型的对象。
        for i in range(len(self)):
            if isinstance(self[i], MessageListClass):
                none_cell2, empty_cell2, error_cell2 = self[i].find_error()
                # 空值
                for x in none_cell2:
                    none_cell.append((i, x))
                # 空白值
                for y in empty_cell2:
                    empty_cell.append((i, y))
                # 错误值
                for z in error_cell2:
                    error_cell.append((i, z))

        return none_cell, empty_cell, error_cell

    def format_route_table(self) -> None:
        """
        格式化整个路由表。
        :return: None
        """
        for index in range(len(self)):
            if isinstance(self[index], MessageListClass):
                self[index].format_message()

    def sort_deal(self) -> bool:
        """
        对路由列表进行排序。如果出现意外值，则放弃排序。
        :return: 排序完成返回True，排序失败返回False
        """
        try:
            # 按照路由列表的第一列进行排序，也就是按照源地址进行排序。
            self.sort(key=lambda message: CHANNEL_MAPPING[message[0]])
            return True
        except KeyError:
            print('源地址数据有误，放弃首列排序')
            return False

    def sort_deal2(self) -> bool:
        """
        对路由列表进行排序。如果出现意外值，则放弃排序。
        在使用这个方法前，应保证数据全是标准的小写十六进制值。
        参考：https://blog.csdn.net/weixin_43721000/article/details/120504199
        :return: 排序完成返回True，排序失败返回False
        """

        copy_route_list = copy.deepcopy(self)

        # 如果排序出现意外情况，放弃排序
        try:

            temp_route = []  # 用于排序的临时列表
            pointer_slow = 0  # 慢指针
            pointer_fast = 0  # 快指针

            # 使用快慢指针算法来对二维数组进行优先级排序。
            # 在数组第一列已经排序的基础上对第二列进行排序。
            while pointer_slow < (len(copy_route_list) - 1):
                # 这里隐藏了一个情况，由于快指针永远都会去查询下一个元素会不会与慢指针的值相等。
                # 所以当快指针达到列表末尾后，再执行一次会导致列表下标溢出。
                # 为了应对下标溢出，当快指针达到列表最后一个元素，应该直接将列表Temp[]中的值进行排序并写回数组。
                if pointer_fast == len(copy_route_list):
                    # 如果快指针的值不同于慢指针，则对temp[]的第二项进行排序。
                    temp_route.sort(key=lambda book: book[1])
                    # 排完序后写按照慢指针写回数组，并且慢指针+1
                    for message in temp_route:
                        copy_route_list[pointer_slow] = message
                        pointer_slow += 1
                    temp_route.clear()
                    break

                # 快慢指针的值相同，则快指针+1，并且把快指针的值填入temp_route[]。
                if copy_route_list[pointer_slow][0] == copy_route_list[pointer_fast][0]:
                    temp_route.append(copy_route_list[pointer_fast])
                    pointer_fast += 1
                else:
                    # 如果快指针的值不同于慢指针，则对temp[]的第二项进行排序。
                    temp_route.sort(key=lambda book: book[1])
                    # 排完序后写按照慢指针写回数组，并且慢指针+1
                    for message in temp_route:
                        copy_route_list[pointer_slow] = message
                        pointer_slow += 1
                    temp_route.clear()
                    # 直到快指针大于超出数组长度，退出循环。

            # 排序结束后将深拷贝的对象写回原列表
            self.clear()
            self.append(copy_route_list)
            return True
        except TypeError:
            print('输入数据有误，放弃id排序')
            return False

    def removal_duplicate_sort(self) -> None:
        """
        对列表进行去重。如果报文的源地址、ID、DLC、目标地址全部相同，则从列表中删除重复的元素。
        需要先对列表进行一次的排序。但时间复杂度上要低于或等于不进行排序的情况。最差时间复杂度为O（x²）。
        参考：https://cloud.tencent.com/developer/article/1694369
        :return: None
        """

        pointer_slow = 0  # 慢指针
        pointer_fast = 0  # 快指针

        # 使用快慢指针算法对列表进行自定义去重
        while pointer_slow < (len(self) - 1):
            # 一开始快慢指针会指向同一个位置。快指针+1。
            pointer_fast += 1
            # 慢指针的位置保持不动。快指针逐渐移动，并进行对比去重。
            while self[pointer_slow][0] == self[pointer_fast][0]:
                # 对比第二列，第三列，第四列。如果都相同，则从列表中删除该元素。
                if self[pointer_fast][1] == self[pointer_slow][1] and \
                        self[pointer_fast][2] == self[pointer_slow][2] and \
                        self[pointer_fast][3] == self[pointer_slow][3]:
                    del self[pointer_fast]
                else:
                    # 如果不相同，则快指针+1
                    pointer_fast += 1
                # 如果快指针达到列表最后，则退出当前的循环。
                if pointer_fast == len(self):
                    break
                    # 直到快慢指针的第一列不相同。
            # 当一个去重阶段结束后慢指针+1
            pointer_slow += 1
            # 让快指针回到慢指针的位置，开始新一轮的去重。
            pointer_fast = pointer_slow
            # 当慢指针达到列表的最后时，退出循环。

    def removal_duplicate_all(self) -> None:
        """
        对列表进行去重。如果报文的源地址、ID、DLC、目标地址全部相同，则从列表中删除重复的元素。
        可以在用不用排序的情况下对最整个列表进行去重。算法时间复杂度为O（x²）
        参考：https://cloud.tencent.com/developer/article/1694369
        :return: None
        """

        pointer_slow = 0  # 慢指针
        pointer_fast = 0  # 快指针

        # 使用快慢指针算法对列表进行自定义去重
        while pointer_slow < (len(self) - 1):
            # 一开始快慢指针会指向同一个位置。快指针+1。
            pointer_fast += 1
            # 慢指针的位置保持不动。快指针逐渐移动，并进行对比去重。
            while pointer_fast < len(self):
                # 对比第一列、第二列、第三列、第四列。如果都相同，则从列表中删除该元素。
                if self[pointer_fast][0] == self[pointer_slow][0] and \
                        self[pointer_fast][1] == self[pointer_slow][1] and \
                        self[pointer_fast][2] == self[pointer_slow][2] and \
                        self[pointer_fast][3] == self[pointer_slow][3]:
                    del self[pointer_fast]
                else:
                    # 如果不相同，则快指针+1
                    pointer_fast += 1
                    # 直到快指针达到列表的最后。
            # 当一个去重阶段结束后慢指针+1
            pointer_slow += 1
            # 让快指针回到慢指针的位置，开始新一轮的去重。
            pointer_fast = pointer_slow
            # 当慢指针达到列表的最后时，退出循环。


if __name__ == '__main__':
    # 测试初始化
    print('——实例化两条报文message1和message2——')
    message1 = MessageListClass(*['q_CAN', '0xa0 000 000', '8', 'H_CAN', '123', 'y', 1, 1, 0])
    message1.format_message()
    print(f'报文message1为：{message1}')
    message2 = MessageListClass(*['H_CAN', '0xa0 000 000', 'D_CAN', '3', '12351', 'y', 1, 1, 0])
    message2.format_message()
    print(f'报文message2为：{message2}')

    print('——实例化路由列表route_list——')
    message_list = [message1, message2]
    route_list = RouteTableClass(*message_list)
    route_list.append(message1)
    print(f'路由表route_list为：')
    for e in route_list:
        print(e)

    print('————打印意外值下标列表————')
    none_list, empty_list, error_list = route_list.print_error()
    print(f'None值下标列表：{none_list}')
    print(f'空白值下标列表：{empty_list}')
    print(f'错误值下标列表：{error_list}')

    # 测试排序
    # message_list = [MessageListClass(*['I_CAN', '0x18DAF102', 8, 'C_CAN', 500, 0, 1, 0, 0, 0, 0, 0, 0, 1]),
    #                 MessageListClass(*['D_CAN', '0x0CFDCC21', 8, 'C_CAN', 500, 1, 1, 0, 0, 1, 0, 0, 0, 0]),
    #                 MessageListClass(*['I_CAN', '0x18DAF105', 8, 'C_CAN', 500, 0, 1, 0, 0, 0, 0, 0, 1, 0]),
    #                 MessageListClass(*['I_CAN', '0x18DAF101', 8, 'C_CAN', 100, 1, 1, 1, 1, 0, 1, 0, 0, 0]),
    #                 MessageListClass(*['I_CAN', '0x18DAF101', 8, 'C_CAN', 100, 1, 1, 1, 1, 0, 1, 0, 0, 0]),
    #                 MessageListClass(*['I_CAN', '0x18DAF101', 8, 'C_CAN', 100, 1, 1, 1, 1, 0, 1, 0, 0, 0]),
    #                 MessageListClass(*['I_CAN', '0x18DAF101', 8, 'C_CAN', 100, 1, 1, 1, 1, 0, 1, 0, 0, 0]),
    #                 MessageListClass(*['I_CAN', '0x18DAF101', 8, 'C_CAN', 100, 1, 1, 1, 1, 0, 1, 0, 0, 0]),
    #                 MessageListClass(*['I_CAN', '0x18DAF103', 8, 'C_CAN', 100, 0, 0, 0, 0, 0, 0, 0, 0, 0]),]
    # route_list = RouteTableClass(*message_list)
    #
    # for e in route_list:
    #     print(f'{type(e)}')
    #     print(e)
    # route_list.sort_deal()
    # print('排序1后：')
    # for e in route_list:
    #     print(f'{type(e)}')
    #     print(e)
    # print('排序2后：')
    # route_list.sort_deal2()
    # for e in route_list:
    #     print(f'{type(e)}')
    #     print(e)
    # # 测试排序去重
    # print('排序去重')
    # route_list.removal_duplicate_sort()
    # for e in route_list:
    #     print(f'{type(e)}')
    #     print(e)

    # 测试不排序去重
    # message_list = [MessageListClass(*['I_CAN', '0x18DAF102', 8, 'C_CAN', 500, 0, 1, 0, 0, 0, 0, 0, 0, 1]),
    #                 MessageListClass(*['D_CAN', '0x0CFDCC21', 8, 'C_CAN', 500, 1, 1, 0, 0, 1, 0, 0, 0, 0]),
    #                 MessageListClass(*['I_CAN', '0x18DAF102', 8, 'C_CAN', 500, 0, 1, 0, 0, 0, 0, 0, 1, 0]),
    #                 MessageListClass(*['I_CAN', '0x18DAF102', 8, 'C_CAN', 100, 1, 1, 1, 1, 0, 1, 0, 0, 0]),
    #                 MessageListClass(*['I_CAN', '0x18DAF102', 8, 'C_CAN', 100, 0, 0, 0, 0, 0, 0, 0, 0, 0])]
    # route_list = RouteTableClass(*message_list)
    # print('不排序去重')
    # route_list.removal_duplicate_all()
    # for e in route_list:
    #     print(e)

    # 测试深拷贝
    # import copy
    # wan = MessageListClass(*['I_CAN', '0x18DAF102', 8, 'C_CAN', 500, 0, 1, 0, 0, 0, 0, 0, 0, 1])
    # route_list = RouteTableClass(wan)
    # route_list2 = copy.deepcopy(route_list)
    # print(123)

    # 测试初始化
    # message1 = MessageListClass(*['q_CAN', '0xa0 000 000', '8', 'H_CAN', '123', 'y', 1, 1, 0])
    # message2 = MessageListClass(['q_CAN', '0xa0 000 000', '8', 'H_CAN', '123', 'y', 1, 1, 0])
    # message3 = MessageListClass(*['q_CAN', '0xa0 000 000', '8', 'H_CAN', '123', 'y', 1, 1, 0])
    # message4 = MessageListClass(*['q_CAN', '0xa0 000 000', '8', 'H_CAN', '123', 'y', 1, 1, 0])
    # route1 = RouteTableClass()
    #
    # route1.append(message_list)
    #
    # route2 = RouteTableClass()
    # route2.append(route1)
    # for e in route2:
    #     print(f'{type(e)}')
    #     print(e)
    # # route1.new([[1, 2], 2,])
    # # route1.new(message1,message2,message3,message4,['H_CAN', '0xa0 000 000', '8', 'H_CAN', '123', 'y', 1, 1, 0])
    #
    # for i in route1:
    #     print(type(i))
    #     print(i)
    #
    # import copy
    #
    # # route1.sort_deal2()
    # route1.append(message1)
    # print(route1)
    # route_list2 = copy.deepcopy(route1)
    # print(type(route_list2))
    # print(type(message4))
    # route_list2.append(message4)
    # print(route_list2)
    # route_list2.append(message4)
    # route_list2[0]=1
    # print(route_list2)
