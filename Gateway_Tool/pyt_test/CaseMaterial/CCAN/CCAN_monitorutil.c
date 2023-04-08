#include <stdint.h>
#include "CCAN_binutil.h"
#include "CCAN_monitorutil.h"


void CCAN_TimeoutInit()
{
	// FBTC_MP5_Mode  0x4fd  500
	CCAN_msglist.FBTC_MP5_Mode.mon1.cycle = 50;
	CCAN_msglist.FBTC_MP5_Mode.mon1.timeout_cycle = 250;

	// FBTC_AC_Front2  0x37c  100
	CCAN_msglist.FBTC_AC_Front2.mon1.cycle = 10;
	CCAN_msglist.FBTC_AC_Front2.mon1.timeout_cycle = 50;

	// FCTB_CBS2  0x3ff  100
	CCAN_msglist.FCTB_CBS2.mon1.cycle = 10;
	CCAN_msglist.FCTB_CBS2.mon1.timeout_cycle = 50;

	// FBTC_MP5_6  0x413  500
	CCAN_msglist.FBTC_MP5_6.mon1.cycle = 50;
	CCAN_msglist.FBTC_MP5_6.mon1.timeout_cycle = 250;

	// FBTC_GW_MP5_2  0x366  500
	CCAN_msglist.FBTC_GW_MP5_2.mon1.cycle = 50;
	CCAN_msglist.FBTC_GW_MP5_2.mon1.timeout_cycle = 250;

	// FCTB_GW_VCUtoDisplay  0x355  100
	CCAN_msglist.FCTB_GW_VCUtoDisplay.mon1.cycle = 10;
	CCAN_msglist.FCTB_GW_VCUtoDisplay.mon1.timeout_cycle = 50;

	// FBTC_GW_AC1  0x322  100
	CCAN_msglist.FBTC_GW_AC1.mon1.cycle = 10;
	CCAN_msglist.FBTC_GW_AC1.mon1.timeout_cycle = 50;

	// FBTC_GW_MP5_TBOX_Time  0x4da  1000
	CCAN_msglist.FBTC_GW_MP5_TBOX_Time.mon1.cycle = 100;
	CCAN_msglist.FBTC_GW_MP5_TBOX_Time.mon1.timeout_cycle = 500;

	// FBTC_GW_IBCM6  0x341  100
	CCAN_msglist.FBTC_GW_IBCM6.mon1.cycle = 10;
	CCAN_msglist.FBTC_GW_IBCM6.mon1.timeout_cycle = 50;

	// FBTC_GW_IBCM3  0x33c  100
	CCAN_msglist.FBTC_GW_IBCM3.mon1.cycle = 10;
	CCAN_msglist.FBTC_GW_IBCM3.mon1.timeout_cycle = 50;

	// FBTC_GW_IBCM2  0x23a  40
	CCAN_msglist.FBTC_GW_IBCM2.mon1.cycle = 4;
	CCAN_msglist.FBTC_GW_IBCM2.mon1.timeout_cycle = 20;

	// FCTB_ACU_Crash  0x30c  100
	CCAN_msglist.FCTB_ACU_Crash.mon1.cycle = 10;
	CCAN_msglist.FCTB_ACU_Crash.mon1.timeout_cycle = 50;

	// FCTB_TAS_SAS_Info  0xa5  10
	CCAN_msglist.FCTB_TAS_SAS_Info.mon1.cycle = 1;
	CCAN_msglist.FCTB_TAS_SAS_Info.mon1.timeout_cycle = 5;

	// FCTB_ESC_FPB1  0x31a  100
	CCAN_msglist.FCTB_ESC_FPB1.mon1.cycle = 10;
	CCAN_msglist.FCTB_ESC_FPB1.mon1.timeout_cycle = 50;

	// FCTB_ESC7  0x431  1000
	CCAN_msglist.FCTB_ESC7.mon1.cycle = 100;
	CCAN_msglist.FCTB_ESC7.mon1.timeout_cycle = 500;

	// FCTB_ESC6  0x123  20
	CCAN_msglist.FCTB_ESC6.mon1.cycle = 2;
	CCAN_msglist.FCTB_ESC6.mon1.timeout_cycle = 10;

	// FCTB_ESC3  0x121  20
	CCAN_msglist.FCTB_ESC3.mon1.cycle = 2;
	CCAN_msglist.FCTB_ESC3.mon1.timeout_cycle = 10;

	// FCTB_ESC2  0xa0  10
	CCAN_msglist.FCTB_ESC2.mon1.cycle = 1;
	CCAN_msglist.FCTB_ESC2.mon1.timeout_cycle = 5;

}

void CCAN_cycleFunc(void)
{
	cycle_CCAN_FBTC_MP5_Mode(&CCAN_msglist.FBTC_MP5_Mode.mon1);
	cycle_CCAN_FBTC_AC_Front2(&CCAN_msglist.FBTC_AC_Front2.mon1);
	cycle_CCAN_FCTB_CBS2(&CCAN_msglist.FCTB_CBS2.mon1);
	cycle_CCAN_FBTC_MP5_6(&CCAN_msglist.FBTC_MP5_6.mon1);
	cycle_CCAN_FBTC_GW_MP5_2(&CCAN_msglist.FBTC_GW_MP5_2.mon1);
	cycle_CCAN_FCTB_GW_VCUtoDisplay(&CCAN_msglist.FCTB_GW_VCUtoDisplay.mon1);
	cycle_CCAN_FBTC_GW_AC1(&CCAN_msglist.FBTC_GW_AC1.mon1);
	cycle_CCAN_FBTC_GW_MP5_TBOX_Time(&CCAN_msglist.FBTC_GW_MP5_TBOX_Time.mon1);
	cycle_CCAN_FBTC_GW_IBCM6(&CCAN_msglist.FBTC_GW_IBCM6.mon1);
	cycle_CCAN_FBTC_GW_IBCM3(&CCAN_msglist.FBTC_GW_IBCM3.mon1);
	cycle_CCAN_FBTC_GW_IBCM2(&CCAN_msglist.FBTC_GW_IBCM2.mon1);
	cycle_CCAN_FCTB_ACU_Crash(&CCAN_msglist.FCTB_ACU_Crash.mon1);
	cycle_CCAN_FCTB_TAS_SAS_Info(&CCAN_msglist.FCTB_TAS_SAS_Info.mon1);
	cycle_CCAN_FCTB_ESC_FPB1(&CCAN_msglist.FCTB_ESC_FPB1.mon1);
	cycle_CCAN_FCTB_ESC7(&CCAN_msglist.FCTB_ESC7.mon1);
	cycle_CCAN_FCTB_ESC6(&CCAN_msglist.FCTB_ESC6.mon1);
	cycle_CCAN_FCTB_ESC3(&CCAN_msglist.FCTB_ESC3.mon1);
	cycle_CCAN_FCTB_ESC2(&CCAN_msglist.FCTB_ESC2.mon1);
}

void CCAN_timeoutFunc(void)
{
	timeout_CCAN_FBTC_MP5_Mode(&CCAN_msglist.FBTC_MP5_Mode.mon1);
	timeout_CCAN_FBTC_AC_Front2(&CCAN_msglist.FBTC_AC_Front2.mon1);
	timeout_CCAN_FCTB_CBS2(&CCAN_msglist.FCTB_CBS2.mon1);
	timeout_CCAN_FBTC_MP5_6(&CCAN_msglist.FBTC_MP5_6.mon1);
	timeout_CCAN_FBTC_GW_MP5_2(&CCAN_msglist.FBTC_GW_MP5_2.mon1);
	timeout_CCAN_FCTB_GW_VCUtoDisplay(&CCAN_msglist.FCTB_GW_VCUtoDisplay.mon1);
	timeout_CCAN_FBTC_GW_AC1(&CCAN_msglist.FBTC_GW_AC1.mon1);
	timeout_CCAN_FBTC_GW_MP5_TBOX_Time(&CCAN_msglist.FBTC_GW_MP5_TBOX_Time.mon1);
	timeout_CCAN_FBTC_GW_IBCM6(&CCAN_msglist.FBTC_GW_IBCM6.mon1);
	timeout_CCAN_FBTC_GW_IBCM3(&CCAN_msglist.FBTC_GW_IBCM3.mon1);
	timeout_CCAN_FBTC_GW_IBCM2(&CCAN_msglist.FBTC_GW_IBCM2.mon1);
	timeout_CCAN_FCTB_ACU_Crash(&CCAN_msglist.FCTB_ACU_Crash.mon1);
	timeout_CCAN_FCTB_TAS_SAS_Info(&CCAN_msglist.FCTB_TAS_SAS_Info.mon1);
	timeout_CCAN_FCTB_ESC_FPB1(&CCAN_msglist.FCTB_ESC_FPB1.mon1);
	timeout_CCAN_FCTB_ESC7(&CCAN_msglist.FCTB_ESC7.mon1);
	timeout_CCAN_FCTB_ESC6(&CCAN_msglist.FCTB_ESC6.mon1);
	timeout_CCAN_FCTB_ESC3(&CCAN_msglist.FCTB_ESC3.mon1);
	timeout_CCAN_FCTB_ESC2(&CCAN_msglist.FCTB_ESC2.mon1);
}

// FBTC_MP5_Mode  0x4fd  500
void cycle_CCAN_FBTC_MP5_Mode(CCAN_FrameMonitor_t* _mon)
{
	_mon->cycle_cnt++;
	if (_mon->cycle_cnt >= _mon->cycle)
	{
		_mon->cycle_cnt = 0;
	}
}

// FBTC_MP5_Mode  0x4fd  500
void timeout_CCAN_FBTC_MP5_Mode(CCAN_FrameMonitor_t* _mon)
{
	_mon->timeout_cnt++;
	if (_mon->timeout_cnt >= _mon->timeout_cycle)
	{
		_mon->timeout_cnt = _mon->timeout_cycle;
		CCAN_msglist.FBTC_MP5_Mode.MP5_VehiclePowerSwitch = 0;
		CCAN_msglist.FBTC_MP5_Mode.MP5_DriveModeSET = 0;
	}
}

// FBTC_AC_Front2  0x37c  100
void cycle_CCAN_FBTC_AC_Front2(CCAN_FrameMonitor_t* _mon)
{
	_mon->cycle_cnt++;
	if (_mon->cycle_cnt >= _mon->cycle)
	{
		_mon->cycle_cnt = 0;
	}
}

// FBTC_AC_Front2  0x37c  100
void timeout_CCAN_FBTC_AC_Front2(CCAN_FrameMonitor_t* _mon)
{
	_mon->timeout_cnt++;
	if (_mon->timeout_cnt >= _mon->timeout_cycle)
	{
		_mon->timeout_cnt = _mon->timeout_cycle;
		CCAN_msglist.FBTC_AC_Front2.AC_InCarTemp = 0;
		CCAN_msglist.FBTC_AC_Front2.AC_FrontEvapTempTarget = 0;
		CCAN_msglist.FBTC_AC_Front2.AC_FrontACStartReq = 0;
		CCAN_msglist.FBTC_AC_Front2.AC_FrontHeaterInletTempSet = 0;
	}
}

// FCTB_CBS2  0x3ff  100
void cycle_CCAN_FCTB_CBS2(CCAN_FrameMonitor_t* _mon)
{
	_mon->cycle_cnt++;
	if (_mon->cycle_cnt >= _mon->cycle)
	{
		_mon->cycle_cnt = 0;
	}
}

// FCTB_CBS2  0x3ff  100
void timeout_CCAN_FCTB_CBS2(CCAN_FrameMonitor_t* _mon)
{
	_mon->timeout_cnt++;
	if (_mon->timeout_cnt >= _mon->timeout_cycle)
	{
		_mon->timeout_cnt = _mon->timeout_cycle;
		CCAN_msglist.FCTB_CBS2.CWB_DimmingSwitch = 0;
		CCAN_msglist.FCTB_CBS2.CWB_PreWashingSwitch = 0;
		CCAN_msglist.FCTB_CBS2.CWB_TurnSwitch = 0;
		CCAN_msglist.FCTB_CBS2.CWB_FrontWiperSwitch = 0;
		CCAN_msglist.FCTB_CBS2.CWB_FrontWiperAdjustment = 0;
	}
}

// FBTC_MP5_6  0x413  500
void cycle_CCAN_FBTC_MP5_6(CCAN_FrameMonitor_t* _mon)
{
	_mon->cycle_cnt++;
	if (_mon->cycle_cnt >= _mon->cycle)
	{
		_mon->cycle_cnt = 0;
	}
}

// FBTC_MP5_6  0x413  500
void timeout_CCAN_FBTC_MP5_6(CCAN_FrameMonitor_t* _mon)
{
	_mon->timeout_cnt++;
	if (_mon->timeout_cnt >= _mon->timeout_cycle)
	{
		_mon->timeout_cnt = _mon->timeout_cycle;
		CCAN_msglist.FBTC_MP5_6.Mp5_LKA_Mode = 0;
		CCAN_msglist.FBTC_MP5_6.Mp5_LKA_main_SW = 0;
		CCAN_msglist.FBTC_MP5_6.Mp5_ISA_Switch = 0;
		CCAN_msglist.FBTC_MP5_6.Mp5_TSRSwitch = 0;
		CCAN_msglist.FBTC_MP5_6.MP5_DriveModeRemSwitch = 0;
		CCAN_msglist.FBTC_MP5_6.MFS_AVASSystemSwitch = 0;
		CCAN_msglist.FBTC_MP5_6.MP5_EnergyReturnIntensionSet = 0;
		CCAN_msglist.FBTC_MP5_6.MP5_SayHi = 0;
		CCAN_msglist.FBTC_MP5_6.MP5_SerchCar = 0;
		CCAN_msglist.FBTC_MP5_6.MP5_Open_Close = 0;
	}
}

// FBTC_GW_MP5_2  0x366  500
void cycle_CCAN_FBTC_GW_MP5_2(CCAN_FrameMonitor_t* _mon)
{
	_mon->cycle_cnt++;
	if (_mon->cycle_cnt >= _mon->cycle)
	{
		_mon->cycle_cnt = 0;
	}
}

// FBTC_GW_MP5_2  0x366  500
void timeout_CCAN_FBTC_GW_MP5_2(CCAN_FrameMonitor_t* _mon)
{
	_mon->timeout_cnt++;
	if (_mon->timeout_cnt >= _mon->timeout_cycle)
	{
		_mon->timeout_cnt = _mon->timeout_cycle;
		CCAN_msglist.FBTC_GW_MP5_2.MP5_HU_SlotUserSelected = 0;
		CCAN_msglist.FBTC_GW_MP5_2.MP5_WorkSt = 0;
		CCAN_msglist.FBTC_GW_MP5_2.MP5_GearshiftRemindFunctionES = 0;
		CCAN_msglist.FBTC_GW_MP5_2.MP5_DDS_resetbutton_request = 0;
		CCAN_msglist.FBTC_GW_MP5_2.MP5_AutoWindLockSe = 0;
		CCAN_msglist.FBTC_GW_MP5_2.MP5_AutoWindUnlockSet = 0;
		CCAN_msglist.FBTC_GW_MP5_2.MP5_AutoWindKeyPressSet = 0;
		CCAN_msglist.FBTC_GW_MP5_2.MP5_Language_Set = 0;
		CCAN_msglist.FBTC_GW_MP5_2.MP5_PM2_5_EnableSwitch = 0;
		CCAN_msglist.FBTC_GW_MP5_2.MP5_HU_ULS_BSD_ACTIVATION = 0;
		CCAN_msglist.FBTC_GW_MP5_2.MP5_HU_ULS_FLK_ACTIVATION = 0;
		CCAN_msglist.FBTC_GW_MP5_2.MP5_BrightnessChange = 0;
		CCAN_msglist.FBTC_GW_MP5_2.MP5_ESCOFFSwitch = 0;
		CCAN_msglist.FBTC_GW_MP5_2.MP5_FCWSwitch = 0;
		CCAN_msglist.FBTC_GW_MP5_2.MP5_AEBSwitch = 0;
		CCAN_msglist.FBTC_GW_MP5_2.MP5_FCW_Sensitivity = 0;
		CCAN_msglist.FBTC_GW_MP5_2.MP5_AVHbutton = 0;
	}
}

// FCTB_GW_VCUtoDisplay  0x355  100
void cycle_CCAN_FCTB_GW_VCUtoDisplay(CCAN_FrameMonitor_t* _mon)
{
	_mon->cycle_cnt++;
	if (_mon->cycle_cnt >= _mon->cycle)
	{
		_mon->cycle_cnt = 0;
	}
}

// FCTB_GW_VCUtoDisplay  0x355  100
void timeout_CCAN_FCTB_GW_VCUtoDisplay(CCAN_FrameMonitor_t* _mon)
{
	_mon->timeout_cnt++;
	if (_mon->timeout_cnt >= _mon->timeout_cycle)
	{
		_mon->timeout_cnt = _mon->timeout_cycle;
		CCAN_msglist.FCTB_GW_VCUtoDisplay.VCU_DrivingPermit = 0;
		CCAN_msglist.FCTB_GW_VCUtoDisplay.VCU_Gear = 0;
		CCAN_msglist.FCTB_GW_VCUtoDisplay.VCU_SystemFaultWarning = 0;
		CCAN_msglist.FCTB_GW_VCUtoDisplay.VCU_PerformanceLimitedWarning = 0;
		CCAN_msglist.FCTB_GW_VCUtoDisplay.VCU_PumpInvalidWarning = 0;
		CCAN_msglist.FCTB_GW_VCUtoDisplay.VCU_CruisingRange = 0;
		CCAN_msglist.FCTB_GW_VCUtoDisplay.VCU_ParkLockStatus = 0;
		CCAN_msglist.FCTB_GW_VCUtoDisplay.VCU_EnergyRecoveryGearSwitch = 0;
		CCAN_msglist.FCTB_GW_VCUtoDisplay.VCU_DCDCworkSt = 0;
		CCAN_msglist.FCTB_GW_VCUtoDisplay.VCU_BrakeEnergyReturnIntension = 0;
	}
}

// FBTC_GW_AC1  0x322  100
void cycle_CCAN_FBTC_GW_AC1(CCAN_FrameMonitor_t* _mon)
{
	_mon->cycle_cnt++;
	if (_mon->cycle_cnt >= _mon->cycle)
	{
		_mon->cycle_cnt = 0;
	}
}

// FBTC_GW_AC1  0x322  100
void timeout_CCAN_FBTC_GW_AC1(CCAN_FrameMonitor_t* _mon)
{
	_mon->timeout_cnt++;
	if (_mon->timeout_cnt >= _mon->timeout_cycle)
	{
		_mon->timeout_cnt = _mon->timeout_cycle;
		CCAN_msglist.FBTC_GW_AC1.AC_AmbTemp = 0;
	}
}

// FBTC_GW_MP5_TBOX_Time  0x4da  1000
void cycle_CCAN_FBTC_GW_MP5_TBOX_Time(CCAN_FrameMonitor_t* _mon)
{
	_mon->cycle_cnt++;
	if (_mon->cycle_cnt >= _mon->cycle)
	{
		_mon->cycle_cnt = 0;
	}
}

// FBTC_GW_MP5_TBOX_Time  0x4da  1000
void timeout_CCAN_FBTC_GW_MP5_TBOX_Time(CCAN_FrameMonitor_t* _mon)
{
	_mon->timeout_cnt++;
	if (_mon->timeout_cnt >= _mon->timeout_cycle)
	{
		_mon->timeout_cnt = _mon->timeout_cycle;
		CCAN_msglist.FBTC_GW_MP5_TBOX_Time.MP5_TBOX_Time_Month = 0;
		CCAN_msglist.FBTC_GW_MP5_TBOX_Time.MP5_TBOX_Time_Valid = 0;
		CCAN_msglist.FBTC_GW_MP5_TBOX_Time.MP5_TBOX_Time_YearMark = 0;
		CCAN_msglist.FBTC_GW_MP5_TBOX_Time.MP5_TBOX_Time_Date = 0;
		CCAN_msglist.FBTC_GW_MP5_TBOX_Time.MP5_TBOX_Time_Hour = 0;
		CCAN_msglist.FBTC_GW_MP5_TBOX_Time.MP5_TBOX_Time_Minute = 0;
		CCAN_msglist.FBTC_GW_MP5_TBOX_Time.MP5_TBOX_Time_Second = 0;
		CCAN_msglist.FBTC_GW_MP5_TBOX_Time.MP5_TBOX_Time_Year = 0;
	}
}

// FBTC_GW_IBCM6  0x341  100
void cycle_CCAN_FBTC_GW_IBCM6(CCAN_FrameMonitor_t* _mon)
{
	_mon->cycle_cnt++;
	if (_mon->cycle_cnt >= _mon->cycle)
	{
		_mon->cycle_cnt = 0;
	}
}

// FBTC_GW_IBCM6  0x341  100
void timeout_CCAN_FBTC_GW_IBCM6(CCAN_FrameMonitor_t* _mon)
{
	_mon->timeout_cnt++;
	if (_mon->timeout_cnt >= _mon->timeout_cycle)
	{
		_mon->timeout_cnt = _mon->timeout_cycle;
		CCAN_msglist.FBTC_GW_IBCM6.BCM_BattVolt = 0;
	}
}

// FBTC_GW_IBCM3  0x33c  100
void cycle_CCAN_FBTC_GW_IBCM3(CCAN_FrameMonitor_t* _mon)
{
	_mon->cycle_cnt++;
	if (_mon->cycle_cnt >= _mon->cycle)
	{
		_mon->cycle_cnt = 0;
	}
}

// FBTC_GW_IBCM3  0x33c  100
void timeout_CCAN_FBTC_GW_IBCM3(CCAN_FrameMonitor_t* _mon)
{
	_mon->timeout_cnt++;
	if (_mon->timeout_cnt >= _mon->timeout_cycle)
	{
		_mon->timeout_cnt = _mon->timeout_cycle;
		CCAN_msglist.FBTC_GW_IBCM3.BCM_DoorLockSt = 0;
		CCAN_msglist.FBTC_GW_IBCM3.BCM_IgnitionSt = 0;
		CCAN_msglist.FBTC_GW_IBCM3.BCM_FrontWiperSwitchSt = 0;
		CCAN_msglist.FBTC_GW_IBCM3.BCM_BackWiperParkst = 0;
		CCAN_msglist.FBTC_GW_IBCM3.BCM_BrakeLampStatus = 0;
		CCAN_msglist.FBTC_GW_IBCM3.BCM_CHMSLStatus = 0;
	}
}

// FBTC_GW_IBCM2  0x23a  40
void cycle_CCAN_FBTC_GW_IBCM2(CCAN_FrameMonitor_t* _mon)
{
	_mon->cycle_cnt++;
	if (_mon->cycle_cnt >= _mon->cycle)
	{
		_mon->cycle_cnt = 0;
	}
}

// FBTC_GW_IBCM2  0x23a  40
void timeout_CCAN_FBTC_GW_IBCM2(CCAN_FrameMonitor_t* _mon)
{
	_mon->timeout_cnt++;
	if (_mon->timeout_cnt >= _mon->timeout_cycle)
	{
		_mon->timeout_cnt = _mon->timeout_cycle;
		CCAN_msglist.FBTC_GW_IBCM2.BCM_HighBeamStatus = 0;
		CCAN_msglist.FBTC_GW_IBCM2.BCM_HazardLampSt = 0;
		CCAN_msglist.FBTC_GW_IBCM2.BCM_PositionLampSt = 0;
		CCAN_msglist.FBTC_GW_IBCM2.BCM_RightligthFaultSt = 0;
		CCAN_msglist.FBTC_GW_IBCM2.BCM_RightligthSt = 0;
		CCAN_msglist.FBTC_GW_IBCM2.BCM_LetfligthFaultSt = 0;
		CCAN_msglist.FBTC_GW_IBCM2.BCM_LetfligthSt = 0;
		CCAN_msglist.FBTC_GW_IBCM2.BCM_TrunkSt = 0;
		CCAN_msglist.FBTC_GW_IBCM2.BCM_FuleTap_LockStatus = 0;
		CCAN_msglist.FBTC_GW_IBCM2.BCM_LRDoorSwitchSt = 0;
		CCAN_msglist.FBTC_GW_IBCM2.BCM_RRDoorSwitchSt = 0;
		CCAN_msglist.FBTC_GW_IBCM2.BCM_RFDoorSwitchSt = 0;
		CCAN_msglist.FBTC_GW_IBCM2.BCM_LFDoorSwitchSt = 0;
		CCAN_msglist.FBTC_GW_IBCM2.BCM_frontFogligthSt = 0;
		CCAN_msglist.FBTC_GW_IBCM2.BCM_BackFogligthSt = 0;
		CCAN_msglist.FBTC_GW_IBCM2.BCM_LowBeamStatus = 0;
		CCAN_msglist.FBTC_GW_IBCM2.BCM_RightTurnSwitchrSt = 0;
		CCAN_msglist.FBTC_GW_IBCM2.BCM_LeftTurnSwitchSt = 0;
		CCAN_msglist.FBTC_GW_IBCM2.BCM_Lock_LED_Output = 0;
		CCAN_msglist.FBTC_GW_IBCM2.BCM_AutoLockFunctionSt = 0;
		CCAN_msglist.FBTC_GW_IBCM2.BCM_RearWindowHeatSt = 0;
		CCAN_msglist.FBTC_GW_IBCM2.BCM_FRTurnlightFbSt = 0;
		CCAN_msglist.FBTC_GW_IBCM2.BCM_RRTurnlightFbSt = 0;
		CCAN_msglist.FBTC_GW_IBCM2.BCM_FLTurnlightFbSt = 0;
		CCAN_msglist.FBTC_GW_IBCM2.BCM_RLTurnlightFbSt = 0;
		CCAN_msglist.FBTC_GW_IBCM2.BCM_LampWashSt = 0;
		CCAN_msglist.FBTC_GW_IBCM2.BCM_EngHoodUnlockWarming = 0;
		CCAN_msglist.FBTC_GW_IBCM2.BCM_ReverseLampSwitchSt = 0;
		CCAN_msglist.FBTC_GW_IBCM2.BCM_RecentlyLockType = 0;
		CCAN_msglist.FBTC_GW_IBCM2.BCM_RecentlyUnlockType = 0;
		CCAN_msglist.FBTC_GW_IBCM2.BCM_RLS_AUTO_SwitchSt = 0;
		CCAN_msglist.FBTC_GW_IBCM2.BCM_FollowMeHomeSt = 0;
		CCAN_msglist.FBTC_GW_IBCM2.BCM_FrontWiperWorkSt = 0;
		CCAN_msglist.FBTC_GW_IBCM2.BCM_MirrorFoldSwitchSt = 0;
		CCAN_msglist.FBTC_GW_IBCM2.BCM_SunShadeStatus = 0;
		CCAN_msglist.FBTC_GW_IBCM2.BCM_RoofWindowStatus = 0;
		CCAN_msglist.FBTC_GW_IBCM2.BCM_RRWindowStatus = 0;
		CCAN_msglist.FBTC_GW_IBCM2.BCM_RFWindowStatus = 0;
		CCAN_msglist.FBTC_GW_IBCM2.BCM_RLWindowStatus = 0;
		CCAN_msglist.FBTC_GW_IBCM2.BCM_LFWindowStatus = 0;
		CCAN_msglist.FBTC_GW_IBCM2.BCM_TailgateUnlockInform = 0;
		CCAN_msglist.FBTC_GW_IBCM2.BCM_TailgateOpenSwitch = 0;
		CCAN_msglist.FBTC_GW_IBCM2.BCM_FrontWiper_AUTO = 0;
		CCAN_msglist.FBTC_GW_IBCM2.BCM_LowBeam_AUTO = 0;
	}
}

// FCTB_ACU_Crash  0x30c  100
void cycle_CCAN_FCTB_ACU_Crash(CCAN_FrameMonitor_t* _mon)
{
	_mon->cycle_cnt++;
	if (_mon->cycle_cnt >= _mon->cycle)
	{
		_mon->cycle_cnt = 0;
	}
}

// FCTB_ACU_Crash  0x30c  100
void timeout_CCAN_FCTB_ACU_Crash(CCAN_FrameMonitor_t* _mon)
{
	_mon->timeout_cnt++;
	if (_mon->timeout_cnt >= _mon->timeout_cycle)
	{
		_mon->timeout_cnt = _mon->timeout_cycle;
		CCAN_msglist.FCTB_ACU_Crash.RollingCounter30C = 0;
		CCAN_msglist.FCTB_ACU_Crash.ACU_AirbagLampSts = 0;
		CCAN_msglist.FCTB_ACU_Crash.ACU_Crashout = 0;
		CCAN_msglist.FCTB_ACU_Crash.ACU_PassengerBeltSwitchSig = 0;
		CCAN_msglist.FCTB_ACU_Crash.ACU_DriverBeltSwitchSig = 0;
		CCAN_msglist.FCTB_ACU_Crash.ACU_CrashoutValid = 0;
		CCAN_msglist.FCTB_ACU_Crash.ACU_CheckSum_ACU = 0;
	}
}

// FCTB_TAS_SAS_Info  0xa5  10
void cycle_CCAN_FCTB_TAS_SAS_Info(CCAN_FrameMonitor_t* _mon)
{
	_mon->cycle_cnt++;
	if (_mon->cycle_cnt >= _mon->cycle)
	{
		_mon->cycle_cnt = 0;
	}
}

// FCTB_TAS_SAS_Info  0xa5  10
void timeout_CCAN_FCTB_TAS_SAS_Info(CCAN_FrameMonitor_t* _mon)
{
	_mon->timeout_cnt++;
	if (_mon->timeout_cnt >= _mon->timeout_cycle)
	{
		_mon->timeout_cnt = _mon->timeout_cycle;
		CCAN_msglist.FCTB_TAS_SAS_Info.TAS_SAS_SteeringAngle = 0;
	}
}

// FCTB_ESC_FPB1  0x31a  100
void cycle_CCAN_FCTB_ESC_FPB1(CCAN_FrameMonitor_t* _mon)
{
	_mon->cycle_cnt++;
	if (_mon->cycle_cnt >= _mon->cycle)
	{
		_mon->cycle_cnt = 0;
	}
}

// FCTB_ESC_FPB1  0x31a  100
void timeout_CCAN_FCTB_ESC_FPB1(CCAN_FrameMonitor_t* _mon)
{
	_mon->timeout_cnt++;
	if (_mon->timeout_cnt >= _mon->timeout_cycle)
	{
		_mon->timeout_cnt = _mon->timeout_cycle;
		CCAN_msglist.FCTB_ESC_FPB1.ESC_EPBDisplayMessageReq = 0;
		CCAN_msglist.FCTB_ESC_FPB1.ESC_EPBCruiseControlCancel = 0;
		CCAN_msglist.FCTB_ESC_FPB1.ESC_EPBWarningIndicationReq = 0;
		CCAN_msglist.FCTB_ESC_FPB1.ESC_EPBSwitchStatics = 0;
		CCAN_msglist.FCTB_ESC_FPB1.ESC_EPBSwitchStaticsValidity = 0;
		CCAN_msglist.FCTB_ESC_FPB1.ESC_EPBStatus = 0;
		CCAN_msglist.FCTB_ESC_FPB1.ESC_CurrentOnRightRearCaliper = 0;
		CCAN_msglist.FCTB_ESC_FPB1.ESC_CurrentOnLeftRearCaliper = 0;
		CCAN_msglist.FCTB_ESC_FPB1.ESC_PbcActuatorStateRight = 0;
		CCAN_msglist.FCTB_ESC_FPB1.ESC_PbcActuatorStateLeft = 0;
		CCAN_msglist.FCTB_ESC_FPB1.ESC_RollingCount_EPB = 0;
		CCAN_msglist.FCTB_ESC_FPB1.ESC_CheckSum_EPB = 0;
	}
}

// FCTB_ESC7  0x431  1000
void cycle_CCAN_FCTB_ESC7(CCAN_FrameMonitor_t* _mon)
{
	_mon->cycle_cnt++;
	if (_mon->cycle_cnt >= _mon->cycle)
	{
		_mon->cycle_cnt = 0;
	}
}

// FCTB_ESC7  0x431  1000
void timeout_CCAN_FCTB_ESC7(CCAN_FrameMonitor_t* _mon)
{
	_mon->timeout_cnt++;
	if (_mon->timeout_cnt >= _mon->timeout_cycle)
	{
		_mon->timeout_cnt = _mon->timeout_cycle;
		CCAN_msglist.FCTB_ESC7.ESC_ITPMSFrontRightPressureWarn = 0;
		CCAN_msglist.FCTB_ESC7.ESC_ITPMSFrontLeftPressureWarn = 0;
		CCAN_msglist.FCTB_ESC7.ESC_ITPMSRearRightPressureWarnin = 0;
		CCAN_msglist.FCTB_ESC7.ESC_ITPMSRearLeftPressureWarning = 0;
		CCAN_msglist.FCTB_ESC7.ESC_DDSSystemStatus = 0;
		CCAN_msglist.FCTB_ESC7.ESC_ITPMSWarningStatus = 0;
		CCAN_msglist.FCTB_ESC7.ESC_ITPMSMalfunctionStatus = 0;
	}
}

// FCTB_ESC6  0x123  20
void cycle_CCAN_FCTB_ESC6(CCAN_FrameMonitor_t* _mon)
{
	_mon->cycle_cnt++;
	if (_mon->cycle_cnt >= _mon->cycle)
	{
		_mon->cycle_cnt = 0;
	}
}

// FCTB_ESC6  0x123  20
void timeout_CCAN_FCTB_ESC6(CCAN_FrameMonitor_t* _mon)
{
	_mon->timeout_cnt++;
	if (_mon->timeout_cnt >= _mon->timeout_cycle)
	{
		_mon->timeout_cnt = _mon->timeout_cycle;
		CCAN_msglist.FCTB_ESC6.ESC_DynamicSlopeAccuracy = 0;
		CCAN_msglist.FCTB_ESC6.ESC_AVHFunctionSwitch = 0;
		CCAN_msglist.FCTB_ESC6.ESC_AVHAvailable = 0;
		CCAN_msglist.FCTB_ESC6.ESC_AVH_Status = 0;
		CCAN_msglist.FCTB_ESC6.ESC_AVH_DisplayMessageReq = 0;
		CCAN_msglist.FCTB_ESC6.ESC_BLRequest = 0;
		CCAN_msglist.FCTB_ESC6.ESC_EmergencyBrakeLightReq = 0;
		CCAN_msglist.FCTB_ESC6.ESC_BrakingEffort = 0;
		CCAN_msglist.FCTB_ESC6.ESC_MSRinRegulation = 0;
		CCAN_msglist.FCTB_ESC6.ESC_BrakeReleasedFailsafe = 0;
		CCAN_msglist.FCTB_ESC6.ESC_UnfilteredYawRate = 0;
		CCAN_msglist.FCTB_ESC6.ESC_VehDrivingDirection = 0;
		CCAN_msglist.FCTB_ESC6.ESC_DynamicSlope = 0;
		CCAN_msglist.FCTB_ESC6.ESC_VehicleHoldStatus = 0;
		CCAN_msglist.FCTB_ESC6.ESC_HBAStatus = 0;
		CCAN_msglist.FCTB_ESC6.ESC_cdpAvailable = 0;
		CCAN_msglist.FCTB_ESC6.ESC_cdpActive = 0;
		CCAN_msglist.FCTB_ESC6.ESC_RollingCount_ESC6 = 0;
		CCAN_msglist.FCTB_ESC6.ESC_CheckSum_ESC6 = 0;
	}
}

// FCTB_ESC3  0x121  20
void cycle_CCAN_FCTB_ESC3(CCAN_FrameMonitor_t* _mon)
{
	_mon->cycle_cnt++;
	if (_mon->cycle_cnt >= _mon->cycle)
	{
		_mon->cycle_cnt = 0;
	}
}

// FCTB_ESC3  0x121  20
void timeout_CCAN_FCTB_ESC3(CCAN_FrameMonitor_t* _mon)
{
	_mon->timeout_cnt++;
	if (_mon->timeout_cnt >= _mon->timeout_cycle)
	{
		_mon->timeout_cnt = _mon->timeout_cycle;
		CCAN_msglist.FCTB_ESC3.ESC_ReqDecreaseTorqueFlag = 0;
		CCAN_msglist.FCTB_ESC3.ESC_ReqIncreaseTorqueFlag = 0;
		CCAN_msglist.FCTB_ESC3.ESC_TCSCtlActive = 0;
		CCAN_msglist.FCTB_ESC3.ESC_ESCAlarmSig = 0;
		CCAN_msglist.FCTB_ESC3.ESC_ESCWorkStatus = 0;
		CCAN_msglist.FCTB_ESC3.ESC_keepingGear = 0;
		CCAN_msglist.FCTB_ESC3.ESC_ESCOFF = 0;
		CCAN_msglist.FCTB_ESC3.ESC_ReqIncreaseTorque = 0;
		CCAN_msglist.FCTB_ESC3.ESC_ReqDecreaseTorque = 0;
		CCAN_msglist.FCTB_ESC3.ESC_epbRequest = 0;
		CCAN_msglist.FCTB_ESC3.ESC_wheelDirectionRLValid = 0;
		CCAN_msglist.FCTB_ESC3.ESC_wheelDirectionRRValid = 0;
		CCAN_msglist.FCTB_ESC3.ESC_FRWDirection = 0;
		CCAN_msglist.FCTB_ESC3.ESC_FLWDirection = 0;
		CCAN_msglist.FCTB_ESC3.ESC_RRWDirection = 0;
		CCAN_msglist.FCTB_ESC3.ESC_RLWDirection = 0;
		CCAN_msglist.FCTB_ESC3.ESC_ESCValidity = 0;
		CCAN_msglist.FCTB_ESC3.ESC_vehicleStandstillValid = 0;
		CCAN_msglist.FCTB_ESC3.ESC_TCSErrorStatus = 0;
		CCAN_msglist.FCTB_ESC3.ESC_VehicleStandstill = 0;
		CCAN_msglist.FCTB_ESC3.GW_ESC_RollingCount_ESC3 = 0;
		CCAN_msglist.FCTB_ESC3.GW_ESC_CheckSum_ESC3 = 0;
	}
}

// FCTB_ESC2  0xa0  10
void cycle_CCAN_FCTB_ESC2(CCAN_FrameMonitor_t* _mon)
{
	_mon->cycle_cnt++;
	if (_mon->cycle_cnt >= _mon->cycle)
	{
		_mon->cycle_cnt = 0;
	}
}

// FCTB_ESC2  0xa0  10
void timeout_CCAN_FCTB_ESC2(CCAN_FrameMonitor_t* _mon)
{
	_mon->timeout_cnt++;
	if (_mon->timeout_cnt >= _mon->timeout_cycle)
	{
		_mon->timeout_cnt = _mon->timeout_cycle;
		CCAN_msglist.FCTB_ESC2.ESC_BrakeOilPress = 0;
		CCAN_msglist.FCTB_ESC2.ESC_RollingCount_ESC2 = 0;
		CCAN_msglist.FCTB_ESC2.ESC_ABSWorkLable = 0;
		CCAN_msglist.FCTB_ESC2.ESC_ABSAlarmSig = 0;
		CCAN_msglist.FCTB_ESC2.ESC_ABSValidity = 0;
		CCAN_msglist.FCTB_ESC2.ESC_VehSpdValidFlag = 0;
		CCAN_msglist.FCTB_ESC2.ESC_EBDAlarmSig = 0;
		CCAN_msglist.FCTB_ESC2.ESC_HBB_StatusValidity = 0;
		CCAN_msglist.FCTB_ESC2.ESC_HBB_Status = 0;
		CCAN_msglist.FCTB_ESC2.ESC_CheckSum_ESC2 = 0;
		CCAN_msglist.FCTB_ESC2.ESC_VehSpd = 0;
	}
}

