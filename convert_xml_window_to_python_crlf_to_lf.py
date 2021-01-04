# replacement strings
WINDOWS_LINE_ENDING = b'\r\n'
UNIX_LINE_ENDING = b'\n'

# relative or absolute file path, e.g.:
file_path = r"/home/congdanh/Downloads/4/Annotations/Border_CCCD_1Can_cuoc_cong_dan_Bui_Thi_Yen.pdf.xml"

with open(file_path, 'rb') as open_file:
    content = open_file.read()

content = content.replace(WINDOWS_LINE_ENDING, UNIX_LINE_ENDING)

with open(file_path, 'wb') as open_file:
    open_file.write(content)