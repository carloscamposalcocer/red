import MySQLdb as mysql
import os
def getserial():
  # Extract serial from cpuinfo file
  cpuserial = "0000000000000000"
  try:
    f = open('/proc/cpuinfo','r')
    for line in f:
      if line[0:6]=='Serial':
        cpuserial = line[10:26]
    f.close()
  except:
    cpuserial = "ERROR000000000"

  return cpuserial

def getip():
  # Extract ip
  ip = os.popen("curl icanhazip.com").read().replace("\n","")
  return ip


db = mysql.connect(user='pi', passwd='octogato',host='localhost',db='db')
cur = db.cursor()
raspserial = getserial()
raspip = getip()

Noip = cur.execute('SELECT ip FROM ips WHERE serial = \"' + raspserial + '\" AND ip = \"' + raspip + '\"')
if Noip==0:
	cur.execute('INSERT INTO ips SET serial=\"' + raspserial + '\",date=CURDATE(),ip=\"' + raspip +'\"')
db.commit()
db.close()



