import random
class Server:
	def __init__(self, **kwargs):
		self.makeDefaultVars()
		self.nodeClass = kwargs["nodeClass"]
		if "json" in kwargs:
			self.parseJson(kwargs["json"])
		if "ip" in kwargs:
			self.ip = kwargs["ip"]
		if "name" in kwargs:
			self.name = kwargs["name"]
		if "money" in kwargs:
			self.money = kwargs["money"]
		if "hackLvl" in kwargs:
			self.hackLvl = kwargs["hackLvl"]
		if "moneyMulti" in kwargs:
			self.moneyMulti = kwargs["moneyMulti"]
		if "nodes" in kwargs:
			self.nodes = kwargs["nodes"]

	def parseJson(self, json):
		if "ip" in json:
			self.ip = json["ip"]
		if "name" in json:
			self.name = json["name"]
		if "money" in json:
			self.money = json["money"]
		if "hackLvl" in json:
			self.hackLvl = json["hackLvl"]
		if "moneyMulti" in json:
			self.moneyMulti = json["moneyMulti"]
		if "nodes" in json:
			for x in json["nodes"]:
				self.nodes.append(self.nodeClass(json=x))
	
	def exportJson(self):
		return {
			"name":self.name,
			"money":self.money,
			"hackLvl":self.hackLvl,
			"moneyMulti":self.moneyMulti,
			"nodes":self.exportNodesJson(),
			"ip":self.ip
		}
	
	def exportNodesJson(self):
		nodesList = []
		for x in self.nodes:
			nodesList.append(x.exportJson())
		return nodesList

		

	def makeDefaultVars(self): #makes them and also to look at the func to see all atributes
		self.working = True
		self.onServer = False
		self.commands = self.makeCommands()
		self.access = False
		self.money = 0
		self.hackLvl = 0
		self.name = "test_server"
		self.ip = "1.1.1.1"
		self.moneyMulti = 10
		self.nodes = []
	def makeCommands(self): #makes all commands and also to look at all avilable commands, put a # at the start of command to make it unavilable
		commands = {
			"access":self.gainAccess,
			"exit":self.exit,
			"enter":self.enter,
			"rob-m":self.takeMoney,
			"info":self.returnInfo,
			"rob-h":self.takeHackerPoints
		}
		return commands

	def command(self, command, **kwargs):
		if self.working:
			if command in self.commands:
				if self.commands[command].__code__.co_argcount != 1:
					return self.commands[command](kwargs)
				else:
					return self.commands[command]()

		return None

	def powerUpServer(self):
		if self.access:
			self.working = True
			self.onServer = False

	def gainAccess(self, kwargs):
		if "hackLvl" in kwargs:
			if kwargs["hackLvl"] >= self.hackLvl and self.working:
				self.access = True
				self.onServer = True
		return self.access

	def enter(self):
		if self.access:
			self.onServer = True
		return self.onServer

	def exit(self):
		if self.access:
			self.onServer = False
		return self.onServer == False

	def takeMoney(self, kwargs):
		
		if "hackLvl" in kwargs:
			
			moneyToTake = random.random() * self.moneyMulti * kwargs["hackLvl"]
			moneyToTake = round(moneyToTake, 0)
			if moneyToTake < self.money:
				self.money -= moneyToTake
				self.working = False
				return moneyToTake
			else:
				self.working = False
				return 0
		return 0

	def returnInfo(self):
		info = {
			"ip":self.ip, 
			"name":self.name, 
			"access":self.access,
			"money":self.money, 
			"hackLvl":self.hackLvl, 
			"onServer":self.onServer,
			"working":self.working,
			"commands":self.commands
			}
		return info
	
	def addNode(self, node):
		self.nodes.append(node)
	
	def getNodes(self):
		return self.nodes

	def takeHackerPoints(self, kwargs):

		if "hackLvl" in kwargs:
			pointsToGain = kwargs["hackLvl"] + 1 * self.hackLvl
			self.working = False
			print(pointsToGain)
			return pointsToGain

	
