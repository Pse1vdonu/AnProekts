#AI
import ctypes
class COORD(ctypes.Structure):
    _fields_ = [("X", ctypes.c_short), ("Y", ctypes.c_short)]
class CONSOLE_FONT_INFOEX(ctypes.Structure):
    _fields_ = [
        ("cbSize", ctypes.c_ulong),
        ("nFont", ctypes.c_ulong),
        ("dwFontSize", COORD),
        ("FontFamily", ctypes.c_uint),
        ("FontWeight", ctypes.c_uint), #Толщина (ctypes.c_uint)
        ("FaceName", ctypes.c_wchar * 32) #Шрифт (ctypes.c_wchar * 32)
    ]
def set_small_font():
    STD_OUTPUT_HANDLE = -11
    handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
    font = CONSOLE_FONT_INFOEX()
    font.cbSize = ctypes.sizeof(CONSOLE_FONT_INFOEX)
    ctypes.windll.kernel32.GetCurrentConsoleFontEx(handle, False, ctypes.byref(font))
    font.dwFontSize.X = 8 #<--Значение можно поменять (8)
    font.dwFontSize.Y = 12 #<--Значение можно поменять (12)
    ctypes.windll.kernel32.SetCurrentConsoleFontEx(handle, False, ctypes.byref(font))