import matplotlib.pyplot as plt

DATA = (
    ('Q1 2017', 100, 5),
    ('Q2 2017', 105, 15),
    ('Q3 2017', 125, 45),
    ('Q4 2017', 115, 80),
)

POS = list(range(len(DATA)))

VALUESA = [valueA for label, valueA, valueB in DATA]
VALUESB = [valueB for label, valueA, valueB in DATA]
LABELS = [label for label, valueA, valueB in DATA]

plt.plot(POS, VALUESA, 'o-')
plt.plot(POS, VALUESB, 'o-')
plt.ylabel('Sales')
plt.xticks(POS, LABELS)
plt.show()