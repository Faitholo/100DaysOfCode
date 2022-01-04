#!/usr/bin/python3

import matplotlib.pyplot as plt

year = [1990, 2000, 2010, 2020, 2030, 2040, 2050]
income = [100, 300, 250, 800, 1100, 1300, 2000]

plt.hist(income, 8)
plt.show()
