@echo off
echo Battery report Generator for windows
echo By shreyanshrp (github.com/shreyanshrp)
powercfg /batteryreport
start battery-report.html
echo Report Opened Successfully!
pause
