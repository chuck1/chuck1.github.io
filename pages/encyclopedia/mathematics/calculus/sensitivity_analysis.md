---
layout: default
---

# sensitivity analysis

## root sum of squares

In general

$$
e_y^2 = \sum \left( \frac{\partial y}{\partial x} e_x \right)^2
$$

### addition

$$
z = x + y
$$

$$
e_z^2 = \left( \frac{\partial z}{\partial x} e_x \right)^2 + \left( \frac{\partial z}{\partial y} e_y \right)^2
$$

$$
e_z^2 = e_x^2 + e_y^2
$$

### multiplication

$$
z = x y
$$

$$
e_z^2 = \left( \frac{\partial z}{\partial x} e_x \right)^2 + \left( \frac{\partial z}{\partial y} e_y \right)^2
$$

$$
e_z^2 = y^2 e_x^2 + x^2 e_y^2
$$

### general function

If we have

$$
f(y, x_1, x_2, ..., x_n) = 0
$$

which cannot be solved for $$y$$

$$
e_y^2 = \sum \left( \frac{\partial y}{\partial f} \frac{\partial f}{\partial x_i} e_{x_i} \right)^2
$$

$$
e_y^2 = \sum \left( \frac{\frac{\partial f}{\partial x_i}}{\frac{\partial f}{\partial y}} e_{x_i} \right)^2
$$

$$
e_y^2 = \frac{1}{\left( \frac{\partial f}{\partial y} \right)^2} \sum \left( \frac{\partial f}{\partial x_i} e_{x_i} \right)^2
$$

### system of equations

Suppose we have a system of equations. For each equation, we can write

$$
\sum \frac{\partial f}{\partial x_i}^2 e_i^2 a_i = 0
$$

where $$a_i$$ is $$-1$$ for exactly one $$i$$ and $$1$$ for all others.
How do you know which $$a_i$$ should be $$-1$$?

For now consider only systems whose graphical representations are a simple cycle.
In other words, each equation has exactly two unknowns.
So for each uncertainty equation there are only two choices.
We can calculate a solution using every possible combination and see what happens.
I have a theory that it for all possible combinations, there is only one valid solution.

Back to the general case. We can rewrite using $j$ instead of $i$ where $j$ represents just the
unknown uncertainties in this particular equation.

$$
\sum \frac{\partial f}{\partial x_j}^2 e_j^2 a_j = b
$$

You can see that with form, we can put all of the equations in a matrix form.





