import matplotlib.pyplot as plt
import numpy as np

x = [0.12,0.02,0.51,0.07]
xerr = [0.18,0.01,0.73,0.11]
y = [0.25,0.03,0.85,0.15]
yerr = [0.38,0.01,1.14,0.12]


fig, axs = plt.subplots(1,1)
axs.errorbar(x, y, xerr=xerr, yerr=yerr, fmt='o')
axs.set_title('Lab 1 Section 4', size=20)
axs.set_xlabel('time [s]', size=20)
axs.set_ylabel('length [cm]', size=20)
plt.savefig('Lab1_Section4.png')

