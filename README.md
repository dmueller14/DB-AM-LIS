# DB-AM-LIS

## Description
DB-AM-LIS is a new database system designed for a laboratory's financial accounting needs. It addresses the limitations of the currently used system by providing necessary SQL statements and allowing users to write 
comments on unpaid receipts directly within the system. The new database will offer a user-friendly GUI designed with customtkinter for enhanced accessibility.

## Key Features
- **SQL Statements**: Execute SQL statements for selecting specific receipts.
- **New Receiver Window**: Add a new receiver of the receipt with a dedicated window and column.
- **Receipt Selection**: Select receipts by receipt number, patient, or order number.
- **Patient Warnings**: Track whether a patient has received a warning.
- **Comments**: Add and manage comments directly within the system.
- **Data Updates**: Update the base data as required.
- **Printing**: Print information to send to a lawyer.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)
- [Contact Information](#contact-information)

## Installation
### Prerequisites
- Python (version 3.7 or higher)
- MySQL Server
- MySQL Connector for Python
- customtkinter library

### Steps
1. **Clone the repository:**
   ```bash
   git clone https://github.com/dmueller14/DB-AM-LIS.git
   cd DB-AM-LIS
   ```
2. **Install required Python packages:**
   ```bash
   pip install mysql-connector-python customtkinter
   ```
3. **Set up the MySQL database:**
   - Create a new database in MySQL.
   - Run the provided SQL script (`setup.sql` *upcoming file*) to create necessary tables and schema.

4. **Configure the database connection:**
   - Update the `config.py` file with your MySQL database credentials.

5. **Run the application:**
   ```bash
   python main.py
   ```

## Usage
### Basic Usage
1. **Launching the Application:**
   - Run `python main.py` to start the GUI application.
   
2. **Using the GUI:**
   - **Select Receipts**: Use the provided fields to select receipts by receipt number, patient, or order number.
   - **Add Receiver**: Use the dedicated window to add a new receiver for the receipt.
   - **Patient Warnings**: Indicate if a patient has received a warning.
   - **Add Comments**: Directly add comments to unpaid receipts within the system.
   - **Update Data**: Make necessary updates to the base data.
   - **Print Information**: Use the print feature to generate documents for legal purposes.

## Contributing
We welcome contributions! Please read our [CONTRIBUTING.md](CONTRIBUTING.md) to learn about the process and code of conduct.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Thanks to all contributors and the community for their support.
- Special thanks to the developers of customtkinter and MySQL Connector for Python.

## Contact Information
For any queries or support, please contact [your email](mailto:d.mueller14@outlook.com).

---

Feel free to customize further based on your specific needs and project details.
Please note that some files mentioned in the Readme-file are still coming up.
Gonna update the readme when the files are implemented.
