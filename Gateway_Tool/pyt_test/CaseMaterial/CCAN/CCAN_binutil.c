/**
* @file         CCAN_binutil.c
* @author       96400
* @note         The code is automatically generated by GatewayTool
* @version      V1.0.0
* @date         2023.01.12, 11:03:06
* @brief        
* @attention    
**/

#include "CCAN_binutil.h"

CCAN_msglist_t CCAN_msglist;

uint32_t CCAN_Transmit(CCAN_msglist_t* _message, uint8_t* _data, uint32_t _msgid, uint8_t* dlc_, uint8_t* _ide)
{

	uint32_t traid = 0;
	switch(_msgid)
	{
		case 0x4fd:
			traid = Pack_CCAN_FBTC_MP5_Mode(&(_message->FBTC_MP5_Mode), _data, dlc_, _ide);
			break;
		case 0x37c:
			traid = Pack_CCAN_FBTC_AC_Front2(&(_message->FBTC_AC_Front2), _data, dlc_, _ide);
			break;
		case 0x3ff:
			traid = Pack_CCAN_FCTB_CBS2(&(_message->FCTB_CBS2), _data, dlc_, _ide);
			break;
		case 0x413:
			traid = Pack_CCAN_FBTC_MP5_6(&(_message->FBTC_MP5_6), _data, dlc_, _ide);
			break;
		case 0x366:
			traid = Pack_CCAN_FBTC_GW_MP5_2(&(_message->FBTC_GW_MP5_2), _data, dlc_, _ide);
			break;
		case 0x355:
			traid = Pack_CCAN_FCTB_GW_VCUtoDisplay(&(_message->FCTB_GW_VCUtoDisplay), _data, dlc_, _ide);
			break;
		case 0x322:
			traid = Pack_CCAN_FBTC_GW_AC1(&(_message->FBTC_GW_AC1), _data, dlc_, _ide);
			break;
		case 0x4da:
			traid = Pack_CCAN_FBTC_GW_MP5_TBOX_Time(&(_message->FBTC_GW_MP5_TBOX_Time), _data, dlc_, _ide);
			break;
		case 0x341:
			traid = Pack_CCAN_FBTC_GW_IBCM6(&(_message->FBTC_GW_IBCM6), _data, dlc_, _ide);
			break;
		case 0x33c:
			traid = Pack_CCAN_FBTC_GW_IBCM3(&(_message->FBTC_GW_IBCM3), _data, dlc_, _ide);
			break;
		case 0x23a:
			traid = Pack_CCAN_FBTC_GW_IBCM2(&(_message->FBTC_GW_IBCM2), _data, dlc_, _ide);
			break;
		case 0x30c:
			traid = Pack_CCAN_FCTB_ACU_Crash(&(_message->FCTB_ACU_Crash), _data, dlc_, _ide);
			break;
		case 0xa5:
			traid = Pack_CCAN_FCTB_TAS_SAS_Info(&(_message->FCTB_TAS_SAS_Info), _data, dlc_, _ide);
			break;
		case 0x31a:
			traid = Pack_CCAN_FCTB_ESC_FPB1(&(_message->FCTB_ESC_FPB1), _data, dlc_, _ide);
			break;
		case 0x431:
			traid = Pack_CCAN_FCTB_ESC7(&(_message->FCTB_ESC7), _data, dlc_, _ide);
			break;
		case 0x123:
			traid = Pack_CCAN_FCTB_ESC6(&(_message->FCTB_ESC6), _data, dlc_, _ide);
			break;
		case 0x121:
			traid = Pack_CCAN_FCTB_ESC3(&(_message->FCTB_ESC3), _data, dlc_, _ide);
			break;
		case 0xa0:
			traid = Pack_CCAN_FCTB_ESC2(&(_message->FCTB_ESC2), _data, dlc_, _ide);
			break;
		default:
			break;
	}
	return traid;
}

uint32_t CCAN_Receive(CCAN_msglist_t* _message, const uint8_t* _data, uint32_t _msgid, uint8_t dlc_)
{

	uint32_t recid = 0;
	switch(_msgid)
	{
		case 0x4fd:
			recid = Unpack_CCAN_FBTC_MP5_Mode(&(_message->FBTC_MP5_Mode), _data, dlc_);
			break;
		case 0x37c:
			recid = Unpack_CCAN_FBTC_AC_Front2(&(_message->FBTC_AC_Front2), _data, dlc_);
			break;
		case 0x3ff:
			recid = Unpack_CCAN_FCTB_CBS2(&(_message->FCTB_CBS2), _data, dlc_);
			break;
		case 0x413:
			recid = Unpack_CCAN_FBTC_MP5_6(&(_message->FBTC_MP5_6), _data, dlc_);
			break;
		case 0x366:
			recid = Unpack_CCAN_FBTC_GW_MP5_2(&(_message->FBTC_GW_MP5_2), _data, dlc_);
			break;
		case 0x355:
			recid = Unpack_CCAN_FCTB_GW_VCUtoDisplay(&(_message->FCTB_GW_VCUtoDisplay), _data, dlc_);
			break;
		case 0x322:
			recid = Unpack_CCAN_FBTC_GW_AC1(&(_message->FBTC_GW_AC1), _data, dlc_);
			break;
		case 0x4da:
			recid = Unpack_CCAN_FBTC_GW_MP5_TBOX_Time(&(_message->FBTC_GW_MP5_TBOX_Time), _data, dlc_);
			break;
		case 0x341:
			recid = Unpack_CCAN_FBTC_GW_IBCM6(&(_message->FBTC_GW_IBCM6), _data, dlc_);
			break;
		case 0x33c:
			recid = Unpack_CCAN_FBTC_GW_IBCM3(&(_message->FBTC_GW_IBCM3), _data, dlc_);
			break;
		case 0x23a:
			recid = Unpack_CCAN_FBTC_GW_IBCM2(&(_message->FBTC_GW_IBCM2), _data, dlc_);
			break;
		case 0x30c:
			recid = Unpack_CCAN_FCTB_ACU_Crash(&(_message->FCTB_ACU_Crash), _data, dlc_);
			break;
		case 0xa5:
			recid = Unpack_CCAN_FCTB_TAS_SAS_Info(&(_message->FCTB_TAS_SAS_Info), _data, dlc_);
			break;
		case 0x31a:
			recid = Unpack_CCAN_FCTB_ESC_FPB1(&(_message->FCTB_ESC_FPB1), _data, dlc_);
			break;
		case 0x431:
			recid = Unpack_CCAN_FCTB_ESC7(&(_message->FCTB_ESC7), _data, dlc_);
			break;
		case 0x123:
			recid = Unpack_CCAN_FCTB_ESC6(&(_message->FCTB_ESC6), _data, dlc_);
			break;
		case 0x121:
			recid = Unpack_CCAN_FCTB_ESC3(&(_message->FCTB_ESC3), _data, dlc_);
			break;
		case 0xa0:
			recid = Unpack_CCAN_FCTB_ESC2(&(_message->FCTB_ESC2), _data, dlc_);
			break;
		default:
			break;
	}
	return recid;
}


/******** END OF FILE ********/