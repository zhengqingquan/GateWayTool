/**
* @file:         abc_definition.c
* @author:       96400
* @note:         The code is automatically generated by GatewayTool
* @version:      V1.0.0
* @date:         2023.02.09, 14:29:32
* @brief:        
* @attention:    
**/

#include <string.h>

#include "abc_MsgParseAOP.h"
#include "abc_definition.h"


/*
Message Name: IC_TCO1
Message Id: 0xcfe6cee (218000622)
+--------------+-----------+--------+---------------+--------------------+--------+--------+------+----------+
| Signal Name  | Start Bit | Length |   Byte Order  | Value Type(Signed) | Factor | Offset | Unit | comments |
+--------------+-----------+--------+---------------+--------------------+--------+--------+------+----------+
| New_Signal_5 |     0     |   8    | little_endian |        True        |   1    |   0    | None |   None   |
| New_Signal_4 |     21    |   7    |   big_endian  |       False        |   2    |   0    | None |   None   |
+--------------+-----------+--------+---------------+--------------------+--------+--------+------+----------+
*/
uint32_t Unpack_abc_IC_TCO1(abc_IC_TCO1_t* _message, const uint8_t _data[], uint8_t _dlc)
{
	BeforeParse_abc_IC_TCO1();

	_message->New_Signal_5 = _data[0] & 0xFFU;
	_message->New_Signal_4 = (_data[1] & 0x0FU) << 3 | (_data[2] & 0xE0U) >> 5;

	_message->monitor.last_cycle = abc_GetSystemTick();
	_message->monitor.timeout_cnt = 0;
	_message->monitor.frame_cnt++;
	_message->monitor.dlc_error = (_dlc != IC_TCO1_DLC);

	AfterParse_abc_IC_TCO1();

	return IC_TCO1_ID;
}

uint32_t Pack_abc_IC_TCO1(abc_IC_TCO1_t* _message, uint8_t* _data, uint8_t* _dlc, uint8_t* _ide)
{
	(void)memset(_data, 0, sizeof(_data));

	_data[0] |= _message->New_Signal_5;
	_data[1] |= (_message->New_Signal_4 >> 3) & 0x0FU;
	_data[2] |= (_message->New_Signal_4 << 3) & 0xE0U;

	*_dlc = IC_TCO1_DLC;
	*_ide = IC_TCO1_IDE;
	return IC_TCO1_ID;
}

/*
Message Name: New_Message_5
Message Id: 0xcfe6cef (218000623)
+--------------+-----------+--------+------------+--------------------+--------+--------+------+----------+
| Signal Name  | Start Bit | Length | Byte Order | Value Type(Signed) | Factor | Offset | Unit | comments |
+--------------+-----------+--------+------------+--------------------+--------+--------+------+----------+
| New_Signal_5 |     18    |   10   | big_endian |        True        |   1    |   0    | None |   None   |
+--------------+-----------+--------+------------+--------------------+--------+--------+------+----------+
*/
uint32_t Unpack_abc_New_Message_5(abc_New_Message_5_t* _message, const uint8_t _data[], uint8_t _dlc)
{
	BeforeParse_abc_New_Message_5();

	_message->New_Signal_5 = (_data[1] & 0x0FU) << 6 | (_data[2] & 0xFCU) >> 2;

	_message->monitor.last_cycle = abc_GetSystemTick();
	_message->monitor.timeout_cnt = 0;
	_message->monitor.frame_cnt++;
	_message->monitor.dlc_error = (_dlc != New_Message_5_DLC);

	AfterParse_abc_New_Message_5();

	return New_Message_5_ID;
}

uint32_t Pack_abc_New_Message_5(abc_New_Message_5_t* _message, uint8_t* _data, uint8_t* _dlc, uint8_t* _ide)
{
	(void)memset(_data, 0, sizeof(_data));

	_data[1] |= (_message->New_Signal_5 >> 6) & 0x0FU;
	_data[2] |= (_message->New_Signal_5 << 6) & 0xFCU;

	*_dlc = New_Message_5_DLC;
	*_ide = New_Message_5_IDE;
	return New_Message_5_ID;
}

/*
Message Name: EMS_CCVS
Message Id: 0x18fef100 (419361024)
+--------------+-----------+--------+---------------+--------------------+--------+--------+------+----------+
| Signal Name  | Start Bit | Length |   Byte Order  | Value Type(Signed) | Factor | Offset | Unit | comments |
+--------------+-----------+--------+---------------+--------------------+--------+--------+------+----------+
| New_Signal_1 |     0     |   8    | little_endian |        True        |   1    |   0    | None |   None   |
| New_Signal_2 |     8     |   8    | little_endian |        True        |   1    |   0    | None |   None   |
| New_Signal_3 |     16    |   8    | little_endian |        True        |   1    |   0    | None |   None   |
| New_Signal_4 |     24    |   8    | little_endian |        True        |   1    |   0    | None |   None   |
+--------------+-----------+--------+---------------+--------------------+--------+--------+------+----------+
*/
uint32_t Unpack_abc_EMS_CCVS(abc_EMS_CCVS_t* _message, const uint8_t _data[], uint8_t _dlc)
{
	BeforeParse_abc_EMS_CCVS();

	_message->New_Signal_1 = _data[0] & 0xFFU;
	_message->New_Signal_2 = _data[1] & 0xFFU;
	_message->New_Signal_3 = _data[2] & 0xFFU;
	_message->New_Signal_4 = _data[3] & 0xFFU;

	_message->monitor.last_cycle = abc_GetSystemTick();
	_message->monitor.timeout_cnt = 0;
	_message->monitor.frame_cnt++;
	_message->monitor.dlc_error = (_dlc != EMS_CCVS_DLC);

	AfterParse_abc_EMS_CCVS();

	return EMS_CCVS_ID;
}

uint32_t Pack_abc_EMS_CCVS(abc_EMS_CCVS_t* _message, uint8_t* _data, uint8_t* _dlc, uint8_t* _ide)
{
	(void)memset(_data, 0, sizeof(_data));

	_data[0] |= _message->New_Signal_1;
	_data[1] |= _message->New_Signal_2;
	_data[2] |= _message->New_Signal_3;
	_data[3] |= _message->New_Signal_4;

	*_dlc = EMS_CCVS_DLC;
	*_ide = EMS_CCVS_IDE;
	return EMS_CCVS_ID;
}

/*
Message Name: IC_CCVS1
Message Id: 0x18fef117 (419361047)
+---------------+-----------+--------+------------+--------------------+--------+--------+------+----------+
|  Signal Name  | Start Bit | Length | Byte Order | Value Type(Signed) | Factor | Offset | Unit | comments |
+---------------+-----------+--------+------------+--------------------+--------+--------+------+----------+
| New_Signal_11 |     8     |   8    | big_endian |       False        |   1    |   0    | None |   None   |
| New_Signal_12 |     16    |   8    | big_endian |       False        |  0.5   |   0    | None |   None   |
| New_Signal_13 |     24    |   8    | big_endian |       False        |   1    |   10   | None |   None   |
| New_Signal_10 |     53    |   6    | big_endian |        True        |   1    |   0    | asd  |   None   |
+---------------+-----------+--------+------------+--------------------+--------+--------+------+----------+
*/
uint32_t Unpack_abc_IC_CCVS1(abc_IC_CCVS1_t* _message, const uint8_t _data[], uint8_t _dlc)
{
	BeforeParse_abc_IC_CCVS1();

	_message->New_Signal_11 = _data[1] & 0xFFU;
	_message->New_Signal_12 = _data[2] & 0xFFU;
	_message->New_Signal_13 = _data[3] & 0xFFU;
	_message->New_Signal_10 = (_data[5] & 0x07U) << 3 | (_data[6] & 0xE0U) >> 5;

	_message->monitor.last_cycle = abc_GetSystemTick();
	_message->monitor.timeout_cnt = 0;
	_message->monitor.frame_cnt++;
	_message->monitor.dlc_error = (_dlc != IC_CCVS1_DLC);

	AfterParse_abc_IC_CCVS1();

	return IC_CCVS1_ID;
}

uint32_t Pack_abc_IC_CCVS1(abc_IC_CCVS1_t* _message, uint8_t* _data, uint8_t* _dlc, uint8_t* _ide)
{
	(void)memset(_data, 0, sizeof(_data));

	_data[1] |= _message->New_Signal_11;
	_data[2] |= _message->New_Signal_12;
	_data[3] |= _message->New_Signal_13;
	_data[5] |= (_message->New_Signal_10 >> 3) & 0x07U;
	_data[6] |= (_message->New_Signal_10 << 3) & 0xE0U;

	*_dlc = IC_CCVS1_DLC;
	*_ide = IC_CCVS1_IDE;
	return IC_CCVS1_ID;
}

/*
Message Name: BCM_CCVS
Message Id: 0x18fef121 (419361057)
+--------------+-----------+--------+---------------+--------------------+--------+--------+------+----------+
| Signal Name  | Start Bit | Length |   Byte Order  | Value Type(Signed) | Factor | Offset | Unit | comments |
+--------------+-----------+--------+---------------+--------------------+--------+--------+------+----------+
| New_Signal_3 |     8     |   3    | little_endian |        True        |   1    |   0    | None |   None   |
+--------------+-----------+--------+---------------+--------------------+--------+--------+------+----------+
*/
uint32_t Unpack_abc_BCM_CCVS(abc_BCM_CCVS_t* _message, const uint8_t _data[], uint8_t _dlc)
{
	BeforeParse_abc_BCM_CCVS();

	_message->New_Signal_3 = _data[1] & 0x07U;

	_message->monitor.last_cycle = abc_GetSystemTick();
	_message->monitor.timeout_cnt = 0;
	_message->monitor.frame_cnt++;
	_message->monitor.dlc_error = (_dlc != BCM_CCVS_DLC);

	AfterParse_abc_BCM_CCVS();

	return BCM_CCVS_ID;
}

uint32_t Pack_abc_BCM_CCVS(abc_BCM_CCVS_t* _message, uint8_t* _data, uint8_t* _dlc, uint8_t* _ide)
{
	(void)memset(_data, 0, sizeof(_data));

	_data[1] |= _message->New_Signal_3;

	*_dlc = BCM_CCVS_DLC;
	*_ide = BCM_CCVS_IDE;
	return BCM_CCVS_ID;
}



/******** END OF FILE ********/
