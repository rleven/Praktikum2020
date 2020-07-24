import matplotlib.pyplot as plt
import numpy as np
import csv

def linsengl(b, g):
    return 1/(1/b+1/g)

b = np.genfromtxt("Data/Bekannt.txt", unpack=True, usecols=0)
g = np.genfromtxt("Data/Bekannt.txt", unpack=True, usecols=1)
b0 = np.zeros(9)
plt.plot(b0, b, '.r')
plt.plot(g, b0, '.b')
for i in range(len(b)):
    x = np.linspace(0, g[i])
    plt.plot(x, -b[i]*x/g[i]+b[i], '-k', linewidth=1)
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot1.pdf')
plt.close()

with open("Data/Bekannt.csv", "w") as f:
    writer= csv.writer(f)
    writer.writerows(zip(b, g))

s = sum(linsengl(b, g))
aver = s/len(b)
print(aver)

del b, g, s, aver

b = np.genfromtxt("Data/Unbekannt.txt", unpack=True, usecols=0)
g = np.genfromtxt("Data/Unbekannt.txt", unpack=True, usecols=1)

#print(linsengl(b, g))

with open("Data/Unbekannt.csv", "w") as f:
    writer= csv.writer(f)
    writer.writerows(zip(b, g))

print(linsengl(b,g))

b1 = np.genfromtxt("Data/Bessel.txt", unpack=True, usecols=1)
g1 = np.genfromtxt("Data/Bessel.txt", unpack=True, usecols=0)
b2 = np.genfromtxt("Data/Bessel.txt", unpack=True, usecols=3)
g2 = np.genfromtxt("Data/Bessel.txt", unpack=True, usecols=2)

with open("Data/Bessel.csv", "w") as f:
    writer= csv.writer(f)
    writer.writerows(zip(b1, g1, b2, g2))

B = np.genfromtxt("Data/Abbe.txt", unpack=True, usecols=1)
G = np.genfromtxt("Data/Abbe.txt", unpack=True, usecols=0)
bs = np.genfromtxt("Data/Abbe.txt", unpack=True, usecols=3)
gs = np.genfromtxt("Data/Abbe.txt", unpack=True, usecols=2)

with open("Data/Abbe.csv", "w") as f:
    writer= csv.writer(f)
    writer.writerows(zip(B, G, bs, gs))

plt.plot(1+B/G, bs, '-r', label="b'")
plt.plot(1+G/B, gs, '-b', label="g'")
plt.xlabel(r'$1\ +\ V$ oder $1\ +\ \frac{1}{V}$ in cm')
plt.ylabel(r"$g'(f)$ oder $b'(f)$ in cm")
plt.legend(loc="best")

# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot.pdf')
plt.close()