class Player:
	def __init__(self, **kwargs):
		self.makeDefaultVars()
		if "json" in kwargs:
			self.parseJson(kwargs["json"])
		else:
			if "name" in kwargs:
				self.name = kwargs["name"]
			if "money" in kwargs:
				self.money = kwargs["money"]
			if "hackLvl" in kwargs:
				self.hackLvl = kwargs["hackLvl"]
			if "servers" in kwargs:
				self.servers = kwargs["servers"]
			

	def parseJson(self, json):
		if "name" in json:
			self.name = json["name"]
		if "money" in json:
			self.money = json["money"]
		if "hackLvl" in json:
			self.hackLvl = json["hackLvl"]
		if "servers" in json:
			for server in json["servers"]:
				self.servers.append(PlayerServer(json=server))
		
	def exportJson(self):
		return {"name":self.name, "money":self.money, "hackLvl":self.hackLvl}

	def makeDefaultVars(self):
		self.money = 0
		self.name = "user#80020172"
		self.hackLvl = 0
		self.servers = []

	def createServer(self, **kwargs):
		self.servers.append(PlayerServer(kwargs))

class PlayerServer:
	def __init__(self, kwargs):
		self.setDefaultVars()
		if "name" in kwargs:
			self.name = kwargs["name"]
		if "json" in kwargs:
			self.parseJson(kwargs["json"])
		if "customers" in kwargs:
			self.customers = kwargs["customers"]
		if "ip" in kwargs:
			self.ip = kwargs["ip"]

		
	def setDefaultVars(self):
		self.name = "player-server"
		self.customers = 0
		self.moneyMulti = 5
		self.upgradePrice = 500
		self.moneyMultiUpgrade = 0.01
		self.ip = "2.2.2.2"

	def parseJson(self, json):
		if "name" in json:
			self.name = json["name"]
		if "customers" in json:
			self.customers = json["customers"]
		if "ip" in json:
			self.ip = json["ip"]

	def calcMoneyAmo(self):
		return self.customers * self.moneyMulti

	def upgrade(self):
		self.moneyMulti += self.moneyMultiUpgrade
		return self.upgradePrice

	

