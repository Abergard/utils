@echo off
call c:\src\pmgai\pyvenv\Scripts\activate.bat
call vcvarsall amd64
start runemacs.exe --daemon
