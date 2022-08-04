from datetime import datetime

TEMPLATE = """
Movies report
--------------

Date: {date}
Movies seen in the last 30 days: {num_movies}
Total munites: {total_minutes}
"""

data = {
    'date':datetime.utcnow(),
    'num_movies':3,
    'total_minutes': 376,
}

report = TEMPLATE.format(**data)

FILENAME_TMPL = "{date}_report.txt"
filename = FILENAME_TMPL.format(date=data['date'].strftime('%Y-%m-%d'))

with open(filename, 'w') as file:
    file.write(report)