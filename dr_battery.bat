@echo off
color F2
echo Battery report generator for windows
echo shreyanshrp (github.com/shreyanshrp)
echo --------------------------------------
echo,
powercfg /batteryreport
start battery-report.html
echo,
echo Report Opened Successfully!
pause
