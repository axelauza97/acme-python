class Parser():
    def __init__(self, content):
        self.content=content
        
    def getData(self):
        name=self.content.split("=")[0]
        days=self.content.split("=")[1].split(",")
        dictDays={}
        dictDays[name]={}
        for day in days:            
            dictDays[name][day[0:2]]={}
            dictDays[name][day[0:2]]=day[2:]
        return dictDays