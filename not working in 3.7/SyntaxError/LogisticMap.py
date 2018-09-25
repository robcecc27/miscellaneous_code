def printIterates(OneDMap, initialConditions, nIterates):
    x=initialConditions
    for i in range(nIterates):
        x=OneDMap(x)
        print i, x

def LogisticMap(x):
    return 4.0 * x * (1.0 - x)

printIterates(LogisticMap, 0.3, 10)

input('Press Enter to Continue...)

C:\Python37\Scripts\;C:\Python37\;C:\ProgramData\Oracle\Java\javapath;c:\Program Files (x86)\Intel\iCLS Client\;c:\Program Files\Intel\iCLS Client\;C:\Windows\system32;C:\Windows;C:\Windows\System32\Wbem;C:\Windows\System32\WindowsPowerShell\v1.0\;C:\Program Files\Intel\Intel(R) Management Engine Components\DAL;C:\Program Files\Intel\Intel(R) Management Engine Components\IPT;C:\Program Files (x86)\Intel\Intel(R) Management Engine Components\DAL;C:\Program Files (x86)\Intel\Intel(R) Management Engine Components\IPT;C:\Program Files\Intel\WiFi\bin\;C:\Program Files\Common Files\Intel\WirelessCommon\;C:\Program Files (x86)\Windows Kits\8.1\Windows Performance Toolkit\;C:\Program Files\Microsoft SQL Server\110\Tools\Binn\;C:\Program Files (x86)\QuickTime\QTSystem\;C:\Program Files\Java\jdk1.8.0_25\bin;%USERPROFILE%\AppData\Local\Microsoft\WindowsApps;C:\Users\Rob\AppData\Roaming\npm;