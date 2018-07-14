import MySQLdb

def readrequest():
	try:
		db=MySQLdb.connect("localhost","pi","octogato","db")
		c=db.cursor()
		sql = "SELECT * FROM request WHERE PlantID=0"
		try:
			c.execute(sql)
			data = c.fetchone()
			db.commit()
		except:
			db.rollback()
		db.close()
		return data
	except MySQLdb.OperationalError as e:
		print("OperationalError")
		print(e)
	
	
def readstatus():
	db=MySQLdb.connect("localhost","pi","octogato","db")
	c=db.cursor()
	sql = "SELECT * FROM status WHERE PlantID=0"
	try:
		c.execute(sql)
		data = c.fetchone()
		db.commit()
	except:
		db.rollback()
	db.close()
	return data

def insertrequest(s):
	db=MySQLdb.connect("localhost","pi","octogato","db")
	c=db.cursor()
	sql = "UPDATE request SET %s WHERE PlantID=0" % (s)
	try:
		c.execute(sql)
		db.commit()
	except:
		db.rollback()
	db.close()
	
def insertstatus(s):
	db=MySQLdb.connect("localhost","pi","octogato","db")
	c=db.cursor()
	sql = "UPDATE status SET %s WHERE PlantID=0" % (s)
	try:
		c.execute(sql)
		db.commit()
	except:
		db.rollback()
	db.close()
	
	
if __name__ == "__main__":
    import sys
    insert(sys.argv[1])



