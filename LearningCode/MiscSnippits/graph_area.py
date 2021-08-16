# sample to put a graph up.  testing sting convert to float

import matplotlib.pyplot as plt
serieslabel='CPU Utilization'
datainput= '12.3 14.2 13.9 16.0 17.2 15.0 13.2 13.2'

seriesdata={ 2.0, 3.0 ,4.0 ,5.0 }
seriesfloat = [float(x) for x in seriesdata]
print (f"series float = {seriesfloat}")

shortseries = [float(x) for x in datainput.split(" ")]
ilen=len(shortseries)

intervals = [val for val in range(0,ilen)]

graphdata = {
    serieslabel: shortseries
}

print(f" keys = {graphdata.keys()}")
print(f" values = {graphdata.values()}")

ig, ax = plt.subplots()
ax.stackplot(intervals, graphdata.values(), labels=graphdata.keys())

ax.legend(loc='upper left')
ax.set_title('title')
ax.set_xlabel('x label')
ax.set_ylabel('y label)')
plt.show()
