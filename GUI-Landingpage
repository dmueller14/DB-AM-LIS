import tkinter as tkinter
import tkinter.messagebox
import customtkinter as ctk

ctk.set_appearance_mode("System")  
ctk.set_default_color_theme("blue")

class GUILandingpage(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Rechnungswesen")
        self.geometry("800x600")
        self.resizable(True, True)
        
        # Creating Labels & Entries
        # Heading
        self.heading_label = ctk.CTkLabel(self, text="Willkommen bei der Rechnungsverwaltung", font=("Arial", 24))
        
        # Entrys for searching-parameter
        self.receipt_number_entry = ctk.CTkEntry(self, placeholder_text="Rechnungsnummer")
        self.order_number_entry = ctk.CTkEntry(self, placeholder_text="Auftragsnummer")
        self.name_entry = ctk.CTkEntry(self, placeholder_text="Name")
        self.prename_entry = ctk.CTkEntry(self, placeholder_text="Vorname")
        self.birthdate_entry = ctk.CTkEntry(self, placeholder_text="Geburtsdatum")
        
        # Creating 'search'-button
        self.search_button = ctk.CTkButton(self, text="Suchen")
        
        # Packing the widgets with the .grid()-method
        # Heading
        self.heading_label.grid(row=0, column=1, columnspan=3, pady=10)
        
        # Entrys for searching-parameter
        self.receipt_number_entry.grid(row=1, column=0)
        self.order_number_entry.grid(row=1, column=1)
        self.name_entry.grid(row=1, column=2)
        self.prename_entry.grid(row=1, column=3)
        self.birthdate_entry.grid(row=1, column=4)
        
        # Packing the search-button
        self.search_button.grid(row=3, column=2, pady=10)
        
        # TODO: Implementing the search-function
        def search(self):
            pass
        
if __name__ == "__main__":
    gui = GUILandingpage()
    gui.mainloop()
        