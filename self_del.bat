@echo off
setlocal

rem Replace "YourTask.exe" with the name of the task you want to kill
set TaskName=Basic_Keylogger.exe

rem Replace "relative\path\to\your\file.txt" with the relative path to your file
set FilePath=C:\Basic_Keylogger.exe
set FilePath2=C:\Captures.txt
rem Kill the task
taskkill /IM %TaskName% /F

rem Delete the file
del "%FilePath%"
del "%FilePath2%"
echo Task and file deletion complete.

endlocal
