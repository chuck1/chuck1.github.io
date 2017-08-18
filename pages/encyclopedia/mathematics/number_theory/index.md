---
layout: default
title: Number Theory
---

# Number Theory

## theorem 1

Consider the equation of the natural numbers


$$
ab=cd
$$


Given any the values of $b$ and $c$, find the minimum value of $a$ and $d$ that satisfies the equation.
Consider the expansion of $b$ and $c$


$$
b = b_1 g
$$



$$
c = c_1 g
$$


where $g$ is the greatest common denominator of $b$ and $c$.


$$
a b_1 g = c_1 g d
$$



$$
a b_1 = c_1 d
$$



$$
a = \frac{c_1 d}{b_1}
$$


\\(b_1\\) and $c_1$ are defined such that they do not share any factors.
Therefor, $d$ must be a multiple of $b_1$.


$$
d = k b_1
$$



$$
a = \frac{k c_1 b_1}{b_1} = k c_1
$$


We now have an equation for all possible solutions for $a$ and $d$.
The smallest values obviously correspond to $k=1$, which we will write below.


$$
a = \frac{c}{\mathrm{gcd}(b,c)}
$$

$$
d = \frac{b}{\mathrm{gcd}(b,c)}
$$




