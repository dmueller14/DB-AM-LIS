import tkinter as tk
import tkinter.messagebox
import customtkinter as ctk
from pymongo import MongoClient, errors

ctk.set_appearance_mode("System")  
ctk.set_default_color_theme("blue")  

class GUIConfig(ctk.CTk):
    def __init__(self, master=None):
        super().__init__()

        self.title("GUI-Config")
        self.geometry("800x800")
        self.resizable(True, True)
        
        # Creating the tabview_frame
        self.tabview_frame = ctk.CTkFrame(self)
        self.tabview_frame.pack(fill="both", expand=True)
        
        # Creating the tabview
        self.tabview = ctk.CTkTabview(self.tabview_frame, width=800, height=800)
        self.tabview.grid(row=0, column=0, padx=10, pady=10)
        
        # adding tabs to the tabview
        self.tabview.add('Patient')
        self.tabview.add('Empfänger')
        self.tabview.add('Rechnung')
        self.tabview.add('Einsender')
        self.tabview.add('Kommentar')
        
        self._create_patient_tab()
        self._create_receiver_tab()
        self._create_receipt_tab()
        self._create_submitter_tab()
        self._create_comment_tab()
        
    # Function for creating the patient-tab    
    def _create_patient_tab(self):
        # Label-Widgets
        self.name_label = ctk.CTkLabel(self.tabview.tab('Patient'), text='Name')
        self.birthdate_label = ctk.CTkLabel(self.tabview.tab('Patient'), text='Geburtsdatum')
        self.address_label = ctk.CTkLabel(self.tabview.tab('Patient'), text='Adresse')
        self.postcode_label = ctk.CTkLabel(self.tabview.tab('Patient'), text='Postleitzahl')
        self.city_label = ctk.CTkLabel(self.tabview.tab('Patient'), text='Stadt')
        self.phone_label = ctk.CTkLabel(self.tabview.tab('Patient'), text='Telefon')
        self.mobile_label = ctk.CTkLabel(self.tabview.tab('Patient'), text='Mobil')
        self.email_label = ctk.CTkLabel(self.tabview.tab('Patient'), text='E-Mail')
        
        # Entry-Widgets 
        self.name_entry = ctk.CTkEntry(self.tabview.tab('Patient'), placeholder_text='Name')
        self.birthdate_entry = ctk.CTkEntry(self.tabview.tab('Patient'), placeholder_text='Geburtsdatum')
        self.address_entry = ctk.CTkEntry(self.tabview.tab('Patient'), placeholder_text='Adresse')
        self.postcode_entry = ctk.CTkEntry(self.tabview.tab('Patient'), placeholder_text='Postleitzahl')
        self.city_entry = ctk.CTkEntry(self.tabview.tab('Patient'), placeholder_text='Stadt')
        self.phone_entry = ctk.CTkEntry(self.tabview.tab('Patient'), placeholder_text='Telefon')
        self.mobile_entry = ctk.CTkEntry(self.tabview.tab('Patient'), placeholder_text='Mobil')
        self.email_entry = ctk.CTkEntry(self.tabview.tab('Patient'), placeholder_text='E-Mail')
        
        # Grid the labels and entries     
        self.name_label.grid(row=0, column=0, pady=10, padx=10)
        self.birthdate_label.grid(row=0, column=1, pady=10, padx=10)
        self.address_label.grid(row=0, column=2, pady=10, padx=10)
        self.postcode_label.grid(row=2, column=0, pady=10, padx=10)
        self.city_label.grid(row=2, column=1, pady=10, padx=10)
        self.phone_label.grid(row=2, column=2, pady=10, padx=10)
        self.mobile_label.grid(row=4, column=0, pady=10, padx=10)
        self.email_label.grid(row=4, column=1, pady=10, padx=10)
        
        self.name_entry.grid(row=1, column=0, pady=10, padx=10)
        self.birthdate_entry.grid(row=1, column=1, pady=10, padx=10)
        self.address_entry.grid(row=1, column=2, pady=10, padx=10)
        self.postcode_entry.grid(row=3, column=0, pady=10, padx=10)
        self.city_entry.grid(row=3, column=1, pady=10, padx=10)
        self.phone_entry.grid(row=3, column=2, pady=10, padx=10)
        self.mobile_entry.grid(row=5, column=0, pady=10, padx=10)
        self.email_entry.grid(row=5, column=1, pady=10, padx=10)
        
        # Label for the update patient data header
        self.patient_update_label = ctk.CTkLabel(self.tabview.tab('Patient'), text='Patientendaten ändern:', font=('Arial', 14))
        self.patient_update_label.grid(row=7, column=0, columnspan=3, pady=10, padx=10)
        
        # Entries for the new patient data
        self.new_name_entry = ctk.CTkEntry(self.tabview.tab('Patient'), placeholder_text='Name')
        self.new_birthdate_entry = ctk.CTkEntry(self.tabview.tab('Patient'), placeholder_text='Geburtsdatum')
        self.new_address_entry = ctk.CTkEntry(self.tabview.tab('Patient'), placeholder_text='Adresse')
        self.new_postcode_entry = ctk.CTkEntry(self.tabview.tab('Patient'), placeholder_text='Postleitzahl')
        self.new_city_entry = ctk.CTkEntry(self.tabview.tab('Patient'), placeholder_text='Stadt')
        self.new_phone_entry = ctk.CTkEntry(self.tabview.tab('Patient'), placeholder_text='Telefon')
        self.new_mobile_entry = ctk.CTkEntry(self.tabview.tab('Patient'), placeholder_text='Mobil')
        self.new_email_entry = ctk.CTkEntry(self.tabview.tab('Patient'), placeholder_text='E-Mail') 
        
        # Grid the entries for the new patient data
        self.new_name_entry.grid(row=9, column=0, pady=10, padx=10)
        self.new_birthdate_entry.grid(row=9, column=1, pady=10, padx=10)
        self.new_address_entry.grid(row=9, column=2, pady=10, padx=10)
        self.new_postcode_entry.grid(row=11, column=0, pady=10, padx=10)
        self.new_city_entry.grid(row=11, column=1, pady=10, padx=10)
        self.new_phone_entry.grid(row=11, column=2, pady=10, padx=10)
        self.new_mobile_entry.grid(row=13, column=0, pady=10, padx=10)
        self.new_email_entry.grid(row=13, column=1, pady=10, padx=10)
        
        # Button for updating the patient data
        self.update_button = ctk.CTkButton(self.tabview.tab('Patient'), text='Aktualisieren', command=self.update_patient)
        self.update_button.grid(row=14, column=1, pady=10, padx=10)
        
    # Function for updating the patient entrys    
    def update_patient(self):
        # collect data from the entries
        new_name = self.new_name_entry.get()
        new_address = self.new_address_entry.get()
        new_postcode = self.new_postcode_entry.get()
        new_city = self.new_city_entry.get()
        new_phone = self.new_phone_entry.get()
        new_mobile = self.new_mobile_entry.get()
        new_email = self.new_email_entry.get()
        
        # validate input
        if not new_name or not new_address or not new_postcode or not new_city or not new_phone or not new_mobile or not new_email:
            tk.messagebox.showerror('Fehler', 'Um die Stammdaten des Patienten zu ändern, fülle bitte alle Felder aus, die du aktualisieren möchtest.')
            return
        if not new_name:
            tk.messagebox.showerror('Fehler', 'Bitte gib den Namen des Patient wie folgt ein: Nachname,Vorname.')
            return
        
        # connect to the database
        try:
            client = MongoClient("mongodb://localhost:27017")
            db = client["accountiantdb"]
            collection = db["patients"]
            
            # build the query
            filter_query ={'Rechnungs-Nr': self.receipt_number}
            update_query = {
                '$set':{
                    'new_RE.Name': new_name,
                    'new_RE.Strasse': new_address,
                    'new_RE.Postleitzahl_Ort': new_postcode + ' ' + new_city,
                    'new_RE.Telefon': new_phone,
                    'new_RE.Mobile': new_mobile,
                    'new_RE.Email': new_email,
                }
            }
            
            result = collection.update_one(filter_query, update_query, upsert=True)
            if result.modified_count > 0:
                tk.messagebox.showinfo('Update', 'Daten erfolgreich aktualisiert.')
            else:
                tk.messagebox.showerror('Fehler', 'Daten konnten nicht aktualisiert werden.')
                
        except Exception as e:
            tk.messagebox.showerror('Fehler', 'Fehler beim Zugriff auf die Datenbank.')
        
    # Function for creating the receiver-tab
    def _create_receiver_tab(self):            
        # Labels for the current receiver data
        self.receiver_name_label = ctk.CTkLabel(self.tabview.tab('Empfänger'), text='Name')
        self.receiver_prename_label = ctk.CTkLabel(self.tabview.tab('Empfänger'), text='Vorname')
        self.receiver_connection_label = ctk.CTkLabel(self.tabview.tab('Empfänger'), text='Angehöriger/Betreuer')
        self.receiver_address_label = ctk.CTkLabel(self.tabview.tab('Empfänger'), text='Adresse')
        self.receiver_postcode_label = ctk.CTkLabel(self.tabview.tab('Empfänger'), text='Postleitzahl')
        self.receiver_city_label = ctk.CTkLabel(self.tabview.tab('Empfänger'), text='Stadt')
        self.receiver_phone_label = ctk.CTkLabel(self.tabview.tab('Empfänger'), text='Telefon')
        self.receiver_mobile_label = ctk.CTkLabel(self.tabview.tab('Empfänger'), text='Mobil')
        self.receiver_email_label = ctk.CTkLabel(self.tabview.tab('Empfänger'), text='E-Mail')
        
        # Entries for the current receiver data
        self.receiver_name_entry = ctk.CTkEntry(self.tabview.tab('Empfänger'), placeholder_text='Name')
        self.receiver_prename_entry = ctk.CTkEntry(self.tabview.tab('Empfänger'), placeholder_text='Vorname')
        self.receiver_connection_entry = ctk.CTkEntry(self.tabview.tab('Empfänger'), placeholder_text='Angehöriger/Betreuer')
        self.receiver_address_entry = ctk.CTkEntry(self.tabview.tab('Empfänger'), placeholder_text='Adresse')
        self.receiver_postcode_entry = ctk.CTkEntry(self.tabview.tab('Empfänger'), placeholder_text='Postleitzahl')
        self.receiver_city_entry = ctk.CTkEntry(self.tabview.tab('Empfänger'), placeholder_text='Stadt')
        self.receiver_phone_entry = ctk.CTkEntry(self.tabview.tab('Empfänger'), placeholder_text='Telefon')
        self.receiver_mobile_entry = ctk.CTkEntry(self.tabview.tab('Empfänger'), placeholder_text='Mobil')
        self.receiver_email_entry = ctk.CTkEntry(self.tabview.tab('Empfänger'), placeholder_text='E-Mail')
        
        # Grid the labels for the current receiver data
        self.receiver_name_label.grid(row=0, column=0, pady=10, padx=10)
        self.receiver_prename_label.grid(row=0, column=1, pady=10, padx=10)
        self.receiver_connection_label.grid(row=0, column=2, pady=10, padx=10)
        self.receiver_address_label.grid(row=2, column=0, pady=10, padx=10)
        self.receiver_postcode_label.grid(row=2, column=1, pady=10, padx=10)
        self.receiver_city_label.grid(row=2, column=2, pady=10, padx=10)
        self.receiver_phone_label.grid(row=4, column=0, pady=10, padx=10)
        self.receiver_mobile_label.grid(row=4, column=1, pady=10, padx=10)
        self.receiver_email_label.grid(row=4, column=2, pady=10, padx=10)
        
        # Grid the entries for the current receiver data
        self.receiver_name_entry.grid(row=1, column=0, pady=10, padx=10)
        self.receiver_prename_entry.grid(row=1, column=1, pady=10, padx=10)
        self.receiver_connection_entry.grid(row=1, column=2, pady=10, padx=10)
        self.receiver_address_entry.grid(row=3, column=0, pady=10, padx=10)
        self.receiver_postcode_entry.grid(row=3, column=1, pady=10, padx=10)
        self.receiver_city_entry.grid(row=3, column=2, pady=10, padx=10)
        self.receiver_phone_entry.grid(row=5, column=0, pady=10, padx=10)
        self.receiver_mobile_entry.grid(row=5, column=1, pady=10, padx=10)
        self.receiver_email_entry.grid(row=5, column=2, pady=10, padx=10)
        
        # Label for the update receiver data header
        self.receiver_update_label = ctk.CTkLabel(self.tabview.tab('Empfänger'), text='Empfängerdaten ändern:', font=('Arial', 14))
        self.receiver_update_label.grid(row=7, column=0, columnspan=3, pady=10, padx=10)
        
        # Entries for the new receiver data
        self.new_receiver_name_entry = ctk.CTkEntry(self.tabview.tab('Empfänger'), placeholder_text='Name')
        self.new_receiver_prename_entry = ctk.CTkEntry(self.tabview.tab('Empfänger'), placeholder_text='Vorname')
        self.new_receiver_connection_label = ctk.CTkEntry(self.tabview.tab('Empfänger'), placeholder_text='Angehöriger/Betreuer')
        self.new_receiver_address_entry = ctk.CTkEntry(self.tabview.tab('Empfänger'), placeholder_text='Adresse')
        self.new_receiver_postcode_entry = ctk.CTkEntry(self.tabview.tab('Empfänger'), placeholder_text='Postleitzahl')
        self.new_receiver_city_entry = ctk.CTkEntry(self.tabview.tab('Empfänger'), placeholder_text='Stadt')
        self.new_receiver_phone_entry = ctk.CTkEntry(self.tabview.tab('Empfänger'), placeholder_text='Telefon')
        self.new_receiver_mobile_entry = ctk.CTkEntry(self.tabview.tab('Empfänger'), placeholder_text='Mobil')
        self.new_receiver_email_entry = ctk.CTkEntry(self.tabview.tab('Empfänger'), placeholder_text='E-Mail')
        
        # Grid the entries for the new receiver data
        self.new_receiver_name_entry.grid(row=9, column=0, pady=10, padx=10)
        self.new_receiver_prename_entry.grid(row=9, column=1, pady=10, padx=10)
        self.new_receiver_connection_label.grid(row=9, column=2, pady=10, padx=10)
        self.new_receiver_address_entry.grid(row=11, column=0, pady=10, padx=10)
        self.new_receiver_postcode_entry.grid(row=11, column=1, pady=10, padx=10)
        self.new_receiver_city_entry.grid(row=11, column=2, pady=10, padx=10)
        self.new_receiver_phone_entry.grid(row=13, column=0, pady=10, padx=10)
        self.new_receiver_mobile_entry.grid(row=13, column=1, pady=10, padx=10)
        self.new_receiver_email_entry.grid(row=13, column=2, pady=10, padx=10)
        
        # Button for updating the receiver data
        self.update_receiver_button = ctk.CTkButton(self.tabview.tab('Empfänger'), text='Aktualisieren', command=self.update_receiver)
        self.update_receiver_button.grid(row=14, column=1, pady=10, padx=10)    
        
    # Function for updating the receiver data    
    def update_receiver(self):
        # Collect data from the entries
        new_receiver_name = self.new_receiver_name_entry.get()
        new_receiver_prename = self.new_receiver_prename_entry.get()
        new_receiver_address = self.new_receiver_address_entry.get()
        new_receiver_postcode = self.new_receiver_postcode_entry.get()
        new_receiver_city = self.new_receiver_city_entry.get()
        new_receiver_phone = self.new_receiver_phone_entry.get()
        new_receiver_mobile = self.new_receiver_mobile_entry.get()
        new_receiver_email = self.new_receiver_email_entry.get()
        
        # Validate input
        if not new_receiver_name or not new_receiver_prename or not new_receiver_address or not new_receiver_postcode or not new_receiver_city or not new_receiver_phone or not new_receiver_mobile or not new_receiver_email:
            tk.messagebox.showerror('Fehler', 'Um die Stammdaten des Empfängers zu ändern, fülle bitte alle Felder aus, die du aktualisieren möchtest.')
            return
        if not new_receiver_name:
            tk.messagebox.showerror('Fehler', 'Bitte gib den Namen des Empfängers wie folgt ein: Nachname,Vorname.')
            return
        
        # Connect to the database
        try:
            client = MongoClient("mongodb://localhost:27017")
            db = client["accountiantdb"]
            collection = db["receivers"]
            
            # Build the query
            filter_query ={'Rechnungs-Nr': self.receipt_number}
            update_query ={
                '$set':{
                    'new_RE.Name': new_receiver_name,
                    'new_RE.Vorname': new_receiver_prename,
                    'new_RE.Strasse': new_receiver_address,
                    'new_RE.Postleitzahl_Ort': new_receiver_postcode + ' ' + new_receiver_city,
                    'new_RE.Telefon': new_receiver_phone,
                    'new_RE.Mobile': new_receiver_mobile,
                    'new_RE.Email': new_receiver_email,
                }
            }
            result = collection
            
            if result.modified_count > 0:
                tk.messagebox.showinfo('Update', 'Daten erfolgreich aktualisiert.')
            else:
                tk.messagebox.showerror('Fehler', 'Daten konnten nicht aktualisiert werden.')
        except Exception as e:
            tk.messagebox.showerror('Fehler', 'Fehler beim Zugriff auf die Datenbank.')
                
    # Function for creating the receipt-tab    
    def _create_receipt_tab(self):
        # Labels for the current receipt data
        self.receipt_number_label = ctk.CTkLabel(self.tabview.tab('Rechnung'), text='Rechnungsnummer')
        self.receipt_order_number_label = ctk.CTkLabel(self.tabview.tab('Rechnung'), text='Auftragsnummer')
        self.receipt_date_label = ctk.CTkLabel(self.tabview.tab('Rechnung'), text='Rechnungsdatum')
        self.receipt_warning_date_label = ctk.CTkLabel(self.tabview.tab('Rechnung'), text='Mahnungsdatum')
        self.receipt_amount_label = ctk.CTkLabel(self.tabview.tab('Rechnung'), text='Rechnungsbetrag')
        self.receipt_status_label = ctk.CTkLabel(self.tabview.tab('Rechnung'), text='Rechnungsstatus')
        self.receipt_payment_label = ctk.CTkLabel(self.tabview.tab('Rechnung'), text='Zahlungsstatus')
        self.receipt_warning_status_label = ctk.CTkLabel(self.tabview.tab('Rechnung'), text='Mahnstatus')
        
        # Entries for the current receipt data
        self.receipt_number_entry = ctk.CTkEntry(self.tabview.tab('Rechnung'), placeholder_text='XX-XX-XXXXXX')
        self.receipt_order_number_entry = ctk.CTkEntry(self.tabview.tab('Rechnung'), placeholder_text='Auftragsnummer')
        self.receipt_date_entry = ctk.CTkEntry(self.tabview.tab('Rechnung'), placeholder_text='Rechnungsdatum')
        self.receipt_warning_date_entry = ctk.CTkEntry(self.tabview.tab('Rechnung'), placeholder_text='Mahnungsdatum')
        self.receipt_amount_entry = ctk.CTkEntry(self.tabview.tab('Rechnung'), placeholder_text='Rechnungsbetrag')
        self.receipt_status_entry = ctk.CTkEntry(self.tabview.tab('Rechnung'), placeholder_text='Rechnungsstatus')
        self.receipt_payment_entry = ctk.CTkEntry(self.tabview.tab('Rechnung'), placeholder_text='Zahlungsstatus')
        self.receipt_warning_status_entry = ctk.CTkEntry(self.tabview.tab('Rechnung'), placeholder_text='Mahnstatus')
        
        # Grid the labels for the current receipt data
        self.receipt_number_label.grid(row=0, column=0, pady=10, padx=10)
        self.receipt_order_number_label.grid(row=0, column=1, pady=10, padx=10)
        self.receipt_date_label.grid(row=0, column=2, pady=10, padx=10)
        self.receipt_warning_date_label.grid(row=0, column=3, pady=10, padx=10)
        self.receipt_amount_label.grid(row=2, column=0, pady=10, padx=10)
        self.receipt_status_label.grid(row=2, column=1, pady=10, padx=10)
        self.receipt_payment_label.grid(row=2, column=2, pady=10, padx=10)
        self.receipt_warning_status_label.grid(row=2, column=3, pady=10, padx=10)
        
        # Grid the entries for the current receipt data
        self.receipt_number_entry.grid(row=1, column=0, pady=10, padx=10)
        self.receipt_order_number_entry.grid(row=1, column=1, pady=10, padx=10)
        self.receipt_date_entry.grid(row=1, column=2, pady=10, padx=10)
        self.receipt_warning_date_entry.grid(row=1, column=3, pady=10, padx=10)
        self.receipt_amount_entry.grid(row=3, column=0, pady=10, padx=10)
        self.receipt_status_entry.grid(row=3, column=1, pady=10, padx=10)
        self.receipt_payment_entry.grid(row=3, column=2, pady=10, padx=10)
        self.receipt_warning_status_entry.grid(row=3, column=3, pady=10, padx=10)
        
        # Label for the update receipt data header
        self.receipt_update_label = ctk.CTkLabel(self.tabview.tab('Rechnung'), text='Rechnungsdaten ändern:', font=('Arial', 14))
        self.receipt_update_label.grid(row=4, column=0, columnspan=3, pady=10, padx=10)
        
        # Entries for the new receipt data
        self.new_receipt_warning_date_entry = ctk.CTkEntry(self.tabview.tab('Rechnung'), placeholder_text='Mahnungsdatum')
        self.new_receipt_amount_entry = ctk.CTkEntry(self.tabview.tab('Rechnung'), placeholder_text='Rechnungsbetrag')
        self.new_receipt_status_entry = ctk.CTkEntry(self.tabview.tab('Rechnung'), placeholder_text='Rechnungsstatus')
        self.new_receipt_payment_entry = ctk.CTkEntry(self.tabview.tab('Rechnung'), placeholder_text='Zahlungsstatus')
        self.new_payment_day_entry = ctk.CTkEntry(self.tabview.tab('Rechnung'), placeholder_text='Zahlungstag')
        self.new_receipt_warning_status_entry = ctk.CTkEntry(self.tabview.tab('Rechnung'), placeholder_text='Mahnstatus')

        # Grid the entries for the new receipt data
        self.new_receipt_warning_date_entry.grid(row=8, column=0, pady=10, padx=10)
        self.new_receipt_amount_entry.grid(row=6, column=0, pady=10, padx=10)
        self.new_receipt_status_entry.grid(row=6, column=1, pady=10, padx=10)
        self.new_receipt_payment_entry.grid(row=6, column=2, pady=10, padx=10)
        self.new_receipt_warning_status_entry.grid(row=6, column=3, pady=10, padx=10)
        
        # Button for updating the receipt data
        self.update_receipt_button = ctk.CTkButton(self.tabview.tab('Rechnung'), text='Aktualisieren', command=self.update_receipt)
        self.update_receipt_button.grid(row=9, column=1, pady=10, padx=10)
        
    # Function for updating the receipt data
    def update_receipt(self):
        # Collect data from the entries
        new_receipt_warning_date = self.new_receipt_warning_date_entry.get()
        new_receipt_amount = self.new_receipt_amount_entry.get()
        new_receipt_status = self.new_receipt_status_entry.get()
        new_receipt_payment = self.new_receipt_payment_entry.get()
        new_payment_day = self.new_payment_day_entry.get()
        new_receipt_warning_status = self.new_receipt_warning_status_entry.get()
        
        # Validate input
        if not new_receipt_warning_date or not new_receipt_amount or not new_receipt_status or not new_receipt_payment or not new_payment_day or not new_receipt_warning_status:
            tk.messagebox.showerror('Fehler', 'Um die Rechnungsdaten zu ändern, fülle bitte alle Felder aus, die du aktualisieren möchtest.')
            return
        
        # Connect to the database
        try:
            client = MongoClient("mongodb://localhost:27017")
            db = client["accountiantdb"]
            collection = db["receipts"]
            
            # Build the query
            filter_query ={'Rechnungs-Nr': self.receipt_number}
            update_query ={
                '$set':{
                    'new_RE.Mahnungsdatum': new_receipt_warning_date,
                    'new_RE.Rechnungsbetrag': new_receipt_amount,
                    'new_RE.Rechnungsstatus': new_receipt_status,
                    'new_RE.Zahlungsstatus': new_receipt_payment,
                    'new_RE.Zahlungstag': new_payment_day,
                    'new_RE.Mahnstatus': new_receipt_warning_status,
                }
            }
            result = collection
            
            if result.modified_count > 0:
                tk.messagebox.showinfo('Update', 'Daten erfolgreich aktualisiert.')
            else:
                tk.messagebox.showerror('Fehler', 'Daten konnten nicht aktualisiert werden.')
        except Exception as e:
            tk.messagebox.showerror('Fehler', 'Fehler beim Zugriff auf die Datenbank.')
       
    def _create_submitter_tab(self):    
        #Einsender-Tab
        # Labels for the current submitter data
        self.submitter_number_label = ctk.CTkLabel(self.tabview.tab('Einsender'), text='Einsender-Nummer')
        self.submitter_name_label = ctk.CTkLabel(self.tabview.tab('Einsender'), text='Name')
        
        # Entries for the current submitter data
        self.submitter_number_entry = ctk.CTkEntry(self.tabview.tab('Einsender'), placeholder_text='Einsender-Nummer')
        self.submitter_name_entry = ctk.CTkEntry(self.tabview.tab('Einsender'), placeholder_text='Name')
        
        # Grid the labels for the current submitter data
        self.submitter_number_label.grid(row=0, column=0, pady=10, padx=10)
        self.submitter_name_label.grid(row=0, column=1, pady=10, padx=10)
        
        # Grid the entries for the current submitter data
        self.submitter_number_entry.grid(row=1, column=0, pady=10, padx=10)
        self.submitter_name_entry.grid(row=1, column=1, pady=10, padx=10)
        
        self.update_submitter_button = ctk.CTkButton(self.tabview.tab('Einsender'), text='Aktualisieren', command=self.update_submitter)
        self.update_submitter_button.grid(row=6, column=1, pady=10, padx=10)
        
    # method for updating the submitter data
    def update_submitter(self):
        # Collect data from the entries
        new_submitter_number = self.submitter_number_entry.get()
        new_submitter_name = self.submitter_name_entry.get()
        
        # Validate input
        if not new_submitter_number or not new_submitter_name:
            tk.messagebox.showerror('Fehler', 'Um die Einsenderdaten zu ändern, fülle bitte alle Felder aus, die du aktualisieren möchtest.')
            return
        try:
            client = MongoClient("mongodb://localhost:27017")
            db = client["accountiantdb"]
            collection = db["submitters"]
            
            # Build the query
            filter_query ={'Rechnungs-Nr': self.receipt_number}
            update_query ={
                '$set':{
                    'new_RE.Einsender-Nummer': new_submitter_number,
                    'new_RE.Name': new_submitter_name,
                }
            }
            result = collection
            
            if result.modified_count > 0:
                tk.messagebox.showinfo('Update', 'Daten erfolgreich aktualisiert.')
            else:
                tk.messagebox.showerror('Fehler', 'Daten konnten nicht aktualisiert werden.')
        except Exception as e:
            tk.messagebox.showerror('Fehler', 'Fehler beim Zugriff auf die Datenbank.')

    def _create_comment_tab(self):
        # Kommentar-Tab
        # Label for the comment entry
        self.submitter_contact_label = ctk.CTkLabel(self.tabview.tab('Kommentar'), text='Kontakt mit Einsender am:')
        self.patient_constact_label = ctk.CTkLabel(self.tabview.tab('Kommentar'), text='Kontakt mit Patient am:')
        self.receiver_contact_label = ctk.CTkLabel(self.tabview.tab('Kommentar'), text='Kontakt mit Empfänger am:')
        
        # Entries for the comment entry
        self.submitter_contact_entry = ctk.CTkEntry(self.tabview.tab('Kommentar'), placeholder_text='Kontakt mit Einsender am:')
        self.patient_contact_entry = ctk.CTkEntry(self.tabview.tab('Kommentar'), placeholder_text='Kontakt mit Patient am:')
        self.receiver_contact_entry = ctk.CTkEntry(self.tabview.tab('Kommentar'), placeholder_text='Kontakt mit Empfänger am:')
        
        # Grid the labels for the comment entry
        self.submitter_contact_label.grid(row=0, column=0, pady=10, padx=10)
        self.patient_constact_label.grid(row=0, column=1, pady=10, padx=10)
        self.receiver_contact_label.grid(row=0, column=2, pady=10, padx=10)
        
        # Grid the entries for the comment entry
        self.submitter_contact_entry.grid(row=1, column=0, pady=10, padx=10)
        self.patient_contact_entry.grid(row=1, column=1, pady=10, padx=10)
        self.receiver_contact_entry.grid(row=1, column=2, pady=10, padx=10)
        
    
        # Button for saving the comment
        self.comment_entry = ctk.CTkEntry(self.tabview.tab('Kommentar'), placeholder_text='Kommentar')
        self.comment_entry.grid(row=2, column=0, columnspan=5, pady=10, padx=10)

        self.save_comment_button = ctk.CTkButton(self.tabview.tab('Kommentar'), text='Kommentar speichern', command=self.safe_comment)
        self.save_comment_button.grid(row=3, column=1, pady=10, padx=10)
        
    # Implement safe_comment method
    def safe_comment(self):
        # Collect data from the entries
        new_submitter_contact = self.submitter_contact_entry.get()
        new_patient_contact = self.patient_contact_entry.get()
        new_receiver_contact = self.receiver_contact_entry.get()
        new_comment = self.comment_entry.get()
        
        # Validate input
        if not new_submitter_contact or not new_patient_contact or not new_receiver_contact or not new_comment:
            tk.messagebox.showerror('Fehler', 'Um einen Kommentar zu speichern, fülle bitte alle Felder aus.')
            return
        
        # Connect to the database
        try:
            client = MongoClient("mongodb://localhost:27017")
            db = client["accountiantdb"]
            collection = db["comments"]
            
            # Build the query
            filter_query ={'Rechnungs-Nr': self.receipt_number}
            update_query ={
                '$set':{
                    'new_RE.Kontakt_mit_Einsender_am': new_submitter_contact,
                    'new_RE.Kontakt_mit_Patient_am': new_patient_contact,
                    'new_RE.Kontakt_mit_Empfänger_am': new_receiver_contact,
                    'new_RE.Kommentar': new_comment,
                }
            }
            result = collection
            
            if result.modified_count > 0:
                tk.messagebox.showinfo('Update', 'Daten erfolgreich aktualisiert.')
            else:
                tk.messagebox.showerror('Fehler', 'Daten konnten nicht aktualisiert werden.')
        except Exception as e:
            tk.messagebox.showerror('Fehler', 'Fehler beim Zugriff auf die Datenbank.')
    
# Main    
if __name__ == '__main__':
    app = GUIConfig()
    app.mainloop()