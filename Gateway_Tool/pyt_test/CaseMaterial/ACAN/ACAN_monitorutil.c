/**
* @file:         ACAN_monitorutil.c
* @author:       96400
* @note:         The code is automatically generated by GatewayTool
* @version:      V1.0.0
* @date:         2023.02.08, 11:17:43
* @brief:        
* @attention:    
**/

#include "ACAN_monitorutil.h"


uint32_t ACAN_GetSystemTick(void)
{
	return 0;
}


void ACAN_ResetMonitor(ACAN_FrameMonitor_t* monitor)
{
	monitor->cycle_cnt = 0;
	monitor->timeout_cnt = 0;
}




/******** END OF FILE ********/
