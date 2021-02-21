import sqlite3 


conn = sqlite3.connect('uacData')
c = conn.cursor()
t = ('Maharashtra',)
sqlpull = c.execute("SELECT totalInfected,newInfected,deceased,newDeceased FROM cases WHERE region='Maharashtra'")
results = sqlpull.fetchall()
for rows in results:
    print("Total Infected - ", rows[0])
#totalInfected,newInfected,deceased,newDeceased = results
conn.commit()
conn.close()