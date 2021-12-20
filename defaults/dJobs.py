
from gameObjects import job

def returnDefaultJobs():
    jobs = [
        job.Job(name="basic-hacker", pay=2, hackLvl=1),
        job.Job(name="basic-pen-tester", pay=4, hackLvl=2, hackLvlUp=0.003),
        job.Job(name="intermediate-hacker", pay=7, hackLvl=4, hackLvlUp=0.01),
        job.Job(name="intermediate-pen-tester", pay=9, hackLvl=5, hackLvlUp=0.012),
        job.Job(name="basic-black-hat-hacker", pay=13, hackLvl=7, hackLvlUp=0.017),
        job.Job(name="pro-hacker", pay=15, hackLvl=9, hackLvlUp=0.02),
        job.Job(name="pro-pen-tester", pay=17, hackLvl=11, hackLvlUp=0.022),
        job.Job(name="pro-black-hat-hacker", pay=20, hackLvl=15, hacklvlUp=0.019),
    ]
    return jobs