class Jobs:
    def __init__(self, **kwargs):
        self.jobs = []
        self.jobClass = kwargs["jobClass"]
        if "jobs" in kwargs:
            self.jobs = kwargs["jobs"]
        if "json" in kwargs:
            self.parseJson(kwargs["json"])
    
    def parseJson(self, json):
        for x in json:
            self.jobs.append(self.jobClass(json=x))

    def returnJobs(self):
        jobs = []
        for x in self.jobs:
            jobs.append({"name":x.name, "pay":x.pay, "hackLvl":x.hackLvl, "employed":x.employed, "hackLvlUp":x.hackLvlUp})
        return jobs
    
    def returnEmployedJobs(self):
        jobs = self.returnJobs()
        employedJobs = []
        for x in jobs:
            if x["employed"] == True:
                employedJobs.append(x)
        return employedJobs

    def applyForJob(self, jobName, hackLvl):
        for job in self.jobs:
            if job.name == jobName and job.hackLvl <= hackLvl:
                job.employed = True
                return True
        return False

    def addJob(self, job):
        self.jobs.append(job)

    def exportJson(self):
        jobsList = []
        for x in self.jobs:
            jobsList.append(x.exportJson())
        return jobsList
