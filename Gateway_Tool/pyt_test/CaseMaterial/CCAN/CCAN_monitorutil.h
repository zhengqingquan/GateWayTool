#pragma once

#include <stdint.h>


typedef struct
{
	// @cycle 报文周期
	// @cycle keeps message cycle
	uint32_t cycle;

	// @cycle 报文周期计时
	// @cycle keeps message cycle count
	uint32_t cycle_cnt;

	// @last_cycle 当最后一帧报文被接收时候保存时值
	// @last_cycle keeps tick-value when last frame was received
	uint32_t last_cycle;

	// @timeout_cycle 保存报文的最大超时，用户有责任初始化该字段并将其用于报文丢失监控功能
	// @timeout_cycle keeps maximum timeout for frame, user responsibility to init this field and use it in missing frame monitoring function
 	uint32_t timeout_cycle;

	// @timeout_cnt 保存报文超时计数，用户有责任初始化并设计该字段用于报文超时计数监控功能
	// @timeout_cnt Save message timeout count
 	uint32_t timeout_cnt;

	// @frame_cnt 记录最近的一帧报文的数据
	// @frame_cnt Record the data of the latest frame message

	// @frame_cnt 记录接收到的报文帧数
	// @frame_cnt keeps count of all the received frames
	uint32_t frame_cnt;

	// @dlc_error 设置@dlc_error位表示收到CAN帧的实际长度CAN矩阵定义的长度
	// @dlc_error setting up @dlc_error bit indicates that the actual length of CAN frame is less then defined by CAN matrix!
 	uint32_t dlc_error : 1;

} CCAN_FrameMonitor_t;

// 这部分内容需要自己实现
// 执行解包时将调用此函数。值将保存在@last_cycle变量中。
// this function will be called when unpacking is performing. Value will be saved in @last_cycle variable
uint32_t CCAN_GetSystemTick(void);

/*
* 超时计数和周期计数器的初始化，用户可以根据需要自己定义超时周期。
* 超时周期默认为报文的五倍周期。
*/
void CCAN_TimeoutInit();

/*
* 该方法会执行所有报文的周期函数。也支持自定义。
*/
void CCAN_cycleFunc(void);
void cycle_CCAN_FBTC_MP5_Mode(CCAN_FrameMonitor_t* _mon);
void cycle_CCAN_FBTC_AC_Front2(CCAN_FrameMonitor_t* _mon);
void cycle_CCAN_FCTB_CBS2(CCAN_FrameMonitor_t* _mon);
void cycle_CCAN_FBTC_MP5_6(CCAN_FrameMonitor_t* _mon);
void cycle_CCAN_FBTC_GW_MP5_2(CCAN_FrameMonitor_t* _mon);
void cycle_CCAN_FCTB_GW_VCUtoDisplay(CCAN_FrameMonitor_t* _mon);
void cycle_CCAN_FBTC_GW_AC1(CCAN_FrameMonitor_t* _mon);
void cycle_CCAN_FBTC_GW_MP5_TBOX_Time(CCAN_FrameMonitor_t* _mon);
void cycle_CCAN_FBTC_GW_IBCM6(CCAN_FrameMonitor_t* _mon);
void cycle_CCAN_FBTC_GW_IBCM3(CCAN_FrameMonitor_t* _mon);
void cycle_CCAN_FBTC_GW_IBCM2(CCAN_FrameMonitor_t* _mon);
void cycle_CCAN_FCTB_ACU_Crash(CCAN_FrameMonitor_t* _mon);
void cycle_CCAN_FCTB_TAS_SAS_Info(CCAN_FrameMonitor_t* _mon);
void cycle_CCAN_FCTB_ESC_FPB1(CCAN_FrameMonitor_t* _mon);
void cycle_CCAN_FCTB_ESC7(CCAN_FrameMonitor_t* _mon);
void cycle_CCAN_FCTB_ESC6(CCAN_FrameMonitor_t* _mon);
void cycle_CCAN_FCTB_ESC3(CCAN_FrameMonitor_t* _mon);
void cycle_CCAN_FCTB_ESC2(CCAN_FrameMonitor_t* _mon);

/*
* 该方法会执行所有报文的超时函数。也支持自定义。
*/
void CCAN_timeoutFunc(void);
void timeout_CCAN_FBTC_MP5_Mode(CCAN_FrameMonitor_t* _mon);
void timeout_CCAN_FBTC_AC_Front2(CCAN_FrameMonitor_t* _mon);
void timeout_CCAN_FCTB_CBS2(CCAN_FrameMonitor_t* _mon);
void timeout_CCAN_FBTC_MP5_6(CCAN_FrameMonitor_t* _mon);
void timeout_CCAN_FBTC_GW_MP5_2(CCAN_FrameMonitor_t* _mon);
void timeout_CCAN_FCTB_GW_VCUtoDisplay(CCAN_FrameMonitor_t* _mon);
void timeout_CCAN_FBTC_GW_AC1(CCAN_FrameMonitor_t* _mon);
void timeout_CCAN_FBTC_GW_MP5_TBOX_Time(CCAN_FrameMonitor_t* _mon);
void timeout_CCAN_FBTC_GW_IBCM6(CCAN_FrameMonitor_t* _mon);
void timeout_CCAN_FBTC_GW_IBCM3(CCAN_FrameMonitor_t* _mon);
void timeout_CCAN_FBTC_GW_IBCM2(CCAN_FrameMonitor_t* _mon);
void timeout_CCAN_FCTB_ACU_Crash(CCAN_FrameMonitor_t* _mon);
void timeout_CCAN_FCTB_TAS_SAS_Info(CCAN_FrameMonitor_t* _mon);
void timeout_CCAN_FCTB_ESC_FPB1(CCAN_FrameMonitor_t* _mon);
void timeout_CCAN_FCTB_ESC7(CCAN_FrameMonitor_t* _mon);
void timeout_CCAN_FCTB_ESC6(CCAN_FrameMonitor_t* _mon);
void timeout_CCAN_FCTB_ESC3(CCAN_FrameMonitor_t* _mon);
void timeout_CCAN_FCTB_ESC2(CCAN_FrameMonitor_t* _mon);
