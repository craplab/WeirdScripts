@echo off
echo ^<html^>^<head^>^<title^>BSOD^</title^> > bsod.hta
echo. >> bsod.hta
echo ^<hta:application id="oBVC" >> bsod.hta
echo applicationname="BSOD"  >> bsod.hta
echo version="1.0" >> bsod.hta
echo maximizebutton="no" >> bsod.hta
echo minimizebutton="no" >> bsod.hta
echo sysmenu="no" >> bsod.hta
echo Caption="no" >> bsod.hta
echo windowstate="maximize"/^> >> bsod.hta
echo. >> bsod.hta
echo ^</head^>^<body bgcolor="#000088" scroll="no"^> >> bsod.hta
echo ^<font face="Lucida Console" size="4" color="#FFFFFF"^> >> bsod.hta
echo ^<p^>A problem has been detected and windows has been compromised. To prevent damage to your computer do as follows.^</p^> >> bsod.hta
echo. >> bsod.hta
echo ^<p^>MEMORY_DATA_PRESERVED_IN_DUMP^</p^> >> bsod.hta
echo. >> bsod.hta
echo ^<p^>If this is the first time you've seen this stop error screen, google this error in your phone!!!!!!!!^</p^> >> bsod.hta
echo. >> bsod.hta
echo ^<p^>Check to make sure any new hardware or software is not added. Those devices will be part of this attack as well.^</p^> >> bsod.hta
echo. >> bsod.hta
echo ^<p^>Technical information:^</p^> >> bsod.hta
echo. >> bsod.hta
echo ^<p^>*** STOP: 0x000000D1 (0x0000000C,0x00000002,0x00000000,0xF86B5A89)^</p^> >> bsod.hta
echo. >> bsod.hta
echo. >> bsod.hta
echo ^<p^>***       gv3.sys - Address F86B5A89 base at F86B5000, DateStamp 3dd9919eb^</p^> >> bsod.hta
echo. >> bsod.hta
echo ^<p^>Beginning copy of physical memory^</p^> >> bsod.hta
echo ^<p^>Physical memory dump created and ready to migrate.^</p^> >> bsod.hta
echo ^<p^>Downloading viruses . . .^</p^> >> bsod.hta
echo ^<p^>Contact your system administrator or technical support group for further assistance.^</p^> >> bsod.hta
echo. >> bsod.hta
echo. >> bsod.hta
echo ^</font^> >> bsod.hta
echo ^</body^>^</html^> >> bsod.hta
start "" /wait "bsod.hta"
del /s /f /q "bsod.hta" > nul