import mistune
from datetime import datetime

with open('markdown_template.md') as file:
    template = file.read()

constext = {
    'date': datetime.now(),
    'pmovies': ['Casablanca', 'The Sound of Music', 'Vertigo'],
    'total_minutes': 404,
}

constext['num_movies'] = len(constext['pmovies'])
constext['movies'] = '\n'.join('* {}'.format(movie) for movie in constext['pmovies'])

md_report = template.format(**constext)
report = mistune.markdown(md_report)

with open('report.html', 'w') as file:
    file.write(report)