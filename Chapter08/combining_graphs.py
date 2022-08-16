import matplotlib.pyplot as plt

DATA = (
    ('Q1 2017', 100, 3000, 3),
    ('Q2 2017', 105, 3200, 5),
    ('Q3 2017', 125, 2900, 7),
    ('Q4 2017', 115, 3100, 3),
)

POS = list(range(len(DATA)))

VALUESA = [valueA for label, valueA, valueB, valueC in DATA]
VALUESB = [valueB for label, valueA, valueB, valueC in DATA]
VALUESC = [valueC for label, valueA, valueB, valueC in DATA]
LABELS = [label for label, valueA, valueB, valueC in DATA]

plt.subplot(2, 1, 1)
VALUEA = plt.bar(POS, VALUESA)

plt.ylabel('Sales A')

plt.twinx()

VALUEB = plt.plot(POS, VALUESB, 'o-', color='red')
plt.ylabel('Sales B')

plt.xticks(POS, LABELS)
plt.subplot(2, 1, 2)
plt.plot(POS, VALUESC)
plt.gca().set_ylim(ymin=0)
plt.xticks(POS, LABELS)
plt.show()
