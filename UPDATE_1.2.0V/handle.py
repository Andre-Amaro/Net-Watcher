import pandas as pd
import subprocess as sp



class Update_files():
    
    def __init__(self):
        self.content = None
        

    def dict_maker(self,controler,key,value):
        self.content = pd.read_csv(controler)
        self.values = str(list(self.content.iloc[:,[value]]))
        self.indexs = str(list(self.content.iloc[:,[key]]))
        self.indexs = self.indexs.strip("[']")
        self.content.set_index(self.indexs,inplace=True)
        
        
        return self.content.to_dict()[self.values.strip("[']")]
    
    def update(self,files):
        try:
            for i in files:
                self.content = pd.read_csv(files[i])
                self.content.to_csv(i, index=False)
        finally:
            print("all Files Updated")

    def open(self,place,local,users,passw):
        
        
        for i in place:
            if i == local:
                self.ip = place[i]
                break        
        for i in users:
            if i == local:
                self.user = users[i]
                break
        for i in passw:
            if i == self.user:
                self.passw = passw[i]
                break
            
        return sp.Popen(f'PuTTY.exe {self.user}@{self.ip} -pw {self.passw}')
        
    def login_handle(self, username,password):
        if username == 'noc' and password == '38302650':
             return True         
        else: return False

                

            