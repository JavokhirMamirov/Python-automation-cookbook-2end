import matplotlib.pyplot as plt
import csv
from matplotlib.ticker import FuncFormatter

with open('scatter.csv') as fp:
    reader = csv.reader(fp)
    data = list(reader)

data_x = [float(x) for x, y in data]
data_y = [float(y) for x, y in data]
plt.scatter(data_x, data_y)

def format_dollars(value, pos):
    return '{}m'.format(int(value))

def format_minutes(value, pos):
    return '{}m'.format(int(value))

plt.gca().yaxis.set_major_formatter(FuncFormatter(format_dollars))
plt.gca().xaxis.set_major_formatter(FuncFormatter(format_minutes))

plt.ylabel('Spending')

plt.show()