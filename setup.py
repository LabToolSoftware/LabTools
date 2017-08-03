import sys
from cx_Freeze import setup, Executable

setup(
    name = "Lab Tools",
    version = "0.1",
    description = "Database for all python executables made by PSFRU members",
    executables = [Executable("main.py", base = "Win32GUI")])
