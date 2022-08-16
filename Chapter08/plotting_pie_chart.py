import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
DATA = (
    ('Common', 100),
    ('Premium', 75),
    ('Luxurious', 50),
    ('Extravagant', 20)
)
total = sum(value for label, value in DATA)
VALUES = [value for label, value in DATA]
LABELS = [label for label, value in DATA]
BY_VALUE = {int(100 * value / total): value for label, value in DATA}

def value_format(percent, **kwargs):
    value = BY_VALUE[int(percent)]
    return '{}'.format(value)

explode = (0, 0, 0.1, 0)

plt.pie(VALUES, labels=LABELS, explode=explode, autopct=value_format, startangle=90, counterclock=False)
plt.gca().axis('equal')

plt.show()
