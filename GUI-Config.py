import tkinter as tk
import tkinter.messagebox
import customtkinter as ctk
import mysql.connector

ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class GUIConfig(ctk.CTk):
    def __init__(self, master=None):
        super().__init__()

        self.title("GUI-Config")
        self.geometry("800x800")
        self.resizable(True, True)
        
        self.tabview = ctk.CTkTabview(self, width=800, height=800)
        self.tabview.grid(row=0, column=0, padx=10, pady=10)
        
        # Creating a Tableview
        self.tabview.add('Patient')
        self.tabview.add('Empfänger')
        self.tabview.add('Rechnung')
        self.tabview.add('Einsender')
        self.tabview.add('Kommentar')
        
        # Patient-tab
        self.name_label = ctk.CTkLabel(self.tabview.tab('Patient'), text='Name')
        self.prename_label = ctk.CTkLabel(self.tabview.tab('Patient'), text='Vorname')
        self.birthdate_label = ctk.CTkLabel(self.tabview.tab('Patient'), text='Geburtsdatum')
        self.address_label = ctk.CTkLabel(self.tabview.tab('Patient'), text='Adresse')
        self.postcode_label = ctk.CTkLabel(self.tabview.tab('Patient'), text='Postleitzahl')
        self.city_label = ctk.CTkLabel(self.tabview.tab('Patient'), text='Stadt')
        self.phone_label = ctk.CTkLabel(self.tabview.tab('Patient'), text='Telefon')
        self.mobile_label = ctk.CTkLabel(self.tabview.tab('Patient'), text='Mobil')
        self.email_label = ctk.CTkLabel(self.tabview.tab('Patient'), text='E-Mail')
        
        self.name_entry = ctk.CTkEntry(self.tabview.tab('Patient'), placeholder_text='Name')
        self.prename_entry = ctk.CTkEntry(self.tabview.tab('Patient'), placeholder_text='Vorname')
        self.birthdate_entry = ctk.CTkEntry(self.tabview.tab('Patient'), placeholder_text='Geburtsdatum')
        self.address_entry = ctk.CTkEntry(self.tabview.tab('Patient'), placeholder_text='Adresse')
        self.postcode_entry = ctk.CTkEntry(self.tabview.tab('Patient'), placeholder_text='Postleitzahl')
        self.city_entry = ctk.CTkEntry(self.tabview.tab('Patient'), placeholder_text='Stadt')
        self.phone_entry = ctk.CTkEntry(self.tabview.tab('Patient'), placeholder_text='Telefon')
        self.mobile_entry = ctk.CTkEntry(self.tabview.tab('Patient'), placeholder_text='Mobil')
        self.email_entry = ctk.CTkEntry(self.tabview.tab('Patient'), placeholder_text='E-Mail')
        
        self.name_label.grid(row=0, column=0, pady=10, padx=10)
        self.prename_label.grid(row=0, column=1, pady=10, padx=10)
        self.birthdate_label.grid(row=0, column=2, pady=10, padx=10)
        self.address_label.grid(row=2, column=0, pady=10, padx=10)
        self.postcode_label.grid(row=2, column=1, pady=10, padx=10)
        self.city_label.grid(row=2, column=2, pady=10, padx=10)
        self.phone_label.grid(row=4, column=0, pady=10, padx=10)
        self.mobile_label.grid(row=4, column=1, pady=10, padx=10)
        self.email_label.grid(row=4, column=2, pady=10, padx=10)
        
        self.name_entry.grid(row=1, column=0, pady=10, padx=10)
        self.prename_entry.grid(row=1, column=1, pady=10, padx=10)
        self.birthdate_entry.grid(row=1, column=2, pady=10, padx=10)
        self.address_entry.grid(row=3, column=0, pady=10, padx=10)
        self.postcode_entry.grid(row=3, column=1, pady=10, padx=10)
        self.city_entry.grid(row=3, column=2, pady=10, padx=10)
        self.phone_entry.grid(row=5, column=0, pady=10, padx=10)
        self.mobile_entry.grid(row=5, column=1, pady=10, padx=10)
        self.email_entry.grid(row=5, column=2, pady=10, padx=10)
        
        self.patient_update_label = ctk.CTkLabel(self.tabview.tab('Patient'), text='Patientendaten ändern:', font=('Arial', 14))
        self.patient_update_label.grid(row=7, column=0, columnspan=3, pady=10, padx=10)
        
        self.new_name_label = ctk.CTkLabel(self.tabview.tab('Patient'), text='Name')
        self.new_prename_label = ctk.CTkLabel(self.tabview.tab('Patient'), text='Vorname')
        self.new_birthdate_label = ctk.CTkLabel(self.tabview.tab('Patient'), text='Geburtsdatum')
        self.new_address_label = ctk.CTkLabel(self.tabview.tab('Patient'), text='Adresse')
        self.new_postcode_label = ctk.CTkLabel(self.tabview.tab('Patient'), text='Postleitzahl')
        self.new_city_label = ctk.CTkLabel(self.tabview.tab('Patient'), text='Stadt')
        self.new_phone_label = ctk.CTkLabel(self.tabview.tab('Patient'), text='Telefon')
        self.new_mobile_label = ctk.CTkLabel(self.tabview.tab('Patient'), text='Mobil')
        self.new_email_label = ctk.CTkLabel(self.tabview.tab('Patient'), text='E-Mail')
        
        self.new_name_entry = ctk.CTkEntry(self.tabview.tab('Patient'), placeholder_text='Name')
        self.new_prename_entry = ctk.CTkEntry(self.tabview.tab('Patient'), placeholder_text='Vorname')
        self.new_birthdate_entry = ctk.CTkEntry(self.tabview.tab('Patient'), placeholder_text='Geburtsdatum')
        self.new_address_entry = ctk.CTkEntry(self.tabview.tab('Patient'), placeholder_text='Adresse')
        self.new_postcode_entry = ctk.CTkEntry(self.tabview.tab('Patient'), placeholder_text='Postleitzahl')
        self.new_city_entry = ctk.CTkEntry(self.tabview.tab('Patient'), placeholder_text='Stadt')
        self.new_phone_entry = ctk.CTkEntry(self.tabview.tab('Patient'), placeholder_text='Telefon')
        self.new_mobile_entry = ctk.CTkEntry(self.tabview.tab('Patient'), placeholder_text='Mobil')
        self.new_email_entry = ctk.CTkEntry(self.tabview.tab('Patient'), placeholder_text='E-Mail') 
        """
        self.new_name_label.grid(row=8, column=0, pady=10, padx=10)
        self.new_prename_label.grid(row=8, column=1, pady=10, padx=10)
        self.new_birthdate_label.grid(row=8, column=2, pady=10, padx=10)
        self.new_address_label.grid(row=10, column=0, pady=10, padx=10)
        self.new_postcode_label.grid(row=10, column=1, pady=10, padx=10)
        self.new_city_label.grid(row=10, column=2, pady=10, padx=10)
        self.new_country_label.grid(row=10, column=3, pady=10, padx=10)
        self.new_phone_label.grid(row=12, column=0, pady=10, padx=10)
        self.new_mobile_label.grid(row=12, column=1, pady=10, padx=10)
        self.new_email_label.grid(row=12, column=2, pady=10, padx=10)
        """
        self.new_name_entry.grid(row=9, column=0, pady=10, padx=10)
        self.new_prename_entry.grid(row=9, column=1, pady=10, padx=10)
        self.new_birthdate_entry.grid(row=9, column=2, pady=10, padx=10)
        self.new_address_entry.grid(row=11, column=0, pady=10, padx=10)
        self.new_postcode_entry.grid(row=11, column=1, pady=10, padx=10)
        self.new_city_entry.grid(row=11, column=2, pady=10, padx=10)
        self.new_phone_entry.grid(row=13, column=0, pady=10, padx=10)
        self.new_mobile_entry.grid(row=13, column=1, pady=10, padx=10)
        self.new_email_entry.grid(row=13, column=2, pady=10, padx=10)
        
        self.update_button = ctk.CTkButton(self.tabview.tab('Patient'), text='Aktualisieren', command=self.update_patient)
        self.update_button.grid(row=14, column=1, pady=10, padx=10)
       
        self.update_patient()
    # Function for updating the patient entrys    
    def update_patient(self):
        # Collect data from the entries
        name = self.new_name_entry.get()
        prename = self.new_prename_entry.get()
        birthdate = self.new_birthdate_entry.get()
        address = self.new_address_entry.get()
        postcode = self.new_postcode_entry.get()
        city = self.new_city_entry.get()
        phone = self.new_phone_entry.get()
        mobile = self.new_mobile_entry.get()
        email = self.new_email_entry.get()

        # Database connection
        try:
            conn = mysql.connector.connect('accountant.db')
            cursor = conn.cursor()

            # SQL-Update-Statement
            cursor.execute("UPDATE patients SET name=%s, prename=%s, birthdate=%s, address=%s, postcode=%s, city=%s, phone=%s, mobile=%s, email=%s WHERE patient_id=%s", (name, prename, birthdate, address, postcode, city, phone, mobile, email, id))

            # Commit
            conn.commit()
        except mysql.connector.Error as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
        
        # Empfänger-Tab
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
        
        # Labels for the new receiver data
        self.new_receiver_name_label = ctk.CTkLabel(self.tabview.tab('Empfänger'), text='Name')
        self.new_receiver_prename_label = ctk.CTkLabel(self.tabview.tab('Empfänger'), text='Vorname')
        self.new_receiver_connection_label = ctk.CTkLabel(self.tabview.tab('Empfänger'), text='Angehöriger/Betreuer')
        self.new_receiver_address_label = ctk.CTkLabel(self.tabview.tab('Empfänger'), text='Adresse')
        self.new_receiver_postcode_label = ctk.CTkLabel(self.tabview.tab('Empfänger'), text='Postleitzahl')
        self.new_receiver_city_label = ctk.CTkLabel(self.tabview.tab('Empfänger'), text='Stadt')
        self.new_receiver_phone_label = ctk.CTkLabel(self.tabview.tab('Empfänger'), text='Telefon')
        self.new_receiver_mobile_label = ctk.CTkLabel(self.tabview.tab('Empfänger'), text='Mobil')
        self.new_receiver_email_label = ctk.CTkLabel(self.tabview.tab('Empfänger'), text='E-Mail')
        
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
        
        """
        self.new_receiver_name_label.grid(row=8, column=0, pady=10, padx=10)
        self.new_receiver_prename_label.grid(row=8, column=1, pady=10, padx=10)
        self.new_receiver_connection_label.grid(row=8, column=2, pady=10, padx=10)
        self.new_receiver_address_label.grid(row=10, column=0, pady=10, padx=10)
        self.new_receiver_postcode_label.grid(row=10, column=1, pady=10, padx=10)
        self.new_receiver_city_label.grid(row=10, column=2, pady=10, padx=10)
        self.new_receiver_phone_label.grid(row=12, column=0, pady=10, padx=10)
        self.new_receiver_mobile_label.grid(row=12, column=1, pady=10, padx=10)
        self.new_receiver_email_label.grid(row=12, column=2, pady=10, padx=10)
        """
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
        self.update_receiver_button = ctk.CTkButton(self.tabview.tab('Empfänger'), text='Aktualisieren', command=self.update)
        self.update_receiver_button.grid(row=14, column=1, pady=10, padx=10)    
        
        self.update_receiver()
    
    # Function for updating the receiver data    
    def update_receiver(self):
        # Collect data from the entries
        name = self.new_receiver_name_entry.get()
        prename = self.new_receiver_prename_entry.get()
        connection = self.new_receiver_connection_entry.get()
        address = self.new_receiver_address_entry.get()
        postcode = self.new_receiver_postcode_entry.get()
        city = self.new_receiver_city_entry.get()
        phone = self.new_receiver_phone_entry.get()
        mobile = self.new_receiver_mobile_entry.get()
        email = self.new_receiver_email_entry.get()

        # Database connection
        try:
            conn = mysql.connector.connect('accountant.db')
            cursor = conn.cursor()

            # SQL-Update-Statement
            cursor.execute("UPDATE receiver SET name=%s, prename=%s, connection=%s, address=%s, postcode=%s, city=%s, phone=%s, mobile=%s, email=%s WHERE patient_id=%s", (name, prename, connection, address, postcode, city, phone, mobile, email, id))

            # Commit
            conn.commit()
        except mysql.connector.Error as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
        
        # Rechnung-Tab
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
        self.receipt_number_entry = ctk.CTkEntry(self.tabview.tab('Rechnung'), placeholder_text='Rechnungsnummer')
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
        
        # Labels for the new receipt data
        self.new_receipt_number_label = ctk.CTkLabel(self.tabview.tab('Rechnung'), text='Rechnungsnummer')
        self.new_receipt_order_number_label = ctk.CTkLabel(self.tabview.tab('Rechnung'), text='Auftragsnummer')
        self.new_receipt_date_label = ctk.CTkLabel(self.tabview.tab('Rechnung'), text='Rechnungsdatum')
        self.new_receipt_warning_date_label = ctk.CTkLabel(self.tabview.tab('Rechnung'), text='Mahnungsdatum')
        self.new_receipt_amount_label = ctk.CTkLabel(self.tabview.tab('Rechnung'), text='Rechnungsbetrag')
        self.new_receipt_warning_status_label = ctk.CTkLabel(self.tabview.tab('Rechnung'), text='Rechnungsstatus')
        self.new_receipt_payment_label = ctk.CTkLabel(self.tabview.tab('Rechnung'), text='Zahlungsstatus')
        
        """
        self.new_receipt_number_entry = ctk.CTkEntry(self.tabview.tab('Rechnung'), placeholder_text='Rechnungsnummer')
        self.new_receipt_order_number_entry = ctk.CTkEntry(self.tabview.tab('Rechnung'), placeholder_text='Auftragsnummer')
        self.new_receipt_date_entry = ctk.CTkEntry(self.tabview.tab('Rechnung'), placeholder_text='Rechnungsdatum')
        """
        # Entries for the new receipt data
        self.new_receipt_warning_date_entry = ctk.CTkEntry(self.tabview.tab('Rechnung'), placeholder_text='Mahnungsdatum')
        self.new_receipt_amount_entry = ctk.CTkEntry(self.tabview.tab('Rechnung'), placeholder_text='Rechnungsbetrag')
        self.new_receipt_status_entry = ctk.CTkEntry(self.tabview.tab('Rechnung'), placeholder_text='Rechnungsstatus')
        self.new_receipt_payment_entry = ctk.CTkEntry(self.tabview.tab('Rechnung'), placeholder_text='Zahlungsstatus')
        self.new_payment_day_entry = ctk.CTkEntry(self.tabview.tab('Rechnung'), placeholder_text='Zahlungstag')
        self.new_receipt_goal_entry = ctk.CTkEntry(self.tabview.tab('Rechnung'), placeholder_text='Zahlungsziel')
        self.new_receipt_warning_status_entry = ctk.CTkEntry(self.tabview.tab('Rechnung'), placeholder_text='Mahnstatus')

        # Create a radio button for setting the new_receipt_goal
        self.new_receipt_goal_radio = ctk.CTkRadioButton(self.tabview.tab('Rechnung'), text='Zahlungsziel verlängern', value='Zahlungsziel')
       
        # set new_receipt_goal_entry to disabled
        self.new_receipt_goal_entry.configure(state='disabled')
        
        self.enable_goal_entry()
        
    # set new_receipt_goal_entry to enabled if new_receipt_goal_radio is selected
    def enable_goal_entry(self):
        if self.new_receipt_goal_radio.get() == 'Zahlungsziel':
            self.new_receipt_goal_entry.configure(state='normal')
        else:
            self.new_receipt_goal_entry.configure(state='disabled')

        """
        # Grid the labels and entries for the new receipt in case user wants to have labels
        self.new_receipt_number_label.grid(row=5, column=0, pady=10, padx=10)
        self.new_receipt_order_number_label.grid(row=5, column=1, pady=10, padx=10)
        self.new_receipt_date_label.grid(row=5, column=2, pady=10, padx=10)
        self.new_receipt_warning_date_label.grid(row=5, column=3, pady=10, padx=10)
        self.new_receipt_amount_label.grid(row=7, column=0, pady=10, padx=10)
        self.new_receipt_status_label.grid(row=7, column=1, pady=10, padx=10)
        self.new_receipt_payment_label.grid(row=7, column=2, pady=10, padx=10)
        self.new_receipt_warning_status_label.grid(row=7, column=3, pady=10, padx=10)
        
        self.new_receipt_number_entry.grid(row=6, column=0, pady=10, padx=10)
        self.new_receipt_order_number_entry.grid(row=6, column=1, pady=10, padx=10)
        self.new_receipt_date_entry.grid(row=6, column=2, pady=10, padx=10)
        """
        # Grid the entries for the new receipt data
        self.new_receipt_goal_radio.grid(row=8, column=2, pady=10, padx=10)
        self.new_receipt_goal_entry.grid(row=8, column=1, pady=10, padx=10)
        self.new_receipt_warning_date_entry.grid(row=8, column=0, pady=10, padx=10)
        self.new_receipt_amount_entry.grid(row=6, column=0, pady=10, padx=10)
        self.new_receipt_status_entry.grid(row=6, column=1, pady=10, padx=10)
        self.new_receipt_payment_entry.grid(row=6, column=2, pady=10, padx=10)
        self.new_receipt_warning_status_entry.grid(row=6, column=3, pady=10, padx=10)
        
        # Button for updating the receipt data
        self.update_receipt_button = ctk.CTkButton(self.tabview.tab('Rechnung'), text='Aktualisieren', command=self.update_receipt)
        self.update_receipt_button.grid(row=9, column=1, pady=10, padx=10)
        
        self.update_receipt()
        
    # Function for updating the receipt data
    def update_receipt(self):
        # Collect data from the entries
        receipt_warning_date = self.new_receipt_warning_date_entry.get()
        receipt_amount = self.new_receipt_amount_entry.get()
        receipt_status = self.new_receipt_status_entry.get()
        receipt_payment = self.new_receipt_payment_entry.get()
        receipt_warning_status = self.new_receipt_warning_status_entry.get()
        payment_day = self.new_payment_day_entry.get()
        receipt_goal = self.new_receipt_goal_entry.get()

        # Database connection
        try:
            conn = mysql.connector.connect('accountant.db')
            cursor = conn.cursor()

            # SQL-Update-Statement
            cursor.execute("UPDATE receipts SET receipt_warning_date=%s, receipt_amount=%s, receipt_status=%s, receipt_payment=%s, receipt_warning_status=%s, payment_day=%s, receipt_goal=%s WHERE patient_id=%s", (receipt_warning_date, receipt_amount, receipt_status, receipt_payment, receipt_warning_status, payment_day, receipt_goal, id))

            # Commit
            conn.commit()
        except mysql.connector.Error as e:
            # show the error message in an additional window
            tkinter.messagebox.showerror('Verbindung zur Datenbank konnte nicht hergestellt werden', e)
        finally:
            cursor.close()
            conn.close()
        
        #Einsender-Tab
        # Labels for the current submitter data
        self.submitter_number_label = ctk.CTkLabel(self.tabview.tab('Einsender'), text='Einsender-Nummer')
        self.submitter_name_label = ctk.CTkLabel(self.tabview.tab('Einsender'), text='Name')
        self.submitter_prename_label = ctk.CTkLabel(self.tabview.tab('Einsender'), text='Vorname')
        self.submitter_titel_label = ctk.CTkLabel(self.tabview.tab('Einsender'), text='Titel')
        self.submitter_address_label = ctk.CTkLabel(self.tabview.tab('Einsender'), text='Adresse')
        self.submitter_postcode_label = ctk.CTkLabel(self.tabview.tab('Einsender'), text='Postleitzahl')
        self.submitter_city_label = ctk.CTkLabel(self.tabview.tab('Einsender'), text='Stadt')
        self.submitter_phone_label = ctk.CTkLabel(self.tabview.tab('Einsender'), text='Telefon')
        self.submitter_mobile_label = ctk.CTkLabel(self.tabview.tab('Einsender'), text='Mobil')
        self.submitter_email_label = ctk.CTkLabel(self.tabview.tab('Einsender'), text='E-Mail')
        
        # Entries for the current submitter data
        self.submitter_number_entry = ctk.CTkEntry(self.tabview.tab('Einsender'), placeholder_text='Einsender-Nummer')
        self.submitter_name_entry = ctk.CTkEntry(self.tabview.tab('Einsender'), placeholder_text='Name')
        self.submitter_prename_entry = ctk.CTkEntry(self.tabview.tab('Einsender'), placeholder_text='Vorname')
        self.submitter_titel_entry = ctk.CTkEntry(self.tabview.tab('Einsender'), placeholder_text='Titel')
        self.submitter_address_entry = ctk.CTkEntry(self.tabview.tab('Einsender'), placeholder_text='Adresse')
        self.submitter_postcode_entry = ctk.CTkEntry(self.tabview.tab('Einsender'), placeholder_text='Postleitzahl')
        self.submitter_city_entry = ctk.CTkEntry(self.tabview.tab('Einsender'), placeholder_text='Stadt')
        self.submitter_phone_entry = ctk.CTkEntry(self.tabview.tab('Einsender'), placeholder_text='Telefon')
        self.submitter_mobile_entry = ctk.CTkEntry(self.tabview.tab('Einsender'), placeholder_text='Mobil')
        self.submitter_email_entry = ctk.CTkEntry(self.tabview.tab('Einsender'), placeholder_text='E-Mail')
        
        # Grid the labels for the current submitter data
        self.submitter_number_label.grid(row=0, column=0, pady=10, padx=10)
        self.submitter_name_label.grid(row=0, column=1, pady=10, padx=10)
        self.submitter_prename_label.grid(row=0, column=2, pady=10, padx=10)
        self.submitter_titel_label.grid(row=0, column=3, pady=10, padx=10)
        self.submitter_address_label.grid(row=2, column=0, pady=10, padx=10)
        self.submitter_postcode_label.grid(row=2, column=1, pady=10, padx=10)
        self.submitter_city_label.grid(row=2, column=2, pady=10, padx=10)
        self.submitter_phone_label.grid(row=4, column=0, pady=10, padx=10)
        self.submitter_mobile_label.grid(row=4, column=1, pady=10, padx=10)
        self.submitter_email_label.grid(row=4, column=2, pady=10, padx=10)
        
        # Grid the entries for the current submitter data
        self.submitter_number_entry.grid(row=1, column=0, pady=10, padx=10)
        self.submitter_name_entry.grid(row=1, column=1, pady=10, padx=10)
        self.submitter_prename_entry.grid(row=1, column=2, pady=10, padx=10)
        self.submitter_titel_entry.grid(row=1, column=3, pady=10, padx=10)
        self.submitter_address_entry.grid(row=3, column=0, pady=10, padx=10)
        self.submitter_postcode_entry.grid(row=3, column=1, pady=10, padx=10)
        self.submitter_city_entry.grid(row=3, column=2, pady=10, padx=10)
        self.submitter_phone_entry.grid(row=5, column=0, pady=10, padx=10)
        self.submitter_mobile_entry.grid(row=5, column=1, pady=10, padx=10)
        self.submitter_email_entry.grid(row=5, column=2, pady=10, padx=10)
        
        self.update_submitter_button = ctk.CTkButton(self.tabview.tab('Einsender'), text='Aktualisieren', command=self.update_submitter)
        self.update_submitter_button.grid(row=6, column=1, pady=10, padx=10)
        
        self.update_submitter()
        
    # method for updating the submitter data
    def update_submitter(self):
        # Collect data from the entries
        submitter_number = self.submitter_number_entry.get()
        submitter_name = self.submitter_name_entry.get()
        submitter_prename = self.submitter_prename_entry.get()
        submitter_titel = self.submitter_titel_entry.get()
        submitter_address = self.submitter_address_entry.get()
        submitter_postcode = self.submitter_postcode_entry.get()
        submitter_city = self.submitter_city_entry.get()
        submitter_phone = self.submitter_phone_entry.get()
        submitter_mobile = self.submitter_mobile_entry.get()
        submitter_email = self.submitter_email_entry.get()

        # Database connection
        try:
            conn = mysql.connector.connect('accountant.db')
            cursor = conn.cursor()

            # SQL-Update-Statement
            cursor.execute("UPDATE submitters SET submitter_number%s, submitter_name=%s, submitter_prename=%s, submitter_titel=%s, submitter_address=%s, submitter_postcode=%s, submitter_city=%s, submitter_phone=%s, submitter_mobile=%s, submitter_email=%s WHERE patient_id=%s", (submitter_number, submitter_name, submitter_prename, submitter_titel, submitter_address, submitter_postcode, submitter_city, submitter_phone, submitter_mobile, submitter_email, id))

            # Commit
            conn.commit()
        except mysql.connector.Error as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
        
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
        
        self.safe_comment()

    # Implement safe_comment method
    def safe_comment(self):
        comment = self.comment_entry.get()
        submitter_contact = self.submitter_contact_entry.get()
        patient_contact = self.patient_contact_entry.get()
        receiver_contact = self.receiver_contact_entry.get()
        try:
            conn = mysql.connector.connect('accountant.db')
            cursor = conn.cursor()

            cursor.execute("INSERT INTO comments (comment, submitter_contact, patient_contact, receiver_contact) VALUES (%s, %s, %s, %s)", (comment, submitter_contact, patient_contact, receiver_contact))

            conn.commit()
        except mysql.connector.Error as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
    
# Main    
if __name__ == '__main__':
    app = GUIConfig()
    """
    app.update_patient()
    app.update_receiver()
    app.update_receipt()
    app.safe_comment()
    app.mainloop()
    """
    
    