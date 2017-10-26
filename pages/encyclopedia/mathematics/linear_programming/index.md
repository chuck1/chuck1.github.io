---
layout: default
---

# linear programming

Linear programming is a method for optimization in a mathematical model whose requirements are linear relationships.

In canonical form:

Maximize or minimize $$\mathbf{c}^\mathrm{T} \mathbf{x}$$ subject to $$\mathbf{A} \mathbf{x} \le \mathbf{b}$$ and $$\mathbf{x} \ge \mathbf{0}$$

where $$\mathbf{x}$$ is a vector of variables, $$\mathbf{b}$$ and $$\mathbf{c}$$ are known vectors, and $$\mathbf{A}$$ is a known matrix.

## optimization problem

If you have a n-dimensional problem and p linear equality constraints, you get a (n-p)-dimensional subspace.
If you then introduce a sufficient number of linear inequalities, we can bound the subspace and create a polytope.
We can optimize by looking at each vertex and evaluating a cost function.
So how do we find the vertices?

For simplicity lets consider the case in which each inequality takes the form $$x_i < a$$ or $$x_i > a$$.
So we can bound our subspace with a greater than and a less then relation for each dimension for a total of 2n inequalities.
To find a vertex, we take the equalities that form our subspace and we need p inequalities to define a point.
These inequalities we choose must each be for a different axis.
If we consider every possible choice of p inequalities where axes are not repeated, we get all possible vertices.
To identify all these possibilities, first consider all combinations of axes.
Then, for each unique set of p axes, consider all combinations of the greater than or the less than inequality for each, which results in $$2^p$$ possibilities.


