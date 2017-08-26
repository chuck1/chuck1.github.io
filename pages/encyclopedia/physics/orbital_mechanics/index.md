---
layout: default
---

## eliptical orbit

### basics

$$
r_a + r_p = 2a
$$

$$
r_a = a + c
$$

$$
r_p = a - c
$$

True anomaly

$$
\nu = \arccos \frac{\mathbf{e} \cdot \mathbf{r}}{|\mathbf{e}| |\mathbf{r}|}
$$

eccentricity vector

$$
\mathbf{e} = \frac{\mathbf{v} \times \mathbf{h}}{\mu} - \frac{\mathbf{r}}{|\mathbf{r}|}
$$

$$
\mathbf{h} = \mathbf{r} \times \mathbf{v}
$$


### other equations

$$
a = r_a - c
$$

$$
a = r_p + c
$$

$$
c = a - r_p = r_a - a
$$

$$
r_1 + r_2 = 2 a
$$

$$\vec{F}_1$$ and $$\vec{F}_2$$ are the position vectors of the focal points.

$$
|\vec{F}_1 - \vec{F}_2| = 2c
$$

$$\vec{r}_1$$ and $$\vec{r}_2$$ are vectors from the focal points to the satellite.

The position of the satellite can be written in terms of either focal point

$$
\vec{F}_1 + \vec{r}_1 = \vec{F}_2 + \vec{r}_2
$$

$$
\vec{F}_1 - \vec{F}_2 = \vec{r}_2 - \vec{r}_1
$$

So we can say

$$
|\vec{r}_1 - \vec{r}_2| = 2c
$$

We also know that

$$
|\vec{r}_1| + |\vec{r}_2| = 2a
$$

$$
r_1 + r_2 = 2a
$$

## ellipse from position, tangent, and apoapsis or periapsis

First find $$\hat{r}_2$$.

We know that $$\hat{r}_2$$ is the reflection of $$\hat{r}_1$$ about a line perpendicular to the tangent line.

$$
\hat{r}_2 = \hat{r}_1 - 2 \hat{t}(\hat{t} \cdot \hat{r}_1)
$$

$$
\vec{r}_2 = r_2 \hat{r}_2
$$

Start with

$$
|r_1 \hat{r}_1 - r_2 \hat{r}_2| = 2c
$$


Rewrite the magnitude in terms of dot product


$$
(r_1 \hat{r}_1 - r_2 \hat{r}_2) \cdot (r_1 \hat{r}_1 - r_2 \hat{r}_2) = 4c^2
$$



$$
r_1^2 (\hat{r}_1 \cdot \hat{r}_1)
- 2 ((r_1 \hat{r}_1) \cdot (r_2 \hat{r}_2))
+ r_2^2 (\hat{r}_2 \cdot \hat{r}_2)
= 4c^2
$$



$$
r_1^2
- 2 r_1 r_2 (\hat{r}_1 \cdot \hat{r}_2)
+ r_2^2
= 4c^2
$$


Note that


$$
c^2 = (a - r_p)^2 = (r_a - a)^2
$$


$$
c^2 = a^2 - 2 a r_p + r_p^2 = r_a^2 - 2 a r_a + a^2
$$


By squaring $$c$$, the apoapsis and periapsis are indistinguishable so we can just write


$$
c^2 = a^2 - 2 a r_e + r_e^2
$$



$$
(2c)^2 = (2a)^2 - 4 (2a) r_e + 4 r_e^2
$$


Substitute $a$ for the radii


$$
(2c)^2 = (r_1+r_2)^2 - 4 (r_1+r_2) r_e + 4 r_e^2
$$



$$
(2c)^2 = r_1^2 + 2r_1r_2 + r_2^2 - 4 (r_1+r_2) r_e + 4 r_e^2
$$


substituting we get


$$
r_1^2
- 2 r_2 (\vec{r}_1 \cdot \hat{r}_2)
+ r_2^2
= 4 r_e^2 + r_1^2 + r_2^2 - 4 r_e r_1 - 4 r_e r_2 + 2 r_1 r_2
$$


do some cancellations


$$
- r_1 r_2 (\hat{r}_1 \cdot \hat{r}_2)
= 2 r_a^2 - 2 r_a r_1 - 2 r_a r_2 + r_1 r_2
$$


solve for $r_2$


$$
- r_1 r_2 (\hat{r}_1 \cdot \hat{r}_2) + 2 r_a r_2 - r_1 r_2
= 2 r_a^2 - 2 r_a r_1
$$



$$
r_2
= \frac{
2 r_a^2 - 2 r_a r_1
}{
- (\hat{r}_1 \cdot \hat{r}_2) r_1 + 2 r_a - r_1
}
$$



$$
r_2
= \frac{
r_{ex} (r_{ex} - r_1)
}{
r_{ex} - \frac{1}{2}(1 + \hat{r}_1 \cdot \hat{r}_2) r_1
}
$$



$$
f=\frac{1}{2}(1+\hat{r}_1 \cdot \hat{r}_2)
$$



$$
r_2
= \frac{
r_{ex} (r_{ex} - r_1)
}{
r_{ex} - f r_1
}
$$


or


$$
r_2
=r_{ex} \frac{
\alpha - 1
}{
\alpha - f
}
$$


where $$\alpha=\frac{r_{ex}}{r_1}$$.

Here we plot the function with $$r_1=1$$ and $$f=0.85$$.

![](https://s3-us-west-2.amazonaws.com/19f075ca4a482833.media/ellipse1.png)

There is a gap between $$fr_1$$ and $$r_1$$ for which the function is not defined and such an ellipse cannot be constructed.

The lower boundary of the gap corresponds to the upper limit of the periapsis and can be found by taking the function


$$
0 = 2 r_{ex}^2 - 2 r_{ex} r_1 - 2 r_{ex} r_2 + r_1 r_2 - r_1 r_2 (\hat{r}_1 \cdot \hat{r}_2)
$$

and solving for $r_{ex}$

$$
r_{ex} = \frac{r_1+r_2}{2} \pm \sqrt{(\frac{r_1+r_2}{2})^2 - 4fr_1r_2}
$$

the periaps is given by

$$
r_{ex} = \frac{r_1+r_2}{2} - \sqrt{(\frac{r_1+r_2}{2})^2 - 4fr_1r_2}
$$

and taking the limit as $$r_2$$ goes to infinity. See a proof [here](/pages/encyclopedia/mathematics/calculus/limits/proof1).

