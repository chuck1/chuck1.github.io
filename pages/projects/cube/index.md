---
layout: default
---

# Cube

A 3D game built with Unity.

## physics

### thrust calculation

The problem is to calculate the individual engine thrust values to produce the desired force or torque
or combination thereof in the desired direction.
There are 6 linear equations of the thrust, 3 for the sum of the forces in each direction and 3 for the sum of the torques in each direction.
If there are insufficient engines to produce the desired motion, the system will be unsolvable.
If there are exactly enough engines, we can solve these equations for our thrust values.

If there are more engines than the minimum requires, then there are multiple solutions.
The goal is to determine the optimal solution.
These will be a cost function which can be used to compare solution and tell us which is best.
But to each for those solutions we will need to use [linear programming](/pages/encyclopedia/mathematics/linear_programming).


