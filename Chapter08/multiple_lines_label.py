import matplotlib.pyplot as plt

DATA = (
    ('Intel 4004', 2_300, 1971),
    ('Motorola 68000', 68_000, 1979),
    ('Pentium', 3_100_000, 1993),
    ('Core i7', 731_000_000, 2008),
)

data_x = [x for label, y, x in DATA]
data_y = [y for label, y, x in DATA]
plt.plot(data_x, data_y, 'v')

for label, y, x in DATA:
    plt.text(x, y, label)

plt.gca().grid()

plt.yscale('log')

plt.show()