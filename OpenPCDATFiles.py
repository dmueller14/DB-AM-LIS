import csv
import customtkinter as ctk
from tkinter import filedialog
import json
import pandas as pd
from pymongo import MongoClient
from tkinter import messagebox


# Class for reading .dat-files and write them into .csv-files
class OpenPCDATFiles(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill='both', expand=True)    
  
        # Creating the opening frame
        self.opening_frame = ctk.CTkFrame(self)
        self.opening_frame.pack(fill='both', expand=True)
        
        self.sidebar_frame = ctk.CTkFrame(self.opening_frame, width=150)
        self.sidebar_frame.grid(row=1, rowspan = 7, column=0, pady=5, sticky="n")
        
        self.show_hp_button = ctk.CTkButton(self.sidebar_frame, text="Startseite", command=lambda: parent.show_page(parent.mainpage))
        self.show_hp_button.grid(row=0, column=0, pady=5)
       
        self.show_OPDF_button = ctk.CTkButton(self.sidebar_frame, text="dat-Dateien öffnen", command=lambda: parent.show_page(parent.openPCDATFiles))
        self.show_OPDF_button.grid(row=1, column=0, pady=5)
        
        self.show_LP_button = ctk.CTkButton(self.sidebar_frame, text="Rechnung suchen", command=lambda: parent.show_page(parent.gUILandingpage))
        self.show_LP_button.grid(row=2, column=0, pady=5)
        
        self.show_GCP_button = ctk.CTkButton(self.sidebar_frame, text="Rechnungsdetails", command=lambda: parent.show_page(parent.gUIConfig))
        self.show_GCP_button.grid(row=3, column=0, pady=5)
            
        # Creating Labels, Entries and Buttons
        self.heading_label = ctk.CTkLabel(self.opening_frame, text='dat-Dateien öffnen', font=('Arial', 20))
        self.heading_label.grid(row=0, column=2, columnspan=4, pady=15, sticky='n')
        
        self.dat_file_label = ctk.CTkLabel(self.opening_frame, text='Öffne die gewünschte .dat-Datei:', font=('Arial', 14))
        self.dat_file_label.grid(row=1, column=2, columnspan=4, padx=15)
        
        self.dat_file_entry = ctk.CTkEntry(self.opening_frame, placeholder_text='Dateipfad')
        self.dat_file_entry.grid(row=1, column=6, padx=15, sticky='e')
        
        self.open_dat_file_button = ctk.CTkButton(self.opening_frame, text='Öffnen', command=self.open_dat_file)
        self.open_dat_file_button.grid(row=2, column=6, padx=15, sticky='e')
        
        self.choose_folder_label = ctk.CTkLabel(self.opening_frame, text='Wähle den Speicherort', font=('Arial', 14))
        self.choose_folder_label.grid(row=3, column=2, columnspan=4, padx=15)
        
        self.folder_entry = ctk.CTkEntry(self.opening_frame, placeholder_text='Speicherort')
        self.folder_entry.grid(row=3, column=6, padx=15, sticky='e')
        
        self.choose_folder_button = ctk.CTkButton(self.opening_frame, text='Wähle Ordner', command=self.choose_folder)
        self.choose_folder_button.grid(row=4, column=6, padx=15, sticky='e')
        
        self.csv_name_label = ctk.CTkLabel(self.opening_frame, text='Geben Sie den Namen der .csv-Datei ein', font=('Arial', 14))
        self.csv_name_label.grid(row=5, column=2, columnspan=4, padx=15)
        
        self.csv_name_entry = ctk.CTkEntry(self.opening_frame, placeholder_text='Dateiname')
        self.csv_name_entry.grid(row=5, column=6, padx=15, sticky='e')
        
        self.save_csv_button = ctk.CTkButton(self.opening_frame, text='Speichern', command=self.save_csv)
        self.save_csv_button.grid(row=6, column=6, padx=15, sticky='e')
        
  
    # Method for opening the .dat-file    
    def open_dat_file(self):
        self.dat_file_entry.delete(0, 'end')
        self.dat_file_entry.insert(0, filedialog.askopenfilename())
    
    # Method for choosing the folder for the .csv-file
    def choose_folder(self):
        self.folder_entry.delete(0, 'end')
        self.folder_entry.insert(0, filedialog.askdirectory())
        
    # Method for saving the .csv-file
    def save_csv(self):
        dat_file = self.dat_file_entry.get()
        csv_file = self.folder_entry.get()
        csv_name = self.csv_name_entry.get()
        
        if not csv_name.endswith('.csv'):
            csv_name += '.csv'
        
        csv_file = csv_file + '/' + csv_name
        
        with open(dat_file, 'r') as dat_file:
            dat_reader = csv.reader(dat_file, delimiter=';')
            with open(csv_file, 'w', newline='') as csv_file:
                csv_writer = csv.writer(csv_file, delimiter=';')
                for row in dat_reader:
                    csv_writer.writerow(row)
    
    # Method for saving the data to the MongoDB
    def save_to_mongo(self):
        dat_file_path = self.dat_file_entry.get()
        
        # read the .dat-file as a pandas dataframe
        df = pd.read_csv(dat_file_path, delimiter=';')
        
        # add additional keys with null values to be updated later by the user
        additional_keys = {
            'new_RE.Name': None,
            'new_RE.Vorname': None,
            'new_RE.Strasse': None,
            'new_RE.Postleitzahl_Ort': None,
            'new_RE.Telefon': None,
            'new_RE.Email': None,
            'new_RE.Mobile': None,
        }        
        
        for key in additional_keys():
            df[key] = additional_keys[key]
        
        # convert the dataframe to JSON
        json_data = json.loads(df.to_json(orient='records'))
        
        # connect to the MongoDB
        client = MongoClient('localhost', 27017)
        db = client['accountantdb']
        collection = db['patients']
        
        # insert the JSON-data into the MongoDB
        collection.insert_many(json_data)
        
    # Method for updating data in the MongoDB
    def update_in_mongo(self):
        dat_file_path =self.dat_file_entry
        
        # Read the .dat-file as a pandas dataframe
        df = pd.read_csv(dat_file_path, delimiter=';')
        
        # Connect to MongoDB
        client = MongoClient('localhost', 27017)
        db = client['accountantdb']
        collection = db['patients']
        
        for _, row in df.iterrows():
            filter_query = {'Rechnungs-Nr': row['Rechnungs-Nr']} # setting 'Rechnungs-Nr' as identifier
            update_query ={
                '$set':{
                    'new_RE.Vorname': row.get('new_RE.Vorname', None),
                    'new_RE.Name': row.get('new_RE.Name', None),
                    'new_RE.Strasse': row.get('new_RE.Strasse', None),
                    'new_RE.Postleitzahl_Ort': row.get('new_RE.Postleitzahl_Ort', None),
                    'phone_number': row.get('new_RE.Telefon', None),
                    'email': row.get('new_RE.Email', None),
                    'mobile': row.get('new_RE.Mobile', None),
                }
            }
            
            # Update the data in the MongoDB
            collection.update_one(filter_query, update_query, upsert = True)
            messagebox.showinfo('Update', 'Daten erfolgreich aktualisiert')
            
    