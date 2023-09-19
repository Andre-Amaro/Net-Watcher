from handle import  Update_files

class constructor():
    
    def __init__(self):
        self.URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQ39yLOYP5IUtaCky0lRlNttc7cJw9SYXqegdExF12Tn0ItSM1RwX3kwCO9XMZQX-thkYPrSUZn5DUB/pub?gid=2084143333&single=true&output=csv"
        self.data = Update_files()
        self.OLT = self.data.dict_maker(controler=self.URL,key=3,value=4)
        self.USERS = self.data.dict_maker(controler=self.URL,key=3,value=6)
        self.PASS = self.data.dict_maker(controler=self.URL,key=3,value=7)
        self.olt_name = []
    
    def putty_open(self,place):
        self.data.open(self.OLT,place,self.USERS,self.PASS)

    def olts(self):
        for i in self.OLT:
            self.olt_name.append(i)
        return self.olt_name