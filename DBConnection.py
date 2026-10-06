import mysql.connector
class DBConnection(object):
	"""docstring for DBConnection"""
	connection=object
	def __init__(self, **args):
		try:
			self.connection = mysql.connector.connect(host=args["Server"], database=args["Database"], user=args["Uid"], password=args["Pwd"])
		except Exception as e:
			raise
		else:
			pass
		finally: 
			pass

	def Select(self, table, columns=[], where={}):
		query = "select " 
		for col in columns:
			if col==columns[-1] or len(columns)==1:
				query += " {}".format(col)
			else:
				query += " {},".format(col)

		query+=" from {}".format(table)

		if len(where)>0:
			query+=" where"

		dic_keys = list(where.keys())
		for ckey,cval in where.items():
			if ckey==dic_keys[0]:
				query+=" {}={}".format(ckey,cval)
			else: 
				query+=" and {}={}".format(ckey,cval) 
		#print(query)
		cursor = self.connection.cursor(dictionary=True) 
		cursor.execute(query)
		result = cursor.fetchall()
		cursor.close()
		return result

	def Exec(self,procName,parameters=()):
		cursor = self.connection.cursor()
		try:
			result = cursor.callproc("add_personel_log",parameters)
			self.connection.commit()
		except mysql.connector.Error as e:
			print(e)
		return result[3]
		 
