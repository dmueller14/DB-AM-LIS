import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from homepage import Mainpage
from GUILandingpage import GUILandingpage
from GUIConfig import GUIConfig
from OpenPCDATFiles import OpenPCDATFiles

ctk.set_appearance_mode("System")  # set appearance mode to system
ctk.set_default_color_theme("blue") # set default color theme to blue

# Class for the main application
class Main(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title('Rechnungswesen')
        self.geometry('1000x1000')
        self.resizable(True, True)
        
        # Create and place pages
        self.mainpage = Mainpage(self)
        self.gUILandingpage = GUILandingpage(self)
        self.gUIConfig = GUIConfig(self)
        self.openPCDATFiles = OpenPCDATFiles(self)
    
        #self.mainpage.pack(fill="both", expand=True)
        
        self.show_page(self.mainpage)
        
    def show_page(self, page):
        self.mainpage.pack_forget()
        self.gUILandingpage.pack_forget()
        self.gUIConfig.pack_forget()
        self.openPCDATFiles.pack_forget()
        page.pack(fill="both", expand=True)
        
if __name__ == "__main__":
    app = Main()
    app.mainloop()