{{{#!html
$$
r_a + r_p = 2a
$$
}}}

{{{#!html
$$
r_a = a + c
$$
}}}

{{{#!html
$$
a = r_a - c
$$
}}}

{{{#!html
$$
r_p = a - c
$$
}}}

{{{#!html
$$
a = r_p + c
$$
}}}

{{{#!html
$$
c = a - r_p = r_a - a
$$
}}}

{{{#!html
$$
r_1 + r_2 = 2 a
$$
}}}


$\vec{F}_1$ and $\vec{F}_2$ are the position vectors of the focal points.

{{{#!html
$$
|\vec{F}_1 - \vec{F}_2| = 2c
$$
}}}

$\vec{r}_1$ and $\vec{r}_2$ are vectors from the focal points to the satellite.

The position of the satellite can be written in terms of either focal point

{{{#!html
$$
\vec{F}_1 + \vec{r}_1 = \vec{F}_2 + \vec{r}_2
$$
}}}

{{{#!html
$$
\vec{F}_1 - \vec{F}_2 = \vec{r}_2 - \vec{r}_1
$$
}}}

So we can say

{{{#!html
$$
|\vec{r}_1 - \vec{r}_2| = 2c
$$
}}}

We also know that

{{{#!html
$$
|\vec{r}_1| + |\vec{r}_2| = 2a
$$
}}}

{{{#!html
$$
r_1 + r_2 = 2a
$$
}}}


== Ellipse From Position, Tangent, and Apoapsis or Periapsis ==

First find $\hat{r}_2$.

We know that $\hat{r}_2$ is the reflection of $\hat{r}_1$ about a line perpendicular to the tangent line.

{{{#!html
$$
\hat{r}_2 = \hat{r}_1 - 2 \hat{t}(\hat{t} \cdot \hat{r}_1)
$$
}}}

{{{#!html
$$
\vec{r}_2 = r_2 \hat{r}_2
$$
}}}

Start with

{{{#!html
$$
|r_1 \hat{r}_1 - r_2 \hat{r}_2| = 2c
$$
}}}

Rewrite the magnitude in terms of dot product

{{{#!html
$$
(r_1 \hat{r}_1 - r_2 \hat{r}_2) \cdot (r_1 \hat{r}_1 - r_2 \hat{r}_2) = 4c^2
$$
}}}

{{{#!html
$$
r_1^2 (\hat{r}_1 \cdot \hat{r}_1)
- 2 ((r_1 \hat{r}_1) \cdot (r_2 \hat{r}_2))
+ r_2^2 (\hat{r}_2 \cdot \hat{r}_2)
= 4c^2
$$
}}}

{{{#!html
$$
r_1^2
- 2 r_1 r_2 (\hat{r}_1 \cdot \hat{r}_2)
+ r_2^2
= 4c^2
$$
}}}

Note that

{{{#!html
$$
c^2 = (a - r_p)^2 = (r_a - a)^2
$$
}}}
{{{#!html
$$
c^2 = a^2 - 2 a r_p + r_p^2 = r_a^2 - 2 a r_a + a^2
$$
}}}

By squaring $c$, the apoapsis and periapsis are indistinguishable so we can just write

{{{#!html
$$
c^2 = a^2 - 2 a r_e + r_e^2
$$
}}}

{{{#!html
$$
(2c)^2 = (2a)^2 - 4 (2a) r_e + 4 r_e^2
$$
}}}

Substitute $a$ for the radii

{{{#!html
$$
(2c)^2 = (r_1+r_2)^2 - 4 (r_1+r_2) r_e + 4 r_e^2
$$
}}}

{{{#!html
$$
(2c)^2 = r_1^2 + 2r_1r_2 + r_2^2 - 4 (r_1+r_2) r_e + 4 r_e^2
$$
}}}

substituting we get

{{{#!html
$$
r_1^2
- 2 r_2 (\vec{r}_1 \cdot \hat{r}_2)
+ r_2^2
= 4 r_e^2 + r_1^2 + r_2^2 - 4 r_e r_1 - 4 r_e r_2 + 2 r_1 r_2
$$
}}}

do some cancellations

{{{#!html
$$
- r_1 r_2 (\hat{r}_1 \cdot \hat{r}_2)
= 2 r_a^2 - 2 r_a r_1 - 2 r_a r_2 + r_1 r_2
$$
}}}

solve for $r_2$

{{{#!html
$$
- r_1 r_2 (\hat{r}_1 \cdot \hat{r}_2) + 2 r_a r_2 - r_1 r_2
= 2 r_a^2 - 2 r_a r_1
$$
}}}

{{{#!html
$$
r_2
= \frac{
2 r_a^2 - 2 r_a r_1
}{
- (\hat{r}_1 \cdot \hat{r}_2) r_1 + 2 r_a - r_1
}
$$
}}}

{{{#!html
$$
r_2
= \frac{
r_{ex} (r_{ex} - r_1)
}{
r_{ex} - \frac{1}{2}(1 + \hat{r}_1 \cdot \hat{r}_2) r_1
}
$$
}}}

{{{#!html
$$
f=\frac{1}{2}(1+\hat{r}_1 \cdot \hat{r}_2)
$$
}}}

{{{#!html
$$
r_2
= \frac{
r_{ex} (r_{ex} - r_1)
}{
r_{ex} - f r_1
}
$$
}}}

or

{{{#!html
$$
r_2
=r_{ex} \frac{
\alpha - 1
}{
\alpha - f
}
$$
}}}

where $\alpha=\frac{r_{ex}}{r_1}$.

Here we plot the function with $r_1=1$ and $f=0.85$.

{{attachment:ellipse1.png}}

There is a gap between $fr_1$ and $r_1$ for which the function is not defined and such an ellipse cannot be constructed.

The lower boundary of the gap corresponds to the upper limit of the periapsis and can be found by taking the function

{{{#!html
$$
0 = 2 r_{ex}^2 - 2 r_{ex} r_1 - 2 r_{ex} r_2 + r_1 r_2 - r_1 r_2 (\hat{r}_1 \cdot \hat{r}_2)
$$
}}}

and solving for $r_{ex}$

{{{#!html
$$
r_{ex} = \frac{r_1+r_2}{2} \pm \sqrt{(\frac{r_1+r_2}{2})^2 - 4fr_1r_2}
$$
}}}

the periaps is given by

{{{#!html
$$
r_{ex} = \frac{r_1+r_2}{2} - \sqrt{(\frac{r_1+r_2}{2})^2 - 4fr_1r_2}
$$
}}}

and taking the limit as $r_2$ goes to infinity. See a proof [[Encyclopedia/Mathematics/Calculus/Limits/Proof1|here]].
