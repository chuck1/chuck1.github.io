---
layout: default
---

# linear programming relaxation

The linear programming relaxation of a 0-1 integer program is obtained by replacing the 
constraint that each variable must be 0 or 1 by a weaker constraint, that each variable 
belong to the interval [0,1].

## integrality gap

The integrality gap for the minimization problem is

$$
IG = \frac{M_{int}}{M_{frac}}
$$

where $$M_{int}$$ is the integer solution and $$M_{frac}$$ is the fractional solution.

The integrality gap for the maximization problem is

$$
IG = \frac{M_{frac}}{M_{int}}
$$


