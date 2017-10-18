---
---
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

x0 = np.linspace(-1,1)

a = 2
b = 1

x1 = -b/a * np.ones(np.shape(x0))

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

ax.plot(x0, x1)

ax.plot(x0,x0)

ax.set_ylim(-1,1)

fn = "/home/crymal/temp/test.svg"

plt.savefig(fn)
with open(fn) as f:
    print(f.read())

