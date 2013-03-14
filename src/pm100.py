'''
Created on 12 Mar 2013

@author: TeraView_Service
'''
import os
pth = os.environ['Path']
#pth = r"C:\Program Files\IVI Foundation\VISA\WinNT\Bin;"+pth
#os.environ['PATH'] = pth
print pth

#for item in pth.split(';'):
#    print item

from ctypes import CDLL, WinDLL, c_uint32, c_int32, c_char_p, \
    POINTER, byref, create_string_buffer, c_uint16, c_int16, c_double

dll = WinDLL("PM100D_Drv_32")
visa = WinDLL("visa32.dll")

ViObject = c_uint32
ViSession = ViObject
ViPSession = POINTER(ViSession)
ViFindList = ViObject
ViPFindList = POINTER(ViFindList)
ViStatus = c_int32
ViString = c_char_p
ViRsrc = ViString
ViBoolean = c_uint16
ViInt16 = c_int16
ViReal64 = c_double

VI_TRUE = 1
VI_FALSE = 0

def errcheck(ret, func, args):
    if ret==0:
        return ret
    obj =args[0]
    if isinstance(obj, ViObject):
        buf = create_string_buffer(256)
        status = viStatusDesc(obj, ret, buf)
        if status==0:
            raise VisaError("VISA Error, code %d: %s"%(ret, buf.value))
        else:
            raise VisaError("Unknown VISA error with code %d"%ret)
    else:
        raise VisaError("Unknown VISA error with code %d"%ret)
    
def cwrap(dll, name, argtypes):
    func = getattr(dll, name)
    func.argtypes = argtypes
    func.restype = ViStatus
    func.errcheck = errcheck
    return func
    
class VisaError(Exception):
    VI_SUCCESS_EVENT_EN                   =(0x3FFF0002L) #/* 3FFF0002,  1073676290 */
    VI_SUCCESS_EVENT_DIS                  =(0x3FFF0003L) #/* 3FFF0003,  1073676291 */
    VI_SUCCESS_QUEUE_EMPTY                =(0x3FFF0004L) #/* 3FFF0004,  1073676292 */
    VI_SUCCESS_TERM_CHAR                  =(0x3FFF0005L) #/* 3FFF0005,  1073676293 */
    VI_SUCCESS_MAX_CNT                    =(0x3FFF0006L) #/* 3FFF0006,  1073676294 */
    VI_SUCCESS_DEV_NPRESENT               =(0x3FFF007DL) #/* 3FFF007D,  1073676413 */
    VI_SUCCESS_TRIG_MAPPED                =(0x3FFF007EL) #/* 3FFF007E,  1073676414 */
    VI_SUCCESS_QUEUE_NEMPTY               =(0x3FFF0080L) #/* 3FFF0080,  1073676416 */
    VI_SUCCESS_NCHAIN                     =(0x3FFF0098L) #/* 3FFF0098,  1073676440 */
    VI_SUCCESS_NESTED_SHARED              =(0x3FFF0099L) #/* 3FFF0099,  1073676441 */
    VI_SUCCESS_NESTED_EXCLUSIVE           =(0x3FFF009AL) #/* 3FFF009A,  1073676442 */
    VI_SUCCESS_SYNC                       =(0x3FFF009BL) #/* 3FFF009B,  1073676443 */
    
    VI_WARN_QUEUE_OVERFLOW                =(0x3FFF000CL) #/* 3FFF000C,  1073676300 */
    VI_WARN_CONFIG_NLOADED                =(0x3FFF0077L) #/* 3FFF0077,  1073676407 */
    VI_WARN_NULL_OBJECT                   =(0x3FFF0082L) #/* 3FFF0082,  1073676418 */
    VI_WARN_NSUP_ATTR_STATE               =(0x3FFF0084L) #/* 3FFF0084,  1073676420 */
    VI_WARN_UNKNOWN_STATUS                =(0x3FFF0085L) #/* 3FFF0085,  1073676421 */
    VI_WARN_NSUP_BUF                      =(0x3FFF0088L) #/* 3FFF0088,  1073676424 */
    VI_WARN_EXT_FUNC_NIMPL                =(0x3FFF00A9L) #/* 3FFF00A9,  1073676457 */
    
    _VI_ERROR = (-2147483647L-1)
    VI_ERROR_SYSTEM_ERROR       =(_VI_ERROR+0x3FFF0000L) #/* BFFF0000, -1073807360 */
    VI_ERROR_INV_OBJECT         =(_VI_ERROR+0x3FFF000EL) #/* BFFF000E, -1073807346 */
    VI_ERROR_RSRC_LOCKED        =(_VI_ERROR+0x3FFF000FL) #/* BFFF000F, -1073807345 */
    VI_ERROR_INV_EXPR           =(_VI_ERROR+0x3FFF0010L) #/* BFFF0010, -1073807344 */
    VI_ERROR_RSRC_NFOUND        =(_VI_ERROR+0x3FFF0011L) #/* BFFF0011, -1073807343 */
    VI_ERROR_INV_RSRC_NAME      =(_VI_ERROR+0x3FFF0012L) #/* BFFF0012, -1073807342 */
    VI_ERROR_INV_ACC_MODE       =(_VI_ERROR+0x3FFF0013L) #/* BFFF0013, -1073807341 */
    VI_ERROR_TMO                =(_VI_ERROR+0x3FFF0015L) #/* BFFF0015, -1073807339 */
    VI_ERROR_CLOSING_FAILED     =(_VI_ERROR+0x3FFF0016L) #/* BFFF0016, -1073807338 */
    VI_ERROR_INV_DEGREE         =(_VI_ERROR+0x3FFF001BL) #/* BFFF001B, -1073807333 */
    VI_ERROR_INV_JOB_ID         =(_VI_ERROR+0x3FFF001CL) #/* BFFF001C, -1073807332 */
    VI_ERROR_NSUP_ATTR          =(_VI_ERROR+0x3FFF001DL) #/* BFFF001D, -1073807331 */
    VI_ERROR_NSUP_ATTR_STATE    =(_VI_ERROR+0x3FFF001EL) #/* BFFF001E, -1073807330 */
    VI_ERROR_ATTR_READONLY      =(_VI_ERROR+0x3FFF001FL) #/* BFFF001F, -1073807329 */
    VI_ERROR_INV_LOCK_TYPE      =(_VI_ERROR+0x3FFF0020L) #/* BFFF0020, -1073807328 */
    VI_ERROR_INV_ACCESS_KEY     =(_VI_ERROR+0x3FFF0021L) #/* BFFF0021, -1073807327 */
    VI_ERROR_INV_EVENT          =(_VI_ERROR+0x3FFF0026L) #/* BFFF0026, -1073807322 */
    VI_ERROR_INV_MECH           =(_VI_ERROR+0x3FFF0027L) #/* BFFF0027, -1073807321 */
    VI_ERROR_HNDLR_NINSTALLED   =(_VI_ERROR+0x3FFF0028L) #/* BFFF0028, -1073807320 */
    VI_ERROR_INV_HNDLR_REF      =(_VI_ERROR+0x3FFF0029L) #/* BFFF0029, -1073807319 */
    VI_ERROR_INV_CONTEXT        =(_VI_ERROR+0x3FFF002AL) #/* BFFF002A, -1073807318 */
    VI_ERROR_QUEUE_OVERFLOW     =(_VI_ERROR+0x3FFF002DL) #/* BFFF002D, -1073807315 */
    VI_ERROR_NENABLED           =(_VI_ERROR+0x3FFF002FL) #/* BFFF002F, -1073807313 */
    VI_ERROR_ABORT              =(_VI_ERROR+0x3FFF0030L) #/* BFFF0030, -1073807312 */
    VI_ERROR_RAW_WR_PROT_VIOL   =(_VI_ERROR+0x3FFF0034L) #/* BFFF0034, -1073807308 */
    VI_ERROR_RAW_RD_PROT_VIOL   =(_VI_ERROR+0x3FFF0035L) #/* BFFF0035, -1073807307 */
    VI_ERROR_OUTP_PROT_VIOL     =(_VI_ERROR+0x3FFF0036L) #/* BFFF0036, -1073807306 */
    VI_ERROR_INP_PROT_VIOL      =(_VI_ERROR+0x3FFF0037L) #/* BFFF0037, -1073807305 */
    VI_ERROR_BERR               =(_VI_ERROR+0x3FFF0038L) #/* BFFF0038, -1073807304 */
    VI_ERROR_IN_PROGRESS        =(_VI_ERROR+0x3FFF0039L) #/* BFFF0039, -1073807303 */
    VI_ERROR_INV_SETUP          =(_VI_ERROR+0x3FFF003AL) #/* BFFF003A, -1073807302 */
    VI_ERROR_QUEUE_ERROR        =(_VI_ERROR+0x3FFF003BL) #/* BFFF003B, -1073807301 */
    VI_ERROR_ALLOC              =(_VI_ERROR+0x3FFF003CL) #/* BFFF003C, -1073807300 */
    VI_ERROR_INV_MASK           =(_VI_ERROR+0x3FFF003DL) #/* BFFF003D, -1073807299 */
    VI_ERROR_IO                 =(_VI_ERROR+0x3FFF003EL) #/* BFFF003E, -1073807298 */
    VI_ERROR_INV_FMT            =(_VI_ERROR+0x3FFF003FL) #/* BFFF003F, -1073807297 */
    VI_ERROR_NSUP_FMT           =(_VI_ERROR+0x3FFF0041L) #/* BFFF0041, -1073807295 */
    VI_ERROR_LINE_IN_USE        =(_VI_ERROR+0x3FFF0042L) #/* BFFF0042, -1073807294 */
    VI_ERROR_NSUP_MODE          =(_VI_ERROR+0x3FFF0046L) #/* BFFF0046, -1073807290 */
    VI_ERROR_SRQ_NOCCURRED      =(_VI_ERROR+0x3FFF004AL) #/* BFFF004A, -1073807286 */
    VI_ERROR_INV_SPACE          =(_VI_ERROR+0x3FFF004EL) #/* BFFF004E, -1073807282 */
    VI_ERROR_INV_OFFSET         =(_VI_ERROR+0x3FFF0051L) #/* BFFF0051, -1073807279 */
    VI_ERROR_INV_WIDTH          =(_VI_ERROR+0x3FFF0052L) #/* BFFF0052, -1073807278 */
    VI_ERROR_NSUP_OFFSET        =(_VI_ERROR+0x3FFF0054L) #/* BFFF0054, -1073807276 */
    VI_ERROR_NSUP_VAR_WIDTH     =(_VI_ERROR+0x3FFF0055L) #/* BFFF0055, -1073807275 */
    VI_ERROR_WINDOW_NMAPPED     =(_VI_ERROR+0x3FFF0057L) #/* BFFF0057, -1073807273 */
    VI_ERROR_RESP_PENDING       =(_VI_ERROR+0x3FFF0059L) #/* BFFF0059, -1073807271 */
    VI_ERROR_NLISTENERS         =(_VI_ERROR+0x3FFF005FL) #/* BFFF005F, -1073807265 */
    VI_ERROR_NCIC               =(_VI_ERROR+0x3FFF0060L) #/* BFFF0060, -1073807264 */
    VI_ERROR_NSYS_CNTLR         =(_VI_ERROR+0x3FFF0061L) #/* BFFF0061, -1073807263 */
    VI_ERROR_NSUP_OPER          =(_VI_ERROR+0x3FFF0067L) #/* BFFF0067, -1073807257 */
    VI_ERROR_INTR_PENDING       =(_VI_ERROR+0x3FFF0068L) #/* BFFF0068, -1073807256 */
    VI_ERROR_ASRL_PARITY        =(_VI_ERROR+0x3FFF006AL) #/* BFFF006A, -1073807254 */
    VI_ERROR_ASRL_FRAMING       =(_VI_ERROR+0x3FFF006BL) #/* BFFF006B, -1073807253 */
    VI_ERROR_ASRL_OVERRUN       =(_VI_ERROR+0x3FFF006CL) #/* BFFF006C, -1073807252 */
    VI_ERROR_TRIG_NMAPPED       =(_VI_ERROR+0x3FFF006EL) #/* BFFF006E, -1073807250 */
    VI_ERROR_NSUP_ALIGN_OFFSET  =(_VI_ERROR+0x3FFF0070L) #/* BFFF0070, -1073807248 */
    VI_ERROR_USER_BUF           =(_VI_ERROR+0x3FFF0071L) #/* BFFF0071, -1073807247 */
    VI_ERROR_RSRC_BUSY          =(_VI_ERROR+0x3FFF0072L) #/* BFFF0072, -1073807246 */
    VI_ERROR_NSUP_WIDTH         =(_VI_ERROR+0x3FFF0076L) #/* BFFF0076, -1073807242 */
    VI_ERROR_INV_PARAMETER      =(_VI_ERROR+0x3FFF0078L) #/* BFFF0078, -1073807240 */
    VI_ERROR_INV_PROT           =(_VI_ERROR+0x3FFF0079L) #/* BFFF0079, -1073807239 */
    VI_ERROR_INV_SIZE           =(_VI_ERROR+0x3FFF007BL) #/* BFFF007B, -1073807237 */
    VI_ERROR_WINDOW_MAPPED      =(_VI_ERROR+0x3FFF0080L) #/* BFFF0080, -1073807232 */
    VI_ERROR_NIMPL_OPER         =(_VI_ERROR+0x3FFF0081L) #/* BFFF0081, -1073807231 */
    VI_ERROR_INV_LENGTH         =(_VI_ERROR+0x3FFF0083L) #/* BFFF0083, -1073807229 */
    VI_ERROR_INV_MODE           =(_VI_ERROR+0x3FFF0091L) #/* BFFF0091, -1073807215 */
    VI_ERROR_SESN_NLOCKED       =(_VI_ERROR+0x3FFF009CL) #/* BFFF009C, -1073807204 */
    VI_ERROR_MEM_NSHARED        =(_VI_ERROR+0x3FFF009DL) #/* BFFF009D, -1073807203 */
    VI_ERROR_LIBRARY_NFOUND     =(_VI_ERROR+0x3FFF009EL) #/* BFFF009E, -1073807202 */
    VI_ERROR_NSUP_INTR          =(_VI_ERROR+0x3FFF009FL) #/* BFFF009F, -1073807201 */
    VI_ERROR_INV_LINE           =(_VI_ERROR+0x3FFF00A0L) #/* BFFF00A0, -1073807200 */
    VI_ERROR_FILE_ACCESS        =(_VI_ERROR+0x3FFF00A1L) #/* BFFF00A1, -1073807199 */
    VI_ERROR_FILE_IO            =(_VI_ERROR+0x3FFF00A2L) #/* BFFF00A2, -1073807198 */
    VI_ERROR_NSUP_LINE          =(_VI_ERROR+0x3FFF00A3L) #/* BFFF00A3, -1073807197 */
    VI_ERROR_NSUP_MECH          =(_VI_ERROR+0x3FFF00A4L) #/* BFFF00A4, -1073807196 */
    VI_ERROR_INTF_NUM_NCONFIG   =(_VI_ERROR+0x3FFF00A5L) #/* BFFF00A5, -1073807195 */
    VI_ERROR_CONN_LOST          =(_VI_ERROR+0x3FFF00A6L) #/* BFFF00A6, -1073807194 */
    VI_ERROR_MACHINE_NAVAIL     =(_VI_ERROR+0x3FFF00A7L) #/* BFFF00A7, -1073807193 */
    VI_ERROR_NPERMISSION        =(_VI_ERROR+0x3FFF00A8L) #/* BFFF00A8, -1073807192 */

PM100USB_FIND_PATTERN = "USB?*INSTR{VI_ATTR_MANF_ID==0x1313 && VI_ATTR_MODEL_CODE==0x8072}"

viFindRsrc = visa.viFindRsrc
viFindRsrc.argtypes = [ViSession, ViString, ViPFindList, 
                       POINTER(c_uint32), c_char_p]
viFindRsrc.restype = ViStatus
viFindRsrc.errcheck = errcheck

viOpenDefaultRM = visa.viOpenDefaultRM
viOpenDefaultRM.argtypes = [ViPSession,]
viOpenDefaultRM.restype = ViStatus
viOpenDefaultRM.errcheck = errcheck

viClose = visa.viClose
viClose.argtypes = [ViObject,]
viClose.restype = ViStatus
viClose.errcheck = errcheck

viFindNext = visa.viFindNext
viFindNext.argtypes = [ViFindList, c_char_p]
viFindNext.restype = ViStatus
viFindNext.errcheck = errcheck

viStatusDesc = visa.viStatusDesc
viStatusDesc.argtypes = [ViObject, ViStatus, c_char_p]
viStatusDesc.restype = ViStatus

PM100D_init = dll.PM100D_init
PM100D_init.argtypes = [ViRsrc, ViBoolean, ViBoolean, POINTER(ViSession)]
PM100D_init.restype = ViStatus
PM100D_init.errcheck = errcheck

PM100D_close = dll.PM100D_close
PM100D_close.argtypes = [ViSession]
PM100D_close.restype = ViStatus
PM100D_close.errcheck = errcheck

PM100D_getWavelength = cwrap(dll, "PM100D_getWavelength", 
                             [ViSession, ViInt16, POINTER(ViReal64)])
PM100D_setWavelength = cwrap(dll, "PM100D_setWavelength", [ViSession, ViReal64])
 
PM100D_measPower = cwrap(dll, "PM100D_measPower", [ViSession, POINTER(ViReal64)]) 
 
PM100D_getPowerRange = cwrap(dll, "PM100D_getPowerRange", [ViSession, ViInt16, POINTER(ViReal64)])
PM100D_setPowerRange = cwrap(dll, "PM100D_setPowerRange", [ViSession, ViReal64])

PM100D_getPowerAutorange = cwrap(dll, "PM100D_getPowerAutorange", [ViSession, POINTER(ViBoolean)])
PM100D_setPowerAutorange = cwrap(dll, "PM100D_setPowerAutoRange", [ViSession, ViBoolean]) 

PM100D_getPowerUnit = cwrap(dll, "PM100D_getPowerUnit", [ViSession, POINTER(ViInt16)])
PM100D_setPowerUnit = cwrap(dll, "PM100D_setPowerUnit", [ViSession, ViInt16])

def find_instruments():
    resMgr = ViSession()
    print "get session", viOpenDefaultRM(byref(resMgr)), resMgr.value
    findPattern = PM100USB_FIND_PATTERN
    findlist = ViFindList()
    findCnt = c_uint32()
    buf = create_string_buffer(256) #buffer length given in visa.h
    ret = viFindRsrc(resMgr, findPattern, byref(findlist), 
                     byref(findCnt), buf)
    print "resources", ret, findCnt.value, buf.value
    if findCnt.value<1:
        viClose(findlist)
        viClose(resMgr)
        return []
    
    output = [buf.value,]
    for i in xrange(1, findCnt.value):
        buf = create_string_buffer(256)
        viFindNext(findlist, buf)
        output.append(buf.value)
    return output

class PM100D(object):
    def __init__(self, id_string):
        handle = ViSession()
        PM100D_init(id_string, VI_FALSE, VI_TRUE, byref(handle))
        self._handle = handle
        self.id_string = id_string
        
    def __del__(self):
        PM100D_close(self._handle)
        print "PM100 closed"
        
    @property
    def wavelength(self):
        wl = ViReal64()
        PM100D_ATTR_SET_VAL = 0
        PM100D_getWavelength(self._handle, PM100D_ATTR_SET_VAL, byref(wl))
        return wl.value
    
    @wavelength.setter
    def wavelength(self, val):
        PM100D_setWavelength(self._handle, val)
        
    @property
    def power(self):
        pwr = ViReal64()
        PM100D_measPower(self._handle, byref(pwr))
        return pwr.value
    
    @property
    def range(self):
        ATTR_SET_VAL = 0
        rng = ViReal64()
        PM100D_getPowerRange(self._handle, ATTR_SET_VAL, byref(rng))
        return rng.value
    
    @range.setter
    def range(self, val):
        PM100D_setPowerRange(self._handle, val)
        
    @property
    def min_range(self):
        ATTR_MIN_VAL = 1
        rng = ViReal64()
        PM100D_getPowerRange(self._handle, ATTR_MIN_VAL, byref(rng))
        return rng.value
    
    @property
    def max_range(self):
        ATTR_MAX_VAL = 2
        rng = ViReal64()
        PM100D_getPowerRange(self._handle, ATTR_MAX_VAL, byref(rng))
        return rng.value
    
    @property
    def autorange(self):
        ar = ViBoolean()
        PM100D_getPowerAutorange(self._handle, byref(ar))
        return True if ar.value==VI_TRUE else False

    @autorange.setter
    def autorange(self, val):
        v = VI_TRUE if val else VI_FALSE
        PM100D_setPowerAutorange(self._handle, v)
    

if __name__=="__main__":
    instlist = find_instruments()
    print instlist
    pm = PM100D(instlist[0])
    print pm
    print pm.wavelength
    pm.wavelength = 780
    print pm.wavelength
    print pm.power
    print pm.range
    print pm.min_range
    print pm.max_range
    pm.range = 0.05 #50 mW
    print pm.range
    print pm.autorange
    pm.autorange = True
    print pm.autorange
    
    
#    codes = [c for c in dir(VisaError) if c.startswith("VI_")]
#    for code in codes:
#        buf = create_string_buffer(256)
#        ret = viStatusDesc(resMgr, getattr(VisaError, code), buf)
#        print code, "->", buf.value
        


