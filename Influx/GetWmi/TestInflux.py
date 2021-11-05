
import wmi
from datetime import datetime
import time
import random
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

# You can generate a Token from the "Tokens Tab" in the UI

def Setup():
    # You can generate a Token from the "Tokens Tab" in the UI

    token = "Ki1AhF29mPKOfCi5QbB-osssaQm-9Qd5_W6IvWPIRn4arbTNpy47fMnlqDULals0ZzzAhiS3HiDN7l5E-EZ4pg=="
    org = "perfcap"
    bucket = "pawzTS"
    OS =""
    HOST=""
    NumberOfProcesses=0
    
    client = InfluxDBClient(url="http://localhost:8086", token=token)

    write_api = client.write_api(write_options=SYNCHRONOUS)


def GetFromWMI():
    c = wmi.WMI()


def Collect():
    i = 0

    while 1:
        dt = int(time.time())      ## not needed    
        i = random.randrange(1,100)
        val = GetFromWMI()
        data = f"FileDataOps,host={HOST},os={OS} value={val}" 
        print(data)
        write_api.write(bucket, org, data)
        time.sleep(60)



if __name__ == "__main__":    
    Setup()
    Collect()

    query = f'from(bucket: \\"{bucket}\\") |> range(start: -1h)'
    tables = client.query_api().query(query, org=org)
    print("-done---")
