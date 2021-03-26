import gspread
from oauth2client.service_account import ServiceAccountCredentials
from flask import Flask, render_template
from flask import jsonify
from flask import request
from flask import session
from flask import redirect,url_for,g,abort

app = Flask(__name__)
app.secret_key='placementcell'

#Google sheet database setup
scope = ['https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)
gc = gspread.authorize(credentials)

sheets_url = "https://docs.google.com/spreadsheets/d/16ef17dVYRxvjfEyHwX9aIRZ0Ir3KnLEr3XRD04nf-Zk/edit?usp=sharing"
my_file = gc.open_by_url(sheets_url)

#testing
print(my_file.worksheets())

#print(sheets_data)
#printing first rows
def rowjob():
    my_sheetjob = my_file.sheet1
    firstrowjob = my_sheetjob.row_values(1)
    return firstrowjob

def rowintern():
    my_sheetintern = my_file.get_worksheet(1)
    firstrowintern = my_sheetintern.row_values(1)
    return firstrowintern

def rowhack():
    my_sheethack = my_file.get_worksheet(2)
    firstrowhack = my_sheethack.row_values(1)
    return firstrowhack

#printing sheet stuff    
def sheetifyjob():
    my_sheetjob = my_file.sheet1
    #list_val = my_sheet.get_all_values()
    #print(list_val)
    #sheets_data = my_sheet.acell('A1').value
    sheets_data_job = my_sheetjob.get_all_records()
    return sheets_data_job

def sheetifyintern():
    my_sheetintern = my_file.get_worksheet(1)
    sheets_data_intern = my_sheetintern.get_all_records()
    return sheets_data_intern

def sheetifyhack():
    my_sheethack = my_file.get_worksheet(2)
    sheets_data_hack = my_sheethack.get_all_records()
    return sheets_data_hack

@app.route('/')
def home():
    return render_template('index.html',sheets_data=sheetifyjob(),firstrow=rowjob())

@app.route('/intern')
def inter():
    return render_template('intern.html',sheets_data=sheetifyintern(),firstrow=rowintern())

@app.route('/hackathon')
def hack():
    return render_template('hack.html',sheets_data=sheetifyhack(),firstrow=rowhack())


if __name__ == '__main__':
    app.run(debug=True)

