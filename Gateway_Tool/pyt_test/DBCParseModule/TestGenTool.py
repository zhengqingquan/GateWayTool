import logging
import unittest

from pyt.src.DBCParseModule.GenTool import LengthToStdint, IntelUnpackToStr, IntelPackToStr, MotorolaUnpackToStr, \
    MotorolaPackToStr, DBCMotorolaStartBitShift, DBCMotorolaEndBitShift


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        logging.basicConfig(level=logging.DEBUG, format='%(levelname)s - %(message)s')

    def test_LengthToStdint(self):
        # case1
        # 测试数据
        data = 64
        signed = False
        # 预期结果
        expected = 'uint64_t'
        # 执行结果
        result = LengthToStdint(data, signed)
        self.assertEqual(expected, result)  # add assertion here

        # case2
        # 测试数据
        data = 3
        signed = False
        # 预期结果
        expected = 'uint8_t'
        # 执行结果
        result = LengthToStdint(data, signed)
        self.assertEqual(expected, result)  # add assertion here

        # case3
        # 测试数据
        data = 15
        signed = True
        # 预期结果
        expected = 'int16_t'
        # 执行结果
        result = LengthToStdint(data, signed)
        self.assertEqual(expected, result)  # add assertion here

    def test_DBCMotorolaStartBitShift(self):
        # case1
        # 测试数据
        StartBit = 7
        Length = 3
        # 预期结果
        expected = 5
        # 执行结果
        result = DBCMotorolaStartBitShift(StartBit, Length)
        self.assertEqual(expected, result)  # add assertion here

        # case2
        # 测试数据
        StartBit = 29
        Length = 10
        # 预期结果
        expected = 36
        # 执行结果
        result = DBCMotorolaStartBitShift(StartBit, Length)
        self.assertEqual(expected, result)  # add assertion here

        # case3
        # 测试数据
        StartBit = 63
        Length = 8
        # 预期结果
        expected = 56
        # 执行结果
        result = DBCMotorolaStartBitShift(StartBit, Length)
        self.assertEqual(expected, result)  # add assertion here

        # case4
        # 测试数据
        StartBit = 7
        Length = 16
        # 预期结果
        expected = 8
        # 执行结果
        result = DBCMotorolaStartBitShift(StartBit, Length)
        self.assertEqual(expected, result)  # add assertion here

    def test_DBCMotorolaEndBitShift(self):
        # case1
        # 测试数据
        StartBit = 5
        Length = 3
        # 预期结果
        expected = 7
        # 执行结果
        result = DBCMotorolaEndBitShift(StartBit, Length)
        self.assertEqual(expected, result)  # add assertion here

        # case2
        # 测试数据
        StartBit = 36
        Length = 10
        # 预期结果
        expected = 29
        # 执行结果
        result = DBCMotorolaEndBitShift(StartBit, Length)
        self.assertEqual(expected, result)  # add assertion here

        # case3
        # 测试数据
        StartBit = 56
        Length = 8
        # 预期结果
        expected = 63
        # 执行结果
        result = DBCMotorolaEndBitShift(StartBit, Length)
        self.assertEqual(expected, result)  # add assertion here

        # case4
        # 测试数据
        StartBit = 8
        Length = 16
        # 预期结果
        expected = 7
        # 执行结果
        result = DBCMotorolaEndBitShift(StartBit, Length)
        self.assertEqual(expected, result)  # add assertion here

        # case5
        # 测试数据
        StartBit = 36
        Length = 4
        # 预期结果
        expected = 39
        # 执行结果
        result = DBCMotorolaEndBitShift(StartBit, Length)
        self.assertEqual(expected, result)  # add assertion here

    def test_IntelUnpackToStr_case1(self):
        # 测试数据
        start = 24
        length = 8
        # 预期结果
        logging.info(f'---------------------------')
        logging.info(f'开始位:{start},长度:{length}')
        logging.info('(_data[3] & 0xFFU)')
        # 执行结果
        logging.info(IntelUnpackToStr(start, length))

        self.assertEqual(True, True)

    def test_IntelUnpackToStr_case2(self):
        # 测试数据
        start = 11
        length = 16
        # 预期结果
        logging.info(f'---------------------------')
        logging.info(f'开始位:{start},长度:{length}')
        logging.info(
            '_m->EMS_ClutchSwitch = ((_d[3] & (0x07U)) << 13) | ((_d[2] & (0xFFU)) << 5) | ((_d[1] >> 3) & (0x1FU));')
        logging.info('(_d[3] & (0x07U) << 11) | (_d[2]) & (0xFFU) << 3 | (_d[1] & (0xF8U) >>3 )')
        # 执行结果
        logging.info(IntelUnpackToStr(start, length))

        self.assertEqual(True, True)

    def test_IntelUnpackToStr_case3(self):
        # 测试数据
        start = 48
        length = 16
        # 预期结果
        logging.info(f'---------------------------')
        logging.info(f'开始位:{start},长度:{length}')
        logging.info('_m->EMS_EngIdleIncrementSwi = ((_d[7] & (0xFFU)) << 8) | (_d[6] & (0xFFU));')
        logging.info('(_d[7] & (0xFFU)) << 8) | (_d[6] & (0xFFU))')
        # 执行结果
        logging.info(IntelUnpackToStr(start, length))

        self.assertEqual(True, True)

    def test_IntelUnpackToStr_case4(self):
        # 测试数据
        start = 52
        length = 8
        # 预期结果
        logging.info(f'---------------------------')
        logging.info(f'开始位:{start},长度:{length}')
        logging.info('_m->EMS_CCSetSpeed = ((_d[7] & (0x0FU)) << 4) | ((_d[6] >> 4) & (0x0FU));')
        logging.info('(_d[7] & (0x0FU) << 4) | (_d[6] & (0xF0U) >> 4)')
        # 执行结果
        logging.info(IntelUnpackToStr(start, length))

        self.assertEqual(True, True)

    def test_IntelUnpackToStr_case5(self):
        # 测试数据
        start = 12
        length = 21
        # 预期结果
        logging.info(f'---------------------------')
        logging.info(f'开始位:{start},长度:{length}')
        logging.info(
            '_m->EMS_EngIdleDecrementSwi = ((_d[4] & (0x01U)) << 20) | ((_d[3] & (0xFFU)) << 12) | ((_d[2] & (0xFFU)) << 4) | ((_d[1] >> 4) & (0x0FU));')
        logging.info(
            '((_d[4] & 0x01U) << 20) | (_d[3] & (0xFFU)) << 12 | (_d[2] & (0xFFU)) << 4 | ((_d[1] & 0x0FU) >> 4)')
        # 执行结果
        logging.info(IntelUnpackToStr(start, length))

        self.assertEqual(True, True)

    def test_IntelUnpackToStr_case6(self):
        # 测试数据
        start = 4
        length = 4
        # 预期结果
        logging.info(f'---------------------------')
        logging.info(f'开始位:{start},长度:{length}')
        logging.info('_data[0] & 0xF0U')
        # 执行结果
        logging.info(IntelUnpackToStr(start, length))

        self.assertEqual(True, True)

    def test_IntelPackToStr_case1(self):
        # 测试数据
        signalName = 'signalName'
        start = 4
        length = 4
        # 预期结果
        logging.info(f'---------------------------')
        logging.info(f'信号名称:{signalName},开始位:{start},长度:{length}')
        logging.info('_date[0] |= (_message->signalName & (0x0FU)) << 4;')
        # 执行结果
        logging.info(IntelPackToStr(signalName, start, length))

        self.assertEqual(True, True)

    def test_IntelPackToStr_case2(self):
        # 测试数据
        signalName = 'signalName'
        start = 0
        length = 8
        # 预期结果
        logging.info(f'---------------------------')
        logging.info(f'信号名称:{signalName},开始位:{start},长度:{length}')
        logging.info('_date[0] |= (_message->signalName & (0xFFU));')
        # 执行结果
        logging.info(IntelPackToStr(signalName, start, length))

        self.assertEqual(True, True)

    def test_IntelPackToStr_case3(self):
        # 测试数据
        signalName = 'signalName'
        start = 12
        length = 8
        # 预期结果
        logging.info(f'---------------------------')
        logging.info(f'信号名称:{signalName},开始位:{start},长度:{length}')
        logging.info('_date[1] |= (_message->signalName & 0x0FU) << 4;\n'
                     '_date[2] |= ((_message->signalName >> 4) & (0x0FU));')
        # 执行结果
        logging.info(IntelPackToStr(signalName, start, length))

        self.assertEqual(True, True)

    def test_IntelPackToStr_case4(self):
        # 测试数据
        signalName = 'signalName'
        start = 12
        length = 16
        # 预期结果
        logging.info(f'---------------------------')
        logging.info(f'信号名称:{signalName},开始位:{start},长度:{length}')
        logging.info('_date[1] |= (_message->signalName & 0x0FU) << 4;\n'
                     '_date[2] |= (_message->signalName >> 4) & 0xFFU;\n'
                     '_date[3] |= (_message->signalName >> 12) & (0x0FU);')
        # 执行结果
        logging.info(IntelPackToStr(signalName, start, length))

        self.assertEqual(True, True)

    def test_MotorolaUnpackToStr(self):
        # -----------------字节内，长度小于8-----------------
        start = 0
        length = 6
        result = '_data[0] & 0x3FU'
        self.assertEqual(result, MotorolaUnpackToStr(start, length))

        start = 3
        length = 5
        result = '(_data[0] & 0xF8U) >> 3'
        self.assertEqual(result, MotorolaUnpackToStr(start, length))

        start = 2
        length = 6
        result = '(_data[0] & 0xFCU) >> 2'
        self.assertEqual(result, MotorolaUnpackToStr(start, length))

        start = 24
        length = 7
        result = '_data[3] & 0x7FU'
        self.assertEqual(result, MotorolaUnpackToStr(start, length))

        # -----------------字节内，长度等于8-----------------
        start = 0
        length = 8
        result = '_data[0] & 0xFFU'
        self.assertEqual(result, MotorolaUnpackToStr(start, length))

        start = 16
        length = 8
        result = '_data[2] & 0xFFU'
        self.assertEqual(result, MotorolaUnpackToStr(start, length))

        # -----------------跨字节，长度小于8-----------------
        start = 15
        length = 4
        result = '(_data[0] & 0x07U) << 1 | (_data[1] & 0x80U) >> 7'
        self.assertEqual(result, MotorolaUnpackToStr(start, length))

        start = 20
        length = 7
        result = '(_data[1] & 0x07U) << 4 | (_data[2] & 0xF0U) >> 4'
        self.assertEqual(result, MotorolaUnpackToStr(start, length))

        # -----------------跨字节，长度等于8-----------------
        start = 20
        length = 8
        result = '(_data[1] & 0x0FU) << 4 | (_data[2] & 0xF0U) >> 4'
        self.assertEqual(result, MotorolaUnpackToStr(start, length))

        start = 25
        length = 8
        result = '(_data[2] & 0x01U) << 7 | (_data[3] & 0xFEU) >> 1'
        self.assertEqual(result, MotorolaUnpackToStr(start, length))

        # -----------------跨字节，长度大于8-----------------
        start = 36
        length = 10
        result = '(_data[3] & 0x3FU) << 4 | (_data[4] & 0xF0U) >> 4'
        self.assertEqual(result, MotorolaUnpackToStr(start, length))

        start = 30
        length = 10
        result = '(_data[2] & 0xFFU) << 2 | (_data[3] & 0xC0U) >> 6'
        self.assertEqual(result, MotorolaUnpackToStr(start, length))

    def test_MotorolaPackToStr(self):
        # -----------------字节内，长度小于8-----------------
        signalName = 'signalName'
        start = 5
        length = 3
        result = '_data[0] |= _message->signalName << 5;'
        self.assertEqual(result, MotorolaPackToStr(signalName, start, length))

        signalName = 'signalName'
        start = 7
        length = 1
        result = '_data[0] |= _message->signalName << 7;'
        self.assertEqual(result, MotorolaPackToStr(signalName, start, length))

        signalName = 'signalName'
        start = 12
        length = 4
        result = '_data[1] |= _message->signalName << 4;'
        self.assertEqual(result, MotorolaPackToStr(signalName, start, length))

        # -----------------字节内，长度等于8-----------------
        signalName = 'signalName'
        start = 0
        length = 8
        result = '_data[0] |= _message->signalName;'
        self.assertEqual(result, MotorolaPackToStr(signalName, start, length))
        # -----------------跨字节，长度小于8-----------------

        # -----------------跨字节，长度等于8-----------------

        # -----------------跨字节，长度大于8-----------------
        signalName = 'signalName'
        start = 36
        length = 10
        result = '_data[3] |= (_message->signalName >> 4) & 0x3FU;\n' \
                 '\t_data[4] |= (_message->signalName << 4) & 0xF0U;'
        self.assertEqual(result, MotorolaPackToStr(signalName, start, length))

        signalName = 'signalName'
        start = 36
        length = 20
        result = '_data[2] |= (_message->signalName >> 12) & 0xFFU;\n' \
                 '\t_data[3] |= (_message->signalName >> 4) & 0xFFU;\n' \
                 '\t_data[4] |= (_message->signalName << 4) & 0xF0U;'
        self.assertEqual(result, MotorolaPackToStr(signalName, start, length))


if __name__ == '__main__':
    unittest.main()
