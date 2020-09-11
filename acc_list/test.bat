@echo off 
if EXIST "Tarjo.{21EC2020-3AEA-1069-A2DD-08002B30309D}" goto UNLOCK
if NOT EXIST Tarjo goto MDPrivate
:LOCK
ren Tarjo "Tarjo.{21EC2020-3AEA-1069-A2DD-08002B30309D}"
attrib +h +s "Tarjo.{21EC2020-3AEA-1069-A2DD-08002B30309D}"
echo Folder locked
pause
goto End
:UNLOCK
attrib -h -s "Tarjo.{21EC2020-3AEA-1069-A2DD-08002B30309D}"
ren "Tarjo.{21EC2020-3AEA-1069-A2DD-08002B30309D}" Tarjo
echo Folder Unlocked successfully
pause
goto End
:MDPrivate
md Tarjo
echo Tarjo created successfully
pause
goto lock
:End