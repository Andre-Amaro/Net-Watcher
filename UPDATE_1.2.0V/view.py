from constructor import constructor
import customtkinter as ctk
from handle import Update_files
from PIL import Image
import os
import datetime

class window():

    def __init__(self):
       self.handle = Update_files()
       self.places = constructor()
       
    '''set theme'''
    def time_date(self):
        self.time = datetime.datetime.now()
        self.ftime = self.time.strftime("%H:%M:%S")
        self.date = datetime.date.today()
        self.fdate = self.date.strftime("%B %d, %Y")
        
        self.date_time = (f"{self.fdate}\n\n{self.ftime}")
        
        self.home_time.configure(text=self.date_time)
        self.home_time.after(1000,self.time_date)
        
    def login(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")


        '''Initialize the main screen settings'''
        self.root = ctk.CTk()
        self.root.geometry('350x197')  # screen size
        self.root.title("Provisionamento")  # screen title
        # root.iconbitmap('Prov/img/rikka.ico')  #screen icon
        self.root.eval('tk::PlaceWindow . center')  # make window center
        self.root.resizable(False,False)  # make window not resizable


        '''Username entry section'''

        # Show Username entry css
        self.user = ctk.CTkEntry(self.root,
                            placeholder_text='Username',
                            corner_radius=25,
                            fg_color='#ffffff',
                            text_color='#000000',
                            width=200                    
                            )
        # Place the username entry
        self.user.pack_configure(pady=20
                            )

        '''Password entry section'''

        # Show Password entry css
        self.password = ctk.CTkEntry(self.root,
                                placeholder_text='Password',
                                corner_radius=25,
                                fg_color='#ffffff',
                                text_color='#000000',
                                width=200,
                                show='*'  # hide the password character
                                )
        # Place the password entry
        self.password.pack_configure(pady=5,
                                side='top'
                                )


        '''Login button section'''

        # Show login name on screen CSS
        self.login_button = ctk.CTkButton(self.root,
                            text='Login',
                            corner_radius=50,
                            width=200,
                            height=30,
                            font=('arial',15),
                            command=self.user_pass_get
                            )
                            
        # Place the login
        self.login_button.pack_configure(pady=20,
                            side='bottom'
                            )
        self.root.mainloop()
    
    def main_screen(self):
        
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "IMG")
        self.home_image = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "home_light.png")),size=(20,20))
        self.add_image = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "add_user_light.png")),size=(20,20))
        self.logo_image = ctk.CTkImage(Image.open(os.path.join(image_path, "logo.png")), size=(240,150 ))
        
        self.main_root = ctk.CTk()
        self.main_root.geometry('650x400')  # screen size
        self.main_root.title("Net Vale")  # screen title
        # root.iconbitmap('Prov/img/rikka.ico')  #screen icon
        self.main_root.eval('tk::PlaceWindow . center')  # make window center
        self.main_root.resizable(False,False)  # make window not resizable
        
        self.main_root.grid_rowconfigure(0, weight=1)
        self.main_root.grid_columnconfigure(1, weight=1)
        

        self.navigation_frame = ctk.CTkFrame(self.main_root,corner_radius=0)
        self.navigation_frame.grid(row=0, column=0,sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4,weight=1)
        
        self.navigation_label = ctk.CTkLabel(self.navigation_frame, 
                                             text="Welcome\nNoc Net Vale",
                                             compound="left",
                                             font=ctk.CTkFont(size=15,weight="bold"))
        self.navigation_label.grid(row=0,column=0, padx=20,pady=20)
        
        self.home_button = ctk.CTkButton(self.navigation_frame,
                                         corner_radius=0,
                                         height=40,
                                         border_spacing=10,
                                         text='Home',
                                         fg_color="transparent",
                                         text_color=("gray10","gray90"),
                                         hover_color=("gray70","gray30"),
                                         anchor="w",
                                         image=self.home_image,
                                         command=self.home_button_event)
        self.home_button.grid(row=1,column=0,sticky="ew")
        
        self.add_button = ctk.CTkButton(self.navigation_frame,
                                         corner_radius=0,
                                         height=40,
                                         border_spacing=10,
                                         text='Provisionar',
                                         fg_color="transparent",
                                         text_color=("gray10","gray90"),
                                         hover_color=("gray70","gray30"),
                                         anchor="w",
                                         image=self.add_image,
                                         command=self.provisionar_button_event)
        self.add_button.grid(row=2,column=0,sticky="ew")        
        
        self.home_frame = ctk.CTkFrame(self.main_root,corner_radius=0,fg_color="transparent")
        self.home_frame.grid_columnconfigure(0,weight=1) 
        
        self.home_time = ctk.CTkLabel(self.home_frame,
                                      font=ctk.CTkFont(size=45,weight="bold"))
        self.home_time.grid(row=0,column=0,padx=20,pady=20)
        self.time_date()
        self.home_logo = ctk.CTkLabel(self.home_frame,image=self.logo_image,text="")
        self.home_logo.grid(row=1,column=0,padx=20,pady=20)
        
        
        self.provisionar_frame = ctk.CTkFrame(self.main_root,corner_radius=0,fg_color="transparent")
        self.provisionar_frame.grid_columnconfigure(0,weight=1)
        
        self.olt = ctk.CTkOptionMenu(self.provisionar_frame,
                                     width=120,
                                     height=40,
                                     corner_radius=0,
                                     values = self.places.olts()
                                     )
        self.olt.grid(row=0,column=0,columnspan=2,padx=20,pady=20)
        
        self.sn_entry = ctk.CTkEntry(self.provisionar_frame,
                                     width=120,
                                     height=40,
                                     corner_radius=0,
                                     placeholder_text="TPLGBb4b5b32"
                                     )
        self.sn_entry.grid(row=1,column=0,padx=20,pady=20)
        
        self.gpon_entry = ctk.CTkEntry(self.provisionar_frame,
                                            width=55,
                                            height=40,
                                            corner_radius=0,
                                            placeholder_text="Gpon")
        self.gpon_entry.grid(row=1,column=1,padx=10,pady=20,sticky="w")
        
        self.onu_entry = ctk.CTkEntry(self.provisionar_frame,
                                            width=55,
                                            height=40,
                                            corner_radius=0,
                                            placeholder_text="Onu")
        self.onu_entry.grid(row=1,column=1,padx=10,pady=20,sticky="e")
        
        self.chassi_option = ctk.CTkOptionMenu(self.provisionar_frame,
                                              width=120,
                                              height=40,
                                              corner_radius=0,
                                              values= self.places.chassis())
        self.chassi_option.grid(row=1,column=2,padx=20,pady=20)
        

        
        self.description_entry = ctk.CTkEntry(self.provisionar_frame,
                                     width=120,
                                     height=40,
                                     corner_radius=0,
                                     placeholder_text="João e maria Cx25-P3"
                                     )
        self.description_entry.grid(row=2,column=0,padx=20,pady=20)
        
        self.type_option = ctk.CTkOptionMenu(self.provisionar_frame,
                                            width=120,
                                            height=40,
                                            corner_radius=0,
                                            values = self.places.type_option_menu(),
                                            dynamic_resizing=False
                                            )
        self.type_option.grid(row=2,column=2,padx=20,pady=20)
        
        self.type_option.set("Modelo")
        self.chassi_option.set("Chassi")
        self.olt.set("Regiões")
        
        self.vlan_entry = ctk.CTkEntry(self.provisionar_frame,
                                     width=70,
                                     height=40,
                                     corner_radius=0,
                                     placeholder_text="15"
                                     )
        self.vlan_entry.grid(row=2,column=1,padx=20,pady=20)
        
        self.pppoe_entry = ctk.CTkEntry (self.provisionar_frame,
                                         width=120,
                                         height=40,
                                         corner_radius=0,
                                         placeholder_text="cliente@netvale.psi.br"
                                         )
        self.pppoe_entry.grid(row=3,column=0,columnspan=2,padx=20,pady=20)
        
        self.pppoe_pass_entry = ctk.CTkEntry (self.provisionar_frame,
                                         width=120,
                                         height=40,
                                         corner_radius=0,
                                         placeholder_text="cliente123"
                                         )
        self.pppoe_pass_entry.grid(row=3,column=1,columnspan=2,padx=20,pady=20)
        
        self.prov_button = ctk.CTkButton(self.provisionar_frame,
                                           width=120,
                                           height=40,
                                           text="Provisionar",
                                           corner_radius=0,
                                           command=self.prov_event)
        self.prov_button.grid(row=5,column=2,pady=20,padx=20)
        
        self.slot_button = ctk.CTkButton(self.provisionar_frame,
                                         width=120,
                                         height=40,
                                         corner_radius=0,
                                         text="Slots",
                                         command=self.slots_button_event)
        self.slot_button.grid(row=5,column=1,padx=20,pady=20)
        
        self.search_button = ctk.CTkButton(self.provisionar_frame,
                                           width=120,
                                           height=40,
                                           text="Search",
                                           corner_radius=0,
                                           command=self.search_button_event)
        self.search_button.grid(row=5,column=0,pady=20,padx=20)
        
        self.olt_button = ctk.CTkButton(self.provisionar_frame,
                                        text="Open",
                                        corner_radius=0,
                                        height=40,
                                        width=120,
                                        command=self.open_button_event                              
                                        )
        self.olt_button.grid(row=0,column=1,columnspan=2,padx=20,pady=20)
        
 
        self.home_button.invoke()       
        self.main_root.mainloop()
            
        
    def user_pass_get(self):
        
        autentication = self.handle.login_handle(self.user.get(),self.password.get())
        if autentication:
            self.root.destroy()
            self.main_screen()
        else:
            try:
                
                notification = ctk.CTkInputDialog(text="Username or password incorrect",
                                                title="Login Failed",
                                                )
            finally:
                ...
    def select_frame_by_name(self, name):
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "Home" else "transparent")
        self.add_button.configure(fg_color=("gray25", "gray25") if name == "Provisionar" else "transparent")
        
        if name == "Home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        
        if name == "Provisionar":
            self.provisionar_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.provisionar_frame.grid_forget()
            
    def home_button_event(self):
        self.select_frame_by_name("Home")
        
    def provisionar_button_event(self):
        self.select_frame_by_name("Provisionar")
        
    def open_button_event(self):
        self.places.putty_open(str(self.olt.get()))
        
    def search_button_event(self):
        try:
            self.handle.search_equip(self.places.comand_controller(str(self.olt.get())),
                                    self.places.ip_get(str(self.olt.get())))
        except Exception:
            notification = ctk.CTkInputDialog(text="OLT not opened",
                                                title="Fail to write",
                                                )
    def slots_button_event(self):
        self.handle.slot_search(name=self.places.ip_get(str(self.olt.get())),
                                equip=self.places.comand_controller(str(self.olt.get())),
                                gpon=self.gpon_entry.get(),
                                chassi=str(self.chassi_option.get())
                                )
    def zte_intelbras(self):
       self.itbr = self.handle.model_change(equip=self.places.comand_controller(str(self.olt.get())),
                                 model=self.places.type_get(self.type_option.get(),self.places.comand_controller(str(self.olt.get()))))
       return self.itbr
    def prov_ZTE_BRIDGE(self):
 
            self.handle.zte_bridge(name=self.places.ip_get(str(self.olt.get())),
                                   gpon=self.gpon_entry.get(),
                                   slot=self.onu_entry.get(),
                                   vlan=self.handle.vlan_check(self.vlan_entry.get()),
                                   typ=self.zte_intelbras(),
                                   sn=self.sn_entry.get(),
                                   description=self.description_entry.get(),
                                   chassi=self.chassi_option.get())
            
    def prov_ZTE_PPPOE(self):
        try:
            self.handle.zte_pppoe(name=self.places.ip_get(str(self.olt.get())),
                                   gpon=self.gpon_entry.get(),
                                   slot=self.onu_entry.get(),
                                   vlan=self.handle.vlan_check(self.vlan_entry.get()),
                                   typ=self.zte_intelbras(),
                                   sn=self.sn_entry.get(),
                                   description=self.description_entry.get(),
                                   chassi=self.chassi_option.get(),
                                   pppoe=self.pppoe_entry.get(),
                                   pppoe_pass=self.pppoe_pass_entry.get())
        except Exception:
            notification = ctk.CTkInputDialog(text="information missing",
                                                title="missing information",
                                                )
    def zte_controller(self):
        if self.pppoe_entry.get() == "":
            return self.prov_ZTE_BRIDGE()
        else:
            return self.prov_ZTE_PPPOE()
    def prov_nova(self):
        self.handle.nova(name=self.places.ip_get(str(self.olt.get())),
                        gpon=self.gpon_entry.get(),
                        slot=self.onu_entry.get(),
                        vlan=self.handle.vlan_check(self.vlan_entry.get()),     
                        sn=self.sn_entry.get(),
                        description=self.description_entry.get(),
                        typ=self.places.type_get(self.type_option.get(),self.places.comand_controller(str(self.olt.get()))))
    def prov_velha(self):
        self.handle.velha(name=self.places.ip_get(str(self.olt.get())),
                        gpon=self.gpon_entry.get(),
                        slot=self.onu_entry.get(),
                        vlan=self.handle.vlan_check(self.vlan_entry.get()),     
                        sn=self.sn_entry.get(),
                        description=self.description_entry.get(),
                        typ=self.places.type_get(self.type_option.get(),self.places.comand_controller(str(self.olt.get()))))
    def prov_cianet(self):
        self.handle.cianet(name=self.places.ip_get(str(self.olt.get())),
                        gpon=self.gpon_entry.get(),
                        slot=self.onu_entry.get(),
                        vlan=self.handle.vlan_check(self.vlan_entry.get()),     
                        sn=self.sn_entry.get(),
                        description=self.description_entry.get())
        
    def prov_event(self):
        self._ = self.places.comand_controller(str(self.olt.get()))
        if self._ == "ZTE":
           return self.zte_controller()
        elif self._ =="NOVA":
            return self.prov_nova()
        elif self._ =="VELHA":
            return self.prov_velha()
        elif self._ =="CIANET":
            return self.prov_cianet()
        