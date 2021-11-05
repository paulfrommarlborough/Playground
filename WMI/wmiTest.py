#  wmiTest.py
#
#   first exploration of the wmi libarary...
#   seems slow and awkward to get performance  data (maybe stick to c++)
#
#   look into --> import win32pdh 
#
import wmi
import time

OsCaption =""
SystemName=""
NumberOfProcesses=0

c = wmi.WMI()

#----------------------------------------------
# general system : get os and system info...
#----------------------------------------------

for os in c.Win32_OperatingSystem():
    SystemName = os.CSName
    OsCaption = os.Caption
    NumberOfProcesses = os.NumberOfProcesses
#    print (os)

print(f'MyPerfDashboardProcess,name={SystemName},os="{OsCaption}",NumberOfProcesses={NumberOfProcesses}')

#----------------------------------------------
# disk: get disk by name ( could get all disks.)
#----------------------------------------------

c_drive = wmi.WMI(moniker='//./root/cimv2:Win32_LogicalDisk.DeviceID="C:\"')
print(f'MyPerfDashboardDisk,name={c_drive.Name},description"{c_drive.Description}",Size={c_drive.size}')

#----------------------------------------------
# Process: just get pid + commandline...
#----------------------------------------------

for process in c.Win32_Process (["Name", "ProcessId", "CommandLine"]):
    print (f"PID = {process.ProcessId} Name = {process.Name}, Cmdline= {process.CommandLine}")

#----------------------------------------------
# watch for new processes
#----------------------------------------------

#process_watcher = c.Win32_Process.watch_for("creation")
#while True:
#    new_process = process_watcher()
#    print (new_process)

#----------------------------------------------
#  remote system
#----------------------------------------------

#cr = wmi.WMI("ECAPDEV", user=r"ECAPDEV\\Administrator", password="ENTERPASSWORD")
#for os in cr.Win32_OperatingSystem():
#    print (os)

#----------------------------------------------
# raw data: touch classes to get them in cache.. (slow..) 
#----------------------------------------------

c = wmi.WMI(find_classes=False)
for perf_class1 in c.subclasses_of("Win32_PerfRawData"):
    getattr(c, perf_class1)               # do nothing, just get it into the cache

# cpp = wmi.WMI(find_classes=False)
# cRaw = wmi.WMI ().instances ("Win32_PerfRawData_PerfOS_System"
# cdsk = wmi.WMI ().instances ("Win32_LogicalDisk")

for cdisk in wmi.WMI ().instances ("Win32_LogicalDisk"):
    print (f'cDisk.Name = {cdisk.Name}')





#----------------------------------------------------
# Processor ->  get total - comput util.
#-----------------------------------------------------


cRawProcessor = c.instances ("Win32_PerfRawData_PerfOS_Processor")
for cProcessor in cRawProcessor:
    if cProcessor.Name == "_Total":
    #    print (cProcessor)
        Timestamp_PerfTime = cProcessor.Timestamp_PerfTime
        Timestamp_Sys100ns = cProcessor.Timestamp_Sys100NS
        Freq_perfTime = cProcessor.Frequency_PerfTime
        Freq_Sys100NS = cProcessor.Frequency_Sys100NS

        print (f"Processor {cProcessor.Name}, ProcessorTime = {cProcessor.PercentProcessorTime}")

    
#print(cRawProcessor[0])

CurrentVal=0
LastVal = 0
fOps = 0.0

#----------------------------------------------------
# System -> FileDataOperationsPerSecond
#-----------------------------------------------------

cRaw = c.instances ("Win32_PerfRawData_PerfOS_System")
for i in range(1, 10):

    LastVal    =  CurrentVal
    CurrentVal = cRaw[0].FileDataOperationsPersec 
    if LastVal > 0:
        fOps = CurrentVal - LastVal

    print(f' FileDataOps =  {cRaw[0].FileDataOperationsPersec}  {fOps / 60.0}')    # fOps for that sec..
    time.sleep(60)
    cRaw = wmi.WMI ().instances ("Win32_PerfRawData_PerfOS_System")


#---------------------------------------------
# Get list raw metric classes: print names
#---------------------------------------------
cpp = wmi.WMI(find_classes=False)
for perf_class1 in cpp.subclasses_of("Win32_PerfRawData"):
        print(perf_class1)

print("done")


