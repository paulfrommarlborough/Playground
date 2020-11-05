""" pyodbc  test
       pip install pyodbc
       cd python\scripts
       pip install pyodbc  
"""

import pyodbc
import csv
import matplotlib.pyplot as plt

def GetLabelAndValues(graphdata):
    RetList = [] 
    l = graphdata.split("'")
    label = l[1]
    values = l[2]
    RetList.append(label)
    RetList.append(values)
    print(RetList)
    return RetList
    
#===================================
# main
#===================================

print ("try pyodbc...")
database_connect_properties = ['{ODBC Driver 17 for SQL Server}', 'tcp:192.168.5.153,1433', 'pawz', 'PAWZDSN', 'LuapJarusEiddam+1']
connect_str =  'DRIVER=' + database_connect_properties[0] + ';SERVER=' + database_connect_properties[1] + ';DATABASE=' + database_connect_properties[2]+ ';UID=' + database_connect_properties[3]+';PWD='+database_connect_properties[4] 

print (database_connect_properties)
print(connect_str)

conn = pyodbc.connect(connect_str) 
cursor = conn.cursor()
cursor.execute("SELECT * FROM nodepolicy")
rs = cursor.fetchall()

for row in rs:
    print (f'row  = {row[1]}')
    print(f"row = {row}")

#with open ("new.csv", "w") as file:
#    for row in rs:
#        csv.writer(file).writerow(row)

cursor.close()
del cursor


cursor1 = conn.cursor()
cursor1.execute("SELECT max(timeid) from time")
rs = cursor1.fetchall()
for row in rs:
    print (f'maxtimeid  = {row}')
    timeid =int(row[0])
    print('timeid as int = {timeid}')
    cursor2 = conn.cursor()
    sql = f'select * from graphdata where timeid = {timeid} and graphid=110'
    cursor2.execute(sql)
    rs2=cursor2.fetchall()
    label=""
    values=""
    for r in rs2:
        graphdata = r[8]
        RetList =GetLabelAndValues(graphdata)
    #    print(f"RL label = {RetList[0]}")
    #    print(f"RL values = {RetList[1]}")
        x = RetList[1].replace("HOLE", "0.0")
        seriesdata = x.split(" ")
        ilen = len(seriesdata)
        seriesdata[0] = '0.0'
        seriesdata[1] = '0.0'
        intervals = [val for val in range(0,ilen)]
      #  print(intervals)
      #  print(seriesdata)
       
        graphdata = {
            RetList[0]: seriesdata
        }

        shortintervals = [val for val in range(0,4)]
        shortseries=[1,2,3,4]
        graphdata1 = {
            RetList[0]: shortseries
        }

        print(f" keys = {graphdata.keys()}")
        print(f" values = {graphdata.values()}")

        ig, ax = plt.subplots()
        ax.stackplot(shortintervals, graphdata1.values(), labels=graphdata1.keys())

      #  ax.stackplot(intervals, graphdata.values(), labels=graphdata.keys())
        ax.legend(loc='upper left')
        ax.set_title('title')
        ax.set_xlabel('x label')
        ax.set_ylabel('y label)')
        plt.show()

    cursor2.close()
    del (cursor2)

cursor1.close()
del (cursor1)
conn.close()

print ("Done.")