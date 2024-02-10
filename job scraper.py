import gspread
from oauth2client.service_account import ServiceAccountCredentials
from PIL import Image, ImageDraw, ImageFont

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('stellar-cipher-413820-564243d36b0b.json', scope)
client = gspread.authorize(creds)

spreadsheet_key = '1YVrx4KBY8XGpz-BpVJzBTKByn494QhbDDfwjeLa6Sik'
worksheet_name = 'ID Data'
sheet = client.open_by_key(spreadsheet_key).worksheet(worksheet_name)


