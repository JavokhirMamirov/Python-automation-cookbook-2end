import matplotlib.pyplot as plt

DATA = (
    ('Q1 2017', 100, 0),
    ('Q2 2017', 105, 15),
    ('Q3 2017', 125, 40),
    ('Q4 2017', 115, 80),
)

POS = list(range(len(DATA)))
VALUESA = [valueA for label, valueA, valueB in DATA]
VALUESB = [valueB for label, valueA, valueB in DATA]
LABELS = [label for label, valueB, valueA in DATA]

plt.bar(POS, VALUESB)
plt.bar(POS, VALUESA, bottom=VALUESB)
plt.ylabel('Seles')
plt.xticks(POS, LABELS)
plt.show()
