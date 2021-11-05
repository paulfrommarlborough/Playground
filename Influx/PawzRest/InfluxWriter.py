from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS


class InfluxWriter:
 
    # not type casting the inputs should be string.

    def __init__(self, myinfluxweb, iuser, ipwd, myorg, mybucket):        
    #    print('InfluxWriter,  init...')
        self.all_files = False
        self.influxweb = myinfluxweb
        self.token = "Ki1AhF29mPKOfCi5QbB-osssaQm-9Qd5_W6IvWPIRn4arbTNpy47fMnlqDULals0ZzzAhiS3HiDN7l5E-EZ4pg=="
        self.token = f"{iuser}:{ipwd}"
        self.org = myorg
        self.bucket = mybucket
        self.client = None
        self.write_api = None

    def Setup(self):
        self.client = InfluxDBClient(url=self.influxweb, token=self.token)
        self.write_api = self.client.write_api(write_options=SYNCHRONOUS)

    def Write(self, strLine):
        self.write_api.write(self.bucket, self.org, strLine)

    # You can generate a Token from the "Tokens Tab" in the UI