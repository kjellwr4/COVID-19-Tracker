
import requests
import json
import urllib
from datetime import date
import gspread
from oauth2client.service_account import ServiceAccountCredentials

url = 'https://covidtracking.com/api/states' # URL that contains current COVID-19 state data.
jsonFile = urllib.request.urlopen(url) # Extract data from URL as a JSON file.
all_states = json.loads(jsonFile.read()) # Parse JSON file as state, territory, and DC entries.
scope = ['https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('/PATH_FOR/credentials.json', scope)
client = gspread.authorize(credentials)
sheet = client.open_by_key('SPREADSHEET_ID').sheet1

for result in all_states:
	today = date.today()
	date1 = today.strftime("%m/%d/%Y")
	abbr = result['state']
	pos = result['positive']
	neg = result['negative']
	pend = result['pending']
	hospital = result['hospitalized']
	dead = result['death']
	row = [date1, abbr, pos, neg, pend, hospital, dead]
	sheet.append_row(row, value_input_option='USER_ENTERED', insert_data_option='INSERT_ROWS', table_range='A1')
