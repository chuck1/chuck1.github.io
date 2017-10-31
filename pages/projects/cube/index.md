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
But to find each of those solutions we will need to use [linear programming](/pages/encyclopedia/mathematics/linear_programming).

I have been trying to write my own method to search for a optimal solution.
I goal was to find every vertex that can be formed in the subspace by intersections of planes defined by engine limit inequalaities.
My first atempt to construct a matrix and invert it failed.
I then created a sort of tree search algorithm in which at each step deeper into the tree, we select a new engine and produce one of the limit planes.
We convert that limit plane to our subspace and then that to create a new subspace with one fewer dimensions.
Each step creates a new subspace until we reach the bottom and the subspace has zero dimensions.
This zero dimensional subspace represents a point in the subspace above.
We can propagate this point upward through the tree, until we reahc the engine space and have a point therein.
Testing has shown that this method does produce valid solutions for force and torque.

This method can produce every possible vertex in the engine space.
However, it is too computationally expensinve to do so.
For example, with 24 engines (4 engines on each side of a cube) the subspace has 18 dimensions.
There are 923795456 possible vertices that can be formed in this subspace using all of the engine limit planes.
The method can find a single solution quickly.
But this solution could have two issues.
First, some of the engine limits could be violated.
Since we only use a subset of the engines to form a vertex, the resulting solution could violate limits of any of the unused engines.
The second issue is that, even if no engine limits are violated, the solution might not be the optimal solution.

Lets consider the first issue.
We could write an algorithm that starts from a violating solution and from there tries to find a non-violating solution.
Consider the fact the any engine the is used in the construction of the vertex must by definition not be violated.
So in order to fix a particular violation we must simply include the violated plane.
This means that we must replace one of the constrains used in the original solution.
We could iterate over all of the original constraints and check all of them, which will only be order $$n$$.
Doing so produces a new set of solutions (which I have not yet proved is not an empty set).
Some of these solutions could have more, less or the same number of violated constraints as the original (proved by testing).
We would like to find a solution that has less violated constraints.
If we do, we should take that solution and repeat the process.
Perhaps this will eventually lead to a valid solution

To speed up this method for practical use, we will want to perform some calculations in advance and save the result.
Of course, we can only do this for calculations that do not depend on the desired force and torque.
We can perform calculations that depend only on the orientation of the engines.
Right now these calculations are performed at the same time inside the subspace data structure.
Refactoring will be required but I think significant optimization is possible.
For the first subspace, $$B$$ depends only on the $$v$$ and $$q$$ vectors for each engine.
For any subspace, $$A$$ depends only on $$B$$.
The calculation that takes us from one subspace to the next is the intersection of a plane and a subspace, which produces a new plane.
The normal vector of this new plane depends only on $$A$$ from the subspace and $$n$$ from the plane.
And finally, for a subspace constructed form planes, the $$B$$ matrix depends only on the normals of those planes.
So all of the $$B$$ and $$A$$ matricies of all subspaces in the search tree can be calculated independent of the desired output.











