/**
* @file:         ACAN_CycleAct.c
* @author:       96400
* @note:         The code is automatically generated by GatewayTool
* @version:      V1.0.0
* @date:         2023.02.08, 11:17:43
* @brief:        
* @attention:    
**/

#include "ACAN_CycleAct.h"
#include "ACAN_binutil.h"
#include "ACAN_config.h"


void CycleActFunc(void)
{

}

void RegularlyCallFunc(ACAN_FrameMonitor_t* monitor)
 {
	monitor->timeout_cnt += CYCLE_FACTOR;
	monitor->cycle_cnt += CYCLE_FACTOR;

	if(monitor->timeout_cnt >= monitor->timeout_cycle){
		monitor->timeout_cnt = monitor->timeout_cycle;
		monitor->TimeoutFunc();
	}

	monitor->TimingFunc();

	if(monitor->cycle_cnt >= monitor->cycle){
		monitor->cycle_cnt = 0;
		monitor->CycleOverFunc();
	}
}




/******** END OF FILE ********/