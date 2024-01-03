class time:
	def __init__(self,hour=0,minute=0,second=0):
		self.hour=hour
		self.minute=minute
		self.second=second
	
	def add(self,other):	
		total_time=self.hour*3600+self.minute*60+self.second+other	
