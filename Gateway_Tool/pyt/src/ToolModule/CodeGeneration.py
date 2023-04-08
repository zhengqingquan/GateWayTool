def structCode(structName, content, isTypedef=True) -> str:
    """
    生成C语言结构体。
    """
    structName = str(structName).strip()

    if isTypedef:
        text = f'typedef struct {structName}\n' \
               '{\n' \
               f'{content}' \
               '} ' \
               f'{structName};' \
               f'\n'
    else:
        text = f'struct {structName}\n' \
               '{\n' \
               f'{content}' \
               '};' \
               '\n'

    return text
