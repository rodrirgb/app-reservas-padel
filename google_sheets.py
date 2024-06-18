import gspread

class GoogleSheets:
    def __init__(self, credentials, document, sheet_name):
        self.gc = gspread.service_account_from_dict(credentials)
        self.sh = self.gc.open(document)
        self.sheet = self.sh.worksheet(sheet_name)

    def write_data(self, range_, data):
        # Suponiendo que data es una lista de listas que contiene los datos que deseas escribir
        # range_ debe ser una cadena que represente el rango de celdas donde deseas escribir los datos
        self.sheet.update(range_, data)

    def get_last_row_range(self):
        last_row = len(self.sheet.get_all_values()) + 1
        data = self.sheet.get_all_values()
        range_start = f"A{last_row}"
        range_end = f"{chr(ord('A') + len(data[0]) - 1)}{last_row}"
        return f"{range_start}:{range_end}"

    