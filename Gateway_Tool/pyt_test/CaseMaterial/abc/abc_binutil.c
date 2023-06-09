/**
* @file:         abc_binutil.c
* @author:       96400
* @note:         The code is automatically generated by GatewayTool
* @version:      V1.0.0
* @date:         2023.02.09, 14:29:32
* @brief:        
* @attention:    
**/

#include "abc_CycleAct.h"
#include "abc_MsgCycAOP.h"
#include "abc_binutil.h"


abc_msglist_t abc_msglist = {
	/* 0xcfe6cee */
	.IC_TCO1.monitor.cycle = IC_TCO1_CYC,
	.IC_TCO1.monitor.timeout_cycle = 500,
	.IC_TCO1.monitor.TimeoutFunc = abc_TimeoutFunc_IC_TCO1,
	.IC_TCO1.monitor.TimingFunc = abc_TimingFunc_IC_TCO1,
	.IC_TCO1.monitor.CycleOverFunc = abc_CycleOverFunc_IC_TCO1,

	/* 0xcfe6cef */
	.New_Message_5.monitor.cycle = New_Message_5_CYC,
	.New_Message_5.monitor.timeout_cycle = 500,
	.New_Message_5.monitor.TimeoutFunc = abc_TimeoutFunc_New_Message_5,
	.New_Message_5.monitor.TimingFunc = abc_TimingFunc_New_Message_5,
	.New_Message_5.monitor.CycleOverFunc = abc_CycleOverFunc_New_Message_5,

	/* 0x18fef100 */
	.EMS_CCVS.monitor.cycle = EMS_CCVS_CYC,
	.EMS_CCVS.monitor.timeout_cycle = 500,
	.EMS_CCVS.monitor.TimeoutFunc = abc_TimeoutFunc_EMS_CCVS,
	.EMS_CCVS.monitor.TimingFunc = abc_TimingFunc_EMS_CCVS,
	.EMS_CCVS.monitor.CycleOverFunc = abc_CycleOverFunc_EMS_CCVS,

	/* 0x18fef117 */
	.IC_CCVS1.monitor.cycle = IC_CCVS1_CYC,
	.IC_CCVS1.monitor.timeout_cycle = 500,
	.IC_CCVS1.monitor.TimeoutFunc = abc_TimeoutFunc_IC_CCVS1,
	.IC_CCVS1.monitor.TimingFunc = abc_TimingFunc_IC_CCVS1,
	.IC_CCVS1.monitor.CycleOverFunc = abc_CycleOverFunc_IC_CCVS1,

	/* 0x18fef121 */
	.BCM_CCVS.monitor.cycle = BCM_CCVS_CYC,
	.BCM_CCVS.monitor.timeout_cycle = 500,
	.BCM_CCVS.monitor.TimeoutFunc = abc_TimeoutFunc_BCM_CCVS,
	.BCM_CCVS.monitor.TimingFunc = abc_TimingFunc_BCM_CCVS,
	.BCM_CCVS.monitor.CycleOverFunc = abc_CycleOverFunc_BCM_CCVS,

};


void abc_init_msglist(void)
{

}


void abc_CycleAct(void)
{
	CycleActFunc();
}


void abc_ResetAllInit(void)
{

}


uint32_t abc_Pack(const uint32_t _msgID, uint8_t* _data, uint8_t* _dlc, uint8_t* _ide)
{
	uint32_t traID = 0;

	switch (_msgID)
	{
	case 0xcfe6cee:
		traID = Pack_abc_IC_TCO1(&(abc_msglist.IC_TCO1), _data, _dlc, _ide);
		break;
	case 0xcfe6cef:
		traID = Pack_abc_New_Message_5(&(abc_msglist.New_Message_5), _data, _dlc, _ide);
		break;
	case 0x18fef100:
		traID = Pack_abc_EMS_CCVS(&(abc_msglist.EMS_CCVS), _data, _dlc, _ide);
		break;
	case 0x18fef117:
		traID = Pack_abc_IC_CCVS1(&(abc_msglist.IC_CCVS1), _data, _dlc, _ide);
		break;
	case 0x18fef121:
		traID = Pack_abc_BCM_CCVS(&(abc_msglist.BCM_CCVS), _data, _dlc, _ide);
		break;
	default:
		break;
	}
	return traID;
}


uint32_t abc_Unpack(const uint32_t _msgID, const uint8_t* _data, const uint8_t _dlc)
{
	uint32_t recID = 0;

	switch (_msgID)
	{
	case 0xcfe6cee:
		recID = Unpack_abc_IC_TCO1(&(abc_msglist.IC_TCO1), _data, _dlc);
		break;
	case 0xcfe6cef:
		recID = Unpack_abc_New_Message_5(&(abc_msglist.New_Message_5), _data, _dlc);
		break;
	case 0x18fef100:
		recID = Unpack_abc_EMS_CCVS(&(abc_msglist.EMS_CCVS), _data, _dlc);
		break;
	case 0x18fef117:
		recID = Unpack_abc_IC_CCVS1(&(abc_msglist.IC_CCVS1), _data, _dlc);
		break;
	case 0x18fef121:
		recID = Unpack_abc_BCM_CCVS(&(abc_msglist.BCM_CCVS), _data, _dlc);
		break;
	default:
		break;
	}
	return recID;
}




/******** END OF FILE ********/
