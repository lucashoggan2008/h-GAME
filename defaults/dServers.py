from gameObjects import server, computerNode

def returnDefaultServers():
    servers = [
        server.Server(ip="11.2.18.6", name="geegle-server", hackLvl=15, nodes=[
            computerNode.ComputerNode(name="pc:806", ip="/8377", hackLvl=16),
            computerNode.ComputerNode(name="laptop:126", ip="/6013", hackLvl=18),
            computerNode.ComputerNode(name="phone:522", ip="/3078", hackLvl=19),
            computerNode.ComputerNode(name="pc:841", ip="/2181", hackLvl=19),
            computerNode.ComputerNode(name="laptop:703", ip="/7383", hackLvl=20),
        ], nodeClass = computerNode.ComputerNode),
        server.Server(ip="12.13.3.7", name="notflix-server", hackLvl=8, nodes=[
            computerNode.ComputerNode(name="phone:592", ip="/8999", hackLvl=12),
            computerNode.ComputerNode(name="laptop:795", ip="/7564", hackLvl=12),
            computerNode.ComputerNode(name="pc:664", ip="/4396", hackLvl=9),
            computerNode.ComputerNode(name="pc:913", ip="/2858", hackLvl=9),
            computerNode.ComputerNode(name="pc:524", ip="/6480", hackLvl=10),
        ], nodeClass = computerNode.ComputerNode),
        server.Server(ip="14.6.13.9", name="gitdock-server", hackLvl=1, nodes=[
            computerNode.ComputerNode(name="laptop:534", ip="/3205", hackLvl=8),
            computerNode.ComputerNode(name="phone:503", ip="/5680", hackLvl=7),
            computerNode.ComputerNode(name="phone:160", ip="/9536", hackLvl=8),
            computerNode.ComputerNode(name="pc:651", ip="/8076", hackLvl=5),
            computerNode.ComputerNode(name="laptop:223", ip="/5381", hackLvl=14),
        ], nodeClass = computerNode.ComputerNode),
        server.Server(ip="5.8.12.20", name="john-security-server", hackLvl=1, nodes=[
            computerNode.ComputerNode(name="pc:376", ip="/8330", hackLvl=4),
            computerNode.ComputerNode(name="pc:825", ip="/5264", hackLvl=2),
            computerNode.ComputerNode(name="laptop:852", ip="/2237", hackLvl=4),
            computerNode.ComputerNode(name="phone:340", ip="/1485", hackLvl=1),
            computerNode.ComputerNode(name="laptop:762", ip="/2367", hackLvl=2),
        ], nodeClass = computerNode.ComputerNode),
    ]
    return servers