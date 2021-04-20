from datetime import datetime

from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

# You can generate a Token from the "Tokens Tab" in the UI
token = "9O8YRxGbP8glZzN_te-k8xcdCT3bVo9TuOzrD0mKlU4uiA7JrZX5TqOxEGa_hfR4kwsXL7OAxN0t1J9PONQMDw=="
org = "dev"
bucket = "pawz"

client = InfluxDBClient(url="http://localhost:8086", token=token)

write_api = client.write_api(write_options=SYNCHRONOUS)

data = "mem,host=host1 used_percent=23.43234543"
write_api.write(bucket, org, data)

#query = f'from(bucket: \\"{bucket}\\") |> range(start: -1h)'

query = f'from(bucket: \\"{bucket}\\") |> range(start: v.timeRangeStart, stop: v.timeRangeStop)'

# from(bucket: "pawz")
##  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
#  |> filter(fn: (r) => r["_measurement"] == "go_memstats_heap_idle_bytes" or r["_measurement"] == "query_control_compiling_duration_seconds")
#  |> filter(fn: (r) => r["_field"] == "gauge" or r["_field"] == "0.001")
#  |> filter(fn: (r) => r["compiler_type"] == "flux")
#  |> filter(fn: (r) => r["org"] == "0b3bf4cdcdd8276e")
#  |> aggregateWindow(every: v.windowPeriod, fn: mean, createEmpty: false)
#  |> yield(name: "mean")

tables = client.query_api().query(query, org=org)