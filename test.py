import gspread
import pandas as pd
from datetime import date, datetime
auth = gspread.service_account("creds.json")

sh = auth.open_by_url(
    "https://docs.google.com/spreadsheets/d/1zRTdhTqTVszV7t-6XkRklj2kXEXAaizp9wOK9FBius8/edit#gid=0")

wks = sh.worksheet("Test1")

cell = wks.find("Gary")

cell_list = wks.range(cell.row, 1, cell.row, 6)

cell_list[0].value = "Mark"

wks.update_cell(cell_list[0].row, cell_list[0].col, cell_list[0].value)
# a = wks.findall("")
# for i in a:
#     if i.value == "":
#         wks.update_cell(i.row, i.col, "Null")


# * Adding a new patient

# info = input("Escriba el dato del paciente: ")  # Patient info

# for cell in wks.findall(info):
#     row_value = wks.row_values(cell.row) #List of the row
#     row_value[0] = "Todo Terreno"
#     wks.append_row(row_value)

# date = datetime.now()

# a = date.strftime("%y-%m-%d")

# ls = [a]
# print(ls)
    

"""
!!!SISTEMA DE NOTIFICACIONES!!!

Para las notificaciones de citas pendientes para los beneficiarios, 
se puede usar el la librería datetime y definir una variable cita registrada por el encargado de
manejar el sistema y, utilizando la expresión  datetime.now() == cita comparamos dia a dia si a 
esa persona le toca cita en el dia o no. También se podría agregar una función para enviar un mensaje al
correo registrado de esa persona avisando que tiene cita el dia siguiente.

"""