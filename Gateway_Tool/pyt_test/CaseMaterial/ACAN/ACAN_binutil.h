/**
* @file:         ACAN_binutil.h
* @author:       96400
* @note:         The code is automatically generated by GatewayTool
* @version:      V1.0.0
* @date:         2023.02.08, 11:17:43
* @brief:        
* @attention:    
**/

#pragma once

#include <stdint.h>

#include "ACAN_definition.h"


/*
* 报文列表结构体
*/
typedef struct
{
	ACAN_IC_TCO1_t IC_TCO1;
	ACAN_New_Message_5_t New_Message_5;
	ACAN_EMS_CCVS_t EMS_CCVS;
	ACAN_IC_CCVS1_t IC_CCVS1;
	ACAN_BCM_CCVS_t BCM_CCVS;
} ACAN_msglist_t;


/*
* 声明外部变量
*/
extern ACAN_msglist_t ACAN_msglist;


/*
* 信号报文初始化
*/
void ACAN_init_msglist(void);


/*
* 定期执行周期相关的函数，主要用于信号报文的发送。
* pollingCycle为轮询周期，单位为毫秒（ms），通常设置为10ms。
* 在配置文件中修改
*/
void ACAN_CycleAct(void);


/*
* 重置所有信号报文的超时计时和周期计时。
*/
void ACAN_ResetAllInit(void);


/*
* 根据_msgID，将信号实际值打包到数组_data、_dlc和_ide上。
*/
uint32_t ACAN_Pack(const uint32_t _msgID, uint8_t* _data, uint8_t* _dlc, uint8_t* _ide);


/*
* 根据输入的_msgID和数据数组_data，对信号进行解析。
*/
uint32_t ACAN_Unpack(const uint32_t _msgID, const uint8_t* _data, const uint8_t _dlc);




/******** END OF FILE ********/
