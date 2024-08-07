import tkinter as tkinter
import tkinter.messagebox
import customtkinter as ctk
from pymongo import MongoClient, errors


# Class for the landingpage of the GUI
class GUILandingpage(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill="both", expand=True)
        
        # creating the main frame
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(fill="both", expand=True)

        # Creating Labels & Entriesll
        # Heading
        self.heading_label = ctk.CTkLabel(self.main_frame, text="Willkommen bei der Rechnungsverwaltung", font=("Arial", 20))
        
        self.sidebar_frame = ctk.CTkFrame(self.main_frame, width=150)
        self.sidebar_frame.grid(row=1, column=0, pady=5, sticky="n")
        
        self.show_hp_button = ctk.CTkButton(self.sidebar_frame, text="Startseite", command=lambda: parent.show_page(parent.mainpage))
        self.show_hp_button.grid(row=0, column=0, pady=5)
       
        self.show_OPDF_button = ctk.CTkButton(self.sidebar_frame, text="dat-Dateien öffnen", command=lambda: parent.show_page(parent.openPCDATFiles))
        self.show_OPDF_button.grid(row=1, column=0, pady=5)
        
        self.show_LP_button = ctk.CTkButton(self.sidebar_frame, text="Rechnung suchen", command=lambda: parent.show_page(parent.gUILandingpage))
        self.show_LP_button.grid(row=2, column=0, pady=5)
        
        self.show_GCP_button = ctk.CTkButton(self.sidebar_frame, text="Rechnungsdetails", command=lambda: parent.show_page(parent.gUIConfig))
        self.show_GCP_button.grid(row=3, column=0, pady=5)
        
        # Entrys for searching-parameter
        self.receipt_number_entry = ctk.CTkEntry(self.main_frame, placeholder_text="Rechnungsnummer")
        self.name_entry = ctk.CTkEntry(self.main_frame, placeholder_text="Name")
        self.prename_entry = ctk.CTkEntry(self.main_frame, placeholder_text="Vorname")
        self.birthdate_entry = ctk.CTkEntry(self.main_frame, placeholder_text="Geburtsdatum")
        
        # Creating 'search'-button
        self.search_button = ctk.CTkButton(self.main_frame, text="Suchen")
        
        # Packing the widgets with the .grid()-method
        # Heading
        self.heading_label.grid(row=0, column=2, columnspan=2, pady=10)
        
        # Entrys for searching-parameter
        self.receipt_number_entry.grid(row=1, column=1, padx =10, pady=10)
        self.name_entry.grid(row=1, column=2, padx =10, pady=10) # name and prename are saved in the same value in the json-file
        self.prename_entry.grid(row=1, column=3, padx =10, pady=10)
        self.birthdate_entry.grid(row=1, column=4, padx =10, pady=10)
        
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