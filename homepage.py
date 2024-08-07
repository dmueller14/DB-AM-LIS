import customtkinter as ctk

# Class for the homepage
class Mainpage(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill="both", expand=True)
        
        # creating the main frame
        self.home_frame = ctk.CTkFrame(self)
        self.home_frame.pack(fill="both", expand=True)
        
        self.heading_label = ctk.CTkLabel(self.home_frame, text="Willkommen bei der Rechnungsverwaltung", font=("Arial", 20))
        self.heading_label.grid(row=0, column=1, columnspan=2, pady=5, sticky= "n")
        
        self.textbox = ctk.CTkTextbox(self.home_frame, font=("Arial", 13), width=800, height=200)
        self.textbox.grid(row=1, column=1, pady=5, padx=5, sticky="n")
        
        self.sidebar_frame = ctk.CTkFrame(self.home_frame, width=150)
        self.sidebar_frame.grid(row=1, column=0, pady=5, sticky="n")
        
        self.textbox.insert("1.0", "Hier können Rechnungen verwaltet werden.\n\n"
                            + "Um Rechnungen hinzuzufügen, müssen auf der Seite 'dat-Dateien öffnen' die entsprechenden .dat-Dateien geöffnet werden.\n\n"
                            + "Hierzu einfach die gewünschte Datei auswählen, diese im entsprechenden Ordner speichern und den Namen der .csv-Datei eingeben.\n\n"
                            + "Die in der .dat-Datei enthaltenen Daten werden dann in die .csv-Datei geschrieben und von Dort in Die Datenbank übertragen.\n\n")
        
        self.show_hp_button = ctk.CTkButton(self.sidebar_frame, text="Startseite", command=lambda: parent.show_page(parent.mainpage))
        self.show_hp_button.grid(row=0, column=0, pady=5)
       
        self.show_OPDF_button = ctk.CTkButton(self.sidebar_frame, text="dat-Dateien öffnen", command=lambda: parent.show_page(parent.openPCDATFiles))
        self.show_OPDF_button.grid(row=1, column=0, pady=5)
        
        self.show_LP_button = ctk.CTkButton(self.sidebar_frame, text="Rechnung suchen", command=lambda: parent.show_page(parent.gUILandingpage))
        self.show_LP_button.grid(row=2, column=0, pady=5)
        
        self.show_GCP_button = ctk.CTkButton(self.sidebar_frame, text="Rechnungsdetails", command=lambda: parent.show_page(parent.gUIConfig))
        self.show_GCP_button.grid(row=3, column=0, pady=5)