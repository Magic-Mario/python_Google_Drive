import gspread
from dataclasses import dataclass
from typing import Any, Optional
import datetime
from validators.url import url


@dataclass
class Patients:

    # *Authentication variables
    auth = gspread.service_account("creds.json")

    # # *Table variables
    # self.name: str
    # self.last_name: str
    # self.cc: int
    # email: str
    # phone_number: int
    # init_date: str
    # end_date: str

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
        return sheet.worksheet(title="Test1")

    def fill_table(self, table):
        """Func to find all the cells without a value and fill them with Null value """

        for cell in table.findall(""):
            if cell.value == "":
                table.update_cell(cell.row, cell.col, "Null")
        return table.get_all_values()

    def find_patient(self):
        """Func to check and find if a patient is in the database"""

        info = input("Escriba el dato del paciente: ")  # Patient info
        wks = self.select_sheet()
        if wks.findall(name):
            return wks.findall(info)
        else:
            print("El paciente no fue encontrado")

    def add_patient(self):
        """Func to add a new patient in the database"""
        pass

    def update_patient(self):
        """Func to update patients info"""

        pass

    def delete_patient(self):
        """Func to remove a patient from the database"""
        pass

    def main(self):
        sheet = self.authentication()
        table = self.select_sheet(sheet)
        return print(self.fill_table(table))


if __name__ == '__main__':

    func = Patients()
    func.main()
