# from constructor import constructor
import customtkinter as ctk
from handle import Update_files
from PIL import Image
import os
import datetime

class window():

    def __init__(self):
       self.handle = Update_files()
       
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
        self.logo_image = ctk.CTkImage(Image.open(os.path.join(image_path, "logo.png")), size=(340,200 ))
        
        self.main_root = ctk.CTk()
        self.main_root.geometry('700x450')  # screen size
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
                                         image=self.add_image)
        self.add_button.grid(row=2,column=0,sticky="ew")        
        
        self.home_frame = ctk.CTkFrame(self.main_root,corner_radius=0,fg_color="transparent")
        self.home_frame.grid_columnconfigure(0,weight=1) 
        
        self.home_time = ctk.CTkLabel(self.home_frame,
                                      font=ctk.CTkFont(size=45,weight="bold"))
        self.home_time.grid(row=0,column=0,padx=20,pady=20)
        self.time_date()
        self.home_logo = ctk.CTkLabel(self.home_frame,image=self.logo_image,text="")
        self.home_logo.grid(row=1,column=0,padx=20,pady=20)
        
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
        
        if name == "Home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
            
    def home_button_event(self):
        self.select_frame_by_name("Home")