@echo OFF

for /f "delims=" %%i in ('whoami') do set output=%%i
NET SESSION >nul 2>&1

IF %ERRORLEVEL% EQU 0 (
    set "PROMPT=*%PROMPT%"
)
@echo ON
