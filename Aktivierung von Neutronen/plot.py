import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat, unumpy as unp
from uncertainties.unumpy import nominal_values as noms, std_devs as stds
from scipy.constants import constants
from scipy.optimize import curve_fit

tva = np.genfromtxt("Data/Vanadium.csv", unpack=True, delimiter=",", usecols=0)
nva = np.genfromtxt("Data/Vanadium.csv", unpack=True, delimiter=",", usecols=1)
deltaN = np.genfromtxt("Data/Vanadium.csv", unpack=True, delimiter=",", usecols=2)

def thingy(x, a, b):
    return a*x+b

def great(x, a, b, c, d):
    return noms(a) * np.exp(-noms(b)*x) + noms(c) * np.exp(-noms(d)*x)

params, cov_matrix = curve_fit(thingy, tva, np.log(nva))
m = ufloat(params[0], np.sqrt(cov_matrix[0, 0]))
b = ufloat(params[1], np.sqrt(cov_matrix[1, 1]))

params_better, cov_matrix_better = curve_fit(thingy, tva[0:13], np.log(nva[0:13]))
m_better = ufloat(params_better[0], np.sqrt(cov_matrix_better[0, 0]))
b_better = ufloat(params_better[1], np.sqrt(cov_matrix_better[1, 1]))

t_lin = np.linspace(tva[0], tva[-1])
t_better = np.linspace(30, 440)
thing = np.exp(thingy(t_lin, *params))
thing_better = np.exp(thingy(t_better, *params_better))

lam = np.abs(m)
lam_noice = np.abs(m_better)
T = np.log(2)/lam
T_noice = np.log(2)/lam_noice

print("Zerfallskonstante: ", lam)
print("HWZ: ", T)
print("Genauere Zerfallskonstante: ", lam_noice)
print("Genauere HWz: ", T_noice)

plt.errorbar(tva, nva, yerr=deltaN, fmt='.r', linewidth=1, label=r"\ce{^{52}V}")
plt.plot(t_lin, thing, "b", linewidth=1, label="Ausgleichsgerade")
plt.plot(t_better, thing_better, "g", linewidth=1, label="Fit bis 2-facher HWZ")
plt.yscale('log')
plt.ylabel(r"Impulse pro Sekunde von \ce{^{52}V}")
plt.xlabel(r"Zeit in $\si{\second}$")
plt.legend(loc="best")

# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot.pdf')
plt.close()

del params, cov_matrix, params_better, cov_matrix_better, m, b, m_better, b_better, t_lin, t_better, thing, thing_better, lam, lam_noice, T, T_noice

trh = np.genfromtxt("Data/Rhodium.csv", unpack=True, delimiter=",", usecols=0)
nrh = np.genfromtxt("Data/Rhodium.csv", unpack=True, delimiter=",", usecols=1)
deltarh = np.genfromtxt("Data/Rhodium.csv", unpack=True, delimiter=",", usecols=2)

params, cov_matrix = curve_fit(thingy, trh[15:43], np.log(nrh[15:43]))
m = ufloat(params[0], np.sqrt(cov_matrix[0, 0]))
b = ufloat(params[1], np.sqrt(cov_matrix[1, 1]))

t_lin = np.linspace(trh[15], trh[-1])
t_better = np.linspace(15, 240)
thing = np.exp(thingy(t_lin, *params))

lam = np.abs(m)
#lam_noice = np.abs(m_better)
T = np.log(2)/lam
print("hwzbbb: ", T)
#T_noice = np.log(2)/lam_noice
#print("hwz: ", T_noice)

N0 =unp.exp(b)
nrh_korr = nrh-N0*unp.exp(-lam*trh)
t_short = trh[0:15]
z_short = nrh_korr[0:15]

params_better, cov_matrix_better = curve_fit(thingy, t_short, unp.nominal_values(unp.log(z_short)))
m_better = ufloat(params_better[0], np.sqrt(cov_matrix_better[0, 0]))
b_better = ufloat(params_better[1], np.sqrt(cov_matrix_better[1, 1]))

thing_better = np.exp(thingy(t_better, *params_better))
lam_noice = np.abs(m_better)
N0_short = unp.exp(b_better)
T_noice = np.log(2)/lam_noice
print(T_noice)
trh_lin = np.linspace(0, 660)

plt.errorbar(trh, nrh, yerr=deltarh, fmt='.r', linewidth=1, label=r"\ce{^{104}Rh}")
plt.plot(t_lin, thing, "b", linewidth=1, label="Langlebiger Zerfall")
plt.plot(t_better, thing_better, "g", linewidth=1, label="Kurzlebiger Zerfall")
plt.plot(trh_lin, great(trh_lin, N0, lam, N0_short, lam_noice), "k", linewidth=1, label="Errechnete Kurve")
plt.yscale('log')
plt.ylabel(r"Impulse pro Sekunde von \ce{^{104}Rh}")
plt.xlabel(r"Zeit in $\si{\second}$")
plt.legend(loc="best")

# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot1.pdf')
plt.close()