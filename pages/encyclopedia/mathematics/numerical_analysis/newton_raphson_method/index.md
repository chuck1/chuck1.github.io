---
layout: default
title: newton raphson method
---
# newton raphson method

* [example 1](example_01)
* [example 2](example_02)

$$
x:f(x)=0
$$

We use the approximation

$$
f(x_{n}) - f(x_{n-1}) \approx f'(x_{n-1}) (x_{n} - x_{n-1})
$$

Then substitute

$$
f(x_{n}) = 0
$$

$$
- f(x_{n-1}) = f'(x_{n-1}) (x_{n} - x_{n-1})
$$

and solve for $$x_{n}$$

$$
x_{n} = x_{n-1} - \frac{f(x_{n-1})}{f'(x_{n-1})}
$$

If $$x$$ is a vector, then $$f'$$ is a matrix so

$$
x_{n} = x_{n-1} - f'(x_{n-1})^{-1} f(x_{n-1})
$$

## condition for convergence

$$\alpha$$ is a root.
The expansion of $$f$$ about $$\alpha$$ is

$$
f(\alpha) = f(x_n) + f'(x_n)(\alpha - x_n) + R_1
$$

$$
R_1 = \frac{1}{2!} f''(\xi_n) (\alpha - x_n)^2
$$

where $$\xi_n$$ is between $$\alpha$$ and $$x_n$$.
Since $$\alpha$$ is a root

$$
0 = f(\alpha) = f(x_n) + f'(x_n)(\alpha - x_n) + \frac{1}{2!} f''(\xi_n) (\alpha - x_n)^2
$$

divide by $$f'(x_n)$$

$$
\frac{f(x_n)}{f'(x_n)} + (\alpha - x_n) = - \frac{1}{2!} \frac{f''(\xi_n)}{f'(x_n)} (\alpha - x_n)^2
$$

remember

$$
x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}
$$

so

$$
\alpha - x_{n+1} = -\frac{f''(\xi_n)}{2 f'(x_n)} (\alpha - x_n)^2
$$

replace $$\alpha - x_i$$ with $$\epsilon_i$$

$$
\epsilon_{n+1} = -\frac{f''(\xi_n)}{2 f'(x_n)} \epsilon_n^2
$$

take the absolute value

$$
|\epsilon_{n+1}| = \frac{|f''(\xi_n)|}{2 |f'(x_n)|} \epsilon_n^2
$$




