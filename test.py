__author__ = 'Harsh'
import gspread                              #google spreadsheet api
from oauth2client.service_account import ServiceAccountCredentials    #authentiction

print("into try function")
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('FRRO-Reminder-API.json', scope)
client = gspread.authorize(creds)
sheet = client.open('FRRO_LOGS').sheet1
db=sheet.get_all_records()       #taking all the records
print(db)