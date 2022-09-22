import gspread

auth = gspread.service_account("creds.json")

sh = auth.open_by_url("https://docs.google.com/spreadsheets/d/1zRTdhTqTVszV7t-6XkRklj2kXEXAaizp9wOK9FBius8/edit#gid=0")

wks = sh.worksheet("Test1")

a = wks.findall("")
for i in a:
    if i.value == "":
        wks.update_cell(i.row, i.col, "Null")