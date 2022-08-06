import openpyxl

xlsfile = openpyxl.load_workbook('movies.xlsx')

sheet = xlsfile['Sheet1']

for row in sheet:
    for cell in row:
        print(cell.value)
