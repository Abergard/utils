@echo OFF

for /f "delims=" %%i in ('whoami') do set output=%%i
NET SESSION >nul 2>&1

IF %ERRORLEVEL% EQU 0 (
	echo ^(admin^) %output%
) ELSE (
	echo %output%
)
@echo ON