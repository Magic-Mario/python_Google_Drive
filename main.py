import gspread
from dataclasses import dataclass
from typing import Any, Optional
import datetime
import pandas as pd
from validators.url import url


@dataclass
class Patients:

    # *Authentication variables
    auth = gspread.service_account("creds.json")

    # *Table variables
    import datetime
    name: str
    last_name: str
    cc: int
    email: str
    phone_number: int
    

    def authentication(self):
        """Func to authenticate if the received url is valid and related to google spreadsheets"""

        try:
            url_input = "https://docs.google.com/spreadsheets/d/1zRTdhTqTVszV7t-6XkRklj2kXEXAaizp9wOK9FBius8/edit#gid=0"
            if url_input.startswith("https://docs.google.com/spreadsheets/") and url(url_input):
                return self.auth.open_by_url(url_input)

        except Exception:
            print("Inserte un url valido")

    def select_sheet(self, sheet):
        """Func to select which sheet you want to use"""

        title = input("Escribe el nombre de la tabla ha utilizar: ")
        return sheet.worksheet(title)

    def fill_table(self, wks):
        """Func to find all the cells without a value and fill them with Null value """

        for cell in table.findall(""):
            if cell.value == "":
                table.update_cell(cell.row, cell.col, "Null")
        return table.get_all_values()

    def find_patient(self, wks):
        """Func to check and find if a patient is in the database"""

        info = input("Escriba el dato del paciente: ")  # Patient info
        for cell in table.findall(info):
            return table.row_values(cell.row)  # List with row's info

    def add_patient(self, wks):
        """Func to add a new patient in the database"""

        row_value = [self.name, self.last_name, self.cc, self.email,
                     self.phone_number]
        return wks.append_row(row_value)

    def update_patient(self):
        """Func to update patients info"""

        pass

    def delete_patient(self):
        """Func to remove a patient from the database"""
        pass

    def main(self):
        sheet = self.authentication()
        wks = self.select_sheet(sheet)
        option = input("Elige una función: ").lower()
        if option == "fill":
            return print(self.fill_table(wks))
        elif option == "find":
            return print(self.find_patient(wks))
        elif option == "new":
            return print(self.add_patient(wks))


if __name__ == '__main__':
    name = input("Nombre: ")
    last_name = input("Apellido: ")
    cc = input("CC: ")
    email = input("Email: ")
    phone_number = int(input("Numero de contacto: "))
    func = Patients(name, last_name, cc, email, phone_number)
    func.main()
