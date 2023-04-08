import json
import logging
import os
from string import Template
from typing import AnyStr

from pyt.src.ToolModule.FileGeneration import generate_description
from pyt.src.ToolModule.FuncTool import runTimeMsg


# TODO 该函数的异常处理可能需要重新考虑，可以抛给上层。
@runTimeMsg(r'模板替换')
def generate_file(jsonPath: AnyStr, templatePath: AnyStr, filePath: AnyStr, isComments: bool = True) -> None:
    """
    使用Template文件和Json文件生成一个替换后的文件。
    :param jsonPath: Json文件路径
    :param templatePath: Template文件路径
    :param filePath: 需要生成的文件的路径
    :param isComments: 是否生成说明
    :return: None
    """
    try:
        # 读取Json文件
        with open(jsonPath, 'r', encoding='utf-8') as file:
            json_dict = json.load(file)
        # 读取模板文件
        with open(templatePath, 'r', encoding='utf-8') as file:
            template = Template(file.read())
        # 把Json中的对象替换到模板中
        content = template.substitute(json_dict)
        # 写入新的文件
        with open(filePath, 'w', encoding='utf-8') as file:
            file.writelines(content)
        # 生成前后的说明
        if isComments:
            generate_description(filePath)
    except FileNotFoundError as e:
        logging.error(f'找不到以下文件：{os.path.abspath(e.filename)}')
    except PermissionError as e:
        logging.error(f'权限被拒绝：{os.path.abspath(e.filename)}')
    except IOError as e:
        logging.error(f'IO错误，{os.path.abspath(e.filename)}')
    except json.decoder.JSONDecodeError as e:
        logging.error(f'Json文件格式有误：{os.path.abspath(jsonPath)}\n'
                      f'{e}')
    except KeyError as e:
        logging.error(f'参数错误，在Json文件中未找到属性{e}，请检查对应的Template和Json文件。\n'
                      f'Json文件：{os.path.abspath(jsonPath)}\n'
                      f'Template文件：{os.path.abspath(templatePath)}')
