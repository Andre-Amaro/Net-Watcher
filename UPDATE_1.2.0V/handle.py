import pandas as pd
import subprocess as sp
import pyautogui as ui
from window_finder import WindowMgr
import time
import keyboard as kb


class Update_files():
    
    def __init__(self):
        self.content = None
        self.wf = WindowMgr()
        self.lista = []
        

    def dict_maker(self,controler,key,value):
        self.content = pd.read_csv(controler)
        self.values = str(list(self.content.iloc[:,[value]]))
        self.indexs = str(list(self.content.iloc[:,[key]]))
        self.indexs = self.indexs.strip("[']")
        self.content.set_index(self.indexs,inplace=True)
        self.content = self.content
        
        
        return self.content.to_dict()[self.values.strip("[']")]
    def update(self,files):
        try:
            for i in files:
                self.content = pd.read_csv(files[i])
                self.content.to_csv(i, index=False)
        finally:
            print("all Files Updated")

    def open(self,place,local,users,passw,protocol):
        
        
        for i in place:
            if i == local:
                self.ip = place[i]
                break        
        for i in users:
            if i == local:
                self.user = users[i]
                break
        for i in passw:
            if i == local:
                self.passw = passw[i]
                break
            
        for i in protocol:
            if i == local:
                self.protocol = protocol[i]
                break

        if self.protocol:
            sp.Popen(f'PuTTY.exe -telnet {self.ip}')
            time.sleep(0.5)
            ui.write(f"""{self.user}\n""")
            time.sleep(0.5)
            for i in range(len(self.passw)):
                ui.write(f"{self.passw[i]}")
            ui.write("\n")
        else:
            return sp.Popen(f'PuTTY.exe {self.user}@{self.ip} -pw {self.passw}')
      
    def model_change(self,model,equip):
        if equip == "ZTE":
            if model == "INTELBRAS(ZNTS)" or model == "INTELBRAS(ITBS)":
                return "ITBR-110B"
            else:
                return model    
    def login_handle(self, username,password):
        if username == 'noc' and password == '38302650':
             return True         
        else: return False
    
    def vlan_check(self,vlan):
        if vlan == "":
            return "15"
        else:
            return vlan
    
    def search_equip(self,equip,name):
        self.wf.find_window_wildcard(f"{name} - PuTTY")
        self.wf.set_foreground()
        time.sleep(0.5)
        if equip == "ZTE":
            ui.write("""show pon onu uncfg\n""")
        elif equip == "NOVA":
            ui.write("""onu show\n""")
        elif equip == "VELHA":
            ui.write(f"""onu show \n""")
            time.sleep(0.5)
            ui.write("""yes\n""")
        elif equip == "CIANET":
            ui.write("""enable \n configure terminal \n show onu unconfig \n""")

    def slot_search(self,equip,name, gpon,chassi=3):
        
        self.wf.find_window_wildcard(f"{name} - PuTTY")
        self.wf.set_foreground()
        
        
        if equip == "ZTE":
            kb.write(f"show pon power onu-rx gpon_olt-1/{chassi}/{gpon}\n")
            time.sleep(0.5)
            ui.write(" ")
            ui.write(" ")
        elif equip == "CIANET":
            kb.write(f"interface gpon-olt 1/{gpon}\n show onu status\n")
            
    def zte_bridge(self,name,gpon,slot,vlan,typ,sn,description,chassi=3):
       
        self.wf.find_window_wildcard(f"{name} - PuTTY")
        self.wf.set_foreground()
        
        kb.write(f"conf t\n")
        kb.write(f"interface gpon_olt-1/{chassi}/{gpon}\n")
        kb.write(f"onu {slot} type {typ} sn {sn}\n")
        kb.write(f"exit\n")
        kb.write(f"interface gpon_onu-1/{chassi}/{gpon}:{slot}\n")
        kb.write(f"name {description}\n")
        kb.write(f"sn-bind enable sn\n")
        kb.write(f"tcont 4 profile 1G\n")
        kb.write(f"gemport 1 tcont 4\n")
        kb.write(f"exit\n")
        kb.write(f"interface vport-1/{chassi}/{gpon}.{slot}:1\n")
        kb.write(f"service-port 1 user-vlan {vlan} vlan {vlan}\n")
        kb.write(f"exit\n")
        kb.write(f"pon-onu-mng gpon_onu-1/{chassi}/{gpon}:{slot}\n")
        kb.write(f"service 1 gemport 1 vlan {vlan}\n")
        kb.write(f"vlan port eth_0/1 mode tag vlan {vlan}\n")
        kb.write(f"exit\n")
        kb.write(f"exit\n")
        kb.write(f"show pon power attenuation gpon_onu-1/{chassi}/{gpon}:{slot}\n") 
        
        
        
    def zte_pppoe(self,name,gpon,slot,vlan,typ,sn,description,pppoe,pppoe_pass,chassi=3):
  
        self.wf.find_window_wildcard(f"{name} - PuTTY")
        self.wf.set_foreground()
        
        kb.write(f"conf t\n")
        kb.write(f"interface gpon_olt-1/{chassi}/{gpon}\n")
        kb.write(f"onu {slot} type {typ} sn {sn}\n")
        kb.write(f"exit\n")
        kb.write(f"interface gpon_onu-1/{chassi}/{gpon}:{slot}\n")
        kb.write(f"name {description}\n")
        kb.write(f"tcont 4 profile 1G\n")
        kb.write(f"gemport 1 tcont 4\n")
        kb.write(f"exit\n")
        kb.write(f"interface vport-1/{chassi}/{gpon}.{slot}:1\n")
        kb.write(f"service-port 1 user-vlan {vlan} vlan {vlan}\n")
        kb.write(f"exit\n")
        kb.write(f"pon-onu-mng gpon_onu-1/{chassi}/{gpon}:{slot}\n")
        kb.write(f"service 1 gemport 1 vlan {vlan}\n")
        kb.write(f"wan-ip 1 ipv4  mode pppoe username {pppoe} password {pppoe_pass} vlan-profile {vlan} host 1\n")
        kb.write(f"firewall enable level medium anti-hack enable\n")
        kb.write(f"security-mgmt 80 state enable mode forward ingress-type iphost 1 protocol web\n")
        kb.write(f"exit\n")
        kb.write(f"exit\n") 
        kb.write(f"show pon power attenuation gpon_onu-1/{chassi}/{gpon}:{slot}\n") 
        
     

        
    def nova(self,name,gpon,slot,vlan,sn,description,typ):

        self.wf.find_window_wildcard(f"{name} - PuTTY")
        self.wf.set_foreground()
            
        kb.write(f"onu set gpon {gpon} onu {slot} serial-number {typ}{sn} meprof intelbras-default\n")
        time.sleep(0.7)
        kb.write(f"bridge add gpon {gpon} onu {slot} downlink vlan {vlan} tagged eth 1\n")
        time.sleep(1) 
        kb.write(f"onu description add gpon {gpon} onu {slot} text {str(description).replace(' ', '_').upper()}\n")
        kb.write(f"onu status gpon {gpon} onu {slot}\n")
                
    def velha(self,name,gpon,slot,vlan,sn,description,typ):

        self.wf.find_window_wildcard(f"{name} - PuTTY")
        self.wf.set_foreground()

        kb.write(f"onu set 1/{gpon}/{slot} meprof intelbras-110g vendorid ZNTS serno fsan {sn}\n")
        time.sleep(2)
        kb.write(f"create gpon-olt-onu-config 1-1-{gpon}-{slot}/gpononu \n")
        time.sleep(1)
        kb.write(f"set serial-no-vendor-id={typ} \n")
        time.sleep(1)
        kb.write(f"commit gpon-olt-onu-config 1-1-{gpon}-{slot}/gpononu \n")
        time.sleep(1)
        kb.write(f"bridge add 1-1-{gpon}-{slot}/gpononu downlink vlan {vlan} tagged eth 1 \n")
        time.sleep(3)
        kb.write(f'port description add 1-1-{gpon}-{slot} "{description}" \n')
        time.sleep(1)
        kb.write(f"onu inventory 1/{gpon}/{slot} \n")
    
    def cianet(self,name,gpon,slot,vlan,sn,description):
  
        self.wf.find_window_wildcard(f"{name} - PuTTY")
        self.wf.set_foreground()
        
        kb.write(f"onu {slot} type 1porta sn {sn} \n")
        kb.write(f"interface gpon-onu 1/{gpon}:{slot} \n")
        kb.write(f"tcont 1 profile giga	\n")
        kb.write(f"gemport 1 tcont 1 \n")
        kb.write(f"service-port 1 gemport 1 user-vlan untagged vlan-add {vlan} \n")
        kb.write(f"remote service 1 gem 1\n")
        kb.write(f"remote uni eth_1/1 vlan-mode transparent	\n")
        kb.write(f"name {description}\n")
        kb.write(f"show onu power \n")
        time.sleep(1)
        kb.write(f"exit\n")
        kb.write(f"exit\n")
        kb.write(f"write\n")