#include <stdint.h>
#include "BCAN_binutil.h"
#include "BCAN_monitorutil.h"


void BCAN_TimeoutInit()
{
	// FBTC_MP5_Mode  0x4fd  500
	BCAN_msglist.FBTC_MP5_Mode.mon1.cycle = 50;
	BCAN_msglist.FBTC_MP5_Mode.mon1.timeout_cycle = 250;

	// FCTB_CBS2  0x3ff  100
	BCAN_msglist.FCTB_CBS2.mon1.cycle = 10;
	BCAN_msglist.FCTB_CBS2.mon1.timeout_cycle = 50;

	// FCTB_IC_ESC_EPB1  0x31a  100
	BCAN_msglist.FCTB_IC_ESC_EPB1.mon1.cycle = 10;
	BCAN_msglist.FCTB_IC_ESC_EPB1.mon1.timeout_cycle = 50;

	// FCTB_IC_ESC3  0x121  20
	BCAN_msglist.FCTB_IC_ESC3.mon1.cycle = 2;
	BCAN_msglist.FCTB_IC_ESC3.mon1.timeout_cycle = 10;

	// FCTB_IC_ESC6  0x123  20
	BCAN_msglist.FCTB_IC_ESC6.mon1.cycle = 2;
	BCAN_msglist.FCTB_IC_ESC6.mon1.timeout_cycle = 10;

	// FCTB_CGW_VCU5  0x355  100
	BCAN_msglist.FCTB_CGW_VCU5.mon1.cycle = 10;
	BCAN_msglist.FCTB_CGW_VCU5.mon1.timeout_cycle = 50;

	// FBTC_AC_Front2  0x37c  100
	BCAN_msglist.FBTC_AC_Front2.mon1.cycle = 10;
	BCAN_msglist.FBTC_AC_Front2.mon1.timeout_cycle = 50;

	// FBTC_MP5_6  0x413  500
	BCAN_msglist.FBTC_MP5_6.mon1.cycle = 50;
	BCAN_msglist.FBTC_MP5_6.mon1.timeout_cycle = 250;

	// FBTC_MP5_TBOX_Time  0x4da  1000
	BCAN_msglist.FBTC_MP5_TBOX_Time.mon1.cycle = 100;
	BCAN_msglist.FBTC_MP5_TBOX_Time.mon1.timeout_cycle = 500;

	// FBTC_MP5_2  0x366  500
	BCAN_msglist.FBTC_MP5_2.mon1.cycle = 50;
	BCAN_msglist.FBTC_MP5_2.mon1.timeout_cycle = 250;

	// FBTC_AC1  0x322  100
	BCAN_msglist.FBTC_AC1.mon1.cycle = 10;
	BCAN_msglist.FBTC_AC1.mon1.timeout_cycle = 50;

	// FBTC_IBCM6  0x341  100
	BCAN_msglist.FBTC_IBCM6.mon1.cycle = 10;
	BCAN_msglist.FBTC_IBCM6.mon1.timeout_cycle = 50;

	// FBTC_IBCM3  0x33c  100
	BCAN_msglist.FBTC_IBCM3.mon1.cycle = 10;
	BCAN_msglist.FBTC_IBCM3.mon1.timeout_cycle = 50;

	// FCTB_GW_ACU_Crash  0x30c  100
	BCAN_msglist.FCTB_GW_ACU_Crash.mon1.cycle = 10;
	BCAN_msglist.FCTB_GW_ACU_Crash.mon1.timeout_cycle = 50;

	// FBTC_IBCM2  0x23a  40
	BCAN_msglist.FBTC_IBCM2.mon1.cycle = 4;
	BCAN_msglist.FBTC_IBCM2.mon1.timeout_cycle = 20;

	// FCTB_GW_ESC7  0x431  1000
	BCAN_msglist.FCTB_GW_ESC7.mon1.cycle = 100;
	BCAN_msglist.FCTB_GW_ESC7.mon1.timeout_cycle = 500;

	// FCTB_IC_ESC2  0xa0  10
	BCAN_msglist.FCTB_IC_ESC2.mon1.cycle = 1;
	BCAN_msglist.FCTB_IC_ESC2.mon1.timeout_cycle = 5;

	// FCTB_IC_SAS_info  0xa5  10
	BCAN_msglist.FCTB_IC_SAS_info.mon1.cycle = 1;
	BCAN_msglist.FCTB_IC_SAS_info.mon1.timeout_cycle = 5;

}

void BCAN_cycleFunc(void)
{
	cycle_BCAN_FBTC_MP5_Mode(&BCAN_msglist.FBTC_MP5_Mode.mon1);
	cycle_BCAN_FCTB_CBS2(&BCAN_msglist.FCTB_CBS2.mon1);
	cycle_BCAN_FCTB_IC_ESC_EPB1(&BCAN_msglist.FCTB_IC_ESC_EPB1.mon1);
	cycle_BCAN_FCTB_IC_ESC3(&BCAN_msglist.FCTB_IC_ESC3.mon1);
	cycle_BCAN_FCTB_IC_ESC6(&BCAN_msglist.FCTB_IC_ESC6.mon1);
	cycle_BCAN_FCTB_CGW_VCU5(&BCAN_msglist.FCTB_CGW_VCU5.mon1);
	cycle_BCAN_FBTC_AC_Front2(&BCAN_msglist.FBTC_AC_Front2.mon1);
	cycle_BCAN_FBTC_MP5_6(&BCAN_msglist.FBTC_MP5_6.mon1);
	cycle_BCAN_FBTC_MP5_TBOX_Time(&BCAN_msglist.FBTC_MP5_TBOX_Time.mon1);
	cycle_BCAN_FBTC_MP5_2(&BCAN_msglist.FBTC_MP5_2.mon1);
	cycle_BCAN_FBTC_AC1(&BCAN_msglist.FBTC_AC1.mon1);
	cycle_BCAN_FBTC_IBCM6(&BCAN_msglist.FBTC_IBCM6.mon1);
	cycle_BCAN_FBTC_IBCM3(&BCAN_msglist.FBTC_IBCM3.mon1);
	cycle_BCAN_FCTB_GW_ACU_Crash(&BCAN_msglist.FCTB_GW_ACU_Crash.mon1);
	cycle_BCAN_FBTC_IBCM2(&BCAN_msglist.FBTC_IBCM2.mon1);
	cycle_BCAN_FCTB_GW_ESC7(&BCAN_msglist.FCTB_GW_ESC7.mon1);
	cycle_BCAN_FCTB_IC_ESC2(&BCAN_msglist.FCTB_IC_ESC2.mon1);
	cycle_BCAN_FCTB_IC_SAS_info(&BCAN_msglist.FCTB_IC_SAS_info.mon1);
}

void BCAN_timeoutFunc(void)
{
	timeout_BCAN_FBTC_MP5_Mode(&BCAN_msglist.FBTC_MP5_Mode.mon1);
	timeout_BCAN_FCTB_CBS2(&BCAN_msglist.FCTB_CBS2.mon1);
	timeout_BCAN_FCTB_IC_ESC_EPB1(&BCAN_msglist.FCTB_IC_ESC_EPB1.mon1);
	timeout_BCAN_FCTB_IC_ESC3(&BCAN_msglist.FCTB_IC_ESC3.mon1);
	timeout_BCAN_FCTB_IC_ESC6(&BCAN_msglist.FCTB_IC_ESC6.mon1);
	timeout_BCAN_FCTB_CGW_VCU5(&BCAN_msglist.FCTB_CGW_VCU5.mon1);
	timeout_BCAN_FBTC_AC_Front2(&BCAN_msglist.FBTC_AC_Front2.mon1);
	timeout_BCAN_FBTC_MP5_6(&BCAN_msglist.FBTC_MP5_6.mon1);
	timeout_BCAN_FBTC_MP5_TBOX_Time(&BCAN_msglist.FBTC_MP5_TBOX_Time.mon1);
	timeout_BCAN_FBTC_MP5_2(&BCAN_msglist.FBTC_MP5_2.mon1);
	timeout_BCAN_FBTC_AC1(&BCAN_msglist.FBTC_AC1.mon1);
	timeout_BCAN_FBTC_IBCM6(&BCAN_msglist.FBTC_IBCM6.mon1);
	timeout_BCAN_FBTC_IBCM3(&BCAN_msglist.FBTC_IBCM3.mon1);
	timeout_BCAN_FCTB_GW_ACU_Crash(&BCAN_msglist.FCTB_GW_ACU_Crash.mon1);
	timeout_BCAN_FBTC_IBCM2(&BCAN_msglist.FBTC_IBCM2.mon1);
	timeout_BCAN_FCTB_GW_ESC7(&BCAN_msglist.FCTB_GW_ESC7.mon1);
	timeout_BCAN_FCTB_IC_ESC2(&BCAN_msglist.FCTB_IC_ESC2.mon1);
	timeout_BCAN_FCTB_IC_SAS_info(&BCAN_msglist.FCTB_IC_SAS_info.mon1);
}

// FBTC_MP5_Mode  0x4fd  500
void cycle_BCAN_FBTC_MP5_Mode(BCAN_FrameMonitor_t* _mon)
{
	_mon->cycle_cnt++;
	if (_mon->cycle_cnt >= _mon->cycle)
	{
		_mon->cycle_cnt = 0;
	}
}

// FBTC_MP5_Mode  0x4fd  500
void timeout_BCAN_FBTC_MP5_Mode(BCAN_FrameMonitor_t* _mon)
{
	_mon->timeout_cnt++;
	if (_mon->timeout_cnt >= _mon->timeout_cycle)
	{
		_mon->timeout_cnt = _mon->timeout_cycle;
		BCAN_msglist.FBTC_MP5_Mode.MP5_VehiclePowerSwitch = 0;
		BCAN_msglist.FBTC_MP5_Mode.MP5_DriveModeSET = 0;
	}
}

// FCTB_CBS2  0x3ff  100
void cycle_BCAN_FCTB_CBS2(BCAN_FrameMonitor_t* _mon)
{
	_mon->cycle_cnt++;
	if (_mon->cycle_cnt >= _mon->cycle)
	{
		_mon->cycle_cnt = 0;
	}
}

// FCTB_CBS2  0x3ff  100
void timeout_BCAN_FCTB_CBS2(BCAN_FrameMonitor_t* _mon)
{
	_mon->timeout_cnt++;
	if (_mon->timeout_cnt >= _mon->timeout_cycle)
	{
		_mon->timeout_cnt = _mon->timeout_cycle;
		BCAN_msglist.FCTB_CBS2.CWB_DimmingSwitch = 0;
		BCAN_msglist.FCTB_CBS2.CWB_PreWashingSwitch = 0;
		BCAN_msglist.FCTB_CBS2.CWB_TurnSwitch = 0;
		BCAN_msglist.FCTB_CBS2.CWB_FrontWiperSwitch = 0;
		BCAN_msglist.FCTB_CBS2.CWB_FrontWiperAdjustment = 0;
	}
}

// FCTB_IC_ESC_EPB1  0x31a  100
void cycle_BCAN_FCTB_IC_ESC_EPB1(BCAN_FrameMonitor_t* _mon)
{
	_mon->cycle_cnt++;
	if (_mon->cycle_cnt >= _mon->cycle)
	{
		_mon->cycle_cnt = 0;
	}
}

// FCTB_IC_ESC_EPB1  0x31a  100
void timeout_BCAN_FCTB_IC_ESC_EPB1(BCAN_FrameMonitor_t* _mon)
{
	_mon->timeout_cnt++;
	if (_mon->timeout_cnt >= _mon->timeout_cycle)
	{
		_mon->timeout_cnt = _mon->timeout_cycle;
		BCAN_msglist.FCTB_IC_ESC_EPB1.ESC_EPBDisplayMessageReq = 0;
		BCAN_msglist.FCTB_IC_ESC_EPB1.ESC_EPBCruiseControlCancel = 0;
		BCAN_msglist.FCTB_IC_ESC_EPB1.ESC_EPBWarningIndicationReq = 0;
		BCAN_msglist.FCTB_IC_ESC_EPB1.ESC_EPBAudibleWarnningRequest = 0;
		BCAN_msglist.FCTB_IC_ESC_EPB1.ESC_EPBSystemStIndicationReq = 0;
		BCAN_msglist.FCTB_IC_ESC_EPB1.ESC_EPBSwitchStatics = 0;
		BCAN_msglist.FCTB_IC_ESC_EPB1.ESC_EPBSwitchStaticsValidity = 0;
		BCAN_msglist.FCTB_IC_ESC_EPB1.ESC_EPBStatus = 0;
		BCAN_msglist.FCTB_IC_ESC_EPB1.ESC_CurrentOnRightRearCaliper = 0;
		BCAN_msglist.FCTB_IC_ESC_EPB1.ESC_CurrentOnLeftRearCaliper = 0;
		BCAN_msglist.FCTB_IC_ESC_EPB1.ESC_EPBErrorStatus = 0;
		BCAN_msglist.FCTB_IC_ESC_EPB1.ESC_PbcActuatorStateRight = 0;
		BCAN_msglist.FCTB_IC_ESC_EPB1.ESC_PbcActuatorStateLeft = 0;
		BCAN_msglist.FCTB_IC_ESC_EPB1.ESC_RollingCount_EPB = 0;
		BCAN_msglist.FCTB_IC_ESC_EPB1.ESC_CheckSum_EPB = 0;
	}
}

// FCTB_IC_ESC3  0x121  20
void cycle_BCAN_FCTB_IC_ESC3(BCAN_FrameMonitor_t* _mon)
{
	_mon->cycle_cnt++;
	if (_mon->cycle_cnt >= _mon->cycle)
	{
		_mon->cycle_cnt = 0;
	}
}

// FCTB_IC_ESC3  0x121  20
void timeout_BCAN_FCTB_IC_ESC3(BCAN_FrameMonitor_t* _mon)
{
	_mon->timeout_cnt++;
	if (_mon->timeout_cnt >= _mon->timeout_cycle)
	{
		_mon->timeout_cnt = _mon->timeout_cycle;
		BCAN_msglist.FCTB_IC_ESC3.ESC_ReqDecreaseTorqueFlag = 0;
		BCAN_msglist.FCTB_IC_ESC3.ESC_ReqIncreaseTorqueFlag = 0;
		BCAN_msglist.FCTB_IC_ESC3.ESC_TCSCtlActive = 0;
		BCAN_msglist.FCTB_IC_ESC3.ESC_ESCAlarmSig = 0;
		BCAN_msglist.FCTB_IC_ESC3.ESC_ESCWorkStatus = 0;
		BCAN_msglist.FCTB_IC_ESC3.ESC_keepingGear = 0;
		BCAN_msglist.FCTB_IC_ESC3.ESC_ESCOFF = 0;
		BCAN_msglist.FCTB_IC_ESC3.ESC_ReqIncreaseTorque = 0;
		BCAN_msglist.FCTB_IC_ESC3.ESC_ReqDecreaseTorque = 0;
		BCAN_msglist.FCTB_IC_ESC3.ESC_epbRequest = 0;
		BCAN_msglist.FCTB_IC_ESC3.ESC_wheelDirectionRLValid = 0;
		BCAN_msglist.FCTB_IC_ESC3.ESC_wheelDirectionRRValid = 0;
		BCAN_msglist.FCTB_IC_ESC3.ESC_FRWDirection = 0;
		BCAN_msglist.FCTB_IC_ESC3.ESC_FLWDirection = 0;
		BCAN_msglist.FCTB_IC_ESC3.ESC_RRWDirection = 0;
		BCAN_msglist.FCTB_IC_ESC3.ESC_RLWDirection = 0;
		BCAN_msglist.FCTB_IC_ESC3.ESC_ESCValidity = 0;
		BCAN_msglist.FCTB_IC_ESC3.ESC_vehicleStandstillValid = 0;
		BCAN_msglist.FCTB_IC_ESC3.ESC_TCSErrorStatus = 0;
		BCAN_msglist.FCTB_IC_ESC3.ESC_VehicleStandstill = 0;
		BCAN_msglist.FCTB_IC_ESC3.GW_ESC_RollingCount_ESC3 = 0;
		BCAN_msglist.FCTB_IC_ESC3.GW_ESC_CheckSum_ESC3 = 0;
	}
}

// FCTB_IC_ESC6  0x123  20
void cycle_BCAN_FCTB_IC_ESC6(BCAN_FrameMonitor_t* _mon)
{
	_mon->cycle_cnt++;
	if (_mon->cycle_cnt >= _mon->cycle)
	{
		_mon->cycle_cnt = 0;
	}
}

// FCTB_IC_ESC6  0x123  20
void timeout_BCAN_FCTB_IC_ESC6(BCAN_FrameMonitor_t* _mon)
{
	_mon->timeout_cnt++;
	if (_mon->timeout_cnt >= _mon->timeout_cycle)
	{
		_mon->timeout_cnt = _mon->timeout_cycle;
		BCAN_msglist.FCTB_IC_ESC6.ESC_DynamicSlopeAccuracy = 0;
		BCAN_msglist.FCTB_IC_ESC6.ESC_AVHFunctionSwitch = 0;
		BCAN_msglist.FCTB_IC_ESC6.ESC_AVHAvailable = 0;
		BCAN_msglist.FCTB_IC_ESC6.ESC_AVH_Status = 0;
		BCAN_msglist.FCTB_IC_ESC6.ESC_AVH_DisplayMessageReq = 0;
		BCAN_msglist.FCTB_IC_ESC6.ESC_BLRequest = 0;
		BCAN_msglist.FCTB_IC_ESC6.ESC_EmergencyBrakeLightReq = 0;
		BCAN_msglist.FCTB_IC_ESC6.ESC_BrakingEffort = 0;
		BCAN_msglist.FCTB_IC_ESC6.ESC_MSRinRegulation = 0;
		BCAN_msglist.FCTB_IC_ESC6.ESC_BrakeReleasedFailsafe = 0;
		BCAN_msglist.FCTB_IC_ESC6.ESC_UnfilteredYawRate = 0;
		BCAN_msglist.FCTB_IC_ESC6.ESC_VehDrivingDirection = 0;
		BCAN_msglist.FCTB_IC_ESC6.ESC_DynamicSlope = 0;
		BCAN_msglist.FCTB_IC_ESC6.ESC_VehicleHoldStatus = 0;
		BCAN_msglist.FCTB_IC_ESC6.ESC_cdpAvailable = 0;
		BCAN_msglist.FCTB_IC_ESC6.ESC_cdpActive = 0;
		BCAN_msglist.FCTB_IC_ESC6.ESC_HBAStatus = 0;
		BCAN_msglist.FCTB_IC_ESC6.ESC_RollingCount_ESC6 = 0;
		BCAN_msglist.FCTB_IC_ESC6.ESC_CheckSum_ESC6 = 0;
	}
}

// FCTB_CGW_VCU5  0x355  100
void cycle_BCAN_FCTB_CGW_VCU5(BCAN_FrameMonitor_t* _mon)
{
	_mon->cycle_cnt++;
	if (_mon->cycle_cnt >= _mon->cycle)
	{
		_mon->cycle_cnt = 0;
	}
}

// FCTB_CGW_VCU5  0x355  100
void timeout_BCAN_FCTB_CGW_VCU5(BCAN_FrameMonitor_t* _mon)
{
	_mon->timeout_cnt++;
	if (_mon->timeout_cnt >= _mon->timeout_cycle)
	{
		_mon->timeout_cnt = _mon->timeout_cycle;
		BCAN_msglist.FCTB_CGW_VCU5.VCU_DrivingPermit = 0;
		BCAN_msglist.FCTB_CGW_VCU5.PDCU_ShiftLvlPosn = 0;
		BCAN_msglist.FCTB_CGW_VCU5.PDCU_SysFaultWarn = 0;
		BCAN_msglist.FCTB_CGW_VCU5.PDCU_PrfmncLimitedWarn = 0;
		BCAN_msglist.FCTB_CGW_VCU5.VCU_PumpInvalidWarning = 0;
		BCAN_msglist.FCTB_CGW_VCU5.PDCU_CruisingRange = 0;
		BCAN_msglist.FCTB_CGW_VCU5.PDCU_ParkLockSt = 0;
		BCAN_msglist.FCTB_CGW_VCU5.PDCU_ActualRegenLvl = 0;
		BCAN_msglist.FCTB_CGW_VCU5.PDCU_DCDCworkSt = 0;
	}
}

// FBTC_AC_Front2  0x37c  100
void cycle_BCAN_FBTC_AC_Front2(BCAN_FrameMonitor_t* _mon)
{
	_mon->cycle_cnt++;
	if (_mon->cycle_cnt >= _mon->cycle)
	{
		_mon->cycle_cnt = 0;
	}
}

// FBTC_AC_Front2  0x37c  100
void timeout_BCAN_FBTC_AC_Front2(BCAN_FrameMonitor_t* _mon)
{
	_mon->timeout_cnt++;
	if (_mon->timeout_cnt >= _mon->timeout_cycle)
	{
		_mon->timeout_cnt = _mon->timeout_cycle;
		BCAN_msglist.FBTC_AC_Front2.AC_InCarTemp = 0;
		BCAN_msglist.FBTC_AC_Front2.AC_FrontEvapTempTarget = 0;
		BCAN_msglist.FBTC_AC_Front2.AC_FrontHeaterInletTempSet = 0;
		BCAN_msglist.FBTC_AC_Front2.AC_FrontACStartReq = 0;
	}
}

// FBTC_MP5_6  0x413  500
void cycle_BCAN_FBTC_MP5_6(BCAN_FrameMonitor_t* _mon)
{
	_mon->cycle_cnt++;
	if (_mon->cycle_cnt >= _mon->cycle)
	{
		_mon->cycle_cnt = 0;
	}
}

// FBTC_MP5_6  0x413  500
void timeout_BCAN_FBTC_MP5_6(BCAN_FrameMonitor_t* _mon)
{
	_mon->timeout_cnt++;
	if (_mon->timeout_cnt >= _mon->timeout_cycle)
	{
		_mon->timeout_cnt = _mon->timeout_cycle;
		BCAN_msglist.FBTC_MP5_6.Mp5_LKA_Mode = 0;
		BCAN_msglist.FBTC_MP5_6.Mp5_LKA_main_SW = 0;
		BCAN_msglist.FBTC_MP5_6.Mp5_ISA_Switch = 0;
		BCAN_msglist.FBTC_MP5_6.Mp5_TSR_Switch = 0;
		BCAN_msglist.FBTC_MP5_6.MP5_DriveModeRemSwitch = 0;
		BCAN_msglist.FBTC_MP5_6.MFS_AVASSystemSwitch = 0;
		BCAN_msglist.FBTC_MP5_6.MP5_EnergyReturnIntensionSet = 0;
		BCAN_msglist.FBTC_MP5_6.MP5_SayHi = 0;
		BCAN_msglist.FBTC_MP5_6.MP5_SerchCar = 0;
		BCAN_msglist.FBTC_MP5_6.MP5_Open_Close = 0;
	}
}

// FBTC_MP5_TBOX_Time  0x4da  1000
void cycle_BCAN_FBTC_MP5_TBOX_Time(BCAN_FrameMonitor_t* _mon)
{
	_mon->cycle_cnt++;
	if (_mon->cycle_cnt >= _mon->cycle)
	{
		_mon->cycle_cnt = 0;
	}
}

// FBTC_MP5_TBOX_Time  0x4da  1000
void timeout_BCAN_FBTC_MP5_TBOX_Time(BCAN_FrameMonitor_t* _mon)
{
	_mon->timeout_cnt++;
	if (_mon->timeout_cnt >= _mon->timeout_cycle)
	{
		_mon->timeout_cnt = _mon->timeout_cycle;
		BCAN_msglist.FBTC_MP5_TBOX_Time.MP5_TBOX_Time_Month = 0;
		BCAN_msglist.FBTC_MP5_TBOX_Time.MP5_TBOX_Time_Valid = 0;
		BCAN_msglist.FBTC_MP5_TBOX_Time.MP5_TBOX_Time_YearMark = 0;
		BCAN_msglist.FBTC_MP5_TBOX_Time.MP5_TBOX_Time_Date = 0;
		BCAN_msglist.FBTC_MP5_TBOX_Time.MP5_TBOX_Time_Hour = 0;
		BCAN_msglist.FBTC_MP5_TBOX_Time.MP5_TBOX_Time_Minute = 0;
		BCAN_msglist.FBTC_MP5_TBOX_Time.MP5_TBOX_Time_Second = 0;
		BCAN_msglist.FBTC_MP5_TBOX_Time.MP5_TBOX_Time_Year = 0;
	}
}

// FBTC_MP5_2  0x366  500
void cycle_BCAN_FBTC_MP5_2(BCAN_FrameMonitor_t* _mon)
{
	_mon->cycle_cnt++;
	if (_mon->cycle_cnt >= _mon->cycle)
	{
		_mon->cycle_cnt = 0;
	}
}

// FBTC_MP5_2  0x366  500
void timeout_BCAN_FBTC_MP5_2(BCAN_FrameMonitor_t* _mon)
{
	_mon->timeout_cnt++;
	if (_mon->timeout_cnt >= _mon->timeout_cycle)
	{
		_mon->timeout_cnt = _mon->timeout_cycle;
		BCAN_msglist.FBTC_MP5_2.MP5_HU_SlotUserSelected = 0;
		BCAN_msglist.FBTC_MP5_2.MP5_WorkSt = 0;
		BCAN_msglist.FBTC_MP5_2.MP5_GearshiftRemindFunctEnaSwi = 0;
		BCAN_msglist.FBTC_MP5_2.MP5_DDS_resetbutton_request = 0;
		BCAN_msglist.FBTC_MP5_2.MP5_AutoWindLockSe = 0;
		BCAN_msglist.FBTC_MP5_2.MP5_AutoWindUnlockSet = 0;
		BCAN_msglist.FBTC_MP5_2.MP5_AutoWindKeyPressSet = 0;
		BCAN_msglist.FBTC_MP5_2.MP5_ICStyle_Set = 0;
		BCAN_msglist.FBTC_MP5_2.MP5_Language_Set = 0;
		BCAN_msglist.FBTC_MP5_2.MP5_IC_PersonalizedSet_right = 0;
		BCAN_msglist.FBTC_MP5_2.MP5_IC_PersonalizedSet_left = 0;
		BCAN_msglist.FBTC_MP5_2.MP5_PM2_5_EnableSwitch = 0;
		BCAN_msglist.FBTC_MP5_2.MP5_HU_ULS_BSD_ACTIVATION = 0;
		BCAN_msglist.FBTC_MP5_2.MP5_HU_ULS_FLK_ACTIVATION = 0;
		BCAN_msglist.FBTC_MP5_2.MP5_BrightnessChange = 0;
		BCAN_msglist.FBTC_MP5_2.MP5_ESCOFFSwitch = 0;
		BCAN_msglist.FBTC_MP5_2.MP5_FCWSwitch = 0;
		BCAN_msglist.FBTC_MP5_2.MP5_AEBSwitch = 0;
		BCAN_msglist.FBTC_MP5_2.MP5_FCW_Sensitivity = 0;
		BCAN_msglist.FBTC_MP5_2.MP5_AVHbutton = 0;
	}
}

// FBTC_AC1  0x322  100
void cycle_BCAN_FBTC_AC1(BCAN_FrameMonitor_t* _mon)
{
	_mon->cycle_cnt++;
	if (_mon->cycle_cnt >= _mon->cycle)
	{
		_mon->cycle_cnt = 0;
	}
}

// FBTC_AC1  0x322  100
void timeout_BCAN_FBTC_AC1(BCAN_FrameMonitor_t* _mon)
{
	_mon->timeout_cnt++;
	if (_mon->timeout_cnt >= _mon->timeout_cycle)
	{
		_mon->timeout_cnt = _mon->timeout_cycle;
		BCAN_msglist.FBTC_AC1.AC_AmbTemp = 0;
		BCAN_msglist.FBTC_AC1.AC_SystemOff = 0;
		BCAN_msglist.FBTC_AC1.AC_IntakeWindSt = 0;
		BCAN_msglist.FBTC_AC1.AC_RearWindowHeatReq = 0;
		BCAN_msglist.FBTC_AC1.AC_BlowerWorkSt = 0;
		BCAN_msglist.FBTC_AC1.AC_ACCompressorReqSig = 0;
		BCAN_msglist.FBTC_AC1.AC_AutoModeSt = 0;
		BCAN_msglist.FBTC_AC1.AC_BlowLvlSt = 0;
		BCAN_msglist.FBTC_AC1.AC_BlowMode = 0;
		BCAN_msglist.FBTC_AC1.BDC_AC_FrontDefrostMAXSt = 0;
		BCAN_msglist.FBTC_AC1.AC_TempLevel = 0;
		BCAN_msglist.FBTC_AC1.AC_EvapTemp = 0;
		BCAN_msglist.FBTC_AC1.AC_AmbTempSensorDTC = 0;
		BCAN_msglist.FBTC_AC1.AC_ACRunningStatus = 0;
		BCAN_msglist.FBTC_AC1.AC_ACStatus = 0;
		BCAN_msglist.FBTC_AC1.AC_WindTemp = 0;
		BCAN_msglist.FBTC_AC1.AC_MP5DisplayPopupReq = 0;
		BCAN_msglist.FBTC_AC1.AC_LED_AC = 0;
	}
}

// FBTC_IBCM6  0x341  100
void cycle_BCAN_FBTC_IBCM6(BCAN_FrameMonitor_t* _mon)
{
	_mon->cycle_cnt++;
	if (_mon->cycle_cnt >= _mon->cycle)
	{
		_mon->cycle_cnt = 0;
	}
}

// FBTC_IBCM6  0x341  100
void timeout_BCAN_FBTC_IBCM6(BCAN_FrameMonitor_t* _mon)
{
	_mon->timeout_cnt++;
	if (_mon->timeout_cnt >= _mon->timeout_cycle)
	{
		_mon->timeout_cnt = _mon->timeout_cycle;
		BCAN_msglist.FBTC_IBCM6.BCM_BattVolt = 0;
		BCAN_msglist.FBTC_IBCM6.BCM_BECB_BattCurrent = 0;
		BCAN_msglist.FBTC_IBCM6.BCM_BECB_BattSOCStatus = 0;
		BCAN_msglist.FBTC_IBCM6.BCM_BECB_BattSOC = 0;
		BCAN_msglist.FBTC_IBCM6.BCM_BECB_Sensor_Config = 0;
		BCAN_msglist.FBTC_IBCM6.BCM_BECB_BattSensorStatus = 0;
		BCAN_msglist.FBTC_IBCM6.IBCM_SunshadCurCloseLockSt = 0;
		BCAN_msglist.FBTC_IBCM6.IBCM_AtwsAlarmedType = 0;
		BCAN_msglist.FBTC_IBCM6.IBCM_PanicType = 0;
		BCAN_msglist.FBTC_IBCM6.BCM_LowPowerWarning = 0;
		BCAN_msglist.FBTC_IBCM6.BCM_CarMode = 0;
	}
}

// FBTC_IBCM3  0x33c  100
void cycle_BCAN_FBTC_IBCM3(BCAN_FrameMonitor_t* _mon)
{
	_mon->cycle_cnt++;
	if (_mon->cycle_cnt >= _mon->cycle)
	{
		_mon->cycle_cnt = 0;
	}
}

// FBTC_IBCM3  0x33c  100
void timeout_BCAN_FBTC_IBCM3(BCAN_FrameMonitor_t* _mon)
{
	_mon->timeout_cnt++;
	if (_mon->timeout_cnt >= _mon->timeout_cycle)
	{
		_mon->timeout_cnt = _mon->timeout_cycle;
		BCAN_msglist.FBTC_IBCM3.BCM_LowBeamFaultStatus = 0;
		BCAN_msglist.FBTC_IBCM3.BCM_LampOnWarning = 0;
		BCAN_msglist.FBTC_IBCM3.BCM_LowBeamSwitchStatus = 0;
		BCAN_msglist.FBTC_IBCM3.BCM_BrakeSwitchSt = 0;
		BCAN_msglist.FBTC_IBCM3.BCM_DoorLockSt = 0;
		BCAN_msglist.FBTC_IBCM3.BCM_IgnitionSt = 0;
		BCAN_msglist.FBTC_IBCM3.BCM_FrontWiperSwitchSt = 0;
		BCAN_msglist.FBTC_IBCM3.BCM_EngLock = 0;
		BCAN_msglist.FBTC_IBCM3.BCM_BuzzerRequest = 0;
		BCAN_msglist.FBTC_IBCM3.BCM_BackWiperWorkSt = 0;
		BCAN_msglist.FBTC_IBCM3.BCM_BackWiperSwitchSt = 0;
		BCAN_msglist.FBTC_IBCM3.BCM_FrontWiperParkst = 0;
		BCAN_msglist.FBTC_IBCM3.BCM_ATWS_Sts = 0;
		BCAN_msglist.FBTC_IBCM3.BCM_ATWSFunctionStatus = 0;
		BCAN_msglist.FBTC_IBCM3.BCM_BackWiperParkst = 0;
		BCAN_msglist.FBTC_IBCM3.BCM_FrontWiperINTTimeStatus = 0;
		BCAN_msglist.FBTC_IBCM3.BCM_PowerMode = 0;
		BCAN_msglist.FBTC_IBCM3.BCM_FrontFogFaultStatus = 0;
		BCAN_msglist.FBTC_IBCM3.BCM_FrontFogSwtichStatus = 0;
		BCAN_msglist.FBTC_IBCM3.BCM_HighBeamFaultStatus = 0;
		BCAN_msglist.FBTC_IBCM3.BCM_HighBeamSwtichStatus = 0;
		BCAN_msglist.FBTC_IBCM3.BCM_FRDoorLampStatus = 0;
		BCAN_msglist.FBTC_IBCM3.BCM_FLDoorLampStatus = 0;
		BCAN_msglist.FBTC_IBCM3.BCM_BrakeLampStatus = 0;
		BCAN_msglist.FBTC_IBCM3.BCM_CHMSLStatus = 0;
		BCAN_msglist.FBTC_IBCM3.BCM_ReverseLampStatus = 0;
		BCAN_msglist.FBTC_IBCM3.BCM_BackFogSwtichStatus = 0;
		BCAN_msglist.FBTC_IBCM3.BCM_IlluminationLampStatus = 0;
		BCAN_msglist.FBTC_IBCM3.BCM_TrunkLampStatus = 0;
		BCAN_msglist.FBTC_IBCM3.BCM_LogLampStatus = 0;
		BCAN_msglist.FBTC_IBCM3.BCM_WelcomeLampStatus = 0;
		BCAN_msglist.FBTC_IBCM3.BCM_PositionLampFaultStatus = 0;
		BCAN_msglist.FBTC_IBCM3.BCM_RightDayTimeRunningLampSta = 0;
		BCAN_msglist.FBTC_IBCM3.BCM_LeftDayTimeRunningLampStatus = 0;
		BCAN_msglist.FBTC_IBCM3.BCM_BatterySaverOutputStatus = 0;
	}
}

// FCTB_GW_ACU_Crash  0x30c  100
void cycle_BCAN_FCTB_GW_ACU_Crash(BCAN_FrameMonitor_t* _mon)
{
	_mon->cycle_cnt++;
	if (_mon->cycle_cnt >= _mon->cycle)
	{
		_mon->cycle_cnt = 0;
	}
}

// FCTB_GW_ACU_Crash  0x30c  100
void timeout_BCAN_FCTB_GW_ACU_Crash(BCAN_FrameMonitor_t* _mon)
{
	_mon->timeout_cnt++;
	if (_mon->timeout_cnt >= _mon->timeout_cycle)
	{
		_mon->timeout_cnt = _mon->timeout_cycle;
		BCAN_msglist.FCTB_GW_ACU_Crash.RollingCounter30C = 0;
		BCAN_msglist.FCTB_GW_ACU_Crash.ACU_AirbagLampSts = 0;
		BCAN_msglist.FCTB_GW_ACU_Crash.ACU_Crashout = 0;
		BCAN_msglist.FCTB_GW_ACU_Crash.ACU_PassengerBeltSwitchSig = 0;
		BCAN_msglist.FCTB_GW_ACU_Crash.ACU_DriverBeltSwitchSig = 0;
		BCAN_msglist.FCTB_GW_ACU_Crash.ACU_CrashoutValid = 0;
		BCAN_msglist.FCTB_GW_ACU_Crash.ACU_CheckSum_ACU = 0;
	}
}

// FBTC_IBCM2  0x23a  40
void cycle_BCAN_FBTC_IBCM2(BCAN_FrameMonitor_t* _mon)
{
	_mon->cycle_cnt++;
	if (_mon->cycle_cnt >= _mon->cycle)
	{
		_mon->cycle_cnt = 0;
	}
}

// FBTC_IBCM2  0x23a  40
void timeout_BCAN_FBTC_IBCM2(BCAN_FrameMonitor_t* _mon)
{
	_mon->timeout_cnt++;
	if (_mon->timeout_cnt >= _mon->timeout_cycle)
	{
		_mon->timeout_cnt = _mon->timeout_cycle;
		BCAN_msglist.FBTC_IBCM2.BCM_HighBeamStatus = 0;
		BCAN_msglist.FBTC_IBCM2.BCM_HazardLampSt = 0;
		BCAN_msglist.FBTC_IBCM2.BCM_PositionLampSt = 0;
		BCAN_msglist.FBTC_IBCM2.BCM_RightligthFaultSt = 0;
		BCAN_msglist.FBTC_IBCM2.BCM_RightligthSt = 0;
		BCAN_msglist.FBTC_IBCM2.BCM_LetfligthFaultSt = 0;
		BCAN_msglist.FBTC_IBCM2.BCM_LetfligthSt = 0;
		BCAN_msglist.FBTC_IBCM2.BCM_TrunkSt = 0;
		BCAN_msglist.FBTC_IBCM2.BCM_LRDoorSwitchSt = 0;
		BCAN_msglist.FBTC_IBCM2.BCM_RRDoorSwitchSt = 0;
		BCAN_msglist.FBTC_IBCM2.BCM_RFDoorSwitchSt = 0;
		BCAN_msglist.FBTC_IBCM2.BCM_LFDoorSwitchSt = 0;
		BCAN_msglist.FBTC_IBCM2.BCM_frontFogligthSt = 0;
		BCAN_msglist.FBTC_IBCM2.BCM_BackFogligthSt = 0;
		BCAN_msglist.FBTC_IBCM2.BCM_LowBeamStatus = 0;
		BCAN_msglist.FBTC_IBCM2.BCM_RightTurnSwitchrSt = 0;
		BCAN_msglist.FBTC_IBCM2.BCM_LeftTurnSwitchSt = 0;
		BCAN_msglist.FBTC_IBCM2.BCM_Lock_LED_Output = 0;
		BCAN_msglist.FBTC_IBCM2.BCM_AutoLockFunctionSt = 0;
		BCAN_msglist.FBTC_IBCM2.BCM_RearWindowHeatSt = 0;
		BCAN_msglist.FBTC_IBCM2.BCM_IntTrunkSwitch = 0;
		BCAN_msglist.FBTC_IBCM2.BCM_FRTurnlightFbSt = 0;
		BCAN_msglist.FBTC_IBCM2.BCM_RRTurnlightFbSt = 0;
		BCAN_msglist.FBTC_IBCM2.BCM_FLTurnlightFbSt = 0;
		BCAN_msglist.FBTC_IBCM2.BCM_RLTurnlightFbSt = 0;
		BCAN_msglist.FBTC_IBCM2.BCM_LampWashSt = 0;
		BCAN_msglist.FBTC_IBCM2.BCM_ReverseLampSwitchSt = 0;
		BCAN_msglist.FBTC_IBCM2.BCM_RecentlyLockType = 0;
		BCAN_msglist.FBTC_IBCM2.BCM_RecentlyUnlockType = 0;
		BCAN_msglist.FBTC_IBCM2.BCM_RLS_AUTO_SwitchSt = 0;
		BCAN_msglist.FBTC_IBCM2.BCM_FrontWiperWorkSt = 0;
		BCAN_msglist.FBTC_IBCM2.BCM_MirrorFoldSwitchSt = 0;
		BCAN_msglist.FBTC_IBCM2.BCM_SunShadeStatus = 0;
		BCAN_msglist.FBTC_IBCM2.BCM_RoofWindowStatus = 0;
		BCAN_msglist.FBTC_IBCM2.BCM_RRWindowStatus = 0;
		BCAN_msglist.FBTC_IBCM2.BCM_RFWindowStatus = 0;
		BCAN_msglist.FBTC_IBCM2.BCM_RLWindowStatus = 0;
		BCAN_msglist.FBTC_IBCM2.BCM_LFWindowStatus = 0;
		BCAN_msglist.FBTC_IBCM2.BCM_TailgateUnlockInform = 0;
		BCAN_msglist.FBTC_IBCM2.BCM_TailgateOpenSwitch = 0;
		BCAN_msglist.FBTC_IBCM2.BCM_FrontWiper_AUTO = 0;
		BCAN_msglist.FBTC_IBCM2.BCM_LowBeam_AUTO = 0;
		BCAN_msglist.FBTC_IBCM2.Right_TurnLamp_Water_Control = 0;
		BCAN_msglist.FBTC_IBCM2.Left_TurnLamp_Water_Control = 0;
	}
}

// FCTB_GW_ESC7  0x431  1000
void cycle_BCAN_FCTB_GW_ESC7(BCAN_FrameMonitor_t* _mon)
{
	_mon->cycle_cnt++;
	if (_mon->cycle_cnt >= _mon->cycle)
	{
		_mon->cycle_cnt = 0;
	}
}

// FCTB_GW_ESC7  0x431  1000
void timeout_BCAN_FCTB_GW_ESC7(BCAN_FrameMonitor_t* _mon)
{
	_mon->timeout_cnt++;
	if (_mon->timeout_cnt >= _mon->timeout_cycle)
	{
		_mon->timeout_cnt = _mon->timeout_cycle;
		BCAN_msglist.FCTB_GW_ESC7.GW_ESC_ITPMSFrontRightPressWarn = 0;
		BCAN_msglist.FCTB_GW_ESC7.GW_ESC_ITPMSFrontLeftPressWarn = 0;
		BCAN_msglist.FCTB_GW_ESC7.GW_ESC_ITPMSRearRightPressWarn = 0;
		BCAN_msglist.FCTB_GW_ESC7.GW_ESC_ITPMSRearLeftPressWarn = 0;
		BCAN_msglist.FCTB_GW_ESC7.GW_ESC_DDS_SystemStatus = 0;
	}
}

// FCTB_IC_ESC2  0xa0  10
void cycle_BCAN_FCTB_IC_ESC2(BCAN_FrameMonitor_t* _mon)
{
	_mon->cycle_cnt++;
	if (_mon->cycle_cnt >= _mon->cycle)
	{
		_mon->cycle_cnt = 0;
	}
}

// FCTB_IC_ESC2  0xa0  10
void timeout_BCAN_FCTB_IC_ESC2(BCAN_FrameMonitor_t* _mon)
{
	_mon->timeout_cnt++;
	if (_mon->timeout_cnt >= _mon->timeout_cycle)
	{
		_mon->timeout_cnt = _mon->timeout_cycle;
		BCAN_msglist.FCTB_IC_ESC2.GW_ESC_BrakeOilPress = 0;
		BCAN_msglist.FCTB_IC_ESC2.GW_ABS_WorkLable = 0;
		BCAN_msglist.FCTB_IC_ESC2.GW_ESC_TCSCtlActive = 0;
		BCAN_msglist.FCTB_IC_ESC2.GW_ESC_ABSAlarmSig = 0;
		BCAN_msglist.FCTB_IC_ESC2.GW_ESC_VehSpdValidFlag = 0;
		BCAN_msglist.FCTB_IC_ESC2.GW_ESC_EBDAlarmSig = 0;
		BCAN_msglist.FCTB_IC_ESC2.GW_ESC_Brake_fluid_level_alarm = 0;
		BCAN_msglist.FCTB_IC_ESC2.GW_ESC_VehSpd = 0;
	}
}

// FCTB_IC_SAS_info  0xa5  10
void cycle_BCAN_FCTB_IC_SAS_info(BCAN_FrameMonitor_t* _mon)
{
	_mon->cycle_cnt++;
	if (_mon->cycle_cnt >= _mon->cycle)
	{
		_mon->cycle_cnt = 0;
	}
}

// FCTB_IC_SAS_info  0xa5  10
void timeout_BCAN_FCTB_IC_SAS_info(BCAN_FrameMonitor_t* _mon)
{
	_mon->timeout_cnt++;
	if (_mon->timeout_cnt >= _mon->timeout_cycle)
	{
		_mon->timeout_cnt = _mon->timeout_cycle;
		BCAN_msglist.FCTB_IC_SAS_info.GW_EPS_SAS_SteeringAngle = 0;
	}
}

