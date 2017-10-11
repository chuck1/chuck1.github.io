---
layout: default
---

$$
f = \log x - x - a = 0
$$

where $$a=-2$$

$$
f' = \frac{1}{x} - 1
$$

$$
x_{n+1} = x_{n} - \frac{
	f(x_{n})
}{
	f'(x_{n})
}
$$

$$
x_{n+1} = x_{n} 
- \frac{
\log x_n - x_n - a
}{
\frac{1}{x_n} - 1
}
$$

![](plot_01.svg)

$$
e^{\log x - x - a} = e^{0}
$$

$$
e^{\log x} e^{-x} e^{-a} = 1
$$

$$
x e^{-x} e^{-a} - 1 = 0
$$

$$
f' = -e^{-a} e^{-x} (x - 1)
$$

$$
x_{n+1} = x_{n} 
- \frac{
x e^{-x_n} e^{-a} - 1
}{
-e^{-a} e^{-x_n} (x_n - 1)
}
$$

$$
x_{n+1} = x_{n} 
+ \frac{
x_n - e^{x_n} e^{a}
}{
(x_n - 1)
}
$$

![](plot_02.svg)

