# -*- coding: utf-8 -*-
import sys
from cx_Freeze import setup, Executable


base = None
if (sys.platform == "win32"):
    base = "Win32GUI"

options = {
    'build.exe': {
        'includes': [
            'test.py'
        ]
    }
}
setup(
name = 'Generate of password',
version = 1.0,
description = 'Generate of password',
options = options,
executables = [Executable("main.py", base=base)]
)