import matplotlib.pyplot as plt
import numpy as np

x = [0.12, 0.18, 0.25, 0.32, 0.38]
y = [0.51, 0.73, 0.85, 0.79, 1.14]
e = [0.07, 0.11, 0.15, 0.18, 0.12]

#No Error
num_a = len(x)*sum([q*r for q,r in zip(x,y)]) - sum(x)*sum(y)
den_a = len(x)*sum([q**2 for q in x]) - sum(x)**2
a = num_a/den_a

num_b = sum([q**2 for q in x])*sum(y) - sum(x)*sum([q*r for q,r in zip(x,y)])
den_b = len(x)*sum([q**2 for q in x]) - sum(x)**2
b = num_b/den_b

num_S = sum([(r - a*q - b)**2 for q,r in zip(x,y)])
S = (num_S/(len(x)-2))**0.5

den_sigma_a = len(x)*sum([q**2 for q in x]) - sum(x)**2
sigma_a = S*(len(x)/den_sigma_a)**0.5

den_sigma_b = len(x)*sum([q**2 for q in x]) - sum(x)**2
sigma_b = S*(sum([q**2 for q in x])/den_sigma_b)**0.5


print("No Error:")
print('a:', a)
print('b:', b)
print('S:', S)
print('sigma_a:', sigma_a)
print('sigma_b:', sigma_b)
print('\n\n')
no_err_a = a
no_err_b = b

#With Error
#Things over sigma**2:
x_over = sum([q/r**2 for q,r in zip(x,e)])
y_over = sum([q/r**2 for q,r in zip(y,e)])
xy_over = sum([q*r/s**2 for q,r,s in zip(x,y,e)])
one_over = sum([1/q**2 for q in e])
x_square_over = sum([q**2/r**2 for q,r in zip(x,e)])


num_a = x_over*y_over - xy_over*one_over
den_a = x_over**2 - x_square_over*one_over
a = num_a/den_a

num_b = x_over*xy_over - y_over*x_square_over
den_b = x_over**2 - x_square_over*one_over
b = num_b/den_b

den_sigma_a = x_square_over*one_over - x_over**2
sigma_a = (one_over/den_sigma_a)**0.5

den_sigma_b = x_square_over*one_over - x_over**2
sigma_b = (x_square_over/den_sigma_b)**0.5

print("No Error:")
print('a:', a)
print('b:', b)
print('sigma_a:', sigma_a)
print('sigma_b:', sigma_b)

fig, axes = plt.subplots(1,1)
axes.errorbar(x, y, yerr=e, fmt='o')
axes.set_title('Lab 1 Section 5', size=20)
axes.set_xlabel('x [s]', size=20)
axes.set_ylabel('y [cm]', size=20)

linx = np.linspace(0, 0.5, 30)
noerry = no_err_a * linx + no_err_b
erry = a*linx + b
plt.plot(linx, noerry, '--', label='No Error')
plt.plot(linx, erry, label='Error')
axes.legend()
plt.savefig('Lab1_Section5.png')
