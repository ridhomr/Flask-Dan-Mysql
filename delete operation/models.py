import pymysql
import config

db = cursor = None

class bukutelp:
	def __init__ (self, no=None, nama=None, no_telp=None):
			self.no = no
			self.nama = nama
			self.no_telp = no_telp

	def openDB(self):
			global db, cursor
			db = pymysql.connect(
					config.DB_HOST,
					config.DB_USER,
					config.DB_PASSWORD,
					config.DB_NAME)
			cursor = db.cursor()

	def closeDB(self):
			global db, cursor
			db.close()

	def selectDB(self):
			self.openDB()
			cursor.execute("SELECT * FROM bukutelp")
			container = []
			for no,nama,no_telp in cursor.fetchall():
				container.append((no,nama,no_telp))
			self.closeDB()
			return container

	def insertDB(self, data):
            self.openDB()
            cursor.execute("INSERT INTO bukutelp (nama,no_telp) VALUES('%s','%s')" % data)
            db.commit()
            self.closeDB()

	def getDBbyNo(self, no):
            self.openDB()
            cursor.execute("SELECT * FROM bukutelp WHERE no='%s'" % no)
            data = cursor.fetchone()
            return data

	def updateDB(self, data):
            self.openDB()
            cursor.execute("UPDATE bukutelp SET nama='%s', no_telp='%s' where no=%s" % data)
            db.commit()
            self.closeDB()

	def deleteDB(self, no):
		self.openDB()
		cursor.execute("DELETE FROM bukutelp WHERE no=%s" % no)
		db.commit()
		self.closeDB()
