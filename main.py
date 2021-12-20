from gameObjects import player, server, computerNode, job, jobs
from defaults import dJobs, dServers
import threading
import time
import os
import json



j = jobs.Jobs(jobClass=job.Job, jobs=dJobs.returnDefaultJobs())
servers = dServers.returnDefaultServers()

testing = True
r = True
p = player.Player(name="jack", money=500, hackLvl=1)
curSystemName = "home"
curNodeName = None
def test():
    global t1
    global t2
    global j
    global p
    global curSystemName
    global curNodeName
    global servers
    print("HackingSystem v1.1")
    while True:
        if curNodeName  == None:
            action = input(f'[{curSystemName}~]>')
        else:
            action = input(f'[{curSystemName}{curNodeName}~]>')
        if action == "player -i":
            print(f"INFO: \n${p.money}\nName: {p.name}\nHack Level: {p.hackLvl}")
        if action == "cls" or action == "clear":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("HackingSystem v1.1")
        
        if action.startswith("connect"):
            words = action.split()
            if len(words) == 2:
                ip = words[1]
                if ip == "home":
                    exitServers()
                    curSystemName = ip
                for x in servers:
                    if x.ip == ip:
                        alowed = x.command("access", hackLvl=p.hackLvl)
                        exitServers()
                        if alowed:
                            curSystemName = x.name
            if len(words) == 3:
                for x in servers:
                    if x.ip == words[1]:
                        for y in x.nodes:
                            if y.ip == "/" + words[2]:
                                exitServers()
                                allowed = x.command("access", hackLvl=p.hackLvl)
                                if allowed:
                                    curNodeName = y.ip
                                    curSystemName = x.name
                                    y.onNode = True
        if action == "scan -s":
            for x in servers:
                print("-"*20)
                print(f"Name: {x.name}\nIP:{x.ip}\nHackLvl:{x.hackLvl}\nWorking:{x.working}")
                print()
        
        if action == "scan -n":
            if curSystemName != "home":
                for x in servers:
                    if x.name == curSystemName:
                        for y in x.nodes:
                            print("-"*20)
                            print(f'Name:{y.name}\nPort:{y.ip}\nHackLvl:{y.hackLvl}\nHacked:{y.hacked}')
                            print()

        if action.startswith("rob -n"):
            mode = action.split()[2]
            for x in servers:
                if x.name == curSystemName:
                    for y in x.nodes:
                        if y.ip == curNodeName:
                            if mode == "-h":
                                p.hackLvl = y.hackForHackLvl(p.hackLvl)
                            else:
                                p.money += y.hackForMoney(p.hackLvl)
        
        if action.startswith("rob -s"):
            mode = action.split()[2]
            for x in servers:
                if x.name == curSystemName:
                    if mode == "-m":
                        preMoney = p.money
                        p.money += x.command("rob-m", hackLvl=p.hackLvl)
                        print(f"You Stole ${p.money - preMoney} but crashed the server")
                        exitServers()
                    else:
                        preHPoints = p.hackLvl
                        p.hackLvl += x.command("rob-h", hackLvl=p.hackLvl)
                        print(f'You Gained {p.hackLvl-preHPoints} Hack Skill Points but crashed the server')
                        exitServers()

        if action.startswith("create -s"):
            serverName = action.split()[2]
            serverIp = action.split()[3]
            if p.money >= 500:
                p.createServer(name = serverName, ip = serverIp, customers=1)
                p.money -= 500

        if action.startswith('scan') and "-s" in action and "-p" in action:
            for x in p.servers:
                print('-'*20)
                print(f'Name:{x.name}\nIP:{x.ip}\nCustomers:{x.customers}')
                print()

        
        if action == "job -s":
            for x in j.returnJobs():
                print("-"*20)
                print(f'Name:{x["name"]}\nPay/s:{x["pay"]}\nHack Lvl to Apply:{x["hackLvl"]}\nHackLvl/s:{x["hackLvlUp"]}')
                print()

        if action.startswith("job -a"):
            jobName = action.split()[2]
            print(j.applyForJob(jobName, p.hackLvl))
        
        if action == "job -c":
            for x in j.returnEmployedJobs():
                print("-"*20)
                print(f'Name:{x["name"]}\nPay/s:{x["pay"]}\nHackLvl/s:{x["hackLvlUp"]}')
                print()

        if action.startswith("save"):
            saveName = action.split()[1]
            with open("player.json", "r") as f:
                playerData = json.load(f)
            with open("jobs.json", "r") as f:
                jobsData = json.load(f)
            with open("servers.json", "r") as f:
                serversData = json.load(f)
            with open("player.json", "w") as f:
                playerData.update({saveName:p.exportJson()})
                json.dump(playerData, f)  
            with open("jobs.json", "w") as f:
                jobsData.update({saveName:j.exportJson()})
                json.dump(jobsData, f)
            with open("servers.json", "w") as f:
                serverList =  []
                for x in servers:
                    serverList.append(x.exportJson()) 
                serversData.update({saveName:serverList})
                json.dump(serversData, f)
        
        if action.startswith("open"):
            saveName = action.split()[1]
            with open("player.json", "r") as f:
                playerData = json.load(f)
            with open("jobs.json", "r") as f:
                jobsData = json.load(f)
            with open("servers.json", "r") as f:
                serversData = json.load(f)
            
            p = player.Player(json=playerData[saveName])
            j = jobs.Jobs(json=jobsData[saveName], jobClass=job.Job)
            servers = []
            for x in serversData[saveName]:
                servers.append(server.Server(nodeClass=computerNode.ComputerNode, json=x))
            

        
        

def exitServers():
    global curNodeName
    global curSystemName
    curNodeName = None
    curSystemName = "home"
    for x in servers:
        x.onServer = False
        for y in x.nodes:
            y.onNode = False

def run():
    while True:
        pass
def payClock():
    global p
    while True:
        time.sleep(1)
        for x in j.returnEmployedJobs():
            if x["employed"] == True:
               p.money += x["pay"]
               p.hackLvl = round(x["hackLvlUp"] + p.hackLvl, 4)
        
def playerServerClock():
    global p
    while True:
        time.sleep(5)
        for x in p.servers:
            x.customers += 1
            p.money += x.calcMoneyAmo()

if __name__ == "__main__":
    if r == True:
        if testing == False:
            t1=threading.Thread(target=run)
            t2=threading.Thread(target=payClock)
            t3 =threading.Thread(target=playerServerClock)
            t1.start()
            t2.start()
            t3.start()
        else:
            t1=threading.Thread(target=test)
            t2=threading.Thread(target=payClock)
            t3 =threading.Thread(target=playerServerClock)
            t1.start()
            t2.start()
            t3.start()
    
