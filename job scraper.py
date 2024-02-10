import gspread
from oauth2client.service_account import ServiceAccountCredentials
from PIL import Image, ImageDraw, ImageFont

# Setting the API
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('stellar-cipher-413820-564243d36b0b.json', scope)
client = gspread.authorize(creds)

# Use the GSheet key for setup
spreadsheet_key = '1YVrx4KBY8XGpz-BpVJzBTKByn494QhbDDfwjeLa6Sik'
worksheet_name = 'ID Data'
sheet = client.open_by_key(spreadsheet_key).worksheet(worksheet_name)

# Upload the template of ID
template_path = 'id template.png'
id_template = Image.open(template_path).convert('RGB')

font = ImageFont.truetype("Times new roman", 30)
draw = ImageDraw.Draw(id_template)

# collect the data from Google Sheets
data = sheet.get_all_records()

# Generate ID cards
for entry in data:
    # Fields are the headers from gsheets
    name = entry['Name ']
    address = entry['Address']
    lrn = entry['LRN']
    student_number = entry['Student Number']
    college_program = entry['College Program']
    contact_number = entry['Contact Number']
    emergency_contact_number = entry['Emergency Contact Number']


