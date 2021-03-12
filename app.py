import gspread
from oauth2client.service_account import ServiceAccountCredentials
from flask import Flask, render_template
from flask import jsonify


app = Flask(__name__)
scope = ['https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)
gc = gspread.authorize(credentials)

sheets_url = "https://docs.google.com/spreadsheets/d/16ef17dVYRxvjfEyHwX9aIRZ0Ir3KnLEr3XRD04nf-Zk/edit?usp=sharing"

#my_file = gc.open_by_url(sheets_url)

#my_sheet = my_file.sheet1

#sheets_data = my_sheet.acell('A1').value

#print(sheets_data)
def row(any_url):
    my_file = gc.open_by_url(any_url)
    my_sheet = my_file.sheet1
    firstrow = my_sheet.row_values(1)
    return firstrow

def sheetify(any_url):
    my_file = gc.open_by_url(any_url)
    my_sheet = my_file.sheet1
    #list_val = my_sheet.get_all_values()
    #print(list_val)
    #sheets_data = my_sheet.acell('A1').value
    sheets_data = my_sheet.get_all_records()
    return sheets_data

def aise(any_url):
    my_file = gc.open_by_url(any_url)
    my_sheet = my_file.sheet1
    data = my_sheet.get_all_records()
    return data

@app.route('/')
def home():
    return render_template('index.html',sheets_data=sheetify(sheets_url),firstrow=row(sheets_url))


if __name__ == '__main__':
    app.run(debug=True)

