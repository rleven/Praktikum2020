import matplotlib.pyplot as plt
import numpy as np
x=7
y=5
plt.plot(x, y)

# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot.pdf')