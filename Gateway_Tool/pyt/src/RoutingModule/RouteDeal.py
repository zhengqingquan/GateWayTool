import copy
import logging

from pyt.src.ToolModule.FuncTool import runTimeMsg
from pyt.src.RoutingModule.MessageDeal import *


@runTimeMsg(r'路由表格式化')
def format_route(alist: list[list]):
    """
    路由表格式化
    :param alist:
    :return:
    """
    for aMessage in alist:
        format_message(aMessage)


@runTimeMsg(r'查找路由表的错误单元格')
def error_route(aRouteTable: list[list]) -> list:
    error_cell = []  # 为意外值的单元格列表

    for index, _message in enumerate(aRouteTable):
        for index2 in find_error(_message):
            error_cell.append((index, index2))

    return error_cell


@runTimeMsg(r'路由表源地址排序')
def source_sort(alist: list[list]) -> None:
    """
    对路由列表进行排序。如果出现意外值，则放弃排序。
    """
    try:
        # 对路由列表的第一列进行排序。排序规则按照源地址映射表从小到大。
        alist.sort(key=lambda message: RouteConfig().CHANNEL_MAPPING[message[0]])
    except KeyError:
        # 如果出现了不在源地址映射表中的值，则放弃排序。
        logging.error(r'源地址数据有误，放弃首列排序')


@runTimeMsg(r'路由表ID排序')
def ID_sort(alist: list[list]) -> None:
    """
    对路由列表进行排序。
    在使用这个方法前，应保证数据全是标准的小写十六进制值。
    参考：https://blog.csdn.net/weixin_43721000/article/details/120504199
    """

    # 进行深拷贝
    copy_route_list = copy.deepcopy(alist)

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
            temp_route.sort(key=lambda message: int(message[1], 0))
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
            temp_route.sort(key=lambda message: int(message[1], 0))
            # 排完序后写按照慢指针写回数组，并且慢指针+1
            for message in temp_route:
                copy_route_list[pointer_slow] = message
                pointer_slow += 1
            temp_route.clear()
            # 直到快指针大于超出数组长度，退出循环。

    # 排序结束后将深拷贝的对象写回原列表
    alist.clear()
    for element in copy_route_list:
        alist.append(element)


@runTimeMsg(r'路由表去重')
def remove_duplicate(alist: list[list]) -> None:
    """
    需要进行排序后使用。时间复杂度为：O(x)
    :param alist:
    :return: None
    """

    # 进行深拷贝
    copy_route_list = copy.deepcopy(alist)

    pointer = 0  # 慢指针

    # 指针和它的下一个数据对比，如果相同则删除
    while pointer < (len(copy_route_list) - 1):
        # 对比第一列，第二列，第三列，第四列。如果都相同，则从列表中删除该元素。
        if copy_route_list[pointer][0] == copy_route_list[pointer + 1][0] and \
                copy_route_list[pointer][1] == copy_route_list[pointer + 1][1] and \
                copy_route_list[pointer][2] == copy_route_list[pointer + 1][2] and \
                copy_route_list[pointer][3] == copy_route_list[pointer + 1][3]:
            logging.info(f'删除了{copy_route_list[pointer + 1]}')
            del copy_route_list[pointer + 1]
        else:
            # 如果不相同，则指针+1
            pointer += 1
        # 如果指针达到列表最后，则退出循环。
        if pointer == len(copy_route_list) - 1:
            break

    # 去重结束后将深拷贝的对象写回原列表
    alist.clear()
    for element in copy_route_list:
        alist.append(element)


# TODO 在生成数组前需要完成排序的校验。
def SortCheck() -> bool:
    """
    对排序进行校验。若ID顺序有误，则返回false。
    """
    pass
