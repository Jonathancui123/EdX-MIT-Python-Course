import pylab as plt

linear = [i for i in range(1,11)]
quadratic = [i**2 for i in range(1,11)]
cubic = [i**3 for i in range(1,11)]
exponential = [1.5**i for i in range(1,11)]

plt.figure('lin')
plt.plot(linear, linear)
plt.figure('quad')
plt.plot(linear, quadratic)
plt.figure('cubic')
plt.plot(linear, cubic)
plt.figure('exponential')
plt.plot(linear,exponential)
plt.show()