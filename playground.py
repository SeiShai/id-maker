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

font_size = 30
font = ImageFont.truetype("arial.ttf", font_size)

# collect the data from Google Sheets
data = sheet.get_all_records()

# Generate ID cards
for idx, entry in enumerate(data, 1):

    # Upload the template of ID
    template_path = 'id template.png'
    id_template = Image.open(template_path).convert('RGB')
    draw = ImageDraw.Draw(id_template)

    # Fields are the headers from gsheets
    name = entry['Name ']
    lrn = entry['LRN']
    student_number = entry['Student Number']
    college_program = entry['College Program']
    contact_number = entry['Contact Number']
    emergency_contact_number = entry['Emergency Contact Number']

    # Function to calculate the center position based on text width
    def center_text(draw, text, y_position):
        text_bbox = draw.textbbox((0, 0), f"{text}", font=font)
        text_width = text_bbox[2] - text_bbox[0]
        x_position = (id_template.width - text_width) // 2
        draw.text((x_position, y_position), f"{text}", font=font, fill='black')

    center_text(draw, name, 535)
    center_text(draw, f"LRN: {lrn}", 710)
    center_text(draw, student_number, 575)
    center_text(draw, college_program, 750)
    center_text(draw, contact_number, 620)
    center_text(draw, f"Emergency: {emergency_contact_number}", 810)

    # Save the generated ID card
    output_path = f"{name}_ID_Card.jpg"
    id_template.save(output_path)

print('Finished Processing')
