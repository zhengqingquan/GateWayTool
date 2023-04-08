import logging
# 日志等级可以分为5个，从低到高分别是:
# 1. DEBUG：程序调试bug时使用
# 2. INFO：程序正常运行时使用
# 3. WARNING：程序未按预期运行时使用，但并不是错误，如:用户登录密码错误
# 4. ERROR：程序出错误时使用，如:IO操作失败
# 5. CRITICAL：特别严重的问题，导致程序不能再继续运行时使用，如:磁盘空间为空，一般很少使用
# logging包默认是WARNING等级，当在WARNING或WARNING之上等级的才记录日志信息。
# 日志等级从低到高的顺序是: DEBUG < INFO < WARNING < ERROR < CRITICAL
# 例如：当等级为ERROR时候，只有ERROR和CRITICAL的日志才被记录；当等级为DEBUG，则所有的日志都被记录。
import os
from pathlib import Path

from pyt.src.SoftwareInfo import LOG_PATH
from pyt.src.server.Redirect import StreamRedirectClass
import Fun


def InitLog(uiName):
    logger = logging.getLogger('logger')

    # 日志输出到系统的标准输出
    sh = logging.StreamHandler()
    sh.setLevel(logging.DEBUG)

    # 日志输出到文本框控件
    streamHandlerBox = StreamRedirectClass(Fun.GetElement(uiName, 'PrintTextFrame'))
    th = logging.StreamHandler(streamHandlerBox)
    th.setLevel(logging.INFO)

    # 日志输出到系统文件
    logPath = Path(LOG_PATH)
    if not os.path.exists(logPath.parent):
        os.makedirs(logPath.parent)
    mode = 'a' if logger.handlers else 'w'  # 如果已经有handler，则用追加模式，否则直接覆盖
    fh = logging.FileHandler(logPath, mode='a+', encoding='utf-8')
    fh.setLevel(logging.DEBUG)

    # 需要先清空handlers, 再添加
    logger.handlers.clear()
    logger.addHandler(th)
    logger.addHandler(sh)
    logger.addHandler(fh)

    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        handlers=logger.handlers)
