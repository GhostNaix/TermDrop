@echo off
color a
title "TermDrop Compiler CLI V1.3"
choice /M "Compile TermDrop ?"
If Errorlevel 2 Goto No
If Errorlevel 1 Goto Yes

:No
echo "Compilation Canceled"
exit

:Yes
echo "Are you sure you wish to Compile ? CTRL+C to quit or"
pause
pyinstaller --clean --onefile "TermDrop_Encoder.py"
move /y dist\*  
rmdir /S /Q build
rmdir /S /Q dist
del /Q "TermDrop_Encoder.spec"
ren TermDrop_Encoder.exe TermDrop_Encoder_win32.exe
rem Compilee 64bit version
rem pyinstaller64 --clean --onefile "TermDrop_Encoder.py"
rem move /y dist\*  
rem rmdir /S /Q build
rem rmdir /S /Q dist
rem del /Q "TermDrop_Encoder.spec"
rem ren TermDrop_Encoder.exe TermDrop_Encoder_win64.exe
pause
exit