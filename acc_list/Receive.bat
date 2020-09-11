@ECHO OFF
if EXIST %3 goto UNLOCK
if NOT EXIST %1 goto MDPrivate
:CONFIRM
echo Are you sure to lock this folder? (Y/N)
set/p "cho=>"
if %cho%==Y goto LOCK
if %cho%==y goto LOCK
if %cho%==n goto END
if %cho%==N goto END
echo Invalid choice.
goto CONFIRM
:LOCK
ren %1 %3
attrib +h +s %3
echo Folder locked
pause
goto End
:UNLOCK
REM echo Enter password to Unlock Your Secure Folder
REM set/p "pass=>"
if NOT %4 == %2 goto FAIL
attrib -h -s %3
ren %3 %1
echo Folder Unlocked successfully
pause
goto End
:FAIL
echo Invalid password
goto end
:MDPrivate
md %1
echo %1 created successfully
pause
goto End
:End