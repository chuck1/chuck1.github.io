---
layout: default
title: newton raphson method
---
# newton raphson method

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

$$
f(\alpha) = f(x_n) + f'(x_n)(\alpha - x_n) + R_1
$$

$$
R_1 = \frac{1}{2!} f''(\zeta_n) (\alpha - x_n)^2
$$

$$
0 = f(\alpha) = f(x_n) + f'(x_n)(\alpha - x_n) + \frac{1}{2!} f''(\zeta_n) (\alpha - x_n)^2
$$

$$
\frac{f(x_n)}{f'(x_n)} + (\alpha - x_n) = - \frac{1}{2!} \frac{f''(\zeta_n)}{f'(x_n)} (\alpha - x_n)^2
$$

remember

$$
x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}
$$

$$
\alpha - x_{n+1} = -\frac{f''(\zeta_n)}{2 f'(x_n)} (\alpha - x_n)^2
$$

$$
\epsilon_{n+1} = -\frac{f''(\zeta_n)}{2 f'(x_n)} \epsilon_n^2
$$

$$
|\epsilon_{n+1}| = \frac{|f''(\zeta_n)|}{2 |f'(x_n)|} \epsilon_n^2
$$




