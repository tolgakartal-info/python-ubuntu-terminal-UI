import DBConnection as db
import datetime as dt
class CheckPersonel(object):
	"""docstring for CheckPersonel"""
	def __init__(self,personelId,password,direction):
		super(CheckPersonel, self).__init__()
		self.personelId = personelId
		self.password = password
		self.direction = direction
		self.proc_result=''
	
	def CheckResult(self):
		con = db.DBConnection(Server="127.0.0.1",Database="terminal",Uid="phpmyadmin", Pwd="880739")
		rows = con.Select("personel",["id","password"],{"id":self.personelId,"password":self.password})
		if len(rows)>0:
			parameters = (self.personelId,dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),self.direction,self.proc_result)
			r = con.Exec("add_personel_log",parameters)
			return True,r
		else:
			return False,r
			
		
