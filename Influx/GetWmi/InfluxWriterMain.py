import wmi
from datetime import datetime
import time
import random

from InfluxWriter import InfluxWriter
from InfluxWriterWmi import InfluxWriterWmi

if __name__ == "__main__":    
    fOps = 0.0
    wmiGetter = InfluxWriterWmi()
    wmiGetter.GetHostInfo()
    ifxWriter = InfluxWriter()
    ifxWriter.Setup()

    fRate = 60.0

    nCount = 0
    while True:
        st = time.time()

        fOps = wmiGetter.Collect() / fRate
        #OutLine=f'{wmiGetter.MetricName},Host={wmiGetter.HostName},Os="{wmiGetter.OsName}" Value={fOps}'
        OutLine=f'{wmiGetter.MetricName},Host={wmiGetter.HostName} Value={fOps}'
        print(OutLine)
        if nCount > 0:
            ifxWriter.Write(OutLine)
        nCount = nCount + 1
        et = time.time()
        tt = et - st
      # print (tt)
        sleeptime = 60 - tt
        if sleeptime > 0:
            time.sleep(sleeptime)
