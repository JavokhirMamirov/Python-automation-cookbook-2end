import matplotlib.pyplot as plt

LEGEND = ('ProductA', 'ProductB', 'ProductC')

DATA = (
    ('Q1 2017', 100, 30, 3),
    ('Q2 2017', 105, 32, 5),
    ('Q3 2017', 125, 29, 40),
    ('Q4 2017', 115, 31, 80),
)

POS = list(range(len(DATA)))

VALUESA = [valueA for label, valueA, valueB, valueC in DATA]
VALUESB = [valueB for label, valueA, valueB, valueC in DATA]
VALUESC = [valueC for label, valueA, valueB, valueC in DATA]
LABELS = [label for label, valueA, valueB, valueC in DATA]

WIDTH = 0.2

plt.bar([p-WIDTH for p in POS], VALUESA, width=WIDTH)
plt.bar([p for p in POS], VALUESB, width=WIDTH)
plt.bar([p+WIDTH for p in POS], VALUESC, width=WIDTH)


plt.ylabel('Sales')

plt.xticks(POS, LABELS)

plt.annotate('400 % growth', xy=(1.2, 18), xytext=(1.3, 40), horizontalalignment='center',
 arrowprops=dict(facecolor='black', shrink=0.05))

plt.legend(LEGEND)

plt.show()

