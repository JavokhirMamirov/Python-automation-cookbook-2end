import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
DATA = (
    ('Q1 2017', 100),
    ('Q2 2017', 150),
    ('Q3 2017', 125),
    ('Q4 2017', 175),
)

def value_format(value, position):
    return '$ {}M'.format(int(value))

POS = list(range(len(DATA)))

VALUES = [value for label, value in DATA]
LABELS = [label for label, value in DATA]

plt.bar(POS, VALUES, color='xkcd:moss green')
plt.xticks(POS, LABELS)

axes = plt.gca()

axes.yaxis.set_major_formatter(FuncFormatter(value_format))

plt.ylabel('Seles')

plt.show()