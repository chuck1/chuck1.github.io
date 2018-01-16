---
layout: default
---

## Compression Problem

We have a collection of positive integers, $$x_i$$.
We know that no two integers are equal.
Our goal is to identify the integers.

We can define a function $$f$$ of a single integer.
The function can be applied to each integer

$$
y_{ij}= f_j(x_i)
$$

We cannot directly use $$y_{ij}$$.
We can, however, use $$z_j$$ where

$$
z_j = \sum y_{ij}
$$

We can use any number of $$z$$ values defined in this manner to determine the values of $$x_i$$.

### Solution

One solution uses a single function

$$
f(x_i) = 2^{x_i}
$$

If we imagine the binary representation of this result, it contains a single one and the rest zero.
So the binary representation of $$z$$ will contain a one for each $$x$$.
If we had allowed 

