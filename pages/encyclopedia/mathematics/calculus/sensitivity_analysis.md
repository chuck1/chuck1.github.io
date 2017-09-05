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


















