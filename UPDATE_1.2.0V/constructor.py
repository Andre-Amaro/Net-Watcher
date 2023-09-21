from handle import  Update_files

class constructor():
    
    def __init__(self):
        self.URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQ39yLOYP5IUtaCky0lRlNttc7cJw9SYXqegdExF12Tn0ItSM1RwX3kwCO9XMZQX-thkYPrSUZn5DUB/pub?gid=2084143333&single=true&output=csv"
        self.data = Update_files()
        self.OLT = self.data.dict_maker(controler=self.URL,key=3,value=4)
        self.USERS = self.data.dict_maker(controler=self.URL,key=3,value=6)
        self.PASS = self.data.dict_maker(controler=self.URL,key=3,value=7)
        self.MODEL = self.data.dict_maker(controler=self.URL,key=3,value=5)
        self.PROTOCOL = self.data.dict_maker(controler=self.URL,key=3,value=8)
        self.TYPE = self.data.dict_maker(controler=self.URL,key=10,value=11)
        self.CHASSI = self.data.dict_maker(controler=self.URL,key=12,value=13)
        
        self.chassi_name = []
        self.olt_name = []
        self.type_name = []
    
    
     
    def putty_open(self,place):
        self.data.open(self.OLT,place,self.USERS,self.PASS,self.PROTOCOL)

    def olts(self):
        for i in self.OLT:
            self.olt_name.append(i)
        return self.olt_name
    def chassis(self):
        for i in self.CHASSI:
            try:
                if int(i):
                    self.chassi_name.append(str(i).strip(".0"))
            except Exception:
                continue
            
        return self.chassi_name
    
    def comand_controller(self,selected):
        for i in self.MODEL:
            if i == selected: 
                return self.MODEL[i]

    def ip_get(self,selected):
        for i in self.OLT:
            if i == selected:
                return self.OLT[i]
    def type_get(self,typ,model):
        for i in self.TYPE:
            if model == "ZTE":
                if i == typ:
                    return i
            else:
                return self.TYPE[i]
        
    def type_option_menu(self):
        for i in self.TYPE:
            try:
                if type(i) == float:
                    pass
                else:
                    self.type_name.append(i)
            except Exception:
                continue
        return self.type_name