import gspread
from dataclasses import dataclass
from typing import Any, Optional
import datetime
from validators.url import url


@dataclass
class Patients:
    # *Authentication variables
    auth = gspread.service_account("creds.json")
    title: str = input("Digite el nombre de la hoja de trabajo: ")

    # *Table variables
    name: str
    last_name: str
    cc: int
    email: str
    phone_number: int
    init_date: str
    end_date: str

    def authentication(self):
        """Func to authenticate if the received url is valid and related to google spreadsheets"""

        try:
            url_input = input(
                "Inserte el url de la base de datos a utilizar: ")
            if url(url_input) and url_input.startswith("https://docs.google.com/spreadsheets/"):
                return self.auth.open_by_url(url_input)

        except Exception:
            print("Inserte un url valido")

    def select_sheet(self):
        """Func to select which sheet you want to use"""

        title = input("Escribe el nombre de la tabla ha utilizar: ")
        sheet = self.authentication()
        return sheet.worksheet(title)

    def fill_table(self):
        """Func to find all the cells without a value and fill them with Null value """

        sheet = self.select_sheet()
        ls = sheet.findall("")
        for i in ls:
            if i.value == "":
                i.value = "Null"

    def main(self):
        pass


# *if __name__ == '__main__':
