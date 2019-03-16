# Modified from http://stackoverflow.com/a/13615802/2924421

import ctypes
from ctypes import wintypes
import time

user32 = ctypes.WinDLL('user32', use_last_error=True)

INPUT_MOUSE    = 0
INPUT_KEYBOARD = 1
INPUT_HARDWARE = 2

KEYEVENTF_EXTENDEDKEY = 0x0001
KEYEVENTF_KEYUP       = 0x0002
KEYEVENTF_UNICODE     = 0x0004
KEYEVENTF_SCANCODE    = 0x0008

MAPVK_VK_TO_VSC = 0

# C struct definitions
wintypes.ULONG_PTR = wintypes.WPARAM

SendInput = ctypes.windll.user32.SendInput

PUL = ctypes.POINTER(ctypes.c_ulong)

class KEYBDINPUT(ctypes.Structure):
    _fields_ = (("wVk",         wintypes.WORD),
                ("wScan",       wintypes.WORD),
                ("dwFlags",     wintypes.DWORD),
                ("time",        wintypes.DWORD),
                ("dwExtraInfo", wintypes.ULONG_PTR))

class MOUSEINPUT(ctypes.Structure):
    _fields_ = (("dx",          wintypes.LONG),
                ("dy",          wintypes.LONG),
                ("mouseData",   wintypes.DWORD),
                ("dwFlags",     wintypes.DWORD),
                ("time",        wintypes.DWORD),
                ("dwExtraInfo", wintypes.ULONG_PTR))

class HARDWAREINPUT(ctypes.Structure):
    _fields_ = (("uMsg",    wintypes.DWORD),
                ("wParamL", wintypes.WORD),
                ("wParamH", wintypes.WORD))

class INPUT(ctypes.Structure):
    class _INPUT(ctypes.Union):
        _fields_ = (("ki", KEYBDINPUT),
                    ("mi", MOUSEINPUT),
                    ("hi", HARDWAREINPUT))
    _anonymous_ = ("_input",)
    _fields_ = (("type",   wintypes.DWORD),
                ("_input", _INPUT))

LPINPUT = ctypes.POINTER(INPUT)

def _check_count(result, func, args):
    if result == 0:
        raise ctypes.WinError(ctypes.get_last_error())
    return args

user32.SendInput.errcheck = _check_count
user32.SendInput.argtypes = (wintypes.UINT, # nInputs
                             LPINPUT,       # pInputs
                             ctypes.c_int)  # cbSize

def KeyDown(unicodeKey):
    key, unikey, uniflag = GetKeyCode(unicodeKey)
    x = INPUT( type=INPUT_KEYBOARD, ki= KEYBDINPUT( key, unikey, uniflag, 0))
    user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))

def KeyUp(unicodeKey):
    key, unikey, uniflag = GetKeyCode(unicodeKey)
    extra = ctypes.c_ulong(0)
    x = INPUT( type=INPUT_KEYBOARD, ki= KEYBDINPUT( key, unikey, uniflag | KEYEVENTF_KEYUP, 0))
    user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))

def KeyPress(unicodeKey):
    time.sleep(0.0001)
    KeyDown(unicodeKey)
    time.sleep(0.0001)
    KeyUp(unicodeKey)
    time.sleep(0.0001)


def GetKeyCode(unicodeKey):
    k = unicodeKey
    curKeyCode = 0
    if k == "up": curKeyCode = 0x26
    elif k == "down": curKeyCode = 0x28
    elif k == "left": curKeyCode = 0x25
    elif k == "right": curKeyCode = 0x27
    elif k == "home": curKeyCode = 0x24
    elif k == "end": curKeyCode = 0x23
    elif k == "insert": curKeyCode = 0x2D
    elif k == "pgup": curKeyCode = 0x21
    elif k == "pgdn": curKeyCode = 0x22
    elif k == "delete": curKeyCode = 0x2E
    elif k == "\n": curKeyCode = 0x0D

    if curKeyCode == 0:
        return 0, int(unicodeKey.encode("hex"), 16), KEYEVENTF_UNICODE
    else:
        return curKeyCode, 0, 0