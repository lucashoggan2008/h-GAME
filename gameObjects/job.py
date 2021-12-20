class Job:
    def __init__(self, **kwargs):
        self.setDefaultAttrs()
        if "json" in kwargs:
            self.parseJson(kwargs["json"])
        if "name" in kwargs:
            self.name = kwargs["name"]
        if "pay" in kwargs:
            self.pay = kwargs["pay"]
        if "hackLvl" in kwargs:
            self.hackLvl = kwargs["hackLvl"]
        if "hackLvlUp" in kwargs:
            self.hackLvlUp = kwargs["hackLvlUp"]

    def parseJson(self, json):
        if "name" in json:
            self.name = json["name"]
        if "pay" in json:
            self.pay = json["pay"]
        if "hackLvl" in json:
            self.hackLvl = json["hackLvl"]
        if "hackLvlUp" in json:
            self.hackLvlUp = json["hackLvlUp"]  
        if "employed" in json:
            self.employed = json["employed"] 
    
    def setDefaultAttrs(self):
        self.employed = False
        self.name = "test"
        self.pay = 2
        self.hackLvl = 1
        self.hackLvlUp = 0.001

    def exportJson(self):
        return {"name":self.name, "pay":self.pay, "hackLvl":self.hackLvl, "hackLvlUp":self.hackLvlUp, "employed":self.employed}

