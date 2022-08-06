import openpyxl
from openpyxl.comments import Comment

xlsfile = openpyxl.load_workbook('movies.xlsx')

sheet = xlsfile['Sheet1']

sheet['D4'].value = 'Spielberg'
sheet['D4'].comment = Comment('Chenged text automatically', 'User')

sheet['B12'] = '=SUM(B2:B11)'

xlsfile.save('movies_comment.xlsx')
