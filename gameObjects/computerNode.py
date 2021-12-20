import random
class ComputerNode:
	def __init__(self, **kwargs):
		self.makeDefaultVars()

		if "json" in kwargs:
			self.parseJson(kwargs["json"])

		if "name" in kwargs:
			self.name = kwargs["name"]
		if "ip" in kwargs:
			self.ip = kwargs["ip"]
		if "hacked" in kwargs:
			self.hacked = kwargs

		if "hackLvl" in kwargs:
			self.hackLvl = kwargs["hackLvl"]

	def parseJson(self, json):
		if "name" in json:
			self.name = json["name"]
		if "ip" in json:
			self.ip = json["ip"]
		if "hacked" in json:
			self.hacked = json
		if "hackLvl" in json:
			self.hackLvl = json["hackLvl"]
	
	def exportJson(self):
		return {"name":self.name, "ip":self.ip, "hacked":self.hacked, "hackLvl":self.hackLvl}

	def makeDefaultVars(self):
		self.name = "Laptop#1"
		self.ip="/8080"
		self.hacked = False
		self.hackLvl = 1
		self.onNode = False

	def hackForHackLvl(self, hackLvl):
		if not self.hacked and self.onNode:
			if hackLvl >= self.hackLvl:
				self.hacked = True
				return hackLvl + 0.3 * self.hackLvl

	def hackForMoney(self, hackLvl):
		if not self.hacked and self.onNode:
			if hackLvl >= self.hackLvl:
				self.hacked = True

				
				return round(random.random() * hackLvl * self.hackLvl * 5, 0)

	