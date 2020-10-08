import pyodbc
import csv


print ("try pyodbc...")
database_connect_properties = ['{ODBC Driver 17 for SQL Server}', 'tcp:192.168.5.151,1433', 'pawz', 'PAWZDSN', 'LuapJarusEiddam+1']
connect_str =  'DRIVER=' + database_connect_properties[0] + ';SERVER=' + database_connect_properties[1] + ';DATABASE=' + database_connect_properties[2]+ ';UID=' + database_connect_properties[3]+';PWD='+database_connect_properties[4] 

print (database_connect_properties)
print(connect_str)

conn = pyodbc.connect(connect_str) 
cursor = conn.cursor()

#cmd_prod_executesp = 'EXECUTE sp_getCurrentScheduler 1'
#cursor.execute(cmd_prod_executesp)
#for row in cursor.fetchall():
#    print ('row  = ' % row)

cursor.execute("SELECT * FROM nodepolicy")
rs = cursor.fetchall()

for row in rs:
    print ( row[1] + " row2: " + row[2])
 #   print ('row  = ' % row[0])


with open ("new.csv", "w") as file:
    for row in rs:
        csv.writer(file).writerow(row)

cursor.close()
del cursor
conn.close()

print ("Done.")