import tkinter as tkinter
import tkinter.messagebox
import customtkinter as ctk
from pymongo import MongoClient, errors


ctk.set_appearance_mode("System")  # set appearance mode to system
ctk.set_default_color_theme("blue") # set default color theme to blue

# Class for the landingpage of the GUI
class GUILandingpage(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Rechnungswesen")
        self.geometry("600x500")
        self.resizable(True, True)

        # creating the main frame
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(fill="both", expand=True)

        # Creating Labels & Entries
        # Heading
        self.heading_label = ctk.CTkLabel(self.main_frame, text="Willkommen bei der Rechnungsverwaltung", font=("Arial", 17))
        
        # Entrys for searching-parameter
        self.receipt_number_entry = ctk.CTkEntry(self.main_frame, placeholder_text="Rechnungsnummer")
        self.name_entry = ctk.CTkEntry(self.main_frame, placeholder_text="Name")
        self.prename_entry = ctk.CTkEntry(self.main_frame, placeholder_text="Vorname")
        self.birthdate_entry = ctk.CTkEntry(self.main_frame, placeholder_text="Geburtsdatum")
        
        # Creating 'search'-button
        self.search_button = ctk.CTkButton(self.main_frame, text="Suchen")
        
        # Packing the widgets with the .grid()-method
        # Heading
        self.heading_label.grid(row=0, column=1, columnspan=2, pady=10)
        
        # Entrys for searching-parameter
        self.receipt_number_entry.grid(row=1, column=0)
        self.name_entry.grid(row=1, column=1) # name and prename are saved in the same value in the json-file
        self.prename_entry.grid(row=1, column=2)
        self.birthdate_entry.grid(row=1, column=3)
        
        # Packing the search-button
        self.search_button.grid(row=3, column=1, columnspan=2, pady=10)
        
    # TODO: Implementing the search-function
    def search(self):
        receipt_number = self.receipt_number_entry.get()
        name = self.name_entry.get()
        prename = self.prename_entry.get()
        birthdate = self.birthdate_entry.get()
   
        try:    
            # Connecting to the MongoDB
            client = MongoClient("mongodb://localhost:27017")
            db = client["accountiantdb"]
            collection = db["receipts"]
            
            # build the query
            query = {}
            if receipt_number:
                query["Rechnungs-Nr"] = receipt_number
            # construct a reges query for the name since we want to search for substrings
            if name or prename:
                full_name_query = {}
                if name:
                    full_name_query["$regex"] = name
                if prename:
                    full_name_query["$regex"] = prename
                query['Patient'] = full_name_query
            if birthdate:
                query["Geb.-Datum"] = birthdate
            
            # execute the query    
            results = collection.find(query)
            
            # show the results
            results_count = results.count()
            if results_count > 0:
                result_message = f"Es wurden {results_count} Ergebnisse gefunden."
                for result in results:
                    result_message += f"\nRechnungs-Nr: {result['Rechnungs-Nr']}, Patient: {result['Patient']}, Geb.-Datum: {result['Geb.-Datum']}"
                tkinter.messagebox.showinfo("Suchergebnisse", result_message)
            else:
                tkinter.messagebox.showinfo("Suchergebnisse", "Keine Ergebnisse gefunden.")
        except errors.ConnectionError:
            tkinter.messagebox.showerror("Fehler", "Verbindung zur Datenbank konnte nicht hergestellt werden.")
        except errors.PymongoError as e:
            tkinter.messagebox.showerror("Fehler", "Fehler beim Zugriff auf die Datenbank.")
        
        
if __name__ == "__main__":
    gui = GUILandingpage()
    gui.mainloop()
        