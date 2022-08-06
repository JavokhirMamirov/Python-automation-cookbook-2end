import openpyxl

xslfile = openpyxl.Workbook()

sheet = xslfile['Sheet']

data = [
    (225.7, 'Gone With the Wind', 'Victor Fleming'),
    (194.4, 'Star Wars', 'George Lucas'),
    (161.0, 'ET: The Extraterrestrial', 'Steven Spielberg'),
]

for row, (addmissions, name, directory) in enumerate(data, 1):
    sheet[f'A{row}'].value = addmissions
    sheet[f'B{row}'].value = name

sheet = xslfile.create_sheet('Directories')

for row, (addmissions, name, directory) in enumerate(data, 1):
    sheet[f'A{row}'].value = directory
    sheet[f'B{row}'].value = name

xslfile.save('movie_sheets.xlsx')
