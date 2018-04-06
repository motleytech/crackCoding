from _winreg import *

"""print r"*** Reading from HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Enum\HID ***" """
aReg = ConnectRegistry(None,HKEY_LOCAL_MACHINE)

FLIP_FLOP_VALUE = 1

aKey = OpenKey(aReg, r"SYSTEM\CurrentControlSet\Enum\HID")

for i in range(1024):
    try:
        asubkey_name = EnumKey(aKey, i)
        asubkey = OpenKey(aKey, asubkey_name)
        for j in range(1024):
            try:
                bsubkey_name = EnumKey(asubkey, j)
                bsubkey = OpenKey(asubkey, bsubkey_name)
                for k in range(1024):
                    try:
                        csubkey_name = EnumKey(bsubkey, k)
                        if csubkey_name != 'Device Parameters':
                            continue
                        csubkey = OpenKey(bsubkey, csubkey_name, 0, KEY_ALL_ACCESS)
                        val = QueryValueEx(csubkey, "FlipFlopWheel")

                        print asubkey_name, bsubkey_name, csubkey_name
                        SetValueEx(csubkey, 'FlipFlopWheel', 0, REG_DWORD, FLIP_FLOP_VALUE)
                        CloseKey(csubkey)
                        print 'Set FFW : %s' % FLIP_FLOP_VALUE

                    except error as e:
                        if 'No more data' in e.strerror:
                            break
                        continue
            except error as e:
                if 'No more data' in e.strerror:
                    break
                continue
    except error as e:
        if 'No more data' in e.strerror:
            break
        continue