import wmi

class InfluxWriterWmi:
 
    # not type casting the inputs should be string.

    def __init__(self):        
        print('InfluxWriterWmi,  init...')
        self.MetricName="FileDataOperations"
        self.HostName = None
        self.OsName  = None
        self.cRaw = None
        self.lastValue=0
        self.currentValue=0
        self.c = wmi.WMI()

    def GetHostInfo(self):
        for os in self.c.Win32_OperatingSystem():
            self.HostName = os.CSName
            self.OsName   = os.Caption  

    def Collect(self):
        fOps = 0.0
        self.cRaw = self.c.instances ("Win32_PerfRawData_PerfOS_System")
    
        self.lastValue = self.currentValue
        self.currentValue = self.cRaw[0].FileDataOperationsPersec
        if self.lastValue > 0:
            fOps = self.currentValue - self.lastValue
        return fOps
