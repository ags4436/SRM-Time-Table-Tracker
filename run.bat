@echo off

if %time% lss 10:00 (
 echo Day Order Finder
 cd "E:\TimeTable" 
 python script.py
)
EXIT